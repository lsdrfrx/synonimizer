import json
from json import JSONDecodeError

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from synonymizer_app.serializers import AuthSerializer, SignUpSerializer
from rest_framework.authtoken.views import obtain_auth_token

# Create your views here.


@require_POST
def sign_in(request: WSGIRequest):
    try:
        json_data = json.loads(request.body)
        auth_serializer = AuthSerializer(data=json_data, context={"request": request})
    except JSONDecodeError:
        return HttpResponse("400 Bad request", status=400)

    if auth_serializer.is_valid():
        a: Response = obtain_auth_token(request)
        print(type(a))
        return a
    else:
        return HttpResponse("401 Unauthorized", status=401)


@require_POST
def sign_up(request):
    try:
        json_data = json.loads(request.body)
        register_serializer = SignUpSerializer(data=json_data)
    except JSONDecodeError:
        return HttpResponse("400 Bad request", status=400)

    try:
        register_serializer.is_valid(raise_exception=True)
        register_serializer.save()
        return obtain_auth_token(request)
    except ValidationError as exception:
        error = ""
        for _, info in exception.detail.items():
            error += str(info) + ' '
        return HttpResponse(error, status=400)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def workspace(request):
    return JsonResponse({"data": str(request.user)})


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def upload_file(request):
    # 1 - сохраняем файл
    # 2 - извлекаем из файла текст и обрабатываем его (находим наиболее часто употребимые слова,
    # оборачиваем в # и добавляем к ним их количество
    # 3 - возвращаем текст
    return JsonResponse({"text": "xуй"})


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def edit_text(request):
    return JsonResponse({"data": "xуй"})


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def give_away_edited():
    return JsonResponse({"data": "xуй"})

