import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .forms import MeowwForm
from .models import Meoww
from .serializers import MeowwSerializer, MeowwActionSerializer
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def meoww_list_view_old(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JS or any frontend (iOS/Android)
    Return JSON Data
    """
    qs = Meoww.objects.all()
    meoww_list = [x.serialize() for x in qs]
    data = {
        "response": meoww_list
    }
    return JsonResponse(data)


@api_view(['GET'])
def meoww_list_view(request, *args, **kwargs):
    qs = Meoww.objects.all()
    serializer = MeowwSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def meoww_detail_view(request, meoww_id, *args, **kwargs):
    qs = Meoww.objects.filter(id=meoww_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = MeowwSerializer(obj)
    return Response(serializer.data, status=200)


@api_view(['GET', 'DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def meoww_delete_view(request, meoww_id, *args, **kwargs):
    qs = Meoww.objects.filter(id=meoww_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You cannot delete this tweet"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Tweet removed!"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def meoww_action_view(request, meoww_id, *args, **kwargs):
    '''
    id required
    action options: like, unlike, retweet
    '''
    serializer = MeowwActionSerializer(request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        meoww_id = data.get("id")
        action = data.get("action")

        qs = Meoww.objects.filter(id=meoww_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
        elif action == "unlike":
            obj.likes.remove(request.user)
        elif action == "retweet":
            pass  # Todo
    return Response({"message": "Tweet removed!"}, status=200)


@api_view(['POST'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def meoww_create_view(request, *args, **kwargs):
    serializer = MeowwSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


def meoww_create_view_old(request, *args, **kwargs):
    """
    REST API VIEW
    """
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    # print("ajax", request.is_ajax())
    form = MeowwForm(request.POST or None)
    next_url = request.POST.get("next") or None
    # print(next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = MeowwForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form})


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello User</h1>")
    return render(request, "pages/home.html", context={}, status=200)


def meoww_detail_view_old(request, meoww_id, *args, **kwargs):
    data = {
        "id": meoww_id,
    }
    status = 200
    try:
        obj = Meoww.objects.get(id=meoww_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data, status=status)
