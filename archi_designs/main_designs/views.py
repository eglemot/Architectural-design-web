from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db.models import Q


def home(request):
    plan_count = models.Plan.objects.count()
    return render(request, 'main_designs/home.html', {
        'plan_count': plan_count,
    })

def plan_list(request):
    plans = models.Plan.objects.all().prefetch_related('floor_pictures', 'plan_pictures')
    query = request.GET.get('q')
    if query:
        plans = plans.filter(Q(name__icontains=query) |
                             Q(description__icontains=query) |
                             Q(style__icontains=query))
    return render(request, 'main_designs/plan_list.html', {'plans': plans})



