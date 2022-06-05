from django.urls import path
from . import views
import re

urlpatterns = [
    path('', views.fronpage),
    path('settings', views.settings),
    path('add_category', views.addCategory),
    path('delete_category/<str:category>', views.deleteCategory),
    path('add_record', views.addRecord),
    path('delete_record', views.deleteRecord)
]
