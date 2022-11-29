from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView,View
from app.forms import UserCreationForm,Blogform
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

class BlogaddView(TemplateView):
    template_name="app/addblog.html"

    def get(self,request,*args,**kwargs):
        fm=Blogform()
        context={}
        context["form"]=fm
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        fm=Blogform(request.POST)
        if fm.is_valid():
            user=request.user
            title=fm.cleaned_data["title"]
            discription=fm.cleaned_data["discription"]
            blog=Blog(user=user,title=title,discription=discription)
            blog.save()
            return HttpResponseRedirect("/dashboard/")
        else:
            return render(request,self.template_name,{"form":fm})

class UpdateblogView(TemplateView):
    template_name="app/updateblog.html"

    def get(self,request,*args,**kwargs):
        pi=Blog.objects.get(id=kwargs["id"])
        fm=Blogform(instance=pi)
        context={}
        context["form"]=fm
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        pi=Blog.objects.get(id=kwargs["id"])
        fm=Blogform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/dashboard/")
        else:
            return render(request,self.template,{"form":fm})

class DeleteblogView(TemplateView):
    def post(self,request,*args,**kwargs):
        print("kwargs",kwargs["id"])
        pi=Blog.objects.get(id=kwargs["id"])
        pi.delete()
        return HttpResponseRedirect("/dashboard/")