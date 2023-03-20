from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Plan, FloorPicture, PlanPicture
from django.core.paginator import Paginator



def home(request):
    plan_count = Plan.objects.count()
    return render(request, 'main_designs/home.html', {
        'plan_count': plan_count,
    })

def plan_list(request):
    min_bedrooms = request.GET.get('min_bedrooms')
    max_bedrooms = request.GET.get('max_bedrooms')
    floors = request.GET.get('floors')
    min_bathrooms = request.GET.get('min_bathrooms')
    max_bathrooms = request.GET.get('max_bathrooms')
    basement = request.GET.get('basement')
    loft = request.GET.get('loft')
    walk_in_pantry = request.GET.get('walk_in_pantry')
    home_office = request.GET.get('home_office')
    mudroom = request.GET.get('mudroom')
    bonus_room = request.GET.get('bonus_room')
    wrap_around_porch = request.GET.get('wrap_around_porch')
    style = request.GET.get('style')
    name_query = request.GET.get('name')

    q_filter = Q()

    if name_query:
        q_filter &= Q(name__icontains=name_query)
    if min_bedrooms:
        q_filter &= Q(max_bedrooms__gte=int(min_bedrooms))
    if max_bedrooms:
        q_filter &= Q(min_bedrooms__lte=int(max_bedrooms))
        if not min_bedrooms:
            q_filter &= Q(max_bedrooms__gte=int(max_bedrooms))
    if min_bathrooms:
        q_filter &= Q(max_bathrooms__gte=float(min_bathrooms))
    if max_bathrooms:
        q_filter &= Q(min_bathrooms__lte=float(max_bathrooms))
        if not min_bathrooms:
            q_filter &= Q(max_bathrooms__gte=float(max_bathrooms))
    if 'min_sq_feet' in request.GET and request.GET['min_sq_feet']:
        q_filter &= Q(heated_sq_feet__gte=float(request.GET['min_sq_feet']))
    if 'max_sq_feet' in request.GET and request.GET['max_sq_feet']:
        q_filter &= Q(heated_sq_feet__lte=float(request.GET['max_sq_feet']))
    if floors:
        q_filter &= Q(floors=int(floors))
    if basement:
        q_filter &= Q(basement=bool(basement))
    if loft:
        q_filter &= Q(loft=bool(loft))
    if walk_in_pantry:
        q_filter &= Q(walk_in_pantry=bool(walk_in_pantry))
    if home_office:
        q_filter &= Q(home_office=bool(home_office))
    if mudroom:
        q_filter &= Q(mudroom=bool(mudroom))
    if bonus_room:
        q_filter &= Q(bonus_room=bool(bonus_room))
    if wrap_around_porch:
        q_filter &= Q(wrap_around_porch=bool(wrap_around_porch))
    if style:
        q_filter &= Q(style=style)

    plans = Plan.objects.filter(q_filter)
    paginator = Paginator(plans, 12)
    page = request.GET.get('page')
    plans_paged = paginator.get_page(page)

    return render(request, 'main_designs/plan_list.html', {'plans': plans_paged})

def plan_detail(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    floor_pictures = FloorPicture.objects.filter(plan=plan)
    plan_pictures = PlanPicture.objects.filter(plan=plan)

    related_plans = Plan.objects.filter(min_bedrooms=plan.min_bedrooms).exclude(id=plan.id).order_by('?')[:4]

    return render(request, 'main_designs/plan_details.html', {
        'plan': plan, 
        'floor_pictures': floor_pictures, 
        'plan_pictures': plan_pictures,
        'related_plans': related_plans,
    })

















