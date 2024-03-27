from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text = "Our Site Homepage<br>I will improve this site"
    # return HttpResponse(text)
    context = {'text': text}
    return render(request, 'index.html', context)
