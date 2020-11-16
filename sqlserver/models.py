from django.db import models

#添加新的app或数据类以后需要执行的操作
# 会自动更新结构，并在数据库下创建app_类名的表
# $ python3 manage.py migrate   # 创建表结构
#
# $ python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
# $ python3 manage.py migrate TestModel   # 创建表结构

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class Ami(models.Model):
    name = models.CharField(max_length=20)