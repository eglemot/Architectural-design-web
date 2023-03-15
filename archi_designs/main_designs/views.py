from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    plan_count = models.Plan.objects.count()
    return render(request, 'main_designs/index.html', {
        'plan_count': plan_count,
    })
