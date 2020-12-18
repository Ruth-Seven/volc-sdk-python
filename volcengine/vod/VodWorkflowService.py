# Code generated by protoc-gen-volcengine-sdk
# source: VodWorkflowService
# DO NOT EDIT!
# coding:utf-8

from __future__ import print_function
import os
import threading
import time
from zlib import crc32
from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service
from volcengine.const.Const import *
from volcengine.Policy import *
from volcengine.util.Util import *
from google.protobuf.json_format import *
from volcengine.vod.VodService import VodService
from volcengine.models.vod.request.request_vod_pb2 import *
from volcengine.models.vod.response.response_vod_pb2 import *


#
# Generated from protobuf service <code>VodWorkflowService</code>
#
class VodWorkflowService(VodService):

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

# end of service interface
