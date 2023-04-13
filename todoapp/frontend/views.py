from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/frontend-react/public/index.html')

