from django.shortcuts import render

def loginview(request):
    return render(request=request, template_name="login.html", context={})



