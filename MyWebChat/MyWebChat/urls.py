"""MyWebChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from MyWebChatApp.views import login_in, registration_in

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', TemplateView.as_view(template_name='login.html')),
    url(r'^registration/$', TemplateView.as_view(template_name='registration.html')),
    url(r'^restore/$', TemplateView.as_view(template_name='restore.html')),
    url(r'^login/login_in$', login_in),
    url(r'^registration/registration_in$', registration_in)
]