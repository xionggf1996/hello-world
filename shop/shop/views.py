from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import json
import time
import random
def index(request):
    return render(request,'index.html')
    # return HttpResponse("dsadadasd")
def lianxi(request):
    return render(request,'members.html')
def login(request):
    return render(request,'login.html')
def login_checked(request):
    data = {"status":"ok","message":"登陆成功","data":[]}
    name=request.POST.get("username","")
    pwd= request.POST.get("pwd","")
    if name =='' and pwd =='':
        data['message']='登录失败'
        data['status']='error'
        return HttpResponse(json.dumps(data))
    if name=="12"  and pwd=="1212":
        return HttpResponse(json.dumps(data))
    else:
        data['message']='登录失败'
        data['status']='error'
        return HttpResponse(json.dumps(data))



        # if ($('.username').length == 0 || $('.pwd').length == 0) {
        #         show ='请输入用户名或密码...'
        #         $.message({
        #             message:show,
        #             type:'info',
        #         });
        #         return
        #     }
        # })




    