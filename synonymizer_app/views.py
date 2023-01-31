from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from rest_framework.authtoken.models import Token

from synonymizer import settings


# Create your views here.


def sign_up(request):
    return JsonResponse({"data": "xуй"})

@login_required
def workspace(request):
    return JsonResponse({"data": "xуй"})


@login_required
def upload_file(request):
    # 1 - сохраняем файл
    # 2 - извлекаем из файла текст и обрабатываем его (находим наиболее часто употребимые слова,
    # оборачиваем в # и добавляем к ним их количество
    # 3 - возвращаем текст
    return JsonResponse({"text": "xуй"})


@login_required
def edit_text(request):
    return JsonResponse({"data": "xуй"})


@login_required
def give_away_edited():
    return JsonResponse({"data": "xуй"})