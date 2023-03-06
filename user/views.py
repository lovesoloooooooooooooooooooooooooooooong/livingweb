import datetime
import sys
import os
import time

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserDetail
from .serializers import UserDetailSerializers
# 生成rtm token的代码
from utils.RtmTokenBuilder import RtmTokenBuilder, Role_Rtm_User
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class UserDetailAPI(APIView):
    def post(self, request, format=None):
        pk = request.user.id
        # pk = request.data.get('pk')
        # pk = request.user
        gender = request.data.get('gender')
        birthdate = request.data.get('birthdate')
        print(gender)
        print("birthday1 : %s %s", type(birthdate), birthdate)
        try:
            birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%dT%H:%M:%S.%fZ")
        except Exception as ex:
            print("date exchange error : %s", ex)
            birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
        print("birthday2 : %s %s", type(birthdate), birthdate)
        birthdate = datetime.date(birthdate.year, birthdate.month, birthdate.day)
        print("birthday3 : % %s", type(birthdate), birthdate)
        tel_num = request.data.get('tel_num')
        nickname = request.data.get('nickname')
        if pk == None:
            return Response({'error_message': 'Lack PK Parameters Error'}, status=status.HTTP_400_BAD_REQUEST)
        userdetail, created = UserDetail.objects.get_or_create(user_id=pk)  # 从数据库查找这个id的对象 找不到就创建一个

        if nickname != None:
            userdetail.nickname = nickname
        if birthdate != None:
            userdetail.birthdate = birthdate
        if gender != None:
            userdetail.gender = gender
        if tel_num != None:
            userdetail.tel_num = tel_num
        userdetail.save() #保存前台传过来的信息
        serializers = UserDetailSerializers(userdetail)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        # http://10.5.112.20:8000/user_api/userdetail/?pk=4
        try:
            # pk = request.GET.get('pk')
            pk = request.user.id
            if pk == None:
                return Response({'error_message': 'Lack PK Parameters Error'}, status=status.HTTP_400_BAD_REQUEST)
            userdetail = UserDetail.objects.get(user=pk)
        except UserDetail.DoesNotExist:
            userdetail, created = UserDetail.objects.get_or_create(user_id=pk)
            serializers = UserDetailSerializers(userdetail)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            serializers = UserDetailSerializers(userdetail)
            return Response(serializers.data, status=status.HTTP_200_OK)



class GetRtmTokenAPI(APIView):
    def get(self, request, format=None):

        appID = "a6f19785b43d46d08ac412a2871b8ede"
        appCertificate = "8c6727c86f3a48ae9e3a6c98995850fa"
        # user = request.user.id
        pk = request.user.id
        user = str(pk)
        expirationTimeInSeconds = 3600
        currentTimestamp = int(time.time())
        privilegeExpiredTs = currentTimestamp + expirationTimeInSeconds
        rtmtoken = RtmTokenBuilder.buildToken(appID, appCertificate, user, Role_Rtm_User, privilegeExpiredTs)
        print("Rtm Token: {}".format(rtmtoken))

        return Response({'rtmtoken':rtmtoken,'userUuid1':user})
