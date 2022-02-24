'''
定义数据模型（数据库）
'''

from django.db import models
from django.db.models.fields import CharField


# Create your models here.

# Rss存储Rss室内指纹数据集
class Rss(models.Model):

    # 30个监测点的信号强度
    position1 = models.FloatField()
    position2 = models.FloatField()
    position3 = models.FloatField()
    position4 = models.FloatField()
    position5 = models.FloatField()
    position6 = models.FloatField()
    position7 = models.FloatField()
    position8 = models.FloatField()
    position9 = models.FloatField()
    position10 = models.FloatField()
    position11 = models.FloatField()
    position12 = models.FloatField()
    position13 = models.FloatField()
    position14 = models.FloatField()
    position15 = models.FloatField()
    position16 = models.FloatField()
    position17 = models.FloatField()
    position18 = models.FloatField()
    position19 = models.FloatField()
    position20 = models.FloatField()
    position21 = models.FloatField()
    position22 = models.FloatField()
    position23 = models.FloatField()
    position24 = models.FloatField()
    position25 = models.FloatField()
    position26 = models.FloatField()
    position27 = models.FloatField()
    position28 = models.FloatField()
    position29 = models.FloatField()
    position30 = models.FloatField()

    # 真实位置坐标(x, y)
    xlabel = models.FloatField()
    ylabel = models.FloatField()

    def __int__(self):
        return self.id

# 存储Rss测试集的数据库
class TestRss(models.Model):
    position1 = models.FloatField()
    position2 = models.FloatField()
    position3 = models.FloatField()
    position4 = models.FloatField()
    position5 = models.FloatField()
    position6 = models.FloatField()
    position7 = models.FloatField()
    position8 = models.FloatField()
    position9 = models.FloatField()
    position10 = models.FloatField()
    position11 = models.FloatField()
    position12 = models.FloatField()
    position13 = models.FloatField()
    position14 = models.FloatField()
    position15 = models.FloatField()
    position16 = models.FloatField()
    position17 = models.FloatField()
    position18 = models.FloatField()
    position19 = models.FloatField()
    position20 = models.FloatField()
    position21 = models.FloatField()
    position22 = models.FloatField()
    position23 = models.FloatField()
    position24 = models.FloatField()
    position25 = models.FloatField()
    position26 = models.FloatField()
    position27 = models.FloatField()
    position28 = models.FloatField()
    position29 = models.FloatField()
    position30 = models.FloatField()
    xlabel = models.FloatField()
    ylabel = models.FloatField()

    def __int__(self):
        return self.id

# 存储三种页面状态（室内地图区，指纹可视化区，定位区）
class Blocks(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

# 用于测试数据库操作的Rss指纹数据库
class Test(models.Model):
    position1 = models.FloatField()
    position2 = models.FloatField()
    position3 = models.FloatField()
    position4 = models.FloatField()
    position5 = models.FloatField()
    position6 = models.FloatField()
    position7 = models.FloatField()
    position8 = models.FloatField()
    position9 = models.FloatField()
    position10 = models.FloatField()
    position11 = models.FloatField()
    position12 = models.FloatField()
    position13 = models.FloatField()
    position14 = models.FloatField()
    position15 = models.FloatField()
    position16 = models.FloatField()
    position17 = models.FloatField()
    position18 = models.FloatField()
    position19 = models.FloatField()
    position20 = models.FloatField()
    position21 = models.FloatField()
    position22 = models.FloatField()
    position23 = models.FloatField()
    position24 = models.FloatField()
    position25 = models.FloatField()
    position26 = models.FloatField()
    position27 = models.FloatField()
    position28 = models.FloatField()
    position29 = models.FloatField()
    position30 = models.FloatField()
    xlabel = models.FloatField()
    ylabel = models.FloatField()

    def __int__(self):
        return self.id
