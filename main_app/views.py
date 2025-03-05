from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Media
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name = 'home.html'

@login_required
def media_index(request):
    media = Media.objects.all() 
    return render(request, 'media/index.html', {'media': media})

@login_required
def media_detail(request, media_id):
    media = Media.objects.get(id=media_id)
    return render(request, 'media/detail.html', {'media': media})


class MediaUpdate(LoginRequiredMixin, UpdateView):
    model = Media
    fields = '__all__'

class MediaDelete(LoginRequiredMixin, DeleteView):
    model = Media
    success_url = '/media/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
  

