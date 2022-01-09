from collections import UserList
from typing_extensions import ParamSpec
from django.contrib import auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from back_end.models import Rss, Blocks, Test
# from myblog.models import Classes
# from myblog.toJson import Classes_data,Userinfo_data
# from myblog.models import UserInfo
import json
from back_end.algorithm import KNN


@api_view(['GET'])
def getRssList(request):
    rsslist = Rss.objects.all()
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
    return Response(data)


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


@api_view(['POST'])
def orientation(request):
    getData = request.POST['rss']
    getData = getData.split(',')
    for i in range(len(getData)):
        getData[i] = float(getData[i])
    rssTest = getData[0:len(getData) - 2]
    testLocation = getData[len(getData) - 2: len(getData)]
    rssList = Rss.objects.all()
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

    result = KNN(rssLoad, rssTest, location)
    print(testLocation)
    return Response([result, testLocation])


@api_view(['POST'])
def updateTestList(request):
    update = request.POST
    print(update)
    getData = Test.objects.get(id=update['id'])
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


@api_view(['DELETE'])
def deleteTestList(request):
    getControl = request.POST
    print(getControl['controlNow'])
    if (getControl['controlNow'] == 'delete'):
        deleteData = Test.objects.get(id=getControl['id'])
        deleteData.delete()
        return Response('ok')
    else:
        return Response('Delete is not allowed now！')


@api_view(['POST'])
def addTestList(request):
    update = request.POST
    getData = Test()
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
    else:
        print('Already exists!')
    return Response('ok')
