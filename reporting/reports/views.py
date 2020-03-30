from django.shortcuts import render
from django.views.generic import ListView
from .models import Summary


# List all data from the Summary model
class IndexView(ListView):

    model = Summary
    ordering = ['Country']
    context_object_name = 'countries'
    paginate_by = 25
    template_name = "reports/index.html"


# View for info about ongoing cases
class CasesView(ListView):

    model = Summary
    context_object_name = 'countries'
    paginate_by = 25
    template_name = "reports/cases.html"

    def get_queryset(self):

        return Summary.objects.order_by('-TotalConfirmed')