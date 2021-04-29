
# ---------------------------------- [edit 21/04/19 김인웅] ---------------------------------- #
from django.urls import path
from . import views

app_name = 'firstpage'

urlpatterns = [
# ------------------------------------------------------------------------------------------- #
    path('', views.index, name='index'),
    path('slist', views.slist, name='slist'),
    path('scenecreate', views.scene_create, name='scene_create'),
    path('slist/<int:scene_id>/', views.slist, name=''),
    ]
