# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/SavedDataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.protos.feast.core import DataSource_pb2 as feast_dot_core_dot_DataSource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66\x65\x61st/core/SavedDataset.proto\x12\nfeast.core\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1b\x66\x65\x61st/core/DataSource.proto\"\xa5\x02\n\x10SavedDatasetSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x03 \x03(\t\x12\x11\n\tjoin_keys\x18\x04 \x03(\t\x12\x1a\n\x12\x66ull_feature_names\x18\x05 \x01(\x08\x12\x30\n\x07storage\x18\x06 \x01(\x0b\x32\x1f.feast.core.SavedDatasetStorage\x12\x1c\n\x14\x66\x65\x61ture_service_name\x18\x08 \x01(\t\x12\x34\n\x04tags\x18\x07 \x03(\x0b\x32&.feast.core.SavedDatasetSpec.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe3\x03\n\x13SavedDatasetStorage\x12:\n\x0c\x66ile_storage\x18\x04 \x01(\x0b\x32\".feast.core.DataSource.FileOptionsH\x00\x12\x42\n\x10\x62igquery_storage\x18\x05 \x01(\x0b\x32&.feast.core.DataSource.BigQueryOptionsH\x00\x12\x42\n\x10redshift_storage\x18\x06 \x01(\x0b\x32&.feast.core.DataSource.RedshiftOptionsH\x00\x12\x44\n\x11snowflake_storage\x18\x07 \x01(\x0b\x32\'.feast.core.DataSource.SnowflakeOptionsH\x00\x12<\n\rtrino_storage\x18\x08 \x01(\x0b\x32#.feast.core.DataSource.TrinoOptionsH\x00\x12<\n\rspark_storage\x18\t \x01(\x0b\x32#.feast.core.DataSource.SparkOptionsH\x00\x12>\n\x0e\x61thena_storage\x18\n \x01(\x0b\x32$.feast.core.DataSource.AthenaOptionsH\x00\x42\x06\n\x04kind\"\xf7\x01\n\x10SavedDatasetMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x13min_event_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x13max_event_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"f\n\x0cSavedDataset\x12*\n\x04spec\x18\x01 \x01(\x0b\x32\x1c.feast.core.SavedDatasetSpec\x12*\n\x04meta\x18\x02 \x01(\x0b\x32\x1c.feast.core.SavedDatasetMetaBV\n\x10\x66\x65\x61st.proto.coreB\x11SavedDatasetProtoZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')



_SAVEDDATASETSPEC = DESCRIPTOR.message_types_by_name['SavedDatasetSpec']
_SAVEDDATASETSPEC_TAGSENTRY = _SAVEDDATASETSPEC.nested_types_by_name['TagsEntry']
_SAVEDDATASETSTORAGE = DESCRIPTOR.message_types_by_name['SavedDatasetStorage']
_SAVEDDATASETMETA = DESCRIPTOR.message_types_by_name['SavedDatasetMeta']
_SAVEDDATASET = DESCRIPTOR.message_types_by_name['SavedDataset']
SavedDatasetSpec = _reflection.GeneratedProtocolMessageType('SavedDatasetSpec', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SAVEDDATASETSPEC_TAGSENTRY,
    '__module__' : 'feast.core.SavedDataset_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.SavedDatasetSpec.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _SAVEDDATASETSPEC,
  '__module__' : 'feast.core.SavedDataset_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.SavedDatasetSpec)
  })
_sym_db.RegisterMessage(SavedDatasetSpec)
_sym_db.RegisterMessage(SavedDatasetSpec.TagsEntry)

SavedDatasetStorage = _reflection.GeneratedProtocolMessageType('SavedDatasetStorage', (_message.Message,), {
  'DESCRIPTOR' : _SAVEDDATASETSTORAGE,
  '__module__' : 'feast.core.SavedDataset_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.SavedDatasetStorage)
  })
_sym_db.RegisterMessage(SavedDatasetStorage)

SavedDatasetMeta = _reflection.GeneratedProtocolMessageType('SavedDatasetMeta', (_message.Message,), {
  'DESCRIPTOR' : _SAVEDDATASETMETA,
  '__module__' : 'feast.core.SavedDataset_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.SavedDatasetMeta)
  })
_sym_db.RegisterMessage(SavedDatasetMeta)

SavedDataset = _reflection.GeneratedProtocolMessageType('SavedDataset', (_message.Message,), {
  'DESCRIPTOR' : _SAVEDDATASET,
  '__module__' : 'feast.core.SavedDataset_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.SavedDataset)
  })
_sym_db.RegisterMessage(SavedDataset)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020feast.proto.coreB\021SavedDatasetProtoZ/github.com/feast-dev/feast/go/protos/feast/core'
  _SAVEDDATASETSPEC_TAGSENTRY._options = None
  _SAVEDDATASETSPEC_TAGSENTRY._serialized_options = b'8\001'
  _SAVEDDATASETSPEC._serialized_start=108
  _SAVEDDATASETSPEC._serialized_end=401
  _SAVEDDATASETSPEC_TAGSENTRY._serialized_start=358
  _SAVEDDATASETSPEC_TAGSENTRY._serialized_end=401
  _SAVEDDATASETSTORAGE._serialized_start=404
  _SAVEDDATASETSTORAGE._serialized_end=887
  _SAVEDDATASETMETA._serialized_start=890
  _SAVEDDATASETMETA._serialized_end=1137
  _SAVEDDATASET._serialized_start=1139
  _SAVEDDATASET._serialized_end=1241
# @@protoc_insertion_point(module_scope)
