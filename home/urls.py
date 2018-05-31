from django.urls import path
from .views import home, saida


urlpatterns = [
    path('', home, name="home"),
    path('logout/', saida, name="saida"),
    ]