# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='groundstation/objects/update_object.proto',
  package='',
  serialized_pb='\n)groundstation/objects/update_object.proto\":\n\x0cUpdateObject\x12\x0c\n\x04sha1\x18\x01 \x02(\x0c\x12\x0e\n\x06parent\x18\x02 \x03(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\x0c')




_UPDATEOBJECT = descriptor.Descriptor(
  name='UpdateObject',
  full_name='UpdateObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sha1', full_name='UpdateObject.sha1', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='parent', full_name='UpdateObject.parent', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='UpdateObject.data', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=45,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['UpdateObject'] = _UPDATEOBJECT

class UpdateObject(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEOBJECT
  
  # @@protoc_insertion_point(class_scope:UpdateObject)

# @@protoc_insertion_point(module_scope)
