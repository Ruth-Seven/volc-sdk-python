# coding:utf-8
from __future__ import print_function

import json

from volcengine.rtc.RtcService import RtcService

if __name__ == '__main__':
    # using your own AK and SK
    AK = 'Your_AK'
    SK = 'Your_SK'

    # Firstly , init an RTCService Class
    rtc_service = RtcService()

    # Then , Set your AK and SK
    rtc_service.set_ak(AK)
    rtc_service.set_sk(SK)

    # You can using this API now ! Here are some Examples
    body = dict()
    body['AppId'] = 'Your_AppId'
    body['StartTime'] = '2021-08-24T00:00:00+08:00'
    body['EndTime'] = '2021-08-25T00:00:00+08:00'
    body['Indicator'] = 'NetworkTransDelay'
    body['OS'] = 'mac'
    body['Network'] = 'wifi'

    body = json.dumps(body)
    resp = rtc_service.list_indicators(body)
    print(resp)

