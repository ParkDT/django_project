from django.shortcuts import render,redirect


def index (request):
    return render(request , "base.html", {"base":"beomsoo"}) 

def redirect(requst):
    return redirect("index")  