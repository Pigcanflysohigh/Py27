from django.conf.urls import url
from publisher import views

urlpatterns = [
    url(r'^publisher_list/$',views.PublisherList.as_view(),name='pub_list'),
    url(r'^publisher/add/$',views.PublisherAdd.as_view(),name='pub_add'),
    url(r'^publisher_del/(?P<pk>\d+)/$',views.PublisherDel.as_view(),name='pub_del'),
    url(r'^publisher_edit/(?P<pk>\d+)/$',views.PublisherEdit.as_view(),name='pub_edit'), # 开头的"/"只有在根下的urls.py里默认添加，如果在第二层就不会自动加'/'了
    url(r'^book_list/$',views.BookList.as_view(),name='book_list'),
    url(r'^book_add/$',views.BookAdd.as_view(),name='book_add'),
    url(r'^book_edit/(?P<pk>\d+)$',views.BookEdit.as_view(),name='book_edit')
]
