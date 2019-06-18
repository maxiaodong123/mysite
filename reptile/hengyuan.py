import requests
from reptile.models import BidInfo
from reptile.utils import phone_num
from django.shortcuts import render

# 引入库 threading
import threading
# import json
# from bs4 import BeautifulSoup

urlpage = 'https://www.qutouwang.com/qtw-invest-api/api/scatteredProduct/pc/findScatteredProductList'
smsUrl = 'https://www.qutouwang.com/qtw-invest-api/api/userRegister/sendMobileCode'
checkUrl = 'https://www.qutouwang.com/qtw-invest-api/api/userRegister/checkPhone'
detailUrl = 'https://www.qutouwang.com/qtw-invest-api/api/scatteredProduct/findP2pPactIssueDetail'

#1秒发送一次请求
def fun_timer():
    print('hello timer')   #打印输出
    global timer  #定义变量
    nop()
    timer = threading.Timer(1,fun_timer)   #60秒调用一次函数
    #定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
    timer.start()    #启用定时器


#定时
# timer = threading.Timer(1,fun_timer)  #首次启动
# timer.start()

def sms(request):
    print(2222222222222)
    phoneNums = phone_num(10)
    for phoneNum in phoneNums:
        r = requests.post(smsUrl, data={'mobile': phoneNum, 'pageSize': "3000"})
    print(r.json())
    result = r.json()
    print(type(result))
    # map = json.loads(result)
    # print(map)
    var = result['data']
    list = var['list']
    print(type(var['list']))
    for map in list:
        # print(map.get('pactissueNo'))
        save(map)

    return render(request, 'reptile/index.html')

def nop():
    print('调用接口')  # 打印输出
    r = requests.post(urlpage, data={'pageNum': "0", 'pageSize': "3000"})

def report(request):
    print(11111111111111)
    r = requests.post(urlpage, data={'pageNum': "0", 'pageSize': "3000"})
    print(r.json())
    result = r.json()
    print(type(result))
    # map = json.loads(result)
    # print(map)
    var = result['data']
    list = var['list']
    print(type(var['list']))
    for map in list:
        # print(map.get('pactissueNo'))
        save(map)

    return render(request, 'reptile/index.html')


# results = table.find_all('tr')
# print('Number of results', results)
# print('Number of results', len(results))
def save(map):
    bidinfo = BidInfo()
    bidinfo.pactissueNo = map.get('pactissueNo')
    bidinfo.bidCash= map.get('bidCash')
    bidinfo.termMonth=map.get('termMonth')
    bidinfo.businessRate=map.get('businessRate')
    bidinfo.issueTime=map.get('issueTime')
    bidinfo.xyLevel=map.get('xyLevel')
    bidinfo.surplusMoney=map.get('surplusMoney')
    bidinfo.applyAmt=map.get('applyAmt')
    bidinfo.bidPeopleNum=map.get('bidPeopleNum')
    bidinfo.returnMethod=map.get('returnMethod')
    bidinfo.balance=map.get('balance')
    bidinfo.closedDay=map.get('closedDay')
    bidinfo.bidState=map.get('bidState')
    bidinfo.bidAmt=map.get('bidAmt')
    bidinfo.bidProgress=map.get('bidProgress')
    bidinfo.applyTitle=map.get('applyTitle')
    BidInfo.save(bidinfo)
    # BidInfo.save()

def detailInfo(request):
    bidinfos =  BidInfo.objects.all()
    for bidInfo in bidinfos:
        r = requests.post(detailUrl, data={'pactissueNo':  bidInfo.pactissueNo})
        result = r.json()
        print(result)


    return render(request, 'reptile/index.html')