from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        # if 验证成功返回user对象,否则返回None
        user=auth.authenticate(username=user,password=pwd)

        if user:
            auth.login(request,user)   # request.user:当前登录对象  实现一个用户登录的功能。它本质上会在后端为该用户生成相关session数据。

            next_url=request.GET.get("next","/index/")
            return  redirect(next_url)


    return render(request,"login.html")



@login_required
def index(request):

    # print("request.user:",request.user.username)  没有用户的话打印匿名AnonymousUser
    # print("request.user:",request.user.id)
    # print("request.user:",request.user.is_anonymous)  是否为匿名
    #
    # #if request.user.is_anonymous:
    # if not request.user.is_authenticated:
    #     return redirect("/login/")

    #username=request.user.username
    #return render(request,"index.html",{"username":username})
    # request.user是全局变量，在视图里不需要传，可以直接使用
    return render(request,"index.html")


@login_required
def order(request):

    # if not request.user.is_authenticated:
    #     return redirect("/login/")


    return render(request,"order.html")







def logout(request):

    auth.logout(request)

    return redirect("/login/")




def reg(request):
    if request.method=="POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        #User.objects.create(username=user,password=pwd)
        user=User.objects.create_user(username=user,password=pwd)  # auth 提供的一个创建新用户的方法

        return redirect("/login/")


    return render(request,"reg.html")


