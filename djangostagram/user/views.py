from django.shortcuts import render,redirect


def index (request):
    return render(request , "base.html", {"base":"beomsoo"}) 

def redirct(requst):
    return redirect("index")