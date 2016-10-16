from django.conf.urls import url

from . import views

app_name = 'serverSide'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^addobject/music/', views.AddMusicObject, name='AddMusicObject'),
    url(r'^addobject/series/', views.AddSeriesObject, name='AddSeriesObject'),
    url(r'^addobject/movie/', views.AddMovieObject, name='AddMovieObject'),
    url(r'^addobject/audiobook/', views.AddAudiobookObject, name='AddAudiobookObject'),

    url(r'^readobject/music/', views.ReadMusicObject, name='ReadMusicObject'),
    url(r'^readobject/series/', views.ReadSeriesObject, name='ReadSeriesObject'),
    url(r'^readobject/movie/', views.ReadMovieObject, name='ReadMovieObject'),
    url(r'^readobject/audiobook/', views.ReadAudiobookObject, name='ReadAudiobookObject'),

    url(r'^files/', views.Filestructure, name='filestructure'),
]
