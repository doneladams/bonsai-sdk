# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bonsai/proto/inkling_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bonsai/proto/inkling_types.proto',
  package='bonsai.inkling_types.proto',
  syntax='proto3',
  serialized_pb=_b('\n bonsai/proto/inkling_types.proto\x12\x1a\x62onsai.inkling_types.proto\":\n\tLuminance\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0e\n\x06pixels\x18\x03 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LUMINANCE = _descriptor.Descriptor(
  name='Luminance',
  full_name='bonsai.inkling_types.proto.Luminance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='bonsai.inkling_types.proto.Luminance.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='bonsai.inkling_types.proto.Luminance.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pixels', full_name='bonsai.inkling_types.proto.Luminance.pixels', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['Luminance'] = _LUMINANCE

Luminance = _reflection.GeneratedProtocolMessageType('Luminance', (_message.Message,), dict(
  DESCRIPTOR = _LUMINANCE,
  __module__ = 'bonsai.proto.inkling_types_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.inkling_types.proto.Luminance)
  ))
_sym_db.RegisterMessage(Luminance)


# @@protoc_insertion_point(module_scope)