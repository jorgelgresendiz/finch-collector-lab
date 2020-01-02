from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Feeding
from .forms import FeedingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    # instantitate feeding form to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        # include the finch and feeding form in the context
        'finch': finch,
        'feeding_form': feeding_form
    })


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['beak', 'description', 'age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches/"
