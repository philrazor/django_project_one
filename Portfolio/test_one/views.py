from django.shortcuts import render

def home(request):
    # Add any context variables here if needed
    return render(request, 'core/home.html')
