import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from .forms import MeowwForm
from .models import Meoww
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def meoww_list_view(request, *args, **kwargs):
    qs = Meoww.objects.all()
    meoww_list = [{"id": x.id, "content": x.content,
                   "likes": random.randint(0, 200)} for x in qs]
    data = {
        "response": meoww_list
    }
    return JsonResponse(data)


def meoww_create_view(request, *args, **kwargs):
    form = MeowwForm(request.POST or None)
    next_url = request.POST.get("next") or None
    # print(next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = MeowwForm()
    return render(request, 'components/form.html', context={"form": form})


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello User</h1>")
    return render(request, "pages/home.html", context={}, status=200)


def meoww_detail_view(request, meoww_id, *args, **kwargs):
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