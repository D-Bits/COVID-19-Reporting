from django.urls import path, include
from .views import IndexView, CasesView, DeathsView, RecoveriesView, about

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', about, name='about'),
    path('cases/', CasesView.as_view(), name="cases"), 
    path('deaths/', DeathsView.as_view(), name="deaths"),
    path('recoveries/', RecoveriesView.as_view(), name="recoveries"),   
]