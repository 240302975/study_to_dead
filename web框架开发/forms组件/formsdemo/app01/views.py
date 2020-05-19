from django.shortcuts import render,HttpResponse

# Create your views here.


from app01.myforms import *


def reg(request):

    if request.method=="POST":

        print(request.POST)

        #form=UserForm({"name":"yu","email":"123@qq.com","xxxx":"alex"})


        form=UserForm(request.POST) # form表单的name属性值应该与forms组件字段名称一致。已绑定数据

        print(form.is_valid()) # 返回布尔值

        if form.is_valid():
            print(form.cleaned_data)  # {"name":"yuan","email":"123@qq.com"}
        else:
            print(form.cleaned_data)  # {"email":"123@qq.com"}
            # print(form.errors)        # {"name":[".........."]}  错误的键以及对应的信息
            # print(type(form.errors))  # ErrorDict
            # print(form.errors.get("name"))
            # print(type(form.errors.get("name")))    # ErrorList
            # print(form.errors.get("name")[0])       #取错误信息


            #   全局钩子错误
            #print("error",form.errors.get("__all__")[0])
            errors=form.errors.get("__all__")


            return render(request,"reg.html",locals())

        '''

        form.is_valid()   :返回布尔值
        form.cleaned_data :{"name":"yuan","email":"123@qq.com"}  通过校验的值,返回类型为字典dict型
        form.errors       :{"name":[".........."]}

        '''


    form=UserForm()  # 未绑定数据的

    return render(request,"reg.html",locals())