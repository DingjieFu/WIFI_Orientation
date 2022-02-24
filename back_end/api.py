'''
处理前端请求的后端服务程序入口
'''

import numpy as np
from matplotlib import pyplot as plt
from collections import UserList
import re
from typing_extensions import ParamSpec
from django.contrib import auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from back_end.models import Rss, Blocks, Test, TestRss
# from myblog.models import Classes
# from myblog.toJson import Classes_data,Userinfo_data
# from myblog.models import UserInfo
import json
from back_end.algorithm import KNN, compare
import matplotlib
matplotlib.use('Agg')

# 从Rss数据集中获取所有Rss指纹数据


@api_view(['GET'])
def getRssList(request):
    # 获取所有数据
    rsslist = Rss.objects.all()

    # 将数据封装为json数据格式
    data = []
    for item in rsslist:
        rss = []
        rss.append(item.position1)
        rss.append(item.position2)
        rss.append(item.position3)
        rss.append(item.position4)
        rss.append(item.position5)
        rss.append(item.position6)
        rss.append(item.position7)
        rss.append(item.position8)
        rss.append(item.position9)
        rss.append(item.position10)
        rss.append(item.position11)
        rss.append(item.position12)
        rss.append(item.position13)
        rss.append(item.position14)
        rss.append(item.position15)
        rss.append(item.position16)
        rss.append(item.position17)
        rss.append(item.position18)
        rss.append(item.position19)
        rss.append(item.position20)
        rss.append(item.position21)
        rss.append(item.position22)
        rss.append(item.position23)
        rss.append(item.position24)
        rss.append(item.position25)
        rss.append(item.position26)
        rss.append(item.position27)
        rss.append(item.position28)
        rss.append(item.position29)
        rss.append(item.position30)
        data_item = {
            'id': item.id,
            'rss': rss,
            'xlabel': item.xlabel,
            'ylabel': item.ylabel
        }
        data.append(data_item)

    # 返回获取的json数据
    return Response(data)


# 从验证数据库中获取所有数据（细节同前，略）
@api_view(['GET'])
def getTestList(request):
    testContent = Test.objects.all()
    data = []
    for item in testContent:
        data_item = {
            'id': item.id,
            'position1': item.position1,
            'position2': item.position2,
            'position3': item.position3,
            'position4': item.position4,
            'position5': item.position5,
            'position6': item.position6,
            'position7': item.position7,
            'position8': item.position8,
            'position9': item.position9,
            'position10': item.position10,

            'position11': item.position11,
            'position12': item.position12,
            'position13': item.position13,
            'position14': item.position14,
            'position15': item.position15,
            'position16': item.position16,
            'position17': item.position17,
            'position18': item.position18,
            'position19': item.position19,
            'position20': item.position20,

            'position21': item.position21,
            'position22': item.position22,
            'position23': item.position23,
            'position24': item.position24,
            'position25': item.position25,
            'position26': item.position26,
            'position27': item.position27,
            'position28': item.position28,
            'position29': item.position29,
            'position30': item.position30,
            'xlabel': item.xlabel,
            'ylabel': item.ylabel
        }
        data.append(data_item)
    return Response(data)

# 获取所有的页面状态


@api_view(['GET'])
def getMenuList(request):
    allBlocks = Blocks.objects.all()

    # 整理数据为json
    data = []
    for item in allBlocks:
        # 设计单条数据的结构
        data_item = {
            'id': item.id,
            'text': item.text
        }
        data.append(data_item)
    return Response(data)

# 对算法性能进行测试


@api_view(['GET'])
def algorithmTest(request):
    # 获取整个测试集
    getData = TestRss.objects.all()
    # 获取整个数据集
    loadData = Rss.objects.all()
    rssTest = []
    rssLoad = []
    testLocation = []
    realLocation = []

    # 整理测试数据
    for item in getData:
        rss = []
        locationItem = []
        rss.append(item.position1)
        rss.append(item.position2)
        rss.append(item.position3)
        rss.append(item.position4)
        rss.append(item.position5)
        rss.append(item.position6)
        rss.append(item.position7)
        rss.append(item.position8)
        rss.append(item.position9)
        rss.append(item.position10)
        rss.append(item.position11)
        rss.append(item.position12)
        rss.append(item.position13)
        rss.append(item.position14)
        rss.append(item.position15)
        rss.append(item.position16)
        rss.append(item.position17)
        rss.append(item.position18)
        rss.append(item.position19)
        rss.append(item.position20)
        rss.append(item.position21)
        rss.append(item.position22)
        rss.append(item.position23)
        rss.append(item.position24)
        rss.append(item.position25)
        rss.append(item.position26)
        rss.append(item.position27)
        rss.append(item.position28)
        rss.append(item.position29)
        rss.append(item.position30)
        rssTest.append(rss)
        locationItem.append(item.xlabel)
        locationItem.append(item.ylabel)
        testLocation.append(locationItem)

    # 整理训练数据
    for item in loadData:
        rss = []
        locationItem = []
        rss.append(item.position1)
        rss.append(item.position2)
        rss.append(item.position3)
        rss.append(item.position4)
        rss.append(item.position5)
        rss.append(item.position6)
        rss.append(item.position7)
        rss.append(item.position8)
        rss.append(item.position9)
        rss.append(item.position10)
        rss.append(item.position11)
        rss.append(item.position12)
        rss.append(item.position13)
        rss.append(item.position14)
        rss.append(item.position15)
        rss.append(item.position16)
        rss.append(item.position17)
        rss.append(item.position18)
        rss.append(item.position19)
        rss.append(item.position20)
        rss.append(item.position21)
        rss.append(item.position22)
        rss.append(item.position23)
        rss.append(item.position24)
        rss.append(item.position25)
        rss.append(item.position26)
        rss.append(item.position27)
        rss.append(item.position28)
        rss.append(item.position29)
        rss.append(item.position30)
        rssLoad.append(rss)
        locationItem.append(item.xlabel)
        locationItem.append(item.ylabel)
        realLocation.append(locationItem)

    # 从compare中获取NN、KNN、WKNN的参数
    accNN, accKNN, best_k_knn, accWK_NNC, best_k_wk_nnc, cdf_NN, cdf_KNN, cdf_WK_NNC = compare(
        rssLoad, rssTest, realLocation, testLocation)
    # 求均值
    avgNN = np.mean(accNN)
    avgKNN = np.mean(accKNN)
    avgWKNNC = np.mean(accWK_NNC)

    # 画出CDF曲线
    plt.step(np.linspace(min(accNN), max(accNN)), cdf_NN(
        np.linspace(min(accNN), max(accNN))), label="NN")
    plt.step(np.linspace(min(accKNN), max(accKNN)), cdf_KNN(np.linspace(min(accKNN), max(accKNN))),
             label=f"KNN(k={best_k_knn})")
    plt.step(np.linspace(min(accWK_NNC), max(accWK_NNC)), cdf_WK_NNC(np.linspace(min(accWK_NNC), max(accWK_NNC))),
             label=f"WK_KNN(k={best_k_wk_nnc})")
    plt.xlabel('distance estimation error(m)'), plt.ylabel('percentage')
    plt.legend()
    plt.savefig('../NN_KNN_WKNNC.jpg')

    return Response([avgNN, avgKNN, avgWKNNC])

# 室内指纹定位服务程序


@api_view(['POST'])
def orientation(request):
    # 由前端获取待预测数据和真实位置
    getData = request.POST['rss']

    # 按照逗号将待预测数据分割，转化为列表的形式（浮点数存储）
    getData = getData.split(',')
    for i in range(len(getData)):
        getData[i] = float(getData[i])

    # 数据处理
    rssTest = getData[0:len(getData) - 2]  # 得到待预测的Rss指纹
    testLocation = getData[len(getData) - 2: len(getData)]  # 得到待预测数据的真实位置
    rssList = Rss.objects.all()  # 得到Rss指纹训练集

    # 整理数据
    rssLoad = []
    location = []
    for item in rssList:
        rss = []
        locationItem = []
        rss.append(item.position1)
        rss.append(item.position2)
        rss.append(item.position3)
        rss.append(item.position4)
        rss.append(item.position5)
        rss.append(item.position6)
        rss.append(item.position7)
        rss.append(item.position8)
        rss.append(item.position9)
        rss.append(item.position10)
        rss.append(item.position11)
        rss.append(item.position12)
        rss.append(item.position13)
        rss.append(item.position14)
        rss.append(item.position15)
        rss.append(item.position16)
        rss.append(item.position17)
        rss.append(item.position18)
        rss.append(item.position19)
        rss.append(item.position20)
        rss.append(item.position21)
        rss.append(item.position22)
        rss.append(item.position23)
        rss.append(item.position24)
        rss.append(item.position25)
        rss.append(item.position26)
        rss.append(item.position27)
        rss.append(item.position28)
        rss.append(item.position29)
        rss.append(item.position30)
        rssLoad.append(rss)
        locationItem.append(item.xlabel)
        locationItem.append(item.ylabel)
        location.append(locationItem)

    # 使用KNN算法得到预测位置
    result = KNN(rssLoad, rssTest, location)
    print(testLocation)

    # 将预测位置返回前端页面
    return Response([result, testLocation])

# 实现数据库的update("改")


@api_view(['POST'])
def updateTestList(request):
    update = request.POST
    print(update)
    getData = Test.objects.get(id=update['id'])  # 得到所需改变数据的id

    # 如果对应表单不为空，就更新对应数据为获取值
    if (update['updateData[1]'] != ''):
        getData.position1 = update['updateData[1]']
    if (update['updateData[2]'] != ''):
        getData.position2 = update['updateData[2]']
    if (update['updateData[3]'] != ''):
        getData.position3 = update['updateData[3]']
    if (update['updateData[4]'] != ''):
        getData.position4 = update['updateData[4]']
    if (update['updateData[5]'] != ''):
        getData.position5 = update['updateData[5]']
    if (update['updateData[6]'] != ''):
        getData.position6 = update['updateData[6]']
    if (update['updateData[7]'] != ''):
        getData.position7 = update['updateData[7]']
    if (update['updateData[8]'] != ''):
        getData.position8 = update['updateData[8]']
    if (update['updateData[9]'] != ''):
        getData.position9 = update['updateData[9]']
    if (update['updateData[10]'] != ''):
        getData.position10 = update['updateData[10]']
    if (update['updateData[11]'] != ''):
        getData.position11 = update['updateData[11]']
    if (update['updateData[12]'] != ''):
        getData.position12 = update['updateData[12]']
    if (update['updateData[13]'] != ''):
        getData.position13 = update['updateData[13]']
    if (update['updateData[14]'] != ''):
        getData.position14 = update['updateData[14]']
    if (update['updateData[15]'] != ''):
        getData.position15 = update['updateData[15]']
    if (update['updateData[16]'] != ''):
        getData.position16 = update['updateData[16]']
    if (update['updateData[17]'] != ''):
        getData.position17 = update['updateData[17]']
    if (update['updateData[18]'] != ''):
        getData.position18 = update['updateData[18]']
    if (update['updateData[19]'] != ''):
        getData.position19 = update['updateData[19]']
    if (update['updateData[20]'] != ''):
        getData.position20 = update['updateData[20]']
    if (update['updateData[21]'] != ''):
        getData.position21 = update['updateData[21]']
    if (update['updateData[22]'] != ''):
        getData.position22 = update['updateData[22]']
    if (update['updateData[23]'] != ''):
        getData.position23 = update['updateData[23]']
    if (update['updateData[24]'] != ''):
        getData.position24 = update['updateData[24]']
    if (update['updateData[25]'] != ''):
        getData.position25 = update['updateData[25]']
    if (update['updateData[26]'] != ''):
        getData.position26 = update['updateData[26]']
    if (update['updateData[27]'] != ''):
        getData.position27 = update['updateData[27]']
    if (update['updateData[28]'] != ''):
        getData.position28 = update['updateData[28]']
    if (update['updateData[29]'] != ''):
        getData.position29 = update['updateData[29]']
    if (update['updateData[30]'] != ''):
        getData.position30 = update['updateData[30]']
    if (update['updateData[31]'] != ''):
        getData.xlabel = update['updateData[31]']
    if (update['updateData[32]'] != ''):
        getData.ylabel = update['updateData[32]']
    # 存储数据
    getData.save()
    return Response('ok')

# 实现数据库的delete（"删"）


@api_view(['DELETE'])
def deleteTestList(request):
    getControl = request.POST  # 获取当前操作状态
    print(getControl['controlNow'])
    # 如果当前状态允许delete，进行delete操作
    if (getControl['controlNow'] == 'delete'):
        deleteData = Test.objects.get(id=getControl['id'])  # 根据数据id定位需要删除的数据
        deleteData.delete()
        return Response('ok')

    # 如果当前状态不允许，则向前端页面返回操作提示
    else:
        return Response('Delete is not allowed now！')

# 实现数据库的add（"增"）


@api_view(['POST'])
def addTestList(request):
    update = request.POST  # 获取前端界面的更新表单
    getData = Test()  # 使用构造函数构造需要更新的数据格式

    # 将更新数据添加进构造的数据格式中
    if len(Test.objects.filter(id=update['updateData[0]'])) == 0:
        if (update['updateData[0]'] != ''):
            getData.id = update['updateData[0]']
        if (update['updateData[1]'] != ''):
            getData.position1 = update['updateData[1]']
        if (update['updateData[2]'] != ''):
            getData.position2 = update['updateData[2]']
        if (update['updateData[3]'] != ''):
            getData.position3 = update['updateData[3]']
        if (update['updateData[4]'] != ''):
            getData.position4 = update['updateData[4]']
        if (update['updateData[5]'] != ''):
            getData.position5 = update['updateData[5]']
        if (update['updateData[6]'] != ''):
            getData.position6 = update['updateData[6]']
        if (update['updateData[7]'] != ''):
            getData.position7 = update['updateData[7]']
        if (update['updateData[8]'] != ''):
            getData.position8 = update['updateData[8]']
        if (update['updateData[9]'] != ''):
            getData.position9 = update['updateData[9]']
        if (update['updateData[10]'] != ''):
            getData.position10 = update['updateData[10]']
        if (update['updateData[11]'] != ''):
            getData.position11 = update['updateData[11]']
        if (update['updateData[12]'] != ''):
            getData.position12 = update['updateData[12]']
        if (update['updateData[13]'] != ''):
            getData.position13 = update['updateData[13]']
        if (update['updateData[14]'] != ''):
            getData.position14 = update['updateData[14]']
        if (update['updateData[15]'] != ''):
            getData.position15 = update['updateData[15]']
        if (update['updateData[16]'] != ''):
            getData.position16 = update['updateData[16]']
        if (update['updateData[17]'] != ''):
            getData.position17 = update['updateData[17]']
        if (update['updateData[18]'] != ''):
            getData.position18 = update['updateData[18]']
        if (update['updateData[19]'] != ''):
            getData.position19 = update['updateData[19]']
        if (update['updateData[20]'] != ''):
            getData.position20 = update['updateData[20]']
        if (update['updateData[21]'] != ''):
            getData.position21 = update['updateData[21]']
        if (update['updateData[22]'] != ''):
            getData.position22 = update['updateData[22]']
        if (update['updateData[23]'] != ''):
            getData.position23 = update['updateData[23]']
        if (update['updateData[24]'] != ''):
            getData.position24 = update['updateData[24]']
        if (update['updateData[25]'] != ''):
            getData.position25 = update['updateData[25]']
        if (update['updateData[26]'] != ''):
            getData.position26 = update['updateData[26]']
        if (update['updateData[27]'] != ''):
            getData.position27 = update['updateData[27]']
        if (update['updateData[28]'] != ''):
            getData.position28 = update['updateData[28]']
        if (update['updateData[29]'] != ''):
            getData.position29 = update['updateData[29]']
        if (update['updateData[30]'] != ''):
            getData.position30 = update['updateData[30]']
        if (update['updateData[31]'] != ''):
            getData.xlabel = update['updateData[31]']
        if (update['updateData[32]'] != ''):
            getData.ylabel = update['updateData[32]']
        getData.save()
        return Response('ok')
    else:
        return Response('Already exists!')
