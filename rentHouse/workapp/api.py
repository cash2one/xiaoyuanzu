
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .models import Area, HouseInfo, UserInfo, Collect, Appointment

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication


class AreaSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(min_length=1)

    class Meta:
        model = Area
        fields = '__all__'
        # fields=('id','username','email','profile')
        depth = 1
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        depth = 1
class AppointmentSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(min_length=1)
    # yytime = serializers.DateTimeField(format={"%m-%d %H:%i"})

    class Meta:
        model = Appointment
        fields = '__all__'
        # fields=('id','username','email','profile')
        depth = 1
class HouseInfoSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(min_length=1)

    class Meta:
        model = HouseInfo
        fields = '__all__'
        # fields=('id','username','email','profile')
        depth = 1


@api_view(['GET'])
def searchHouselist(request, area_id):
    print("area_id = " + area_id)
    a = Area.objects.get(id=area_id)
    house_list = HouseInfo.objects.filter(area_to=a).order_by('-rent')
    if request.method == 'GET':
        serializer = HouseInfoSerializer(house_list, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def indexapi(request):
    context = {}
    area_list = Area.objects.all()
    context['area_list'] = AreaSerializer(area_list,many=True).data

    cheapest_house_list = HouseInfo.objects.order_by('rent')[:3]
    context['excellent_house_list'] = HouseInfoSerializer(cheapest_house_list,many=True).data

    house_list = HouseInfo.objects.order_by('distance')
    near_area_list = []
    nearby_area_count = 0
    for house in house_list:
        nearby_area = house.area_to.all()
        for area in nearby_area:
            if area not in near_area_list:
                near_area_list.append(area)
                nearby_area_count += 1
            if nearby_area_count >= 3:
                break
        if nearby_area_count >= 3:
            break
    context['near_area_list'] = AreaSerializer(near_area_list,many=True).data

    return Response(context)


@api_view(['GET', 'POST'])
def readappoint(request, userid):
    print('userid: ',userid, 'readappoint api')
    resp = {}
    user = User.objects.get(id=userid)
    appoint_list = user.appoint_u.all()
    serializer = AppointmentSerializer(appoint_list, many=True)

    userinfo = UserInfoSerializer(user.user_info)
    resp['userinfo'] = userinfo.data
    resp['appoint_list'] = serializer.data
    return Response(resp)



@api_view(['GET', 'POST'])
# @authentication_classes((TokenAuthentication,))
def gethouseinfo(request,id):
    # if not request.user.is_superuser:
    #     body = {"msg": "Auth fail"}
    #     return Response(body, status=status.HTTP_403_FORBIDDEN)

    context = {}
    houseinfo = HouseInfo.objects.get(id=id)
    context['mianji'] = houseinfo.house.split(',')[0]
    context['louceng'] = houseinfo.house.split(',')[1]
    context['zhuangxiu'] = houseinfo.house.split(',')[2]
    context['chaoxiang'] = houseinfo.house.split(',')[3]
    context['zhuzhaileixing'] = houseinfo.house.split(',')[4]
    context['installations'] = houseinfo.installations.split(',')
    serializer = HouseInfoSerializer(houseinfo)
    context['houseinfo'] = serializer.data

    return Response(context)