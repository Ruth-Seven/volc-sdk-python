# Code generated by protoc-gen-volcengine-sdk
# source: VodService
# DO NOT EDIT!
# coding:utf-8
from __future__ import print_function
import volcengine.Policy as *
from google.protobuf.json_format import *
from volcengine.vod.VodServiceConfig import VodServiceConfig
from retry import retry
from zlib import crc32
import os
import time
import datetime
from volcengine.util.Util import Util
from volcengine.vod.models.request.request_vod_pb2 import *
from volcengine.vod.models.response.response_vod_pb2 import *

MinChunkSize = 1024 * 1024 * 20
LargeFileSize = 1024 * 1024 * 1024


#
# Generated from protobuf service <code>VodService</code>
#
class VodService(VodServiceConfig):

    def get_private_drm_play_auth_token(self, request: VodGetPrivateDrmPlayAuthRequest, expire: int):
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            if expire > 0:
                params['X-Expires'] = str(expire)
            data = self.get_sign_url('GetPrivateDrmPlayAuth', params)
            return data
        except Exception as Argument:
            raise Argument

    def create_hls_drm_auth_token(self, auth_algorithm, expire_seconds):
        try:
            if expire_seconds == 0:
                raise Exception("invalid expire")
            deadline = int(datetime.datetime.now().timestamp()) + expire_seconds
            deadTime = datetime.datetime.utcfromtimestamp(deadline).strftime("%Y%m%dT%H%M%SZ")
            kDate = Util.hmac_sha256(bytes(self.service_info.credentials.sk, encoding='utf-8'), deadTime)
            kRegion = Util.hmac_sha256(kDate, self.service_info.credentials.region)
            kService = Util.hmac_sha256(kRegion, 'vod')
            kCredentials = Util.hmac_sha256(kService, 'request')
            key = Util.to_hex(kCredentials)
            signDataString = '&'.join([auth_algorithm, '2.0', str(deadline)])
            if auth_algorithm == 'HMAC-SHA1':
                signBytes = Util.hmac_sha1(bytes(key, encoding='utf-8'), signDataString)
            else:
                raise Exception('invalid authAlgorithm')
            sign = base64.b64encode(signBytes).decode('utf-8')
            token = ':'.join([auth_algorithm, '2.0', str(deadline), self.service_info.credentials.ak, sign])
            params = dict()
            params['DrmAuthToken'] = token
            params['X-Expires'] = str(expire_seconds)
            getAuth = self.get_sign_url("GetHlsDecryptionKey", params)
            return getAuth
        except Exception as e:
            raise e

    def get_sha1_hls_drm_auth_token(self, expire_seconds):
        try:
            return self.create_hls_drm_auth_token('HMAC-SHA1', expire_seconds)
        except Exception as Argument:
            raise Argument

    def get_play_auth_token(self, request: VodGetPlayInfoRequest, expire: int):
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            if expire > 0:
                params['X-Expires'] = str(expire)
            token = self.get_sign_url('GetPlayInfo', params)
            ret = {'TokenVersion': 'V2', 'GetPlayInfoToken': token}
            data = json.dumps(ret)
        except Exception as Argument:
            raise Argument
        else:
            if sys.version_info[0] == 3:
                return base64.b64encode(data.encode('utf-8')).decode('utf-8')
            else:
                return base64.b64encode(data.decode('utf-8'))

    def get_subtitle_auth_token(self, request: VodGetSubtitleInfoListRequest, expire: int):
        try:
            if request.Vid == "":
                raise Exception("Vid is None")
            params = {"Vid": request.Vid}
            params["Status"] = "Published"
            if expire > 0:
                params['X-Expires'] = str(expire)
            token = self.get_sign_url('GetSubtitleInfoList', params)
            ret = {'GetSubtitleAuthToken': token}
            data = json.dumps(ret)
        except Exception as Argument:
            raise Argument
        else:
            if sys.version_info[0] == 3:
                return base64.b64encode(data.encode('utf-8')).decode('utf-8')
            else:
                return base64.b64encode(data.decode('utf-8'))

    def upload_media(self, request):
        oid, session_key, avg_speed = self.upload_tob(request.SpaceName, request.FilePath, "")
        req = VodCommitUploadInfoRequest()
        req.SpaceName = request.SpaceName
        req.SessionKey = session_key
        req.Functions = request.Functions
        req.CallbackArgs = request.CallbackArgs
        resp = self.commit_upload_info(req)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.RequestId)
            raise Exception(resp.ResponseMetadata.Error)
        return resp

    def upload_tob(self, space_name, file_path, file_type):
        if not os.path.isfile(file_path):
            raise Exception("no such file on file path")
        apply_req = VodApplyUploadInfoRequest()
        apply_req.SpaceName = space_name
        apply_req.FileType = file_type
        resp = self.apply_upload_info(apply_req)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.RequestId)
            raise Exception(resp.ResponseMetadata.Error)
        upload_address = resp.Result.Data.UploadAddress
        oid = upload_address.StoreInfos[0].StoreUri
        session_key = upload_address.SessionKey
        auth = upload_address.StoreInfos[0].Auth
        host = upload_address.UploadHosts[0]
        start = time.time()
        file_size = os.path.getsize(file_path)
        if file_size < MinChunkSize:
            self.direct_upload(host, oid, auth, file_path)
        elif file_size > LargeFileSize:
            self.chunk_upload(file_path, host, oid, auth, file_size, True)
        else:
            self.chunk_upload(file_path, host, oid, auth, file_size, False)
        cost = (time.time() - start) * 1000
        file_size = os.path.getsize(file_path)
        avg_speed = float(file_size) / float(cost)
        return oid, session_key, avg_speed

    @retry(tries=3, delay=1, backoff=2)
    def direct_upload(self, host, oid, auth, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
            check_sum = crc32(data) & 0xFFFFFFFF
        check_sum = "%08x" % check_sum
        url = 'http://{}/{}'.format(host, oid)
        headers = {'Content-CRC32': check_sum, 'Authorization': auth}
        upload_status, resp = self.put(url, file_path, headers)
        if not upload_status:
            raise Exception("direct upload error")
        resp = json.loads(resp)
        if resp.get('success') is None or resp['success'] != 0:
            raise Exception("direct upload error")

    def chunk_upload(self, file_path, host, oid, auth, size, is_large_file):
        upload_id = self.init_upload_part(host, oid, auth, is_large_file)
        n = size // MinChunkSize
        last_num = n - 1
        parts = []
        with open(file_path, 'rb') as f:
            for i in range(0, last_num):
                data = f.read(MinChunkSize)
                part = self.upload_part(host, oid, auth, upload_id, i, data, is_large_file)
                parts.append(part)
            data = f.read()
            part = self.upload_part(host, oid, auth, upload_id, last_num, data, is_large_file)
            parts.append(part)
        return self.upload_merge_part(host, oid, auth, upload_id, parts, is_large_file)

    @retry(tries=3, delay=1, backoff=2)
    def init_upload_part(self, host, oid, auth, is_large_file):
        url = 'http://{}/{}?uploads'.format(host, oid)
        headers = {'Authorization': auth}
        if is_large_file:
            headers['X-Storage-Mode'] = 'gateway'
        upload_status, resp = self.put_data(url, None, headers)
        resp = json.loads(resp)
        if not upload_status:
            raise Exception("init upload error")
        if resp.get('success') is None or resp['success'] != 0:
            raise Exception("init upload error")
        return resp['payload']['uploadID']

    @retry(tries=3, delay=1, backoff=2)
    def upload_part(self, host, oid, auth, upload_id, part_number, data, is_large_file):
        url = 'http://{}/{}?partNumber={}&uploadID={}'.format(host, oid,
                                                              part_number, upload_id)
        check_sum = crc32(data) & 0xFFFFFFFF
        check_sum = "%08x" % check_sum
        headers = {'Content-CRC32': check_sum, 'Authorization': auth}
        if is_large_file:
            headers['X-Storage-Mode'] = 'gateway'
        upload_status, resp = self.put_data(url, data, headers)
        if not upload_status:
            raise Exception(url + json.dumps(resp))
        resp = json.loads(resp)
        if resp.get('success') is None or resp['success'] != 0:
            raise Exception("upload part error")
        return check_sum

    @staticmethod
    def generate_merge_body(check_sum_list):
        if len(check_sum_list) == 0:
            raise Exception('crc32 list empty')
        s = []
        for i in range(len(check_sum_list)):
            s.append('{}:{}'.format(i, check_sum_list[i]))
        comma = ','
        return comma.join(s)

    @retry(tries=3, delay=1, backoff=2)
    def upload_merge_part(self, host, oid, auth, upload_id, check_sum_list, is_large_file):
        url = 'http://{}/{}?uploadID={}'.format(host, oid, upload_id)
        data = self.generate_merge_body(check_sum_list)
        headers = {'Authorization': auth}
        if is_large_file:
            headers['X-Storage-Mode'] = 'gateway'
        upload_status, resp = self.put_data(url, data, headers)
        resp = json.loads(resp)
        if not upload_status:
            raise Exception("init upload error")
        if resp.get('success') is None or resp['success'] != 0:
            raise Exception("init upload error")

    def get_upload_sts2_with_expired_time(self, expired_time):
        actions = ["vod:ApplyUploadInfo", "vod:CommitUploadInfo"]
        resources = []
        statement = Statement.new_allow_statement(actions, resources)
        inline_policy = Policy([statement])
        return self.sign_sts2(inline_policy, expired_time)

    def get_upload_sts2(self):
        return self.get_upload_sts2_with_expired_time(60 * 60)

    def upload_material(self, request):
        oid, session_key, avg_speed = self.upload_tob(request.SpaceName, request.FilePath, request.FileType)

        req = VodCommitUploadInfoRequest()
        req.SpaceName = request.SpaceName
        req.SessionKey = session_key
        req.Functions = request.Functions
        req.CallbackArgs = request.CallbackArgs

        resp = self.commit_upload_info(req)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.RequestId)
            raise Exception(resp.ResponseMetadata.Error)
        return resp

    #
    # GetPlayInfo.
    #
    # @param request VodGetPlayInfoRequest
    # @return VodGetPlayInfoResponse
    # @raise Exception
    def get_play_info(self, request: VodGetPlayInfoRequest) -> VodGetPlayInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("GetPlayInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetPlayInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetPlayInfoResponse(), True)

    #
    # GetPrivateDrmPlayAuth.
    #
    # @param request VodGetPrivateDrmPlayAuthRequest
    # @return VodGetPrivateDrmPlayAuthResponse
    # @raise Exception
    def get_private_drm_play_auth(self, request: VodGetPrivateDrmPlayAuthRequest) -> VodGetPrivateDrmPlayAuthResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("GetPrivateDrmPlayAuth", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetPrivateDrmPlayAuthResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetPrivateDrmPlayAuthResponse(), True)

    #
    # GetHlsDecryptionKey.
    #
    # @param request VodGetHlsDecryptionKeyRequest
    # @return VodGetHlsDecryptionKeyResponse
    # @raise Exception
    def get_hls_decryption_key(self, request: VodGetHlsDecryptionKeyRequest) -> VodGetHlsDecryptionKeyResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("GetHlsDecryptionKey", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetHlsDecryptionKeyResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetHlsDecryptionKeyResponse(), True)

    #
    # UploadMediaByUrl.
    #
    # @param request VodUrlUploadRequest
    # @return VodUrlUploadResponse
    # @raise Exception
    def upload_media_by_url(self, request: VodUrlUploadRequest) -> VodUrlUploadResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("UploadMediaByUrl", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUrlUploadResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUrlUploadResponse(), True)

    #
    # QueryUploadTaskInfo.
    #
    # @param request VodQueryUploadTaskInfoRequest
    # @return VodQueryUploadTaskInfoResponse
    # @raise Exception
    def query_upload_task_info(self, request: VodQueryUploadTaskInfoRequest) -> VodQueryUploadTaskInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("QueryUploadTaskInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodQueryUploadTaskInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodQueryUploadTaskInfoResponse(), True)

    #
    # ApplyUploadInfo.
    #
    # @param request VodApplyUploadInfoRequest
    # @return VodApplyUploadInfoResponse
    # @raise Exception
    def apply_upload_info(self, request: VodApplyUploadInfoRequest) -> VodApplyUploadInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("ApplyUploadInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodApplyUploadInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodApplyUploadInfoResponse(), True)

    #
    # CommitUploadInfo.
    #
    # @param request VodCommitUploadInfoRequest
    # @return VodCommitUploadInfoResponse
    # @raise Exception
    def commit_upload_info(self, request: VodCommitUploadInfoRequest) -> VodCommitUploadInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("CommitUploadInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodCommitUploadInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodCommitUploadInfoResponse(), True)

    #
    # UpdateMediaInfo.
    #
    # @param request VodUpdateMediaInfoRequest
    # @return VodUpdateMediaInfoResponse
    # @raise Exception
    def update_media_info(self, request: VodUpdateMediaInfoRequest) -> VodUpdateMediaInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("UpdateMediaInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUpdateMediaInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUpdateMediaInfoResponse(), True)

    #
    # UpdateMediaPublishStatus.
    #
    # @param request VodUpdateMediaPublishStatusRequest
    # @return VodUpdateMediaPublishStatusResponse
    # @raise Exception
    def update_media_publish_status(self, request: VodUpdateMediaPublishStatusRequest) -> VodUpdateMediaPublishStatusResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("UpdateMediaPublishStatus", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUpdateMediaPublishStatusResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUpdateMediaPublishStatusResponse(), True)

    #
    # GetMediaInfos.
    #
    # @param request VodGetMediaInfosRequest
    # @return VodGetMediaInfosResponse
    # @raise Exception
    def get_media_infos(self, request: VodGetMediaInfosRequest) -> VodGetMediaInfosResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("GetMediaInfos", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetMediaInfosResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetMediaInfosResponse(), True)

    #
    # GetRecommendedPoster.
    #
    # @param request VodGetRecommendedPosterRequest
    # @return VodGetRecommendedPosterResponse
    # @raise Exception
    def get_recommended_poster(self, request: VodGetRecommendedPosterRequest) -> VodGetRecommendedPosterResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("GetRecommendedPoster", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetRecommendedPosterResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetRecommendedPosterResponse(), True)

    #
    # DeleteMedia.
    #
    # @param request VodDeleteMediaRequest
    # @return VodDeleteMediaResponse
    # @raise Exception
    def delete_media(self, request: VodDeleteMediaRequest) -> VodDeleteMediaResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("DeleteMedia", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodDeleteMediaResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodDeleteMediaResponse(), True)

    #
    # DeleteTranscodes.
    #
    # @param request VodDeleteTranscodesRequest
    # @return VodDeleteTranscodesResponse
    # @raise Exception
    def delete_transcodes(self, request: VodDeleteTranscodesRequest) -> VodDeleteTranscodesResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("DeleteTranscodes", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodDeleteTranscodesResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodDeleteTranscodesResponse(), True)

    #
    # GetMediaList.
    #
    # @param request VodGetMediaListRequest
    # @return VodGetMediaListResponse
    # @raise Exception
    def get_media_list(self, request: VodGetMediaListRequest) -> VodGetMediaListResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("GetMediaList", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetMediaListResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetMediaListResponse(), True)

    #
    # GetSubtitleInfoList.
    #
    # @param request VodGetSubtitleInfoListRequest
    # @return VodGetSubtitleInfoListResponse
    # @raise Exception
    def get_subtitle_info_list(self, request: VodGetSubtitleInfoListRequest) -> VodGetSubtitleInfoListResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("GetSubtitleInfoList", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetSubtitleInfoListResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetSubtitleInfoListResponse(), True)

    #
    # UpdateSubtitleStatus.
    #
    # @param request VodUpdateSubtitleStatusRequest
    # @return VodUpdateSubtitleStatusResponse
    # @raise Exception
    def update_subtitle_status(self, request: VodUpdateSubtitleStatusRequest) -> VodUpdateSubtitleStatusResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("UpdateSubtitleStatus", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUpdateSubtitleStatusResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUpdateSubtitleStatusResponse(), True)

    #
    # UpdateSubtitleInfo.
    #
    # @param request VodUpdateSubtitleInfoRequest
    # @return VodUpdateSubtitleInfoResponse
    # @raise Exception
    def update_subtitle_info(self, request: VodUpdateSubtitleInfoRequest) -> VodUpdateSubtitleInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("UpdateSubtitleInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUpdateSubtitleInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUpdateSubtitleInfoResponse(), True)

    #
    # StartWorkflow.
    #
    # @param request VodStartWorkflowRequest
    # @return VodStartWorkflowResponse
    # @raise Exception
    def start_workflow(self, request: VodStartWorkflowRequest) -> VodStartWorkflowResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            for k, v in params.items():
                if isinstance(v, (int, float, bool, str)) is True:
                    continue
                else:
                    params[k] = json.dumps(v)
            res = self.get("StartWorkflow", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodStartWorkflowResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodStartWorkflowResponse(), True)

