from django.http import QueryDict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Q
# Create your views here.
from rest_framework import viewsets
from .serializers import courseSerializer,usercourseSerializer
from .models import course, usercourse
from user.models import UserDetail

# class Course_to_user_Api(APIView):
#     def get(self, request, format=None):
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.vod.v20180717 import vod_client, models


class CourseDeatilApi(APIView):
    def post(self, request, format=None):
        roomid = request.data.get('roomid')
        course_name =request.data.get('roomname')
        course_describe = request.data.get('course_describe')
        type = request.data.get('type')
        print(roomid)
        print(course_name)
        print(course_describe)
        if roomid == None:
            return Response({'error_message': 'Lack PK Parameters Error'}, status=status.HTTP_400_BAD_REQUEST)
        u1 = UserDetail.objects.get(id=request.user.id)
        d1 = timezone.now()
        coursedetail= course.objects.create(room_id=roomid, course_name=course_name, course_describe=course_describe,created_on=d1,user=u1, type=type)
        coursedetail.save()
        serializers = courseSerializer(coursedetail)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        course_list = course.objects.all()
        serializers = courseSerializer(course_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        try:
            c1 = course.objects.get(user=request.user.id)
        except course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        c1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 判断用户是否关注了主播
class issubscribeAPI(APIView):
    def post(self, request, format=None):
        print(request.user.id)
        room_id=request.data.get('room_id')
        print(room_id)
        print(request.data)
        if usercourse.objects.filter(Q(room_id=room_id) & Q(user_id=request.user.id)).exists():
            return Response({'issubscribe': True}, status=status.HTTP_200_OK)
        else:
            return Response({'issubscribe': False}, status=status.HTTP_200_OK)


class UserCourselApi(APIView):
    def post(self, request, format=None):
        # 主播id
        room_id = request.data.get('room_id')
        # 用户id
        user_id = request.data.get('user_id')
        print(room_id)
        print(user_id)
        us = usercourse.objects.create()
        us.user_id = user_id
        us.room_id = room_id
        us.save()
        us1 = usercourseSerializer(instance=us)
        return Response(us1.data, status=status.HTTP_200_OK)
    # 显示当前用户订阅过的主播id
    def get(self, request, format=None):
        uc = usercourse.objects.filter(user_id=request.user.id)
        print(uc)
        course2=[]
        for i in uc:
            # 根据当前房间号找到对应直播间信息
            course1 = course.objects.filter(room_id=i.room_id)
            course2.extend(course1)
            print(course1)
        uc_list = courseSerializer(instance=course2, many=True)
        return Response(uc_list.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        try:


            room_id=request.GET.get('room_id')
            print('roomid is')
            print(room_id)

            uc1 = usercourse.objects.filter(user_id=request.user.id,room_id=room_id)
        except course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        uc1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class geturlApi(APIView):
    def get(self, request, format=None):
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
            print(type(abc))
            abc = json.loads(abc)
            print(type(abc))
            # print(abc)
            # bbb = resp["MediaInfoSet"][0]["BasicInfo"]["MediaUrl"]
            total = {}
            for it in abc["MediaInfoSet"]:
                video_url = it["BasicInfo"]["MediaUrl"]
                name = it["BasicInfo"]["Name"]
                total = dict(total, **({video_url: name}))
            print(total)
            return Response(total, status=status.HTTP_200_OK)
        except TencentCloudSDKException as err:
            print(err)

    def post(self, request, format=None):
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
            print(type(abc))
            abc = json.loads(abc)
            print(type(abc))
            # print(abc)
            # bbb = resp["MediaInfoSet"][0]["BasicInfo"]["MediaUrl"]
            total = []
            for it in abc["MediaInfoSet"]:
                CoverUrl = it["BasicInfo"]["CoverUrl"].split(" ")
                CoverUrl = list(CoverUrl)
                total = (total+CoverUrl)
            print(total)
            return Response(total, status=status.HTTP_200_OK)
        except TencentCloudSDKException as err:
            print(err)

