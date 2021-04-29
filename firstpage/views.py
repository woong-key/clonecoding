from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Scene
from .forms import SceneForm

# Create your views here.
# ---------------------------------- [edit 21/04/19 김인웅] ---------------------------------- #
from django.http import HttpResponse

def index(request):
    Scene_list = Scene.objects.order_by('-scene_datetime')
    return render(request, 'firstpage.html', {'scene': Scene_list})
# ------------------------------------------------------------------------------------------- #

# 2021.04.28 김인웅 - scene_list 뷰 작성

def slist(request):
    page = request.GET.get('page', '1')
    scene_list = Scene.objects.order_by('scene_datetime')
    paginator = Paginator(scene_list, 5)
    show_page = paginator.get_page(page)
    return render(request, 'scene_list.html', {'show_page': show_page, 'page': page})


def scene_create(request):
    form = SceneForm(request.POST)
    if form.is_valid():
        scene = form.save(commit=False)
        scene.scene_datetime = timezone.now()
        scene.save()
        return redirect('firstpage:slist')
