# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/RemoveEndpointsMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9pyatv/protocols/mrp/protobuf/RemoveEndpointsMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\".\n\x16RemoveEndpointsMessage\x12\x14\n\x0c\x65ndpointUIDs\x18\x01 \x03(\t:I\n\x16removeEndpointsMessage\x12\x10.ProtocolMessage\x18T \x01(\x0b\x32\x17.RemoveEndpointsMessage')


REMOVEENDPOINTSMESSAGE_FIELD_NUMBER = 84
removeEndpointsMessage = DESCRIPTOR.extensions_by_name['removeEndpointsMessage']

_REMOVEENDPOINTSMESSAGE = DESCRIPTOR.message_types_by_name['RemoveEndpointsMessage']
RemoveEndpointsMessage = _reflection.GeneratedProtocolMessageType('RemoveEndpointsMessage', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEENDPOINTSMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.RemoveEndpointsMessage_pb2'
  # @@protoc_insertion_point(class_scope:RemoveEndpointsMessage)
  })
_sym_db.RegisterMessage(RemoveEndpointsMessage)

if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(removeEndpointsMessage)

  DESCRIPTOR._options = None
  _REMOVEENDPOINTSMESSAGE._serialized_start=113
  _REMOVEENDPOINTSMESSAGE._serialized_end=159
# @@protoc_insertion_point(module_scope)
