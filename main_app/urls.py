from django.urls import path
from . import views 


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('media/', views.media_index, name='media-index'),
    path('media/<int:media_id>/', views.media_detail, name='media-detail'),
    path('media/<int:pk>/update/', views.MediaUpdate.as_view(), name='media-update'),
    path('media/<int:pk>/delete/', views.MediaDelete.as_view(), name='media-delete'),
    path('media/create/', views.MediaCreate.as_view(), name='media-create'),
    path('media/<int:media_id>/review/', views.add_review, name='add-review'),

]