from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from app.models import Blog,Comment
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

