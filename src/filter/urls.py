from django.urls import path, re_path
from .views import *

urlpatterns = [

    path('create/', filter_create, name='filter_create'),

    # Retrieve task list
    path('', filter_list, name='filter_list'),

    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', filter_detail, name='filter_detail'),

    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', filter_update, name='filter_update'),

    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', filter_delete, name='filter_delete'),
    
    path("json", jsondata,name = "jsondata"),
]