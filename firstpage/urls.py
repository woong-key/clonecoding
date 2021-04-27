
# ---------------------------------- [edit 21/04/19 김인웅] ---------------------------------- #
from django.urls import path
from . import views

app_name = 'firstpage'

urlpatterns = [
# ------------------------------------------------------------------------------------------- #
    path('', views.index, name='index'),
]