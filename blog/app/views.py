from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView,View
from app.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from app.models import Blog,Comment
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
class Home(TemplateView):
    template_name="app/home.html"
    blog=Blog.objects.all()

    def get_context(self,request,*args,**kwargs):
        context={}
        context["blog"]=self.blog
        return context

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context(request,*args,**kwargs))

class SignupView(TemplateView):
    template_name="app/signup.html"

    def get_context(self,request,*args,**kwargs):
        fm=UserCreationForm()
        context={}
        context["form"]=fm
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
        context={}
        context["form"]=fm
        return render(request,self.template_name,context)

    def get(self,request,*args,**kwargs):
        fm=UserCreationForm()
        return render(request,self.template_name,{"form":fm})

class DashboardView(TemplateView):
    template_name="app/dashboard.html"
    blog=Blog.objects.all()

    def get_context(self,request,*args,**kwargs):
        context={}
        context["blog"]=self.blog
        return context

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context(self,request,*args,**kwargs))

class LoginView(TemplateView):
    template_name="app/login.html"

    def get(self,request,*args,**kwargs):
        fm=AuthenticationForm()
        context={}
        context["form"]=fm
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data["username"]
            password=fm.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')
        else:
            return render(request,self.template_name,{"form":fm})

class LogoutView(TemplateView):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")