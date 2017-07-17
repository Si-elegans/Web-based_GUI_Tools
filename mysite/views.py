from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from django, try out <a href='/admin/'>/admin/</a>\n")