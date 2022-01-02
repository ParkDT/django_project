from django.shortcuts import render,redirct


def index (request):
    return render(request , "base.html", {"base":"beomsoo"}) 

def redirct(requst):
    return redirct("index")