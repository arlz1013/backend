from django.urls import path

from start.views.UsersView import API as uss

urlpatterns = [
    # * Show Users
    path('uss', uss.user)
]