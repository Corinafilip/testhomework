from django.http import HttpResponse


def greetings(request):
    name = "Corina"
    return HttpResponse(f"<h1> Hello, {name}  </h1>")
