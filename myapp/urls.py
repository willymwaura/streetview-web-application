from django.urls import path
from. import views

urlpatterns=[

    path('',views.index,name='index'),
    path('test',views.test,name='test'),
    path('search',views.search,name='search'),
    path('random',views.random,name='random'),


]