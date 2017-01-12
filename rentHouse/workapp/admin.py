from django.contrib import admin
from workapp.models import *


admin.site.register(Appointment)
admin.site.register(Area)
admin.site.register(Collect)
admin.site.register(HouseInfo)
admin.site.register(UserInfo)

# 超级管理员账号密码: Admin/Admin123456
