from django.shortcuts import render
from django.http import HttpResponse
def feedback(request):
    return render(request, 'feedback.html')
