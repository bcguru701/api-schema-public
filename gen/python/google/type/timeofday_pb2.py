# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/timeofday.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgoogle/type/timeofday.proto\x12\x0bgoogle.type\"K\n\tTimeOfDay\x12\r\n\x05hours\x18\x01 \x01(\x05\x12\x0f\n\x07minutes\x18\x02 \x01(\x05\x12\x0f\n\x07seconds\x18\x03 \x01(\x05\x12\r\n\x05nanos\x18\x04 \x01(\x05\x42l\n\x0f\x63om.google.typeB\x0eTimeOfDayProtoP\x01Z>google.golang.org/genproto/googleapis/type/timeofday;timeofday\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3')



_TIMEOFDAY = DESCRIPTOR.message_types_by_name['TimeOfDay']
TimeOfDay = _reflection.GeneratedProtocolMessageType('TimeOfDay', (_message.Message,), {
  'DESCRIPTOR' : _TIMEOFDAY,
  '__module__' : 'google.type.timeofday_pb2'
  # @@protoc_insertion_point(class_scope:google.type.TimeOfDay)
  })
_sym_db.RegisterMessage(TimeOfDay)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.google.typeB\016TimeOfDayProtoP\001Z>google.golang.org/genproto/googleapis/type/timeofday;timeofday\370\001\001\242\002\003GTP'
  _TIMEOFDAY._serialized_start=44
  _TIMEOFDAY._serialized_end=119
# @@protoc_insertion_point(module_scope)
