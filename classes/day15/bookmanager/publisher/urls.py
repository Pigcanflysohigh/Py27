from django.conf.urls import url
from django.contrib import admin
from publisher import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher_list_bak/$',views.publisher_list,name='pub_list'),  # 查看    # publisher_list_bak 在web界面输入该url时，又views.py文件里的publisher_list函数处理
    url(r'^publisher_add/$',views.publisher_add,name='pub_add'),    # 增加
    url(r'^publisher_del/(?P<pk>\d+)/$',views.publisher_del,name='pub_del'),    # 删除
    url(r'^publisher_edit/$',views.publisher_edit,name='pub_edit'),  # 编辑
]
