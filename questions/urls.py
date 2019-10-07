from django.urls import path
from . import views

app_name = "questinos"
urlpatterns = [
    path('', views.index, name="index"),
]
