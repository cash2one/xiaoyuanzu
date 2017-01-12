from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


#学校表
class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)
    introduce = models.TextField(blank=True)
    picture = models.ImageField(upload_to='area_pic', blank=True)

    def __str__(self):
        return self.name


# 租房信息表
class HouseInfo(models.Model):
    title = models.CharField(max_length=200, blank=True)  # 房源标题
    # 所有房源图片，首张房源配图
    rent = models.IntegerField(default=1000)  # 房源价格
    type = models.CharField(max_length=200, blank=True)  # 类型
    house = models.TextField(default="", blank=True)  # 房屋信息
    address = models.CharField(max_length=200, blank=True)  # 地址信息
    community = models.TextField(default="", blank=True)  # 小区信息
    circum = models.TextField(default="", blank=True)  # 周边信息
    translate = models.TextField(default="", blank=True)  # 交通信息
    installations = models.CharField(max_length=200, blank=True)  # 设施信息
    area_to = models.ManyToManyField(to=Area, related_name='area_to')  # 房源对应学校名字
    label = models.CharField(max_length=200)  # 房源标签
    houseIntroduce = models.TextField()  # 房源简介
    distance = models.IntegerField(default=500)  # 房源和学校距离

    ARTICLE_CHOICES = {
        ('一室一厅一卫', '一室一厅一卫'),
        ('二室一厅一卫', '二室一厅一卫'),
        ('三室一厅一卫', '三室一厅一卫'),
        ('三室一厅两卫', '三室一厅两卫'),
        ('三室两厅两卫', '三室两厅两卫'),
        ('四室两厅两卫', '四室两厅两卫'),
    }
    housetype = models.CharField(choices=ARTICLE_CHOICES, max_length=200, blank=True)  # 户型
    # 标题，如清华东路27号院2居室整租

    # introduce = models.TextField()#详细介绍周边和交通
    # floor_decorate = models.CharField(max_length=300)#房屋面积和装修程度
    # housing_estate = models.CharField(max_length=200)#住宅小区

    pic_max = models.ImageField(upload_to='house_pic')
    pic_1 = models.ImageField(upload_to='house_pic', blank=True)
    pic_2 = models.ImageField(upload_to='house_pic', blank=True)
    pic_3 = models.ImageField(upload_to='house_pic', blank=True)
    pic_4 = models.ImageField(upload_to='house_pic', blank=True)
    pic_5 = models.ImageField(upload_to='house_pic', blank=True)
    pic_6 = models.ImageField(upload_to='house_pic', blank=True)
    pic_7 = models.ImageField(upload_to='house_pic', blank=True)
    pic_8 = models.ImageField(upload_to='house_pic', blank=True)
    pic_9 = models.ImageField(upload_to='house_pic', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['rent']


# 用户信息表
class UserInfo(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='user_info')
    name = models.CharField(max_length=50)
    # username = models.CharField(blank=True, null=False, unique=True, max_length=10)
    # password = models.CharField(blank=True, null=False, max_length=8)
    phone_number = models.CharField(max_length=11, blank=True)
    ARTICLE_CHOICES = {
        ('保密', '保密'),
        ('男', '男'),
        ('女', '女'),
    }
    sex = models.CharField(choices=ARTICLE_CHOICES, max_length=10, default='保密')
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatar', default='avatar/wenhao.png')

    def __str__(self):
        return self.name


class Collect(models.Model):
    user = models.ForeignKey(to=UserInfo, related_name='user')
    house_title = models.ForeignKey(to=HouseInfo, related_name='house_title')
    datetime = models.DateTimeField(null=False, default=now)


# 提交预约
class Appointment(models.Model):
    yytime = models.DateTimeField(null=False, default=now)  # 预约时间
    yyname = models.CharField(max_length=200, blank=True)  # 预约人
    yyphone = models.CharField(max_length=200, blank=True)  # 预约号码
    userinfo = models.ForeignKey(to=User,related_name="appoint_u",default=False)
    houseinfo = models.ForeignKey(to=HouseInfo,related_name="appoint_h",default=False)

    def __str__(self):
        return self.yyname
