from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from user.form import LoginForm


def index (request):
    return render(request , "base.html", {"base":"beomsoo"}) 

def redirect(requst):
    return redirect("index")  

def Login(request):
    if request.method == "GET":
        loginForm = LoginForm()   
        return render(request,'login.html',{"fields":loginForm})
    else:
        form = LoginForm(request.POST, request.FILES)
        msg = "올바르지 않은 데이터"
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            password = form.cleaned_data.get("password")
            user = authenticate(user_id=user_id,password=password)
            if user is not None:
                msg="로그인 성공"

        return render(request,'login.html',{"fields":form,"msg":msg})