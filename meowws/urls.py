
from django.contrib import admin
from django.urls import path
from .views import (home_view, meoww_detail_view, meoww_action_view,
                    meoww_list_view, meoww_create_view, meoww_delete_view)

urlpatterns = [
    path('', meoww_list_view),
    path('create/', meoww_create_view),
    path('action/', meoww_action_view),
    path('<int:meoww_id>/', meoww_detail_view),
    path('<int:meoww_id>/delete/', meoww_delete_view),
]
