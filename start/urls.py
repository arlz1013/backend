from django.urls import path

from start.views import UsersView as uss

urlpatterns = [
    # * Show Users
    path('uss', uss.user)
]