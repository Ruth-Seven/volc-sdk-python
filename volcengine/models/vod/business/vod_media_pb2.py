# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/business/vod_media.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.models.vod.business import vod_common_pb2 as vod_dot_business_dot_vod__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vod/business/vod_media.proto',
  package='Volcengine.Models.Vod.Business',
  syntax='proto3',
  serialized_options=b'\n!com.volcengine.model.vod.businessB\010VodMediaP\001Z9github.com/volcengine/volc-sdk-golang/models/vod/business\240\001\001\330\001\001\302\002\000\312\002\030Volc\\Models\\Vod\\Business\342\002\033Volc\\Models\\Vod\\GPBMetadata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cvod/business/vod_media.proto\x12\x1eVolcengine.Models.Vod.Business\x1a\x1dvod/business/vod_common.proto\"\xa3\x01\n\x11VodMediaBasicInfo\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\r\n\x05Title\x18\x03 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x04 \x01(\t\x12\x11\n\tPosterUri\x18\x05 \x01(\t\x12\x15\n\rPublishStatus\x18\x06 \x01(\t\x12\x0c\n\x04Tags\x18\x07 \x03(\t\x12\x12\n\nCreateTime\x18\x08 \x01(\t\"\xe1\x01\n\x0cVodMediaInfo\x12\x44\n\tBasicInfo\x18\x01 \x01(\x0b\x32\x31.Volcengine.Models.Vod.Business.VodMediaBasicInfo\x12\x41\n\nSourceInfo\x18\x02 \x01(\x0b\x32-.Volcengine.Models.Vod.Business.VodSourceInfo\x12H\n\x0eTranscodeInfos\x18\x03 \x03(\x0b\x32\x30.Volcengine.Models.Vod.Business.VodTranscodeInfo\"q\n\x14VodGetMediaInfosData\x12\x43\n\rMediaInfoList\x18\x01 \x03(\x0b\x32,.Volcengine.Models.Vod.Business.VodMediaInfo\x12\x14\n\x0cNotExistVids\x18\x02 \x03(\t\"2\n\x10VodStoreUriGroup\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x11\n\tStoreUris\x18\x02 \x03(\t\"u\n\x13VodGetRecPosterData\x12H\n\x0eStoreUriGroups\x18\x01 \x03(\x0b\x32\x30.Volcengine.Models.Vod.Business.VodStoreUriGroup\x12\x14\n\x0cNotExistVids\x18\x02 \x03(\tB\xac\x01\n!com.volcengine.model.vod.businessB\x08VodMediaP\x01Z9github.com/volcengine/volc-sdk-golang/models/vod/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02\x18Volc\\Models\\Vod\\Business\xe2\x02\x1bVolc\\Models\\Vod\\GPBMetadatab\x06proto3'
  ,
  dependencies=[vod_dot_business_dot_vod__common__pb2.DESCRIPTOR,])




_VODMEDIABASICINFO = _descriptor.Descriptor(
  name='VodMediaBasicInfo',
  full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpaceName', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.SpaceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Vid', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.Vid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Title', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.Title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Description', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.Description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PosterUri', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.PosterUri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PublishStatus', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.PublishStatus', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Tags', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.Tags', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CreateTime', full_name='Volcengine.Models.Vod.Business.VodMediaBasicInfo.CreateTime', index=7,
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
  serialized_start=96,
  serialized_end=259,
)


_VODMEDIAINFO = _descriptor.Descriptor(
  name='VodMediaInfo',
  full_name='Volcengine.Models.Vod.Business.VodMediaInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='BasicInfo', full_name='Volcengine.Models.Vod.Business.VodMediaInfo.BasicInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SourceInfo', full_name='Volcengine.Models.Vod.Business.VodMediaInfo.SourceInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TranscodeInfos', full_name='Volcengine.Models.Vod.Business.VodMediaInfo.TranscodeInfos', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=262,
  serialized_end=487,
)


_VODGETMEDIAINFOSDATA = _descriptor.Descriptor(
  name='VodGetMediaInfosData',
  full_name='Volcengine.Models.Vod.Business.VodGetMediaInfosData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MediaInfoList', full_name='Volcengine.Models.Vod.Business.VodGetMediaInfosData.MediaInfoList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='NotExistVids', full_name='Volcengine.Models.Vod.Business.VodGetMediaInfosData.NotExistVids', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=489,
  serialized_end=602,
)


_VODSTOREURIGROUP = _descriptor.Descriptor(
  name='VodStoreUriGroup',
  full_name='Volcengine.Models.Vod.Business.VodStoreUriGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vid', full_name='Volcengine.Models.Vod.Business.VodStoreUriGroup.Vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StoreUris', full_name='Volcengine.Models.Vod.Business.VodStoreUriGroup.StoreUris', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=604,
  serialized_end=654,
)


_VODGETRECPOSTERDATA = _descriptor.Descriptor(
  name='VodGetRecPosterData',
  full_name='Volcengine.Models.Vod.Business.VodGetRecPosterData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='StoreUriGroups', full_name='Volcengine.Models.Vod.Business.VodGetRecPosterData.StoreUriGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='NotExistVids', full_name='Volcengine.Models.Vod.Business.VodGetRecPosterData.NotExistVids', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=656,
  serialized_end=773,
)

_VODMEDIAINFO.fields_by_name['BasicInfo'].message_type = _VODMEDIABASICINFO
_VODMEDIAINFO.fields_by_name['SourceInfo'].message_type = vod_dot_business_dot_vod__common__pb2._VODSOURCEINFO
_VODMEDIAINFO.fields_by_name['TranscodeInfos'].message_type = vod_dot_business_dot_vod__common__pb2._VODTRANSCODEINFO
_VODGETMEDIAINFOSDATA.fields_by_name['MediaInfoList'].message_type = _VODMEDIAINFO
_VODGETRECPOSTERDATA.fields_by_name['StoreUriGroups'].message_type = _VODSTOREURIGROUP
DESCRIPTOR.message_types_by_name['VodMediaBasicInfo'] = _VODMEDIABASICINFO
DESCRIPTOR.message_types_by_name['VodMediaInfo'] = _VODMEDIAINFO
DESCRIPTOR.message_types_by_name['VodGetMediaInfosData'] = _VODGETMEDIAINFOSDATA
DESCRIPTOR.message_types_by_name['VodStoreUriGroup'] = _VODSTOREURIGROUP
DESCRIPTOR.message_types_by_name['VodGetRecPosterData'] = _VODGETRECPOSTERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VodMediaBasicInfo = _reflection.GeneratedProtocolMessageType('VodMediaBasicInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODMEDIABASICINFO,
  '__module__' : 'vod.business.vod_media_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Business.VodMediaBasicInfo)
  })
_sym_db.RegisterMessage(VodMediaBasicInfo)

VodMediaInfo = _reflection.GeneratedProtocolMessageType('VodMediaInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODMEDIAINFO,
  '__module__' : 'vod.business.vod_media_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Business.VodMediaInfo)
  })
_sym_db.RegisterMessage(VodMediaInfo)

VodGetMediaInfosData = _reflection.GeneratedProtocolMessageType('VodGetMediaInfosData', (_message.Message,), {
  'DESCRIPTOR' : _VODGETMEDIAINFOSDATA,
  '__module__' : 'vod.business.vod_media_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Business.VodGetMediaInfosData)
  })
_sym_db.RegisterMessage(VodGetMediaInfosData)

VodStoreUriGroup = _reflection.GeneratedProtocolMessageType('VodStoreUriGroup', (_message.Message,), {
  'DESCRIPTOR' : _VODSTOREURIGROUP,
  '__module__' : 'vod.business.vod_media_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Business.VodStoreUriGroup)
  })
_sym_db.RegisterMessage(VodStoreUriGroup)

VodGetRecPosterData = _reflection.GeneratedProtocolMessageType('VodGetRecPosterData', (_message.Message,), {
  'DESCRIPTOR' : _VODGETRECPOSTERDATA,
  '__module__' : 'vod.business.vod_media_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Models.Vod.Business.VodGetRecPosterData)
  })
_sym_db.RegisterMessage(VodGetRecPosterData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)