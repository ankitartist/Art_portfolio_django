from django.urls import path
from django.conf.urls import url
from artapp import views

app_name='artapp'

urlpatterns=[path("user_login/",views.user_login,name="user_login"),
path("register",views.register,name="register"),
path("profile",views.profile,name='profile'),
url(r'^artworks1/(?P<pk>[0-9]+)$', views.artworks1, name='artworks1'),
path("viewart/",views.viewart,name='viewart'),
path("viewall/",views.viewall,name='viewall'),
url(r'^more1/(?P<pk>[0-9]+)$', views.more1, name='more1'),
url(r'^more2/(?P<pk>[0-9]+)$', views.more22, name='more2'),
url(r'^details/(?P<pk>[0-9]+)$', views.details1, name='details'),
path('portfolio', views.portfolio, name='portfolio'),
]