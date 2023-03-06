from rest_framework import  serializers
from .models import course,usercourse
from user.serializers import UserDetailSerializers
from user.models import UserDetail

class courseSerializer(serializers.ModelSerializer):
    user = UserDetailSerializers()
    class Meta:
        model = course
        fields = ('room_id', 'course_name', 'course_describe', 'created_on', 'updated_on', 'user','type')

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        user = UserDetail.objects.create(**user_data)
        validated_data['user'] = user
        c = course.objects.create(**validated_data)
        return c

class usercourseSerializer(serializers.ModelSerializer):
    class Meta:
            model = usercourse
            fields = '__all__'