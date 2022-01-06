
from django.urls.conf import path

from . import views

urlpatterns = [
    path('home', views.landingPage, name='landingPage'),
    path('categories', views.categories, name='categories'),
    path('recommended', views.recommended, name='recommended'),
    path('about', views.about, name='about'),
]
