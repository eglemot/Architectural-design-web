from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Plan, FloorPicture, PlanPicture
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class HomePageView(ListView):
    queryset = Plan.objects.all()
    template_name = 'main_designs/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_plans'] = Plan.objects.filter(id__in=[1, 2, 3, 4, 5, 6, 7, 8])

        under_2000 = Plan.objects.filter(heated_sq_feet__lt=2000)
        between_2000_3000 = Plan.objects.filter(heated_sq_feet__gte=2000, heated_sq_feet__lte=3000)
        above_3000 = Plan.objects.filter(heated_sq_feet__gt=3000)

        context['under_2000'] = under_2000
        context['between_2000_3000'] = between_2000_3000
        context['above_3000'] = above_3000

        context['plan_count'] = self.queryset.count()

        return context

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

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'main_designs/contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = f'New contact form submission: {title}'
        body = render_to_string('main_designs/email_body.txt', {'name': name, 'email': email, 'message': message})
        email = EmailMessage(subject, body, email, [settings.DEFAULT_FROM_EMAIL])
        email.send()

        messages.success(self.request, 'Thank you for your message!')
        return super().form_valid(form)
    
def privacy_policy(request):
    return render(request, 'main_designs/privacy_policy.html')

def affiliate_disclosure(request):
    return render(request, 'main_designs/affiliate_disclosure.html')













