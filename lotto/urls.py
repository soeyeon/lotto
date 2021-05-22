from django.urls import path
from . import views

urlpatterns = [
    path('', views.lottopage, name="lottopage"),
    path('lottoresult/', views.lottoresult, name="lottoresult"),
]