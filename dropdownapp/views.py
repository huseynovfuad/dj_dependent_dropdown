from django.shortcuts import render,get_object_or_404,redirect
from .models import Country,City,Travel
from .forms import TravelForm
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.


def create_travel(request):
    context = {}
    form = TravelForm()
    if request.method == "POST":
        form = TravelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('create-travel')
    context['form']=form
    return render(request,'home.html',context)

def update_travel(request,travel_id):
    context = {}
    travel = get_object_or_404(Travel,id=travel_id)
    form = TravelForm(instance=travel)
    if request.method == 'POST':
        form = TravelForm(request.POST or None,instance=travel)
        if form.is_valid():
            form.save()
            return redirect('update-travel',travel_id=travel_id)
    context['form']=form
    return render(request,'update.html',context)

def upload_cities(request):
    data = {}
    country_id = int(request.GET['country_id'])
    cities = City.objects.filter(country_id = country_id)
    data['include'] = render_to_string('include.html', {'cities': cities}, request)
    return JsonResponse(data)
