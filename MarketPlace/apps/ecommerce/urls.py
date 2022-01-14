
from django.urls.conf import path
#from mptt.views import ItemsByCategoryView, CategoryListView

from . import views

urlpatterns = [
    path('home', views.landingPage, name='landingPage'),
    path('categories', views.categories, name='categories'),
    path('recommended', views.recommended, name='recommended'),
    path('about', views.about, name='about'),
    path('categories/', views.CategoryListView.as_view() , name='category-list'),
    path('<str:slug>/', views.ItemsByCategoryView.as_view() , name='category-detail'),

]
