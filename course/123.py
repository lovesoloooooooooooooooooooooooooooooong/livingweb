# import json
# from tencentcloud.common import credential
# from tencentcloud.common.profile.client_profile import ClientProfile
# from tencentcloud.common.profile.http_profile import HttpProfile
# from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# from tencentcloud.vod.v20180717 import vod_client, models
# try:
#     abc = {"TotalCount": 2, "MediaInfoSet": [{"BasicInfo": {"Name": "1400621582_1_main_2022-04-02-15-46-28_2022-04-02-15-46-43", "Description": "", "CreateTime": "2022-04-02T07:46:45Z", "UpdateTime": "2022-04-02T07:46:45Z", "ExpireTime": "2022-04-09T07:46:44Z", "ClassId": 881530, "ClassName": "音视频录播", "ClassPath": "音视频录播", "CoverUrl": "", "Type": "m3u8", "MediaUrl": "http://1309192954.vod2.myqcloud.com/3b63f66dvodcq1309192954/a4d25c99387702298544824551/playlist.m3u8", "SourceInfo": {"SourceType": "Record", "SourceContext": "rtmp://164666.livepush.myqcloud.com/trtc_1400621582/1?cliRecoId=0&client_business_type=0&from=interactive&groupid=1&pid=8b7da4f3b4436a44199d494d3a7f86d6&product_name=CSIG_TRTC&record_name=1400621582_1_main&roomid=3477564&sdkappid=1400621582&sdkapptype=1&tinyid=144115242025165272&trtcclientip=9.222.192.15&ts=6247ff3a&txHost=164666.livepush.myqcloud.com&txSecret=457fc4c1bcfbd9305f4d5108ed3b1304&txTime=74d2174c&userdefinerecordid=1400621582_1&userid=MQ=="}, "StorageRegion": "ap-chongqing", "TagSet": [], "Vid": "1309192954_5c125fc64f8f4f8d92fb9be317e13e46", "Category": "Video", "Status": "Normal", "StorageClass": "STANDARD"}, "MetaData": {"Size": 2099480, "Container": "hls", "Bitrate": 878030, "Height": 720, "Width": 1280, "Duration": 19.129, "Rotate": 0, "VideoStreamSet": [{"Bitrate": 810511, "Height": 720, "Width": 1280, "Codec": "h264", "Fps": 0}], "AudioStreamSet": [{"Bitrate": 67519, "SamplingRate": 48000, "Codec": "aac"}], "VideoDuration": 19.129, "AudioDuration": 19.129}, "TranscodeInfo": {"TranscodeSet": [{"Url": "http://1309192954.vod2.myqcloud.com/3b63f66dvodcq1309192954/a4d25c99387702298544824551/playlist.m3u8", "Definition": 0, "Bitrate": 878030, "Height": 720, "Width": 1280, "Size": 2099480, "Duration": 19, "Container": "hls", "Md5": "", "AudioStreamSet": [{"Bitrate": 67519, "SamplingRate": 48000, "Codec": "aac"}], "VideoStreamSet": [{"Bitrate": 810511, "Height": 720, "Width": 1280, "Codec": "h264", "Fps": 0}]}]}, "AnimatedGraphicsInfo": 0, "SampleSnapshotInfo": 0, "ImageSpriteInfo": 0, "SnapshotByTimeOffsetInfo": 0, "KeyFrameDescInfo": 0, "AdaptiveDynamicStreamingInfo": 0, "MiniProgramReviewInfo": 0, "SubtitleInfo": 0, "FileId": "387702298544824551"}, {"BasicInfo": {"Name": "1400621582_1_main_2022-04-01-18-59-46_2022-04-01-19-00-42", "Description": "", "CreateTime": "2022-04-01T11:00:44Z", "UpdateTime": "2022-04-01T11:00:44Z", "ExpireTime": "2022-04-08T11:00:44Z", "ClassId": 881530, "ClassName": "音视频录播", "ClassPath": "音视频录播", "CoverUrl": "", "Type": "m3u8", "MediaUrl": "http://1309192954.vod2.myqcloud.com/3b63f66dvodcq1309192954/60b72be0387702298496542555/playlist.m3u8", "SourceInfo": {"SourceType": "Record", "SourceContext": "rtmp://164666.livepush.myqcloud.com/trtc_1400621582/1?cliRecoId=0&client_business_type=0&from=interactive&groupid=1&pid=8b7da4f3b4436a44199d494d3a7f86d6&product_name=CSIG_TRTC&record_name=1400621582_1_main&roomid=2887740&sdkappid=1400621582&sdkapptype=1&tinyid=144115242025165272&trtcclientip=9.222.24.98&ts=6246db0a&txHost=164666.livepush.myqcloud.com&txSecret=c34de8188ef6580e19e2839886b2bdc4&txTime=74d0f319&userdefinerecordid=1400621582_1&userid=MQ=="}, "StorageRegion": "ap-chongqing", "TagSet": [], "Vid": "1309192954_4e35e1a29dcc401bb4ddc4abedcea556", "Category": "Video", "Status": "Normal", "StorageClass": "STANDARD"}, "MetaData": {"Size": 13472108, "Container": "hls", "Bitrate": 1799400, "Height": 720, "Width": 1280, "Duration": 59.896, "Rotate": 0, "VideoStreamSet": [{"Bitrate": 1732585, "Height": 720, "Width": 1280, "Codec": "h264", "Fps": 0}], "AudioStreamSet": [{"Bitrate": 66815, "SamplingRate": 48000, "Codec": "aac"}], "VideoDuration": 59.896, "AudioDuration": 59.896}, "TranscodeInfo": {"TranscodeSet": [{"Url": "http://1309192954.vod2.myqcloud.com/3b63f66dvodcq1309192954/60b72be0387702298496542555/playlist.m3u8", "Definition": 0, "Bitrate": 1799400, "Height": 720, "Width": 1280, "Size": 13472108, "Duration": 59, "Container": "hls", "Md5": "", "AudioStreamSet": [{"Bitrate": 66815, "SamplingRate": 48000, "Codec": "aac"}], "VideoStreamSet": [{"Bitrate": 1732585, "Height": 720, "Width": 1280, "Codec": "h264", "Fps": 0}]}]}, "AnimatedGraphicsInfo": 0, "SampleSnapshotInfo": 0, "ImageSpriteInfo": 0, "SnapshotByTimeOffsetInfo": 0, "KeyFrameDescInfo": 0, "AdaptiveDynamicStreamingInfo": 0, "MiniProgramReviewInfo": 0, "SubtitleInfo": 0, "FileId": "387702298496542555"}], "RequestId": "39aa9965-1082-4a73-ac81-614b27e14c4e"}
#
#     bbb = abc["MediaInfoSet"][0]["BasicInfo"]["MediaUrl"]
#     print(bbb)
#     total = {}
#     for it in abc["MediaInfoSet"]:
#         video_url = it["BasicInfo"]["MediaUrl"]
#         name = it["BasicInfo"]["Name"]
#         total = dict(total, **({video_url:name}))
#     print(total)
# except TencentCloudSDKException as err:
#     print(err)
#
import ast
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.vod.v20180717 import vod_client, models

try:
    cred = credential.Credential("AKIDznNnwoPjfPt61f290atuf9LGvIPFo66q", "UhcGciX6ORDm7ByUjgMltjIabKmxOYR4")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "vod.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = vod_client.VodClient(cred, "", clientProfile)

    req = models.SearchMediaRequest()
    params = {

    }
    req.from_json_string(json.dumps(params))

    resp = client.SearchMedia(req)
    abc = resp.to_json_string()
    print( type(abc))
    abc = json.loads(abc)
    print(type(abc))
    #print(abc)
    # bbb = resp["MediaInfoSet"][0]["BasicInfo"]["MediaUrl"]
    total = {}
    for it in abc["MediaInfoSet"]:
        video_url = it["BasicInfo"]["MediaUrl"]
        name = it["BasicInfo"]["Name"]
        total = dict(total, **({video_url: name}))
    print(total)

except TencentCloudSDKException as err:
    print(err)

