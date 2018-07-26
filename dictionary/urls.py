"""dictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from number_registry import views
from number_registry import views as core_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'', views.index, name='index'),
    url(r'', include('number_registry.urls')),
    url(r'^reserve$', views.reserve_new,  name='reserve_new'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <-- For Social




    #url(r'^ordered/',  include('number_registry.urls')),
    ]