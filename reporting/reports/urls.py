from django.urls import path, include
from .views import IndexView, CasesView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('cases/', CasesView.as_view(), name="cases"),    
]