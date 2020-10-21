from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	path('add1',views.home,name='home'),
    path('ad',views.ad,name='ad'),
    path('res',views.res,name='res'),
    path('dp',views.dp,name='dp'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('',views.res1,name='res1'),
    path('dp1',views.dp1,name='dp1'),
    path('update',views.update,name='update'),
    path('updat',views.updat,name='updat'),
    path('updt',views.updt,name='updt'),
    path('chnm',views.chnm,name='chnm'),
    path('chpn',views.chpn,name='chpn'),
    path('delete',views.delete,name='delete'),
    path('delt',views.delt,name='delt'),
]