# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/SetNowPlayingClientMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.protocols.mrp.protobuf import NowPlayingClient_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=pyatv/protocols/mrp/protobuf/SetNowPlayingClientMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\x1a\x33pyatv/protocols/mrp/protobuf/NowPlayingClient.proto\"?\n\x1aSetNowPlayingClientMessage\x12!\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x11.NowPlayingClient:Q\n\x1asetNowPlayingClientMessage\x12\x10.ProtocolMessage\x18\x32 \x01(\x0b\x32\x1b.SetNowPlayingClientMessage')


SETNOWPLAYINGCLIENTMESSAGE_FIELD_NUMBER = 50
setNowPlayingClientMessage = DESCRIPTOR.extensions_by_name['setNowPlayingClientMessage']

_SETNOWPLAYINGCLIENTMESSAGE = DESCRIPTOR.message_types_by_name['SetNowPlayingClientMessage']
SetNowPlayingClientMessage = _reflection.GeneratedProtocolMessageType('SetNowPlayingClientMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETNOWPLAYINGCLIENTMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.SetNowPlayingClientMessage_pb2'
  # @@protoc_insertion_point(class_scope:SetNowPlayingClientMessage)
  })
_sym_db.RegisterMessage(SetNowPlayingClientMessage)

if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(setNowPlayingClientMessage)

  DESCRIPTOR._options = None
  _SETNOWPLAYINGCLIENTMESSAGE._serialized_start=170
  _SETNOWPLAYINGCLIENTMESSAGE._serialized_end=233
# @@protoc_insertion_point(module_scope)
