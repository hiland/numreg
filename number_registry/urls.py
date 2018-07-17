from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.entry_list, name='entry_list'),
    #url(r'^reserve', views.reserve_new, name='reserve_new'),
	#url(r'^ordered/', views.entry_list, name='entry_list_ordered'),
]