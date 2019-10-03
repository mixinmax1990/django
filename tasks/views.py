from django.shortcuts import rendergit pull

def hello(request, name):
    return render(request, "hello.html", {"name":name})
    
    # return HttpResponse("<b>Hello " + name +"</b>")