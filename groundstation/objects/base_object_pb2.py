# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groundstation/objects/base_object.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='groundstation/objects/base_object.proto',
  package='',
  serialized_pb='\n\'groundstation/objects/base_object.proto\"&\n\nBaseObject\x12\x18\n\x04type\x18\x0f \x02(\x0e\x32\n.GizmoType*8\n\tGizmoType\x12\x0b\n\x07REQUEST\x10\x00\x12\x0c\n\x08RESPONSE\x10\x01\x12\x10\n\x0cNOTIFICATION\x10\x02')

_GIZMOTYPE = _descriptor.EnumDescriptor(
  name='GizmoType',
  full_name='GizmoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTIFICATION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=83,
  serialized_end=139,
)

GizmoType = enum_type_wrapper.EnumTypeWrapper(_GIZMOTYPE)
REQUEST = 0
RESPONSE = 1
NOTIFICATION = 2



_BASEOBJECT = _descriptor.Descriptor(
  name='BaseObject',
  full_name='BaseObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='BaseObject.type', index=0,
      number=15, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=43,
  serialized_end=81,
)

_BASEOBJECT.fields_by_name['type'].enum_type = _GIZMOTYPE
DESCRIPTOR.message_types_by_name['BaseObject'] = _BASEOBJECT

class BaseObject(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BASEOBJECT

  # @@protoc_insertion_point(class_scope:BaseObject)


# @@protoc_insertion_point(module_scope)