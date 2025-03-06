from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Media, Review, Profile
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import search_film
from .forms import ReviewForm



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def media_index(request):
    media = Media.objects.all()
    return render(request, 'media/index.html', {'media': media})

@login_required
def media_detail(request, media_id):
    media = Media.objects.get(id=media_id)
    profile = Profile.objects.get(user = request.user.id)
    review_form = ReviewForm()
    return render(request, 'media/detail.html', {
        'media': media, 'review_form': review_form, 'profile': profile,
        })

class MediaCreate(LoginRequiredMixin, CreateView):
    model = Media
    fields = ['title', 'year', 'imdbID']

    def form_valid(self, form):
        
        title = form.cleaned_data.get('title')
        year = form.cleaned_data.get('year')
        imdb_id = form.cleaned_data.get('imdbID')

        
        api_response = search_film(title=title, imdb_id=imdb_id, year=year)

        if 'error' in api_response:
            form.add_error(None, api_response['error'])  
            return self.form_invalid(form)

        
        data = api_response
        form.instance.title = data.get('Title', title)
        form.instance.year = data.get('Year', year)
        form.instance.imdbID = data.get('imdbID', imdb_id)
        form.instance.genre = data.get('Genre', '')
        form.instance.director = data.get('Director', '')
        form.instance.plot = data.get('Plot', '')
        form.instance.poster = data.get('Poster', '')
        form.instance.location = 'Some location' 
        form.instance.type = data.get('Type')  
        form.instance.is_viewed = False  
        form.instance.rating = None 
        form.instance.user = self.request.user  

        if Media.objects.filter(imdbID = form.instance.imdbID).exists():
            form.add_error(None, 'This already exists!')
            return self.form_invalid(form)

        return super().form_valid(form)

    

class MediaUpdate(LoginRequiredMixin, UpdateView):
    model = Media
    fields = ['location', 'is_viewed', 'rating']

class MediaDelete(LoginRequiredMixin, DeleteView):
    model = Media
    success_url = '/media/'

@login_required
def add_review(request, media_id):
    media = Media.objects.get(id=media_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.media = media
            review.save()
            return redirect('media-detail', media_id=media.id)
    else:
        form = ReviewForm()
    return render(request, 'media/review_form.html', {'form': form, 'media': media})

@login_required
def toggle_watchlist(request, media_id):
    media = Media.objects.get(id=media_id)
    profile = Profile.objects.get(user=request.user.id)
    if media_id in profile.watchlist.all():
        profile.watchlist.remove(media)
    else:
        profile.watchlist.add(media)
    return redirect('media-detail', media_id=media.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
  

