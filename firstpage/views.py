from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Scene
from .forms import SceneForm

# Create your views here.
# ---------------------------------- [edit 21/04/19 김인웅] ---------------------------------- #
from django.http import HttpResponse

def index(request):
    return render(request, 'firstpage.html')

    # Scene_list = Scene.objects.order_by('-scene_datetime')
    # return render(request, 'firstpage.html', {'scene': Scene_list})
# ------------------------------------------------------------------------------------------- #

# 2021.04.28 김인웅 - scene_list 뷰 작성

def slist(request):
    page = request.GET.get('page', '1')
    scene_list = Scene.objects.order_by('-scene_datetime')
    paginator = Paginator(scene_list, 5)
    show_page = paginator.get_page(page)
    return render(request, 'scene_list.html', {'show_page': show_page, 'page': page})


def scene_create(request):

    form = SceneForm(request.POST)
    if form.is_valid():
        scene = form.save(commit=False)
        scene.scene_subject = scene.scene_content[:10]
        scene.scene_datetime = timezone.now()
        scene.save()
        return redirect('firstpage:slist')

# 2021.04.29 김인웅 - scene_content, delete 뷰 작성

def scene_content(request, scene_id):

    scene = get_object_or_404(Scene, pk=scene_id)
    return render(request, 'scene_content.html', {'scene': scene})


def scene_delete(request, scene_id):

    scene = get_object_or_404(Scene, pk=scene_id)
    form = SceneForm(request.POST)

    if request.method == "POST":
        print(form.is_valid())
        if form.scene_password.value == scene.scene_password:
            scene.delete()
            return redirect(request, 'firstpage:slist')