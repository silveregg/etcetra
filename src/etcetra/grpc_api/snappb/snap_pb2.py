# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: snap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from etcetra.grpc_api.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nsnap.proto\x12\x06snappb\x1a\x14gogoproto/gogo.proto\"+\n\x08snapshot\x12\x11\n\x03\x63rc\x18\x01 \x01(\rB\x04\xc8\xde\x1f\x00\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x42\x10\xc8\xe2\x1e\x01\xe0\xe2\x1e\x01\xd0\xe2\x1e\x01\xc8\xe1\x1e\x00')
_descriptor_pool.Default()._internal_db._file_desc_protos_by_file['snappb/snap.proto'] = DESCRIPTOR


_SNAPSHOT = DESCRIPTOR.message_types_by_name['snapshot']
snapshot = _reflection.GeneratedProtocolMessageType('snapshot', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOT,
  '__module__' : 'snap_pb2'
  # @@protoc_insertion_point(class_scope:snappb.snapshot)
  })
_sym_db.RegisterMessage(snapshot)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\310\342\036\001\340\342\036\001\320\342\036\001\310\341\036\000'
  _SNAPSHOT.fields_by_name['crc']._options = None
  _SNAPSHOT.fields_by_name['crc']._serialized_options = b'\310\336\037\000'
  _SNAPSHOT._serialized_start=44
  _SNAPSHOT._serialized_end=87
# @@protoc_insertion_point(module_scope)
