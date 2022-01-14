from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Item, Category


class CategoryListView(generic.ListView):
    model = Category
    template_name = "ecommerce/categories.html"

class ItemsByCategoryView(generic.ListView):
    ordering = 'id'
    paginate_by = 10
    template_name = 'ecommerce/items.html'

    def get_queryset(self):
        # https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/#dynamic-filtering
        # the following category will also be added to the context data
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Item.objects.filter(category=self.category)
         # need to set ordering to get consistent pagination results
        queryset = queryset.order_by(self.ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

def landingPage(request):
    return render(request, 'ecommerce/landingPage.html')

def categories(request):
    return render(request, 'ecommerce/categories.html')

def recommended(request):
    return render(request, 'ecommerce/recommended.html')

def about(request):
    return render(request, 'ecommerce/about.html')

