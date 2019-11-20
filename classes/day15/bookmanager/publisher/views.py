from django.shortcuts import render,redirect
from publisher import models

# Create your views here.
def publisher_list(request):
    # 查询所有出版社的信息
    all_publishers = models.Publisher.objects.all()
    # 返回一个页面来展示
    return render(request,'publisher_listabc.html',{'all_publishers':all_publishers})
    # render函数中第二个参数，决定返回templates文件夹下哪个html文件

def publisher_add(request):
    if request.method == "POST":
        # 获取提交的数据
        pub_name = request.POST.get('pub_name')
        # 提交数据的校验
        if not pub_name:
            return render(request,'publisher_add.html',{'error':'名称不能为空'})
        # 插入数据库
        ret = models.Publisher.objects.create(name=pub_name)
        print(ret,type(ret))
        # 返回展示页面
        # return redirect('/publisher_list_bak/')
        return redirect(reversed('pub_list'))
    return render(request,'publisher_add.html')

def publisher_del(request,pk):
    # 获取提交的数据，通过get获取的
    # pk = request.GET.get('pk')
    # 删除对应的数据
    # models.Publisher.objects.get(pk=pk).delete()    # 删除单个对象
    models.Publisher.objects.filter(pk=pk).delete() # 获取对象列表，删除多个对象
    # 跳转回展示页面
    # return  redirect('/publisher_list_bak')
    return redirect(reversed('pub_list'))

def publisher_edit(request):
    # 获取从list页面提交的数据
    pk = request.GET.get('pk')
    # 查找对应对象，并编辑
    obj = models.Publisher.objects.get(pk=pk)
    # 处理提交数据
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        obj.name = pub_name # 于内存中修改name属性
        obj.save()  # 向数据库提交更新
        # 跳转回展示页面
        # return redirect('/publisher_list_bak')  # 重定向   # 即重新get请求ublisher_listabc.html页面
        return redirect(reversed('pub_list'))
    # 将要编辑的对象返回编辑页面
    return render(request,'publisher_edit.html',{'obj':obj})

# urls.py ：指定get方式请求的链接与views.py文件夹中函数的对应关系；请求的链接不一定和返回的html文件名称一致.(不负责返回页面，只负责请求与函数的对应关系；返回页面由函数中render决定)
# views.py ： 定义通过前端获取数据，并反馈到后台的逻辑的函数
    # render ：是以get方式请求某页面并返回，参数中指定templates文件夹下具体的html文件，参数名和html文件名保持一致
    # redirect ： 重定向新的页面，但是redirect带的参数要和urls.py文件中指定的链接保持一致，而不是templates下的html文件名；也就是说他只是模拟请求，最后返回页面还是靠render函数
# models.py ： 定义一个类，实现和数据库数据的一一对应，相当于一个数据库操作接口