import django.http
from django.shortcuts import render

# Create your views here.
# ---------------------------------- [edit 21/04/19 김인웅] ---------------------------------- #
from django.http import HttpResponse

def index(request):
    return render(request, 'firstpage.html')
# ------------------------------------------------------------------------------------------- #