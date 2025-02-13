"""High level implementation of Companion API."""

from enum import Enum
import logging
from random import randint
from typing import Any, Dict, Mapping, Optional, cast

from pyatv import exceptions
from pyatv.auth.hap_pairing import parse_credentials
from pyatv.auth.hap_srp import SRPAuthHandler
from pyatv.core import Core
from pyatv.core.protocol import MessageDispatcher
from pyatv.protocols.companion.connection import CompanionConnection, FrameType
from pyatv.protocols.companion.protocol import (
    CompanionProtocol,
    CompanionProtocolListener,
    MessageType,
)

_LOGGER = logging.getLogger(__name__)


# pylint: disable=invalid-name


class HidCommand(Enum):
    """HID command constants."""

    Up = 1
    Down = 2
    Left = 3
    Right = 4
    Menu = 5
    Select = 6
    Home = 7
    VolumeUp = 8
    VolumeDown = 9
    Siri = 10
    Screensaver = 11
    Sleep = 12
    Wake = 13
    PlayPause = 14
    ChannelIncrement = 15
    ChannelDecrement = 16
    Guide = 17
    PageUp = 18
    PageDown = 19


class MediaControlCommand(Enum):
    """Media Control command constants."""

    Play = 1
    Pause = 2
    NextTrack = 3
    PreviousTrack = 4
    GetVolume = 5
    SetVolume = 6
    SkipBy = 7
    FastForwardBegin = 8
    FastForwardEnd = 9
    RewindBegin = 10
    RewindEnd = 11
    GetCaptionSettings = 12
    SetCaptionSettings = 13


# pylint: enable=invalid-name


class CompanionAPI(
    MessageDispatcher[str, Mapping[str, Any]], CompanionProtocolListener
):
    """Implementation of Companion API."""

    def __init__(self, core: Core):
        """Initialize a new CompanionAPI instance."""
        super().__init__()
        self.core = core
        self._connection: Optional[CompanionConnection] = None
        self._protocol: Optional[CompanionProtocol] = None
        self.sid: int = 0

    async def disconnect(self):
        """Disconnect from companion device."""
        if self._protocol is None:
            return

        try:
            # Sometimes unsubscribe fails for an unknown reason, but we are no
            # going to bother with that and just swallow the error.
            await self.unsubscribe_event("_iMC")
            await self._session_stop()
        except Exception as ex:
            _LOGGER.debug("Ignoring error during disconnect: %s", ex)
        finally:
            self._protocol.stop()
            self._protocol = None

    def event_received(self, event_name: str, data: Dict[str, Any]) -> None:
        """Event was received."""
        _LOGGER.debug("Got event %s from device: %s", event_name, data)
        self.dispatch(event_name, data)

    async def connect(self):
        """Connect to remote host."""
        if self._protocol:
            return

        _LOGGER.debug("Connect to Companion from API")
        self._connection = CompanionConnection(
            self.core.loop,
            str(self.core.config.address),
            self.core.service.port,
            self.core.device_listener,
        )
        self._protocol = CompanionProtocol(
            self._connection, SRPAuthHandler(), self.core.service
        )
        self._protocol.listener = self
        await self._protocol.start()

        await self.system_info()
        await self._session_start()
        await self.subscribe_event("_iMC")

    async def _send_command(
        self,
        identifier: str,
        content: Dict[str, object],
        message_type: MessageType = MessageType.Request,
    ) -> Mapping[str, Any]:
        """Send a command to the device and return response."""
        await self.connect()
        if self._protocol is None:
            raise RuntimeError("not connected to companion")

        try:
            resp = await self._protocol.exchange_opack(
                FrameType.E_OPACK,
                {
                    "_i": identifier,
                    "_t": message_type.value,
                    "_c": content,
                },
            )
        except exceptions.ProtocolError:
            raise
        except Exception as ex:
            raise exceptions.ProtocolError(f"Command {identifier} failed") from ex
        else:
            return resp

    async def system_info(self):
        """Send system information to device."""
        _LOGGER.debug("Sending system information")
        creds = parse_credentials(self.core.service.credentials)

        # Bunch of semi-random values here...
        await self._send_command(
            "_systemInfo",
            {
                "_bf": 0,
                "_cf": 512,
                "_clFl": 128,
                "_i": "cafecafecafe",  # TODO: Figure out what to put here
                "_idsID": creds.client_id,
                "_pubID": "aa:bb:cc:dd:ee:ff",
                "_sf": 256,  # Status flags?
                "_sv": "170.18",  # Software Version (I guess?)
                "model": "iPhone14,3",
                "name": "pyatv",
            },
        )

    async def _session_start(self) -> None:
        local_sid = randint(0, 2 ** 32 - 1)
        resp = await self._send_command(
            "_sessionStart", {"_srvT": "com.apple.tvremoteservices", "_sid": local_sid}
        )

        content = resp.get("_c")
        if content is None:
            raise exceptions.ProtocolError("missing content")

        remote_sid = cast(Mapping[str, Any], resp["_c"])["_sid"]
        self.sid = (remote_sid << 32) | local_sid
        _LOGGER.debug("Started session with SID 0x%X", self.sid)

    async def _session_stop(self) -> None:
        await self._send_command(
            "_sessionStop", {"_srvT": "com.apple.tvremoteservices", "_sid": self.sid}
        )
        _LOGGER.debug("Stopped session with SID 0x%X", self.sid)

    async def _send_event(self, identifier: str, content: Mapping[str, Any]) -> None:
        """Subscribe to updates to an event."""
        await self.connect()
        if self._protocol is None:
            raise RuntimeError("not connected to companion")

        try:
            self._protocol.send_opack(
                FrameType.E_OPACK,
                {
                    "_i": identifier,
                    "_t": MessageType.Event.value,
                    "_c": content,
                },
            )
        except exceptions.ProtocolError:
            raise
        except Exception as ex:
            raise exceptions.ProtocolError("Send event failed") from ex

    async def subscribe_event(self, event: str) -> None:
        """Subscribe to updates to an event."""
        await self._send_event("_interest", {"_regEvents": [event]})

    async def unsubscribe_event(self, event: str) -> None:
        """Subscribe to updates to an event."""
        await self._send_event("_interest", {"_deregEvents": [event]})

    async def launch_app(self, bundle_identifier: str) -> None:
        """Launch an app on the remote device."""
        await self._send_command("_launchApp", {"_bundleID": bundle_identifier})

    async def app_list(self) -> Mapping[str, Any]:
        """Return list of launchable apps on remote device."""
        return await self._send_command("FetchLaunchableApplicationsEvent", {})

    async def hid_command(self, down: bool, command: HidCommand) -> None:
        """Send a HID command."""
        await self._send_command(
            "_hidC", {"_hBtS": 1 if down else 2, "_hidC": command.value}
        )

    async def mediacontrol_command(
        self, command: MediaControlCommand, args: Optional[Mapping[str, Any]] = None
    ) -> Mapping[str, Any]:
        """Send a HID command."""
        return await self._send_command("_mcc", {"_mcc": command.value, **(args or {})})
