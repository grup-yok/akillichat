"""chat URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from front import views as Front
from backoffice import views as BackOffice

urlpatterns = [
    url(r'^$', Front.index, name="home"),
    url(r'^office/index', BackOffice.index, name="backoffice"),
    url(r'^office/add', BackOffice.add, name="backofficeadd"),
    url(r'^office/update', BackOffice.update, name="backofficeupdate"),
    url(r'^office/ajax', BackOffice.ajax, name="backofficeajax"),
    url(r'^api/ask', Front.messageReceive, name="ask"),
    url(r'^admin/', admin.site.urls),
]
