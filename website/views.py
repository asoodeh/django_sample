from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse


# def http_test(request):
#     return HttpResponse('<h1> this is a test </h1>')

# def json_test(request):
#     return JsonResponse({'ali':'20'})

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    # return HttpResponse('<h1> this is a test about </h1>')
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def element_view(request):
    return render(request, 'website/elements.html')



