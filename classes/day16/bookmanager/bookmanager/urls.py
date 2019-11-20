"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from publisher import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^',include('publisher.urls')),    # 什么都不写，相当于写了一个根"/";如匹配/publisher_list/，在此处匹配到了/，剩下的会交给publiser.urls.py继续去匹配
    url(r'^publisher/',include('publisher.urls',namespace='app01'))# 此时给publisher.urls里的链接都加了/publisher/前缀，也就是需要访问/publisher/publisher_list

]
