from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import json
import time
import random
import os.path


def addGoods(request):
    return render(request, 'addGoods.html')
def goods_add(request):
    return render(request,"in_cont.html")

data = {
        'status': 'ok',
        'msg': '操作成功',
        'data': []
    }
cursor = connection.cursor()


def sql_yuju(sql):
    jieguo = cursor.execute(sql)
    return jieguo


def shop_select(request):
    data["data"] = []
    goodsname = request.GET.get("goodsname", "")
    try:
        sql = 'SELECT * FROM goods WHERE goodsname LIKE "%' + goodsname + '%"'
        sql_yuju(sql)
        jieguo = cursor.fetchall()
        print(jieguo)
        print(type(jieguo))
        if jieguo == '':
            data["status"] = 'error'
            data['msg'] = '查询失败'
            return HttpResponse(json.dumps(data))
        else:
            data["data"].append(jieguo)
            return HttpResponse(json.dumps(data))
    except:
        data["status"] = 'error'
        data['msg'] = '查询失败'
        return HttpResponse(json.dumps(data))
# 上传模块
#


def shop_insert(request):
    # print(request.POST)

    # print("----------------------")

    # print("我是文件.....")
    # print(request.FILES)


    timenow = int((time.time())*100)
    number = random.randint(1, 10)
    goodsid = timenow * number
    goodsname = request.POST.get("goodsname", "")
    shopname = request.POST.get("shopname","")
    prodect_brand = request.POST.get("brand", "")
    prodect_number = request.POST.get("numbering","")
    prodect_brief_info = request.POST.get("brief_introduction", "")
    guige = request.POST.get("class","")
    keyword = request.POST.get("tagEditor_cont","")
    # keywords = request.POST.get("keywords", "")
    market_price = request.POST.get("market_price", "")
    shop_price = request.POST.get("shop_price", "")
    counts = request.POST.get("kucun", "")
    songjifen = request.POST.get("jifen","")
    jifenprice = request.POST.get("jifen_price","")
    rebate = request.POST.get("fanli","")
    transportm = request.POST.get("yunfei","")
    canshuname = request.POST.get("canshuname","")
    canshuzhi = request.POST.get("canshuzhi","") 
    # status = request.POST.get("status", "")
    img_data = request.FILES["img"].__dict__["file"].read()
    # type(request.FILES.get("img"))
    img_name = request.FILES["img"].__dict__['_name']
    img_hz = os.path.splitext(img_name)[1]
    img = "static/img/"+str(goodsid)+img_hz
    with open(img, "wb") as f:
        f.write(img_data)
    if goodsname=='':
        data["status"] = 'error'
        data['msg'] ='添加失败'
        return HttpResponse(json.dumps(data))
    try:
        sql ='insert into goods (goodsid,goodsname,shopname,prodect_brand,product_number,prodect_brief_info,guige,keywords,market_price,shop_price,counts,songjifen,jifenprice,rebate,transportm,canshuname,canshuzhi,img) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (goodsid,goodsname,shopname,prodect_brand,prodect_number,prodect_brief_info,guige,keyword,market_price,shop_price,counts,songjifen,jifenprice,rebate,transportm,canshuname,canshuzhi,img)
        row = sql_yuju(sql)
        connection.commit()
        if row:
            return HttpResponse(json.dumps(data))
        else:
            data["status"] = 'error'
            data['msg'] ='添加失败'
            connection.rollback()
            return HttpResponse(json.dumps(data))
    except Exception as f:
        print(f)
        data["status"] ='error'
        data["msg"] = '添加失败'
        connection.rollback()
    return HttpResponse(json.dumps(data))
    # return HttpResponse("上传成功")

    
def shop_update(request):
    goodsname=request.GET.get("goodsname","")
    newgoodsname=request.GET.get("newgoodsname","")
    print(goodsname,newgoodsname)
    try:
        sql ='update goods set goodsname ="%s" where goodsname="%s"'%(newgoodsname,goodsname)
        print(sql)
        sql_yuju(sql)
        connection.commit()
        return HttpResponse(json.dumps(data))
    except:
        data["status"] = 'error'
        data['msg'] ='更新失败'
        connection.rollback()
        return HttpResponse(json.dumps(data))
def shop_del(request):
    data["data"]=[]
    goodsname=request.GET.get("goodsname","")
    try:
        sql ='delete from goods where goodsname="%s"'%goodsname      
        sql_yuju(sql)
        connection.commit()
        return HttpResponse(json.dumps(data))
    except:
        data["status"] = 'error'
        data['msg'] ='删除失败'
        connection.rollback()
        return HttpResponse(json.dumps(data))
