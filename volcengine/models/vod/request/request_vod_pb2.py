# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/request/request_vod.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from volcengine.models.vod.business import vod_workflow_pb2 as vod_dot_business_dot_vod__workflow__pb2
from volcengine.models.vod.business import vod_upload_pb2 as vod_dot_business_dot_vod__upload__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vod/request/request_vod.proto',
  package='Volcengine.Models.Vod.Request',
  syntax='proto3',
  serialized_options=b'\n com.volcengine.model.vod.requestB\nVodRequestP\001Z8github.com/volcengine/volc-sdk-golang/models/vod/request\240\001\001\330\001\001\312\002\027Volc\\Models\\Vod\\Request\342\002\027Volc\\Models\\GPBMetadata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dvod/request/request_vod.proto\x12\x1dVolcengine.Models.Vod.Request\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fvod/business/vod_workflow.proto\x1a\x1dvod/business/vod_upload.proto\"\x98\x01\n\x15VodGetPlayInfoRequest\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0e\n\x06\x46ormat\x18\x02 \x01(\t\x12\r\n\x05\x43odec\x18\x03 \x01(\t\x12\x12\n\nDefinition\x18\x04 \x01(\t\x12\x10\n\x08\x46ileType\x18\x05 \x01(\t\x12\x10\n\x08LogoType\x18\x06 \x01(\t\x12\x0e\n\x06\x42\x61se64\x18\x07 \x01(\t\x12\x0b\n\x03Ssl\x18\x08 \x01(\t\"I\n\x1dVodGetOriginalPlayInfoRequest\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0e\n\x06\x42\x61se64\x18\x02 \x01(\t\x12\x0b\n\x03Ssl\x18\x03 \x01(\t\"m\n\x13VodUrlUploadRequest\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x43\n\x07URLSets\x18\x02 \x03(\x0b\x32\x32.Volcengine.Models.Vod.Business.VodUrlUploadURLSet\"/\n\x1dVodQueryUploadTaskInfoRequest\x12\x0e\n\x06JobIds\x18\x01 \x01(\t\"T\n\x19VodApplyUploadInfoRequest\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x12\n\nSessionKey\x18\x02 \x01(\t\x12\x10\n\x08\x46ileSize\x18\x03 \x01(\x05\"e\n\x15VodUploadMediaRequest\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x10\n\x08\x46ilePath\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x11\n\tFunctions\x18\x04 \x01(\t\"l\n\x1aVodCommitUploadInfoRequest\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x12\n\nSessionKey\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x11\n\tFunctions\x18\x04 \x01(\t\"=\n\x17VodUrlUploadJsonRequest\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x0f\n\x07URLSets\x18\x02 \x01(\t\".\n\x1eVodGetRecommendedPosterRequest\x12\x0c\n\x04Vids\x18\x01 \x01(\t\"A\n\"VodUpdateMediaPublishStatusRequest\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0e\n\x06Status\x18\x02 \x01(\t\"\xe5\x01\n\x19VodUpdateMediaInfoRequest\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12/\n\tPosterUri\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05Title\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x44\x65scription\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04Tags\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\'\n\x17VodGetMediaInfosRequest\x12\x0c\n\x04Vids\x18\x01 \x01(\t\"\xa1\x01\n\x17VodStartWorkflowRequest\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x12\n\nTemplateId\x18\x02 \x01(\t\x12=\n\x05Input\x18\x03 \x01(\x0b\x32..Volcengine.Models.Vod.Business.WorkflowParams\x12\x10\n\x08Priority\x18\x04 \x01(\x05\x12\x14\n\x0c\x43\x61llbackArgs\x18\x05 \x01(\tB\xa4\x01\n com.volcengine.model.vod.requestB\nVodRequestP\x01Z8github.com/volcengine/volc-sdk-golang/models/vod/request\xa0\x01\x01\xd8\x01\x01\xca\x02\x17Volc\\Models\\Vod\\Request\xe2\x02\x17Volc\\Models\\GPBMetadatab\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,vod_dot_business_dot_vod__workflow__pb2.DESCRIPTOR,vod_dot_business_dot_vod__upload__pb2.DESCRIPTOR,])




_VODGETPLAYINFOREQUEST = _descriptor.Descriptor(
  name='VodGetPlayInfoRequest',
  full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vid', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.Vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Format', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.Format', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Codec', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.Codec', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Definition', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.Definition', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FileType', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.FileType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LogoType', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.LogoType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Base64', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.Base64', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ssl', full_name='Volcengine.Models.Vod.Request.VodGetPlayInfoRequest.Ssl', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=313,
)


_VODGETORIGINALPLAYINFOREQUEST = _descriptor.Descriptor(
  name='VodGetOriginalPlayInfoRequest',
  full_name='Volcengine.Models.Vod.Request.VodGetOriginalPlayInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vid', full_name='Volcengine.Models.Vod.Request.VodGetOriginalPlayInfoRequest.Vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Base64', full_name='Volcengine.Models.Vod.Request.VodGetOriginalPlayInfoRequest.Base64', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ssl', full_name='Volcengine.Models.Vod.Request.VodGetOriginalPlayInfoRequest.Ssl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=388,
)


_VODURLUPLOADREQUEST = _descriptor.Descriptor(
  name='VodUrlUploadRequest',
  full_name='Volcengine.Models.Vod.Request.VodUrlUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpaceName', full_name='Volcengine.Models.Vod.Request.VodUrlUploadRequest.SpaceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='URLSets', full_name='Volcengine.Models.Vod.Request.VodUrlUploadRequest.URLSets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=499,
)


_VODQUERYUPLOADTASKINFOREQUEST = _descriptor.Descriptor(
  name='VodQueryUploadTaskInfoRequest',
  full_name='Volcengine.Models.Vod.Request.VodQueryUploadTaskInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='JobIds', full_name='Volcengine.Models.Vod.Request.VodQueryUploadTaskInfoRequest.JobIds', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=548,
)


_VODAPPLYUPLOADINFOREQUEST = _descriptor.Descriptor(
  name='VodApplyUploadInfoRequest',
  full_name='Volcengine.Models.Vod.Request.VodApplyUploadInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpaceName', full_name='Volcengine.Models.Vod.Request.VodApplyUploadInfoRequest.SpaceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionKey', full_name='Volcengine.Models.Vod.Request.VodApplyUploadInfoRequest.SessionKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FileSize', full_name='Volcengine.Models.Vod.Request.VodApplyUploadInfoRequest.FileSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=634,
)


_VODUPLOADMEDIAREQUEST = _descriptor.Descriptor(
  name='VodUploadMediaRequest',
  full_name='Volcengine.Models.Vod.Request.VodUploadMediaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpaceName', full_name='Volcengine.Models.Vod.Request.VodUploadMediaRequest.SpaceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FilePath', full_name='Volcengine.Models.Vod.Request.VodUploadMediaRequest.FilePath', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CallbackArgs', full_name='Volcengine.Models.Vod.Request.VodUploadMediaRequest.CallbackArgs', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Functions', full_name='Volcengine.Models.Vod.Request.VodUploadMediaRequest.Functions', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=737,
)


_VODCOMMITUPLOADINFOREQUEST = _descriptor.Descriptor(
  name='VodCommitUploadInfoRequest',
  full_name='Volcengine.Models.Vod.Request.VodCommitUploadInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpaceName', full_name='Volcengine.Models.Vod.Request.VodCommitUploadInfoRequest.SpaceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionKey', full_name='Volcengine.Models.Vod.Request.VodCommitUploadInfoRequest.SessionKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CallbackArgs', full_name='Volcengine.Models.Vod.Request.VodCommitUploadInfoRequest.CallbackArgs', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Functions', full_name='Volcengine.Models.Vod.Request.VodCommitUploadInfoRequest.Functions', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=739,
  serialized_end=847,
)


_VODURLUPLOADJSONREQUEST = _descriptor.Descriptor(
  name='VodUrlUploadJsonRequest',
  full_name='Volcengine.Models.Vod.Request.VodUrlUploadJsonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpaceName', full_name='Volcengine.Models.Vod.Request.VodUrlUploadJsonRequest.SpaceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='URLSets', full_name='Volcengine.Models.Vod.Request.VodUrlUploadJsonRequest.URLSets', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=849,
  serialized_end=910,
)


_VODGETRECOMMENDEDPOSTERREQUEST = _descriptor.Descriptor(
  name='VodGetRecommendedPosterRequest',
  full_name='Volcengine.Models.Vod.Request.VodGetRecommendedPosterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vids', full_name='Volcengine.Models.Vod.Request.VodGetRecommendedPosterRequest.Vids', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=912,
  serialized_end=958,
)


_VODUPDATEMEDIAPUBLISHSTATUSREQUEST = _descriptor.Descriptor(
  name='VodUpdateMediaPublishStatusRequest',
  full_name='Volcengine.Models.Vod.Request.VodUpdateMediaPublishStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vid', full_name='Volcengine.Models.Vod.Request.VodUpdateMediaPublishStatusRequest.Vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Status', full_name='Volcengine.Models.Vod.Request.VodUpdateMediaPublishStatusRequest.Status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=960,
  serialized_end=1025,
)


_VODUPDATEMEDIAINFOREQUEST = _descriptor.Descriptor(
  name='VodUpdateMediaInfoRequest',
  full_name='Volcengine.Models.Vod.Request.VodUpdateMediaInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vid', full_name='Volcengine.Models.Vod.Request.VodUpdateMediaInfoRequest.Vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PosterUri', full_name='Volcengine.Models.Vod.Request.VodUpdateMediaInfoRequest.PosterUri', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Title', full_name='Volcengine.Models.Vod.Request.VodUpdateMediaInfoRequest.Title', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Description', full_name='Volcengine.Models.Vod.Request.VodUpdateMediaInfoRequest.Description', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Tags', full_name='Volcengine.Models.Vod.Request.VodUpdateMediaInfoRequest.Tags', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1028,
  serialized_end=1257,
)


_VODGETMEDIAINFOSREQUEST = _descriptor.Descriptor(
  name='VodGetMediaInfosRequest',
  full_name='Volcengine.Models.Vod.Request.VodGetMediaInfosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vids', full_name='Volcengine.Models.Vod.Request.VodGetMediaInfosRequest.Vids', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1259,
  serialized_end=1298,
)


_VODSTARTWORKFLOWREQUEST = _descriptor.Descriptor(
  name='VodStartWorkflowRequest',
  full_name='Volcengine.Models.Vod.Request.VodStartWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vid', full_name='Volcengine.Models.Vod.Request.VodStartWorkflowRequest.Vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TemplateId', full_name='Volcengine.Models.Vod.Request.VodStartWorkflowRequest.TemplateId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Input', full_name='Volcengine.Models.Vod.Request.VodStartWorkflowRequest.Input', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Priority', full_name='Volcengine.Models.Vod.Request.VodStartWorkflowRequest.Priority', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CallbackArgs', full_name='Volcengine.Models.Vod.Request.VodStartWorkflowRequest.CallbackArgs', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1301,
  serialized_end=1462,
)

_VODURLUPLOADREQUEST.fields_by_name['URLSets'].message_type = vod_dot_business_dot_vod__upload__pb2._VODURLUPLOADURLSET
_VODUPDATEMEDIAINFOREQUEST.fields_by_name['PosterUri'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_VODUPDATEMEDIAINFOREQUEST.fields_by_name['Title'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_VODUPDATEMEDIAINFOREQUEST.fields_by_name['Description'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_VODUPDATEMEDIAINFOREQUEST.fields_by_name['Tags'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_VODSTARTWORKFLOWREQUEST.fields_by_name['Input'].message_type = vod_dot_business_dot_vod__workflow__pb2._WORKFLOWPARAMS
DESCRIPTOR.message_types_by_name['VodGetPlayInfoRequest'] = _VODGETPLAYINFOREQUEST
DESCRIPTOR.message_types_by_name['VodGetOriginalPlayInfoRequest'] = _VODGETORIGINALPLAYINFOREQUEST
DESCRIPTOR.message_types_by_name['VodUrlUploadRequest'] = _VODURLUPLOADREQUEST
DESCRIPTOR.message_types_by_name['VodQueryUploadTaskInfoRequest'] = _VODQUERYUPLOADTASKINFOREQUEST
DESCRIPTOR.message_types_by_name['VodApplyUploadInfoRequest'] = _VODAPPLYUPLOADINFOREQUEST
DESCRIPTOR.message_types_by_name['VodUploadMediaRequest'] = _VODUPLOADMEDIAREQUEST
DESCRIPTOR.message_types_by_name['VodCommitUploadInfoRequest'] = _VODCOMMITUPLOADINFOREQUEST
DESCRIPTOR.message_types_by_name['VodUrlUploadJsonRequest'] = _VODURLUPLOADJSONREQUEST
DESCRIPTOR.message_types_by_name['VodGetRecommendedPosterRequest'] = _VODGETRECOMMENDEDPOSTERREQUEST
DESCRIPTOR.message_types_by_name['VodUpdateMediaPublishStatusRequest'] = _VODUPDATEMEDIAPUBLISHSTATUSREQUEST
DESCRIPTOR.message_types_by_name['VodUpdateMediaInfoRequest'] = _VODUPDATEMEDIAINFOREQUEST
DESCRIPTOR.message_types_by_name['VodGetMediaInfosRequest'] = _VODGETMEDIAINFOSREQUEST
DESCRIPTOR.message_types_by_name['VodStartWorkflowRequest'] = _VODSTARTWORKFLOWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VodGetPlayInfoRequest = _reflection.GeneratedProtocolMessageType('VodGetPlayInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODGETPLAYINFOREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodGetPlayInfoRequest)
  })
_sym_db.RegisterMessage(VodGetPlayInfoRequest)

VodGetOriginalPlayInfoRequest = _reflection.GeneratedProtocolMessageType('VodGetOriginalPlayInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODGETORIGINALPLAYINFOREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodGetOriginalPlayInfoRequest)
  })
_sym_db.RegisterMessage(VodGetOriginalPlayInfoRequest)

VodUrlUploadRequest = _reflection.GeneratedProtocolMessageType('VodUrlUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODURLUPLOADREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodUrlUploadRequest)
  })
_sym_db.RegisterMessage(VodUrlUploadRequest)

VodQueryUploadTaskInfoRequest = _reflection.GeneratedProtocolMessageType('VodQueryUploadTaskInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYUPLOADTASKINFOREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodQueryUploadTaskInfoRequest)
  })
_sym_db.RegisterMessage(VodQueryUploadTaskInfoRequest)

VodApplyUploadInfoRequest = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFOREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodApplyUploadInfoRequest)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoRequest)

VodUploadMediaRequest = _reflection.GeneratedProtocolMessageType('VodUploadMediaRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADMEDIAREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodUploadMediaRequest)
  })
_sym_db.RegisterMessage(VodUploadMediaRequest)

VodCommitUploadInfoRequest = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFOREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodCommitUploadInfoRequest)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoRequest)

VodUrlUploadJsonRequest = _reflection.GeneratedProtocolMessageType('VodUrlUploadJsonRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODURLUPLOADJSONREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodUrlUploadJsonRequest)
  })
_sym_db.RegisterMessage(VodUrlUploadJsonRequest)

VodGetRecommendedPosterRequest = _reflection.GeneratedProtocolMessageType('VodGetRecommendedPosterRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODGETRECOMMENDEDPOSTERREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodGetRecommendedPosterRequest)
  })
_sym_db.RegisterMessage(VodGetRecommendedPosterRequest)

VodUpdateMediaPublishStatusRequest = _reflection.GeneratedProtocolMessageType('VodUpdateMediaPublishStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODUPDATEMEDIAPUBLISHSTATUSREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodUpdateMediaPublishStatusRequest)
  })
_sym_db.RegisterMessage(VodUpdateMediaPublishStatusRequest)

VodUpdateMediaInfoRequest = _reflection.GeneratedProtocolMessageType('VodUpdateMediaInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODUPDATEMEDIAINFOREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodUpdateMediaInfoRequest)
  })
_sym_db.RegisterMessage(VodUpdateMediaInfoRequest)

VodGetMediaInfosRequest = _reflection.GeneratedProtocolMessageType('VodGetMediaInfosRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODGETMEDIAINFOSREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodGetMediaInfosRequest)
  })
_sym_db.RegisterMessage(VodGetMediaInfosRequest)

VodStartWorkflowRequest = _reflection.GeneratedProtocolMessageType('VodStartWorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _VODSTARTWORKFLOWREQUEST,
  '__module__' : 'vod.request.request_vod_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Request.VodStartWorkflowRequest)
  })
_sym_db.RegisterMessage(VodStartWorkflowRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
