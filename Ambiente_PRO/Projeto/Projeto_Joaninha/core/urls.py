from django.urls import path
from django.contrib.auth.views import LogoutView
from Projeto_Joaninha.core import views as v


app_name = 'core'


urlpatterns = [
    path('logout/',LogoutView.as_view(),name='logout'),
    path('', v.index, name='index'),
    
    
]
