"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.Common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class NowPlayingInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ALBUM_FIELD_NUMBER: builtins.int
    ARTIST_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    ELAPSEDTIME_FIELD_NUMBER: builtins.int
    PLAYBACKRATE_FIELD_NUMBER: builtins.int
    REPEATMODE_FIELD_NUMBER: builtins.int
    SHUFFLEMODE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    UNIQUEIDENTIFIER_FIELD_NUMBER: builtins.int
    ISEXPLICITTRACK_FIELD_NUMBER: builtins.int
    ISMUSICAPP_FIELD_NUMBER: builtins.int
    RADIOSTATIONIDENTIFIER_FIELD_NUMBER: builtins.int
    RADIOSTATIONHASH_FIELD_NUMBER: builtins.int
    RADIOSTATIONNAME_FIELD_NUMBER: builtins.int
    ARTWORKDATADIGEST_FIELD_NUMBER: builtins.int
    ISALWAYSLIVE_FIELD_NUMBER: builtins.int
    ISADVERTISEMENT_FIELD_NUMBER: builtins.int
    album: typing.Text = ...
    artist: typing.Text = ...
    duration: builtins.float = ...
    elapsedTime: builtins.float = ...
    playbackRate: builtins.float = ...
    repeatMode: pyatv.protocols.mrp.protobuf.Common_pb2.RepeatMode.Enum.ValueType = ...
    shuffleMode: pyatv.protocols.mrp.protobuf.Common_pb2.ShuffleMode.Enum.ValueType = ...
    timestamp: builtins.float = ...
    title: typing.Text = ...
    uniqueIdentifier: builtins.int = ...
    isExplicitTrack: builtins.bool = ...
    isMusicApp: builtins.bool = ...
    radioStationIdentifier: builtins.int = ...
    radioStationHash: typing.Text = ...
    radioStationName: typing.Text = ...
    artworkDataDigest: builtins.bytes = ...
    isAlwaysLive: builtins.bool = ...
    isAdvertisement: builtins.bool = ...
    def __init__(self,
        *,
        album : typing.Optional[typing.Text] = ...,
        artist : typing.Optional[typing.Text] = ...,
        duration : typing.Optional[builtins.float] = ...,
        elapsedTime : typing.Optional[builtins.float] = ...,
        playbackRate : typing.Optional[builtins.float] = ...,
        repeatMode : typing.Optional[pyatv.protocols.mrp.protobuf.Common_pb2.RepeatMode.Enum.ValueType] = ...,
        shuffleMode : typing.Optional[pyatv.protocols.mrp.protobuf.Common_pb2.ShuffleMode.Enum.ValueType] = ...,
        timestamp : typing.Optional[builtins.float] = ...,
        title : typing.Optional[typing.Text] = ...,
        uniqueIdentifier : typing.Optional[builtins.int] = ...,
        isExplicitTrack : typing.Optional[builtins.bool] = ...,
        isMusicApp : typing.Optional[builtins.bool] = ...,
        radioStationIdentifier : typing.Optional[builtins.int] = ...,
        radioStationHash : typing.Optional[typing.Text] = ...,
        radioStationName : typing.Optional[typing.Text] = ...,
        artworkDataDigest : typing.Optional[builtins.bytes] = ...,
        isAlwaysLive : typing.Optional[builtins.bool] = ...,
        isAdvertisement : typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["album",b"album","artist",b"artist","artworkDataDigest",b"artworkDataDigest","duration",b"duration","elapsedTime",b"elapsedTime","isAdvertisement",b"isAdvertisement","isAlwaysLive",b"isAlwaysLive","isExplicitTrack",b"isExplicitTrack","isMusicApp",b"isMusicApp","playbackRate",b"playbackRate","radioStationHash",b"radioStationHash","radioStationIdentifier",b"radioStationIdentifier","radioStationName",b"radioStationName","repeatMode",b"repeatMode","shuffleMode",b"shuffleMode","timestamp",b"timestamp","title",b"title","uniqueIdentifier",b"uniqueIdentifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["album",b"album","artist",b"artist","artworkDataDigest",b"artworkDataDigest","duration",b"duration","elapsedTime",b"elapsedTime","isAdvertisement",b"isAdvertisement","isAlwaysLive",b"isAlwaysLive","isExplicitTrack",b"isExplicitTrack","isMusicApp",b"isMusicApp","playbackRate",b"playbackRate","radioStationHash",b"radioStationHash","radioStationIdentifier",b"radioStationIdentifier","radioStationName",b"radioStationName","repeatMode",b"repeatMode","shuffleMode",b"shuffleMode","timestamp",b"timestamp","title",b"title","uniqueIdentifier",b"uniqueIdentifier"]) -> None: ...
global___NowPlayingInfo = NowPlayingInfo
