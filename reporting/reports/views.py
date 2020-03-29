from django.shortcuts import render
from django.views.generic import ListView
from .models import Summary


# List all data from the Summary model
class IndexView(ListView):

    model = Summary
    ordering = ['-Country']
    template_name = "reports/base.html"
