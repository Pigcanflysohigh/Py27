from django.shortcuts import render,redirect,reverse
from publisher import models
from django.views import View
# Create your views here.


class PublisherList(View):
    def get(self,request,*args,**kwargs):
        allPub = models.Publisher.objects.all().values()
        return render(request,'publisher_list.html',{'all_Pub':allPub})

class PublisherAdd(View):
    def get(self,request,*args,**kwargs):
        return render(self.request,'publisher_add.html')

    def post(self,request,*args,**kwargs):
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(self.request,'publisher_add.html',{'error':'出版社不能为空'})
        models.Publisher.objects.create(name=pub_name)
        return redirect(reverse('app01:pub_list'))

class PublisherDel(View):
    def get(self,request,*args,**kwargs):   # 如果此处不写request，后面代码要用self.request来代替(两者是相同的)
        pk = kwargs['pk']
        print(pk)
        models.Publisher.objects.filter(pk=pk).delete()
        return redirect(reverse('app01:pub_list'))

class PublisherEdit(View):
    def get(self,request,*args,**kwargs):
        pk = kwargs['pk']
        obj = models.Publisher.objects.get(pk=pk)
        return render(request,'publisher_edit.html',{'name':obj.name})
    def post(self,request,*args,**kwargs):
        pub_name = request.POST.get('pub_name')
        pk = kwargs['pk']
        obj = models.Publisher.objects.get(pk=pk)
        if not pub_name:
            return render(request,'publisher_edit.html',{'error':'出版社不能为空'})
        obj.name = pub_name
        obj.save()
        return redirect(reverse('app01:pub_list'))

class BookList(View):
    def get(self,request,*args,**kwargs):
        all_books = models.Book.objects.all()   # .all()返回的是一个对象，如果再加上.values()则是返回的字典
        # print(all_books)
        return render(request,'book_list.html',{'all_books':all_books})

class BookAdd(View):
    def get(self,request,*args,**kwargs):
        # 查询所有出版社
        all_pubs = models.Publisher.objects.all()
        return render(request,'book_add.html',{'all_pubs':all_pubs})
    def post(self,request,*args,**kwargs):
        # 获取参数
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')
        # 判断图书填写是否为空
        if not title:
            all_pubs = models.Publisher.objects.all()
            return render(request,'book_add.html',{'all_pubs':all_pubs,'error':'图书不能为空'})
        # 插入数据
        # models.Book.objects.create(title=title,pub=models.Publisher.objects.get(pk=pub_id))
        models.Book.objects.create(title=title,pub_id=pub_id)
        # 重定向
        return redirect(reverse('app01:book_list'))



# 图书编辑
class BookEdit(View):
    def get(self,request,pk):
        book_obj = models.Book.objects.get(pk=pk)
        all_pubs = models.Publisher.objects.all()
        return render(request,'book_exit.html',{'book_obj':book_obj,'all_pubs':all_pubs})
    def post(self,request,pk):
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')
        models.Book.objects.filter(pk=pk).update(title=title,pub_id=pub_id)
        return redirect(reverse('app01:book_list'))

