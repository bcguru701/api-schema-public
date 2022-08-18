# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kentik/bgp_monitoring/v202205beta1/bgp_monitoring.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from kentik.core.v202012alpha1 import annotations_pb2 as kentik_dot_core_dot_v202012alpha1_dot_annotations__pb2
from kentik.ktrac.route.v202104 import elem_pb2 as kentik_dot_ktrac_dot_route_dot_v202104_dot_elem__pb2
from kentik.ktrac.route.v202104 import annotations_pb2 as kentik_dot_ktrac_dot_route_dot_v202104_dot_annotations__pb2
from kentik.synthetics.v202202 import synthetics_pb2 as kentik_dot_synthetics_dot_v202202_dot_synthetics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7kentik/bgp_monitoring/v202205beta1/bgp_monitoring.proto\x12\"kentik.bgp_monitoring.v202205beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a+kentik/core/v202012alpha1/annotations.proto\x1a%kentik/ktrac/route/v202104/elem.proto\x1a,kentik/ktrac/route/v202104/annotations.proto\x1a*kentik/synthetics/v202202/synthetics.proto\"\x91\x01\n\x04Nlri\x12\x31\n\x03\x61\x66i\x18\x01 \x01(\x0e\x32\x1f.kentik.ktrac.route.v202104.AfiR\x03\x61\x66i\x12\x34\n\x04safi\x18\x02 \x01(\x0e\x32 .kentik.ktrac.route.v202104.SafiR\x04safi\x12\x18\n\x06prefix\x18\x03 \x01(\tH\x00R\x06prefixB\x06\n\x04type\"{\n\x11\x42gpHealthSettings\x12\x31\n\x14reachability_warning\x18\x01 \x01(\x02R\x13reachabilityWarning\x12\x33\n\x15reachability_critical\x18\x02 \x01(\x02R\x14reachabilityCritical\"\xe9\x02\n\x12\x42gpMonitorSettings\x12!\n\x0c\x61llowed_asns\x18\x01 \x03(\rR\x0b\x61llowedAsns\x12\x42\n\x07targets\x18\x02 \x03(\x0b\x32(.kentik.bgp_monitoring.v202205beta1.NlriR\x07targets\x12\x1d\n\ncheck_rpki\x18\x03 \x01(\x08R\tcheckRpki\x12\x38\n\x18include_covered_prefixes\x18\x04 \x01(\x08R\x16includeCoveredPrefixes\x12^\n\x0fhealth_settings\x18\x05 \x01(\x0b\x32\x35.kentik.bgp_monitoring.v202205beta1.BgpHealthSettingsR\x0ehealthSettings\x12\x33\n\x15notification_channels\x18\x06 \x03(\tR\x14notificationChannels\"\xdf\x03\n\nBgpMonitor\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12L\n\x06status\x18\x03 \x01(\x0e\x32\x34.kentik.bgp_monitoring.v202205beta1.BgpMonitorStatusR\x06status\x12R\n\x08settings\x18\x04 \x01(\x0b\x32\x36.kentik.bgp_monitoring.v202205beta1.BgpMonitorSettingsR\x08settings\x12\x30\n\x05\x63\x64\x61te\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05\x63\x64\x61te\x12\x30\n\x05\x65\x64\x61te\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05\x65\x64\x61te\x12\x42\n\ncreated_by\x18\x07 \x01(\x0b\x32#.kentik.synthetics.v202202.UserInfoR\tcreatedBy\x12K\n\x0flast_updated_by\x18\x08 \x01(\x0b\x32#.kentik.synthetics.v202202.UserInfoR\rlastUpdatedBy\x12\x16\n\x06labels\x18\t \x03(\tR\x06labels\"\xdf\x03\n\tRouteInfo\x12<\n\x04nlri\x18\x01 \x01(\x0b\x32(.kentik.bgp_monitoring.v202205beta1.NlriR\x04nlri\x12U\n\norigin_asn\x18\x02 \x01(\rB6\x92\x41\x33\x32\x31The autonomous system number originating the NLRIR\toriginAsn\x12P\n\x07\x61s_path\x18\x03 \x03(\tB7\x92\x41\x34\x32\x32\x41S path observed at the vantage point for the NLRIR\x06\x61sPath\x12\x87\x01\n\rvantage_point\x18\x04 \x01(\x0b\x32(.kentik.ktrac.route.v202104.VantagePointB8\x92\x41\x35\x32\x33Name of the vantage point providing the observationR\x0cvantagePoint\x12G\n\x0brpki_status\x18\x05 \x01(\x0e\x32&.kentik.ktrac.route.v202104.RpkiStatusR\nrpkiStatus\x12\x18\n\x07nexthop\x18\x06 \x01(\tR\x07nexthop\"\xd6\x01\n\tBgpMetric\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12<\n\x04nlri\x18\x02 \x01(\x0b\x32(.kentik.bgp_monitoring.v202205beta1.NlriR\x04nlri\x12$\n\x0creachability\x18\x03 \x01(\x02H\x00R\x0creachability\x12#\n\x0cpath_changes\x18\x05 \x01(\rH\x00R\x0bpathChangesB\x06\n\x04type\"\x15\n\x13ListMonitorsRequest\"\x87\x01\n\x14ListMonitorsResponse\x12J\n\x08monitors\x18\x01 \x03(\x0b\x32..kentik.bgp_monitoring.v202205beta1.BgpMonitorR\x08monitors\x12#\n\rinvalid_count\x18\x02 \x01(\rR\x0cinvalidCount\"`\n\x14\x43reateMonitorRequest\x12H\n\x07monitor\x18\x01 \x01(\x0b\x32..kentik.bgp_monitoring.v202205beta1.BgpMonitorR\x07monitor\"a\n\x15\x43reateMonitorResponse\x12H\n\x07monitor\x18\x01 \x01(\x0b\x32..kentik.bgp_monitoring.v202205beta1.BgpMonitorR\x07monitor\"#\n\x11GetMonitorRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"^\n\x12GetMonitorResponse\x12H\n\x07monitor\x18\x01 \x01(\x0b\x32..kentik.bgp_monitoring.v202205beta1.BgpMonitorR\x07monitor\"`\n\x14UpdateMonitorRequest\x12H\n\x07monitor\x18\x01 \x01(\x0b\x32..kentik.bgp_monitoring.v202205beta1.BgpMonitorR\x07monitor\"a\n\x15UpdateMonitorResponse\x12H\n\x07monitor\x18\x01 \x01(\x0b\x32..kentik.bgp_monitoring.v202205beta1.BgpMonitorR\x07monitor\"&\n\x14\x44\x65leteMonitorRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x17\n\x15\x44\x65leteMonitorResponse\"w\n\x17SetMonitorStatusRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12L\n\x06status\x18\x02 \x01(\x0e\x32\x34.kentik.bgp_monitoring.v202205beta1.BgpMonitorStatusR\x06status\"\x1a\n\x18SetMonitorStatusResponse\"\xc6\x02\n\x1aGetMetricsForTargetRequest\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12@\n\x06target\x18\x03 \x01(\x0b\x32(.kentik.bgp_monitoring.v202205beta1.NlriR\x06target\x12\'\n\x0finclude_covered\x18\x04 \x01(\x08R\x0eincludeCovered\x12K\n\x07metrics\x18\x05 \x03(\x0e\x32\x31.kentik.bgp_monitoring.v202205beta1.BgpMetricTypeR\x07metrics\"f\n\x1bGetMetricsForTargetResponse\x12G\n\x07metrics\x18\x01 \x03(\x0b\x32-.kentik.bgp_monitoring.v202205beta1.BgpMetricR\x07metrics\"\xd5\x01\n\x19GetRoutesForTargetRequest\x12.\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04time\x12@\n\x06target\x18\x02 \x01(\x0b\x32(.kentik.bgp_monitoring.v202205beta1.NlriR\x06target\x12\'\n\x0finclude_covered\x18\x04 \x01(\x08R\x0eincludeCovered\x12\x1d\n\ncheck_rpki\x18\x05 \x01(\x08R\tcheckRpki\"\x87\x02\n\x1aGetRoutesForTargetResponse\x12\x45\n\x06routes\x18\x01 \x03(\x0b\x32-.kentik.bgp_monitoring.v202205beta1.RouteInfoR\x06routes\x12\x66\n\x08\x61s_names\x18\x05 \x03(\x0b\x32K.kentik.bgp_monitoring.v202205beta1.GetRoutesForTargetResponse.AsNamesEntryR\x07\x61sNames\x1a:\n\x0c\x41sNamesEntry\x12\x10\n\x03key\x18\x01 \x01(\rR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01*\x94\x01\n\x10\x42gpMonitorStatus\x12\"\n\x1e\x42GP_MONITOR_STATUS_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x42GP_MONITOR_STATUS_ACTIVE\x10\x01\x12\x1d\n\x19\x42GP_MONITOR_STATUS_PAUSED\x10\x02\x12\x1e\n\x1a\x42GP_MONITOR_STATUS_DELETED\x10\x03*t\n\rBgpMetricType\x12\x1f\n\x1b\x42GP_METRIC_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1c\x42GP_METRIC_TYPE_REACHABILITY\x10\x01\x12 \n\x1c\x42GP_METRIC_TYPE_PATH_CHANGES\x10\x02\x32\xc8\x0e\n\x19\x42gpMonitoringAdminService\x12\x90\x02\n\x0cListMonitors\x12\x37.kentik.bgp_monitoring.v202205beta1.ListMonitorsRequest\x1a\x38.kentik.bgp_monitoring.v202205beta1.ListMonitorsResponse\"\x8c\x01\x92\x41\x43\x12\x12List BGP Monitors.\x1a\x1fReturns a list of BGP monitors.*\x0cMonitorsList\xf2\xd7\x02\x15\x61\x64min.synthetics:read\x82\xd3\xe4\x93\x02\'\x12%/bgp_monitoring/v202205beta1/monitors\x12\xd0\x01\n\rCreateMonitor\x12\x38.kentik.bgp_monitoring.v202205beta1.CreateMonitorRequest\x1a\x39.kentik.bgp_monitoring.v202205beta1.CreateMonitorResponse\"J\xf2\xd7\x02\x16\x61\x64min.synthetics:write\x82\xd3\xe4\x93\x02*\"%/bgp_monitoring/v202205beta1/monitors:\x01*\x12\xaf\x02\n\nGetMonitor\x12\x35.kentik.bgp_monitoring.v202205beta1.GetMonitorRequest\x1a\x36.kentik.bgp_monitoring.v202205beta1.GetMonitorResponse\"\xb1\x01\x92\x41\x63\x12\x1eGet BGP Monitor configuration.\x1a\x35Return configuration of BGP monitor with specific ID.*\nMonitorGet\xf2\xd7\x02\x15\x61\x64min.synthetics:read\x82\xd3\xe4\x93\x02,\x12*/bgp_monitoring/v202205beta1/monitors/{id}\x12\xf2\x02\n\rUpdateMonitor\x12\x38.kentik.bgp_monitoring.v202205beta1.UpdateMonitorRequest\x1a\x39.kentik.bgp_monitoring.v202205beta1.UpdateMonitorResponse\"\xeb\x01\x92\x41\x90\x01\x12!Update BGP Monitor configuration.\x1a\\Update configuration of BGP monitor with specific ID. Returns updated monitor configuration.*\rMonitorUpdate\xf2\xd7\x02\x16\x61\x64min.synthetics:write\x82\xd3\xe4\x93\x02\x37\x1a\x32/bgp_monitoring/v202205beta1/monitors/{monitor.id}:\x01*\x12\xa6\x02\n\rDeleteMonitor\x12\x38.kentik.bgp_monitoring.v202205beta1.DeleteMonitorRequest\x1a\x39.kentik.bgp_monitoring.v202205beta1.DeleteMonitorResponse\"\x9f\x01\x92\x41P\x12\x13\x44\x65lete BGP Monitor.\x1a*Delete BGP monitor with  with specific ID.*\rMonitorDelete\xf2\xd7\x02\x16\x61\x64min.synthetics:write\x82\xd3\xe4\x93\x02,**/bgp_monitoring/v202205beta1/monitors/{id}\x12\xc8\x02\n\x10SetMonitorStatus\x12;.kentik.bgp_monitoring.v202205beta1.SetMonitorStatusRequest\x1a<.kentik.bgp_monitoring.v202205beta1.SetMonitorStatusResponse\"\xb8\x01\x92\x41_\x12\x1aSet status of BGP monitor.\x1a/Set the status of BGP monitor with specific ID.*\x10SetMonitorStatus\xf2\xd7\x02\x16\x61\x64min.synthetics:write\x82\xd3\xe4\x93\x02\x36\x1a\x31/bgp_monitoring/v202205beta1/monitors/{id}/status:\x01*\x1a*\xca\x41\x13grpc.api.kentik.com\xea\xd7\x02\x10\x61\x64min.synthetics2\x96\x06\n\x18\x42gpMonitoringDataService\x12\xeb\x02\n\x13GetMetricsForTarget\x12>.kentik.bgp_monitoring.v202205beta1.GetMetricsForTargetRequest\x1a?.kentik.bgp_monitoring.v202205beta1.GetMetricsForTargetResponse\"\xd2\x01\x92\x41\x8c\x01\x12-Get metrics for a single BGP target (prefix).\x1a\x46Retrieve metric data for single BGP target (prefix) and time interval.*\x13GetMetricsForTarget\xf2\xd7\x02\x0fsynthetics:read\x82\xd3\xe4\x93\x02)\"$/bgp_monitoring/v202205beta1/metrics:\x01*\x12\xe5\x02\n\x12GetRoutesForTarget\x12=.kentik.bgp_monitoring.v202205beta1.GetRoutesForTargetRequest\x1a>.kentik.bgp_monitoring.v202205beta1.GetRoutesForTargetResponse\"\xcf\x01\x92\x41\x8a\x01\x12*Get routes for single BGP target (prefix).\x1aHRetrieve route information for signle BGP target (prefix) and timestamp.*\x12GetRoutesForTarget\xf2\xd7\x02\x0fsynthetics:read\x82\xd3\xe4\x93\x02(\"#/bgp_monitoring/v202205beta1/routes:\x01*\x1a$\xca\x41\x13grpc.api.kentik.com\xea\xd7\x02\nsyntheticsB\xe5\x03ZUgithub.com/kentik/api-schema/gen/go/kentik/bgp_monitoring/v202205beta1;bgp_monitoring\x92\x41\x8a\x03\x12\x9d\x01\n\x12\x42GP Monitoring API\x12\x38\x41PI for interaction with Kentik BGP Monitoring Service.\n\"E\n\x16Kentik API Engineering\x12+https://github.com/kentik/api-schema-public2\x06\x32\x30\x32\x32\x30\x35*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZD\n\x1e\n\x05\x65mail\x12\x15\x08\x02\x1a\x0fX-CH-Auth-Email \x02\n\"\n\x05token\x12\x19\x08\x02\x1a\x13X-CH-Auth-API-Token \x02\x62\x16\n\t\n\x05\x65mail\x12\x00\n\t\n\x05token\x12\x00rc\n More about Kentik BGP monitoring\x12?https://kb.kentik.com/v4/Ma03.htm#Ma03-BGP_Monitor_Details_Pageb\x06proto3')

_BGPMONITORSTATUS = DESCRIPTOR.enum_types_by_name['BgpMonitorStatus']
BgpMonitorStatus = enum_type_wrapper.EnumTypeWrapper(_BGPMONITORSTATUS)
_BGPMETRICTYPE = DESCRIPTOR.enum_types_by_name['BgpMetricType']
BgpMetricType = enum_type_wrapper.EnumTypeWrapper(_BGPMETRICTYPE)
BGP_MONITOR_STATUS_UNSPECIFIED = 0
BGP_MONITOR_STATUS_ACTIVE = 1
BGP_MONITOR_STATUS_PAUSED = 2
BGP_MONITOR_STATUS_DELETED = 3
BGP_METRIC_TYPE_UNSPECIFIED = 0
BGP_METRIC_TYPE_REACHABILITY = 1
BGP_METRIC_TYPE_PATH_CHANGES = 2


_NLRI = DESCRIPTOR.message_types_by_name['Nlri']
_BGPHEALTHSETTINGS = DESCRIPTOR.message_types_by_name['BgpHealthSettings']
_BGPMONITORSETTINGS = DESCRIPTOR.message_types_by_name['BgpMonitorSettings']
_BGPMONITOR = DESCRIPTOR.message_types_by_name['BgpMonitor']
_ROUTEINFO = DESCRIPTOR.message_types_by_name['RouteInfo']
_BGPMETRIC = DESCRIPTOR.message_types_by_name['BgpMetric']
_LISTMONITORSREQUEST = DESCRIPTOR.message_types_by_name['ListMonitorsRequest']
_LISTMONITORSRESPONSE = DESCRIPTOR.message_types_by_name['ListMonitorsResponse']
_CREATEMONITORREQUEST = DESCRIPTOR.message_types_by_name['CreateMonitorRequest']
_CREATEMONITORRESPONSE = DESCRIPTOR.message_types_by_name['CreateMonitorResponse']
_GETMONITORREQUEST = DESCRIPTOR.message_types_by_name['GetMonitorRequest']
_GETMONITORRESPONSE = DESCRIPTOR.message_types_by_name['GetMonitorResponse']
_UPDATEMONITORREQUEST = DESCRIPTOR.message_types_by_name['UpdateMonitorRequest']
_UPDATEMONITORRESPONSE = DESCRIPTOR.message_types_by_name['UpdateMonitorResponse']
_DELETEMONITORREQUEST = DESCRIPTOR.message_types_by_name['DeleteMonitorRequest']
_DELETEMONITORRESPONSE = DESCRIPTOR.message_types_by_name['DeleteMonitorResponse']
_SETMONITORSTATUSREQUEST = DESCRIPTOR.message_types_by_name['SetMonitorStatusRequest']
_SETMONITORSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['SetMonitorStatusResponse']
_GETMETRICSFORTARGETREQUEST = DESCRIPTOR.message_types_by_name['GetMetricsForTargetRequest']
_GETMETRICSFORTARGETRESPONSE = DESCRIPTOR.message_types_by_name['GetMetricsForTargetResponse']
_GETROUTESFORTARGETREQUEST = DESCRIPTOR.message_types_by_name['GetRoutesForTargetRequest']
_GETROUTESFORTARGETRESPONSE = DESCRIPTOR.message_types_by_name['GetRoutesForTargetResponse']
_GETROUTESFORTARGETRESPONSE_ASNAMESENTRY = _GETROUTESFORTARGETRESPONSE.nested_types_by_name['AsNamesEntry']
Nlri = _reflection.GeneratedProtocolMessageType('Nlri', (_message.Message,), {
  'DESCRIPTOR' : _NLRI,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.Nlri)
  })
_sym_db.RegisterMessage(Nlri)

BgpHealthSettings = _reflection.GeneratedProtocolMessageType('BgpHealthSettings', (_message.Message,), {
  'DESCRIPTOR' : _BGPHEALTHSETTINGS,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.BgpHealthSettings)
  })
_sym_db.RegisterMessage(BgpHealthSettings)

BgpMonitorSettings = _reflection.GeneratedProtocolMessageType('BgpMonitorSettings', (_message.Message,), {
  'DESCRIPTOR' : _BGPMONITORSETTINGS,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.BgpMonitorSettings)
  })
_sym_db.RegisterMessage(BgpMonitorSettings)

BgpMonitor = _reflection.GeneratedProtocolMessageType('BgpMonitor', (_message.Message,), {
  'DESCRIPTOR' : _BGPMONITOR,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.BgpMonitor)
  })
_sym_db.RegisterMessage(BgpMonitor)

RouteInfo = _reflection.GeneratedProtocolMessageType('RouteInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEINFO,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.RouteInfo)
  })
_sym_db.RegisterMessage(RouteInfo)

BgpMetric = _reflection.GeneratedProtocolMessageType('BgpMetric', (_message.Message,), {
  'DESCRIPTOR' : _BGPMETRIC,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.BgpMetric)
  })
_sym_db.RegisterMessage(BgpMetric)

ListMonitorsRequest = _reflection.GeneratedProtocolMessageType('ListMonitorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMONITORSREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.ListMonitorsRequest)
  })
_sym_db.RegisterMessage(ListMonitorsRequest)

ListMonitorsResponse = _reflection.GeneratedProtocolMessageType('ListMonitorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMONITORSRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.ListMonitorsResponse)
  })
_sym_db.RegisterMessage(ListMonitorsResponse)

CreateMonitorRequest = _reflection.GeneratedProtocolMessageType('CreateMonitorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMONITORREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.CreateMonitorRequest)
  })
_sym_db.RegisterMessage(CreateMonitorRequest)

CreateMonitorResponse = _reflection.GeneratedProtocolMessageType('CreateMonitorResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMONITORRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.CreateMonitorResponse)
  })
_sym_db.RegisterMessage(CreateMonitorResponse)

GetMonitorRequest = _reflection.GeneratedProtocolMessageType('GetMonitorRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMONITORREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.GetMonitorRequest)
  })
_sym_db.RegisterMessage(GetMonitorRequest)

GetMonitorResponse = _reflection.GeneratedProtocolMessageType('GetMonitorResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMONITORRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.GetMonitorResponse)
  })
_sym_db.RegisterMessage(GetMonitorResponse)

UpdateMonitorRequest = _reflection.GeneratedProtocolMessageType('UpdateMonitorRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMONITORREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.UpdateMonitorRequest)
  })
_sym_db.RegisterMessage(UpdateMonitorRequest)

UpdateMonitorResponse = _reflection.GeneratedProtocolMessageType('UpdateMonitorResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMONITORRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.UpdateMonitorResponse)
  })
_sym_db.RegisterMessage(UpdateMonitorResponse)

DeleteMonitorRequest = _reflection.GeneratedProtocolMessageType('DeleteMonitorRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMONITORREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.DeleteMonitorRequest)
  })
_sym_db.RegisterMessage(DeleteMonitorRequest)

DeleteMonitorResponse = _reflection.GeneratedProtocolMessageType('DeleteMonitorResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMONITORRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.DeleteMonitorResponse)
  })
_sym_db.RegisterMessage(DeleteMonitorResponse)

SetMonitorStatusRequest = _reflection.GeneratedProtocolMessageType('SetMonitorStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETMONITORSTATUSREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.SetMonitorStatusRequest)
  })
_sym_db.RegisterMessage(SetMonitorStatusRequest)

SetMonitorStatusResponse = _reflection.GeneratedProtocolMessageType('SetMonitorStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETMONITORSTATUSRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.SetMonitorStatusResponse)
  })
_sym_db.RegisterMessage(SetMonitorStatusResponse)

GetMetricsForTargetRequest = _reflection.GeneratedProtocolMessageType('GetMetricsForTargetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMETRICSFORTARGETREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.GetMetricsForTargetRequest)
  })
_sym_db.RegisterMessage(GetMetricsForTargetRequest)

GetMetricsForTargetResponse = _reflection.GeneratedProtocolMessageType('GetMetricsForTargetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMETRICSFORTARGETRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.GetMetricsForTargetResponse)
  })
_sym_db.RegisterMessage(GetMetricsForTargetResponse)

GetRoutesForTargetRequest = _reflection.GeneratedProtocolMessageType('GetRoutesForTargetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETROUTESFORTARGETREQUEST,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.GetRoutesForTargetRequest)
  })
_sym_db.RegisterMessage(GetRoutesForTargetRequest)

GetRoutesForTargetResponse = _reflection.GeneratedProtocolMessageType('GetRoutesForTargetResponse', (_message.Message,), {

  'AsNamesEntry' : _reflection.GeneratedProtocolMessageType('AsNamesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETROUTESFORTARGETRESPONSE_ASNAMESENTRY,
    '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
    # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.GetRoutesForTargetResponse.AsNamesEntry)
    })
  ,
  'DESCRIPTOR' : _GETROUTESFORTARGETRESPONSE,
  '__module__' : 'kentik.bgp_monitoring.v202205beta1.bgp_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:kentik.bgp_monitoring.v202205beta1.GetRoutesForTargetResponse)
  })
_sym_db.RegisterMessage(GetRoutesForTargetResponse)
_sym_db.RegisterMessage(GetRoutesForTargetResponse.AsNamesEntry)

_BGPMONITORINGADMINSERVICE = DESCRIPTOR.services_by_name['BgpMonitoringAdminService']
_BGPMONITORINGDATASERVICE = DESCRIPTOR.services_by_name['BgpMonitoringDataService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZUgithub.com/kentik/api-schema/gen/go/kentik/bgp_monitoring/v202205beta1;bgp_monitoring\222A\212\003\022\235\001\n\022BGP Monitoring API\0228API for interaction with Kentik BGP Monitoring Service.\n\"E\n\026Kentik API Engineering\022+https://github.com/kentik/api-schema-public2\006202205*\001\0022\020application/json:\020application/jsonZD\n\036\n\005email\022\025\010\002\032\017X-CH-Auth-Email \002\n\"\n\005token\022\031\010\002\032\023X-CH-Auth-API-Token \002b\026\n\t\n\005email\022\000\n\t\n\005token\022\000rc\n More about Kentik BGP monitoring\022?https://kb.kentik.com/v4/Ma03.htm#Ma03-BGP_Monitor_Details_Page'
  _ROUTEINFO.fields_by_name['origin_asn']._options = None
  _ROUTEINFO.fields_by_name['origin_asn']._serialized_options = b'\222A321The autonomous system number originating the NLRI'
  _ROUTEINFO.fields_by_name['as_path']._options = None
  _ROUTEINFO.fields_by_name['as_path']._serialized_options = b'\222A422AS path observed at the vantage point for the NLRI'
  _ROUTEINFO.fields_by_name['vantage_point']._options = None
  _ROUTEINFO.fields_by_name['vantage_point']._serialized_options = b'\222A523Name of the vantage point providing the observation'
  _GETROUTESFORTARGETRESPONSE_ASNAMESENTRY._options = None
  _GETROUTESFORTARGETRESPONSE_ASNAMESENTRY._serialized_options = b'8\001'
  _BGPMONITORINGADMINSERVICE._options = None
  _BGPMONITORINGADMINSERVICE._serialized_options = b'\312A\023grpc.api.kentik.com\352\327\002\020admin.synthetics'
  _BGPMONITORINGADMINSERVICE.methods_by_name['ListMonitors']._options = None
  _BGPMONITORINGADMINSERVICE.methods_by_name['ListMonitors']._serialized_options = b'\222AC\022\022List BGP Monitors.\032\037Returns a list of BGP monitors.*\014MonitorsList\362\327\002\025admin.synthetics:read\202\323\344\223\002\'\022%/bgp_monitoring/v202205beta1/monitors'
  _BGPMONITORINGADMINSERVICE.methods_by_name['CreateMonitor']._options = None
  _BGPMONITORINGADMINSERVICE.methods_by_name['CreateMonitor']._serialized_options = b'\362\327\002\026admin.synthetics:write\202\323\344\223\002*\"%/bgp_monitoring/v202205beta1/monitors:\001*'
  _BGPMONITORINGADMINSERVICE.methods_by_name['GetMonitor']._options = None
  _BGPMONITORINGADMINSERVICE.methods_by_name['GetMonitor']._serialized_options = b'\222Ac\022\036Get BGP Monitor configuration.\0325Return configuration of BGP monitor with specific ID.*\nMonitorGet\362\327\002\025admin.synthetics:read\202\323\344\223\002,\022*/bgp_monitoring/v202205beta1/monitors/{id}'
  _BGPMONITORINGADMINSERVICE.methods_by_name['UpdateMonitor']._options = None
  _BGPMONITORINGADMINSERVICE.methods_by_name['UpdateMonitor']._serialized_options = b'\222A\220\001\022!Update BGP Monitor configuration.\032\\Update configuration of BGP monitor with specific ID. Returns updated monitor configuration.*\rMonitorUpdate\362\327\002\026admin.synthetics:write\202\323\344\223\0027\0322/bgp_monitoring/v202205beta1/monitors/{monitor.id}:\001*'
  _BGPMONITORINGADMINSERVICE.methods_by_name['DeleteMonitor']._options = None
  _BGPMONITORINGADMINSERVICE.methods_by_name['DeleteMonitor']._serialized_options = b'\222AP\022\023Delete BGP Monitor.\032*Delete BGP monitor with  with specific ID.*\rMonitorDelete\362\327\002\026admin.synthetics:write\202\323\344\223\002,**/bgp_monitoring/v202205beta1/monitors/{id}'
  _BGPMONITORINGADMINSERVICE.methods_by_name['SetMonitorStatus']._options = None
  _BGPMONITORINGADMINSERVICE.methods_by_name['SetMonitorStatus']._serialized_options = b'\222A_\022\032Set status of BGP monitor.\032/Set the status of BGP monitor with specific ID.*\020SetMonitorStatus\362\327\002\026admin.synthetics:write\202\323\344\223\0026\0321/bgp_monitoring/v202205beta1/monitors/{id}/status:\001*'
  _BGPMONITORINGDATASERVICE._options = None
  _BGPMONITORINGDATASERVICE._serialized_options = b'\312A\023grpc.api.kentik.com\352\327\002\nsynthetics'
  _BGPMONITORINGDATASERVICE.methods_by_name['GetMetricsForTarget']._options = None
  _BGPMONITORINGDATASERVICE.methods_by_name['GetMetricsForTarget']._serialized_options = b'\222A\214\001\022-Get metrics for a single BGP target (prefix).\032FRetrieve metric data for single BGP target (prefix) and time interval.*\023GetMetricsForTarget\362\327\002\017synthetics:read\202\323\344\223\002)\"$/bgp_monitoring/v202205beta1/metrics:\001*'
  _BGPMONITORINGDATASERVICE.methods_by_name['GetRoutesForTarget']._options = None
  _BGPMONITORINGDATASERVICE.methods_by_name['GetRoutesForTarget']._serialized_options = b'\222A\212\001\022*Get routes for single BGP target (prefix).\032HRetrieve route information for signle BGP target (prefix) and timestamp.*\022GetRoutesForTarget\362\327\002\017synthetics:read\202\323\344\223\002(\"#/bgp_monitoring/v202205beta1/routes:\001*'
  _BGPMONITORSTATUS._serialized_start=4041
  _BGPMONITORSTATUS._serialized_end=4189
  _BGPMETRICTYPE._serialized_start=4191
  _BGPMETRICTYPE._serialized_end=4307
  _NLRI._serialized_start=406
  _NLRI._serialized_end=551
  _BGPHEALTHSETTINGS._serialized_start=553
  _BGPHEALTHSETTINGS._serialized_end=676
  _BGPMONITORSETTINGS._serialized_start=679
  _BGPMONITORSETTINGS._serialized_end=1040
  _BGPMONITOR._serialized_start=1043
  _BGPMONITOR._serialized_end=1522
  _ROUTEINFO._serialized_start=1525
  _ROUTEINFO._serialized_end=2004
  _BGPMETRIC._serialized_start=2007
  _BGPMETRIC._serialized_end=2221
  _LISTMONITORSREQUEST._serialized_start=2223
  _LISTMONITORSREQUEST._serialized_end=2244
  _LISTMONITORSRESPONSE._serialized_start=2247
  _LISTMONITORSRESPONSE._serialized_end=2382
  _CREATEMONITORREQUEST._serialized_start=2384
  _CREATEMONITORREQUEST._serialized_end=2480
  _CREATEMONITORRESPONSE._serialized_start=2482
  _CREATEMONITORRESPONSE._serialized_end=2579
  _GETMONITORREQUEST._serialized_start=2581
  _GETMONITORREQUEST._serialized_end=2616
  _GETMONITORRESPONSE._serialized_start=2618
  _GETMONITORRESPONSE._serialized_end=2712
  _UPDATEMONITORREQUEST._serialized_start=2714
  _UPDATEMONITORREQUEST._serialized_end=2810
  _UPDATEMONITORRESPONSE._serialized_start=2812
  _UPDATEMONITORRESPONSE._serialized_end=2909
  _DELETEMONITORREQUEST._serialized_start=2911
  _DELETEMONITORREQUEST._serialized_end=2949
  _DELETEMONITORRESPONSE._serialized_start=2951
  _DELETEMONITORRESPONSE._serialized_end=2974
  _SETMONITORSTATUSREQUEST._serialized_start=2976
  _SETMONITORSTATUSREQUEST._serialized_end=3095
  _SETMONITORSTATUSRESPONSE._serialized_start=3097
  _SETMONITORSTATUSRESPONSE._serialized_end=3123
  _GETMETRICSFORTARGETREQUEST._serialized_start=3126
  _GETMETRICSFORTARGETREQUEST._serialized_end=3452
  _GETMETRICSFORTARGETRESPONSE._serialized_start=3454
  _GETMETRICSFORTARGETRESPONSE._serialized_end=3556
  _GETROUTESFORTARGETREQUEST._serialized_start=3559
  _GETROUTESFORTARGETREQUEST._serialized_end=3772
  _GETROUTESFORTARGETRESPONSE._serialized_start=3775
  _GETROUTESFORTARGETRESPONSE._serialized_end=4038
  _GETROUTESFORTARGETRESPONSE_ASNAMESENTRY._serialized_start=3980
  _GETROUTESFORTARGETRESPONSE_ASNAMESENTRY._serialized_end=4038
  _BGPMONITORINGADMINSERVICE._serialized_start=4310
  _BGPMONITORINGADMINSERVICE._serialized_end=6174
  _BGPMONITORINGDATASERVICE._serialized_start=6177
  _BGPMONITORINGDATASERVICE._serialized_end=6967
# @@protoc_insertion_point(module_scope)
