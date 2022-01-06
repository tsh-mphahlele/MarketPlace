from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request, 'ecommerce/landingPage.html')

def categories(request):
    return render(request, 'ecommerce/categories.html')

def recommended(request):
    return render(request, 'ecommerce/recommended.html')

def about(request):
    return render(request, 'ecommerce/about.html')

