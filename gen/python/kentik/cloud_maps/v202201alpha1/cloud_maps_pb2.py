# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kentik/cloud_maps/v202201alpha1/cloud_maps.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import http_pb2 as google_dot_api_dot_http__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from kentik.core.v202012alpha1 import annotations_pb2 as kentik_dot_core_dot_v202012alpha1_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0kentik/cloud_maps/v202201alpha1/cloud_maps.proto\x12\x1fkentik.cloud_maps.v202201alpha1\x1a\x15google/api/http.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a+kentik/core/v202012alpha1/annotations.proto\"u\n(ProvideAwsMetadataStorageLocationRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1d\n\x15source_aws_account_id\x18\x02 \x01(\t\x12\x19\n\x11source_aws_region\x18\x03 \x01(\t\"?\n)ProvideAwsMetadataStorageLocationResponse\x12\x12\n\ntarget_url\x18\x01 \x01(\t\"n\n!GetAwsCrawlerConfigurationRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1d\n\x15source_aws_account_id\x18\x02 \x01(\t\x12\x19\n\x11source_aws_region\x18\x03 \x01(\t\"6\n\"GetAwsCrawlerConfigurationResponse\x12\x10\n\x08services\x18\x01 \x01(\t2\xf1\x06\n\x10\x43loudMapsService\x12\xa8\x03\n!ProvideAwsMetadataStorageLocation\x12I.kentik.cloud_maps.v202201alpha1.ProvideAwsMetadataStorageLocationRequest\x1aJ.kentik.cloud_maps.v202201alpha1.ProvideAwsMetadataStorageLocationResponse\"\xeb\x01\xf2\xd7\x02\x16\x61\x64min.cloud_maps:write\x82\xd3\xe4\x93\x02:\"5/cloud_maps/v202201alpha1/ingest/aws_storage_location:\x01*\x92\x41\x8d\x01\x12\'Provide location for given AWS metadata\x1a\x46Provides location at which the API client may store AWS cloud metadata*\x1a\x41wsMetadataStorageLocation\x12\x85\x03\n\x1aGetAwsCrawlerConfiguration\x12\x42.kentik.cloud_maps.v202201alpha1.GetAwsCrawlerConfigurationRequest\x1a\x43.kentik.cloud_maps.v202201alpha1.GetAwsCrawlerConfigurationResponse\"\xdd\x01\xf2\xd7\x02\x15\x61\x64min.cloud_maps:read\x82\xd3\xe4\x93\x02\x37\"2/cloud_maps/v202201alpha1/ingest/aws_configuration:\x01*\x92\x41\x83\x01\x12\x1dGet AWS crawler configuration\x1aPGet AWS crawler configuration that determines what AWS cloud metadata to collect*\x10\x41wsConfiguration\x1a*\xca\x41\x13grpc.api.kentik.com\xea\xd7\x02\x10\x61\x64min.cloud_mapsB\xca\x02ZNgithub.com/kentik/api-schema/gen/go/kentik/cloud_maps/v202201alpha1;cloud_maps\x92\x41\xf6\x01\x12\x38\n\x0e\x43loud Maps API\"\x18\n\x16Kentik API Engineering2\x0c\x32\x30\x32\x32\x30\x31\x61lpha1*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZD\n\x1e\n\x05\x65mail\x12\x15\x08\x02\x1a\x0fX-CH-Auth-Email \x02\n\"\n\x05token\x12\x19\x08\x02\x1a\x13X-CH-Auth-API-Token \x02\x62\x16\n\t\n\x05\x65mail\x12\x00\n\t\n\x05token\x12\x00r5\n\x16More about Kentik APIs\x12\x1bhttps://docs.kentik.com/apib\x06proto3')



_PROVIDEAWSMETADATASTORAGELOCATIONREQUEST = DESCRIPTOR.message_types_by_name['ProvideAwsMetadataStorageLocationRequest']
_PROVIDEAWSMETADATASTORAGELOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['ProvideAwsMetadataStorageLocationResponse']
_GETAWSCRAWLERCONFIGURATIONREQUEST = DESCRIPTOR.message_types_by_name['GetAwsCrawlerConfigurationRequest']
_GETAWSCRAWLERCONFIGURATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetAwsCrawlerConfigurationResponse']
ProvideAwsMetadataStorageLocationRequest = _reflection.GeneratedProtocolMessageType('ProvideAwsMetadataStorageLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEAWSMETADATASTORAGELOCATIONREQUEST,
  '__module__' : 'kentik.cloud_maps.v202201alpha1.cloud_maps_pb2'
  # @@protoc_insertion_point(class_scope:kentik.cloud_maps.v202201alpha1.ProvideAwsMetadataStorageLocationRequest)
  })
_sym_db.RegisterMessage(ProvideAwsMetadataStorageLocationRequest)

ProvideAwsMetadataStorageLocationResponse = _reflection.GeneratedProtocolMessageType('ProvideAwsMetadataStorageLocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEAWSMETADATASTORAGELOCATIONRESPONSE,
  '__module__' : 'kentik.cloud_maps.v202201alpha1.cloud_maps_pb2'
  # @@protoc_insertion_point(class_scope:kentik.cloud_maps.v202201alpha1.ProvideAwsMetadataStorageLocationResponse)
  })
_sym_db.RegisterMessage(ProvideAwsMetadataStorageLocationResponse)

GetAwsCrawlerConfigurationRequest = _reflection.GeneratedProtocolMessageType('GetAwsCrawlerConfigurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAWSCRAWLERCONFIGURATIONREQUEST,
  '__module__' : 'kentik.cloud_maps.v202201alpha1.cloud_maps_pb2'
  # @@protoc_insertion_point(class_scope:kentik.cloud_maps.v202201alpha1.GetAwsCrawlerConfigurationRequest)
  })
_sym_db.RegisterMessage(GetAwsCrawlerConfigurationRequest)

GetAwsCrawlerConfigurationResponse = _reflection.GeneratedProtocolMessageType('GetAwsCrawlerConfigurationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAWSCRAWLERCONFIGURATIONRESPONSE,
  '__module__' : 'kentik.cloud_maps.v202201alpha1.cloud_maps_pb2'
  # @@protoc_insertion_point(class_scope:kentik.cloud_maps.v202201alpha1.GetAwsCrawlerConfigurationResponse)
  })
_sym_db.RegisterMessage(GetAwsCrawlerConfigurationResponse)

_CLOUDMAPSSERVICE = DESCRIPTOR.services_by_name['CloudMapsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZNgithub.com/kentik/api-schema/gen/go/kentik/cloud_maps/v202201alpha1;cloud_maps\222A\366\001\0228\n\016Cloud Maps API\"\030\n\026Kentik API Engineering2\014202201alpha1*\001\0022\020application/json:\020application/jsonZD\n\036\n\005email\022\025\010\002\032\017X-CH-Auth-Email \002\n\"\n\005token\022\031\010\002\032\023X-CH-Auth-API-Token \002b\026\n\t\n\005email\022\000\n\t\n\005token\022\000r5\n\026More about Kentik APIs\022\033https://docs.kentik.com/api'
  _CLOUDMAPSSERVICE._options = None
  _CLOUDMAPSSERVICE._serialized_options = b'\312A\023grpc.api.kentik.com\352\327\002\020admin.cloud_maps'
  _CLOUDMAPSSERVICE.methods_by_name['ProvideAwsMetadataStorageLocation']._options = None
  _CLOUDMAPSSERVICE.methods_by_name['ProvideAwsMetadataStorageLocation']._serialized_options = b'\362\327\002\026admin.cloud_maps:write\202\323\344\223\002:\"5/cloud_maps/v202201alpha1/ingest/aws_storage_location:\001*\222A\215\001\022\'Provide location for given AWS metadata\032FProvides location at which the API client may store AWS cloud metadata*\032AwsMetadataStorageLocation'
  _CLOUDMAPSSERVICE.methods_by_name['GetAwsCrawlerConfiguration']._options = None
  _CLOUDMAPSSERVICE.methods_by_name['GetAwsCrawlerConfiguration']._serialized_options = b'\362\327\002\025admin.cloud_maps:read\202\323\344\223\0027\"2/cloud_maps/v202201alpha1/ingest/aws_configuration:\001*\222A\203\001\022\035Get AWS crawler configuration\032PGet AWS crawler configuration that determines what AWS cloud metadata to collect*\020AwsConfiguration'
  _PROVIDEAWSMETADATASTORAGELOCATIONREQUEST._serialized_start=256
  _PROVIDEAWSMETADATASTORAGELOCATIONREQUEST._serialized_end=373
  _PROVIDEAWSMETADATASTORAGELOCATIONRESPONSE._serialized_start=375
  _PROVIDEAWSMETADATASTORAGELOCATIONRESPONSE._serialized_end=438
  _GETAWSCRAWLERCONFIGURATIONREQUEST._serialized_start=440
  _GETAWSCRAWLERCONFIGURATIONREQUEST._serialized_end=550
  _GETAWSCRAWLERCONFIGURATIONRESPONSE._serialized_start=552
  _GETAWSCRAWLERCONFIGURATIONRESPONSE._serialized_end=606
  _CLOUDMAPSSERVICE._serialized_start=609
  _CLOUDMAPSSERVICE._serialized_end=1490
# @@protoc_insertion_point(module_scope)
