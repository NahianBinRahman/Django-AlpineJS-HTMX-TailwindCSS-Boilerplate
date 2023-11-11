from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return render(request, 'home.html')


def update_content(request):
    # Logic to update content goes here
    updated_content = "Updated Content"
    return HttpResponse(updated_content)
