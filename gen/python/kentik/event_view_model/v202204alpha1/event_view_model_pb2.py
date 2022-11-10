# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kentik/event_view_model/v202204alpha1/event_view_model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from kentik.core.v202012alpha1 import annotations_pb2 as kentik_dot_core_dot_v202012alpha1_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<kentik/event_view_model/v202204alpha1/event_view_model.proto\x12%kentik.event_view_model.v202204alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a+kentik/core/v202012alpha1/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x1c\n\nAlarmEvent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"!\n\x0fMitigationEvent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x1e\n\x0cInsightEvent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x94\x02\n\x13GetViewModelRequest\x12I\n\x05\x61larm\x18\x02 \x01(\x0b\x32\x31.kentik.event_view_model.v202204alpha1.AlarmEventH\x00R\x05\x61larm\x12X\n\nmitigation\x18\x03 \x01(\x0b\x32\x36.kentik.event_view_model.v202204alpha1.MitigationEventH\x00R\nmitigation\x12O\n\x07insight\x18\x04 \x01(\x0b\x32\x33.kentik.event_view_model.v202204alpha1.InsightEventH\x00R\x07insightB\x07\n\x05\x65vent\"{\n\x0f\x45ventViewDetail\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12\x10\n\x03tag\x18\x03 \x01(\tR\x03tag\x12,\n\x05value\x18\x04 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value\"\x9b\x04\n\x0e\x45ventViewModel\x12H\n\x04type\x18\x01 \x01(\x0e\x32\x34.kentik.event_view_model.v202204alpha1.EventViewTypeR\x04type\x12\x14\n\x05group\x18\x02 \x01(\tR\x05group\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1b\n\tis_active\x18\x04 \x01(\x08R\x08isActive\x12\x39\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12#\n\rcurrent_state\x18\x07 \x01(\tR\x0c\x63urrentState\x12%\n\x0eprevious_state\x18\x08 \x01(\tR\rpreviousState\x12Z\n\nimportance\x18\t \x01(\x0e\x32:.kentik.event_view_model.v202204alpha1.EventViewImportanceR\nimportance\x12P\n\x07\x64\x65tails\x18\n \x03(\x0b\x32\x36.kentik.event_view_model.v202204alpha1.EventViewDetailR\x07\x64\x65tails\"c\n\x14GetViewModelResponse\x12K\n\x05model\x18\x01 \x01(\x0b\x32\x35.kentik.event_view_model.v202204alpha1.EventViewModelR\x05model*\xcb\x01\n\rEventViewType\x12\x1f\n\x1b\x45VENT_VIEW_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x45VENT_VIEW_TYPE_ALERT\x10\x01\x12\x1e\n\x1a\x45VENT_VIEW_TYPE_MITIGATION\x10\x02\x12\x1d\n\x19\x45VENT_VIEW_TYPE_SYNTHETIC\x10\x03\x12\x1b\n\x17\x45VENT_VIEW_TYPE_INSIGHT\x10\x04\x12\"\n\x1e\x45VENT_VIEW_TYPE_CUSTOM_INSIGHT\x10\x05*\xac\x02\n\x13\x45ventViewImportance\x12%\n!EVENT_VIEW_IMPORTANCE_UNSPECIFIED\x10\x00\x12!\n\x1d\x45VENT_VIEW_IMPORTANCE_HEALTHY\x10\x01\x12 \n\x1c\x45VENT_VIEW_IMPORTANCE_NOTICE\x10\x02\x12\x1f\n\x1b\x45VENT_VIEW_IMPORTANCE_MINOR\x10\x03\x12!\n\x1d\x45VENT_VIEW_IMPORTANCE_WARNING\x10\x04\x12\x1f\n\x1b\x45VENT_VIEW_IMPORTANCE_MAJOR\x10\x05\x12 \n\x1c\x45VENT_VIEW_IMPORTANCE_SEVERE\x10\x06\x12\"\n\x1e\x45VENT_VIEW_IMPORTANCE_CRITICAL\x10\x07\x32\x97\x03\n\x15\x45ventViewModelService\x12\xe1\x02\n\x0cGetViewModel\x12:.kentik.event_view_model.v202204alpha1.GetViewModelRequest\x1a;.kentik.event_view_model.v202204alpha1.GetViewModelResponse\"\xd7\x01\x92\x41\x98\x01\x12MEvent view model will provide event context necessary to render notifications\x1a\x39GetViewModel will provide event view model data structure*\x0cGetViewModel\x82\xd3\xe4\x93\x02\x35\"0/event_view_model/v202204alpha1/event_view_model:\x01*\x1a\x1a\xca\x41\x13grpc.api.kentik.com\xf8\xd7\x02\x01\x42\xfc\x01ZZgithub.com/kentik/api-schema/gen/go/kentik/event_view_model/v202204alpha1;event_view_model\x92\x41\x9c\x01\x12<\n\x12\x45ventViewModel API\"\x18\n\x16Kentik API Engineering2\x0c\x32\x30\x32\x32\x30\x34\x61lpha1*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonr5\n\x16More about Kentik APIs\x12\x1bhttps://docs.kentik.com/apib\x06proto3')

_EVENTVIEWTYPE = DESCRIPTOR.enum_types_by_name['EventViewType']
EventViewType = enum_type_wrapper.EnumTypeWrapper(_EVENTVIEWTYPE)
_EVENTVIEWIMPORTANCE = DESCRIPTOR.enum_types_by_name['EventViewImportance']
EventViewImportance = enum_type_wrapper.EnumTypeWrapper(_EVENTVIEWIMPORTANCE)
EVENT_VIEW_TYPE_UNSPECIFIED = 0
EVENT_VIEW_TYPE_ALERT = 1
EVENT_VIEW_TYPE_MITIGATION = 2
EVENT_VIEW_TYPE_SYNTHETIC = 3
EVENT_VIEW_TYPE_INSIGHT = 4
EVENT_VIEW_TYPE_CUSTOM_INSIGHT = 5
EVENT_VIEW_IMPORTANCE_UNSPECIFIED = 0
EVENT_VIEW_IMPORTANCE_HEALTHY = 1
EVENT_VIEW_IMPORTANCE_NOTICE = 2
EVENT_VIEW_IMPORTANCE_MINOR = 3
EVENT_VIEW_IMPORTANCE_WARNING = 4
EVENT_VIEW_IMPORTANCE_MAJOR = 5
EVENT_VIEW_IMPORTANCE_SEVERE = 6
EVENT_VIEW_IMPORTANCE_CRITICAL = 7


_ALARMEVENT = DESCRIPTOR.message_types_by_name['AlarmEvent']
_MITIGATIONEVENT = DESCRIPTOR.message_types_by_name['MitigationEvent']
_INSIGHTEVENT = DESCRIPTOR.message_types_by_name['InsightEvent']
_GETVIEWMODELREQUEST = DESCRIPTOR.message_types_by_name['GetViewModelRequest']
_EVENTVIEWDETAIL = DESCRIPTOR.message_types_by_name['EventViewDetail']
_EVENTVIEWMODEL = DESCRIPTOR.message_types_by_name['EventViewModel']
_GETVIEWMODELRESPONSE = DESCRIPTOR.message_types_by_name['GetViewModelResponse']
AlarmEvent = _reflection.GeneratedProtocolMessageType('AlarmEvent', (_message.Message,), {
  'DESCRIPTOR' : _ALARMEVENT,
  '__module__' : 'kentik.event_view_model.v202204alpha1.event_view_model_pb2'
  # @@protoc_insertion_point(class_scope:kentik.event_view_model.v202204alpha1.AlarmEvent)
  })
_sym_db.RegisterMessage(AlarmEvent)

MitigationEvent = _reflection.GeneratedProtocolMessageType('MitigationEvent', (_message.Message,), {
  'DESCRIPTOR' : _MITIGATIONEVENT,
  '__module__' : 'kentik.event_view_model.v202204alpha1.event_view_model_pb2'
  # @@protoc_insertion_point(class_scope:kentik.event_view_model.v202204alpha1.MitigationEvent)
  })
_sym_db.RegisterMessage(MitigationEvent)

InsightEvent = _reflection.GeneratedProtocolMessageType('InsightEvent', (_message.Message,), {
  'DESCRIPTOR' : _INSIGHTEVENT,
  '__module__' : 'kentik.event_view_model.v202204alpha1.event_view_model_pb2'
  # @@protoc_insertion_point(class_scope:kentik.event_view_model.v202204alpha1.InsightEvent)
  })
_sym_db.RegisterMessage(InsightEvent)

GetViewModelRequest = _reflection.GeneratedProtocolMessageType('GetViewModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVIEWMODELREQUEST,
  '__module__' : 'kentik.event_view_model.v202204alpha1.event_view_model_pb2'
  # @@protoc_insertion_point(class_scope:kentik.event_view_model.v202204alpha1.GetViewModelRequest)
  })
_sym_db.RegisterMessage(GetViewModelRequest)

EventViewDetail = _reflection.GeneratedProtocolMessageType('EventViewDetail', (_message.Message,), {
  'DESCRIPTOR' : _EVENTVIEWDETAIL,
  '__module__' : 'kentik.event_view_model.v202204alpha1.event_view_model_pb2'
  # @@protoc_insertion_point(class_scope:kentik.event_view_model.v202204alpha1.EventViewDetail)
  })
_sym_db.RegisterMessage(EventViewDetail)

EventViewModel = _reflection.GeneratedProtocolMessageType('EventViewModel', (_message.Message,), {
  'DESCRIPTOR' : _EVENTVIEWMODEL,
  '__module__' : 'kentik.event_view_model.v202204alpha1.event_view_model_pb2'
  # @@protoc_insertion_point(class_scope:kentik.event_view_model.v202204alpha1.EventViewModel)
  })
_sym_db.RegisterMessage(EventViewModel)

GetViewModelResponse = _reflection.GeneratedProtocolMessageType('GetViewModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVIEWMODELRESPONSE,
  '__module__' : 'kentik.event_view_model.v202204alpha1.event_view_model_pb2'
  # @@protoc_insertion_point(class_scope:kentik.event_view_model.v202204alpha1.GetViewModelResponse)
  })
_sym_db.RegisterMessage(GetViewModelResponse)

_EVENTVIEWMODELSERVICE = DESCRIPTOR.services_by_name['EventViewModelService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZZgithub.com/kentik/api-schema/gen/go/kentik/event_view_model/v202204alpha1;event_view_model\222A\234\001\022<\n\022EventViewModel API\"\030\n\026Kentik API Engineering2\014202204alpha1*\001\0022\020application/json:\020application/jsonr5\n\026More about Kentik APIs\022\033https://docs.kentik.com/api'
  _EVENTVIEWMODELSERVICE._options = None
  _EVENTVIEWMODELSERVICE._serialized_options = b'\312A\023grpc.api.kentik.com\370\327\002\001'
  _EVENTVIEWMODELSERVICE.methods_by_name['GetViewModel']._options = None
  _EVENTVIEWMODELSERVICE.methods_by_name['GetViewModel']._serialized_options = b'\222A\230\001\022MEvent view model will provide event context necessary to render notifications\0329GetViewModel will provide event view model data structure*\014GetViewModel\202\323\344\223\0025\"0/event_view_model/v202204alpha1/event_view_model:\001*'
  _EVENTVIEWTYPE._serialized_start=1459
  _EVENTVIEWTYPE._serialized_end=1662
  _EVENTVIEWIMPORTANCE._serialized_start=1665
  _EVENTVIEWIMPORTANCE._serialized_end=1965
  _ALARMEVENT._serialized_start=314
  _ALARMEVENT._serialized_end=342
  _MITIGATIONEVENT._serialized_start=344
  _MITIGATIONEVENT._serialized_end=377
  _INSIGHTEVENT._serialized_start=379
  _INSIGHTEVENT._serialized_end=409
  _GETVIEWMODELREQUEST._serialized_start=412
  _GETVIEWMODELREQUEST._serialized_end=688
  _EVENTVIEWDETAIL._serialized_start=690
  _EVENTVIEWDETAIL._serialized_end=813
  _EVENTVIEWMODEL._serialized_start=816
  _EVENTVIEWMODEL._serialized_end=1355
  _GETVIEWMODELRESPONSE._serialized_start=1357
  _GETVIEWMODELRESPONSE._serialized_end=1456
  _EVENTVIEWMODELSERVICE._serialized_start=1968
  _EVENTVIEWMODELSERVICE._serialized_end=2375
# @@protoc_insertion_point(module_scope)
