from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Meoww
# Create your views here.


def meoww_list_view(request, *args, **kwargs):
    qs = Meoww.objects.all()
    meoww_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": meoww_list
    }
    return JsonResponse(data)


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
