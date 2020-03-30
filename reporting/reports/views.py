from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Sum
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


# View for info about deaths from COVID-19
class DeathsView(ListView):

    model = Summary
    context_object_name = 'countries'
    paginate_by = 25
    template_name = "reports/deaths.html"

    def get_queryset(self):

        return Summary.objects.order_by('-TotalDeaths')


# View for data about COVID-19 recoveries
class RecoveriesView(ListView):

    model = Summary
    context_object_name = 'countries'
    paginate_by = 25
    template_name = "reports/recoveries.html"

    def get_queryset(self):

        return Summary.objects.order_by('-TotalRecovered').aggregate(Sum('TotalRecovered'))


# For about page
def about(request):

    return render(request, 'reports/about.html')