from django.urls import path
from app.views import Home,SignupView,DashboardView,LoginView,LogoutView,BlogaddView,UpdateblogView,DeleteblogView
from django.contrib.auth import views as _views
urlpatterns=[
    path("",Home.as_view(),name="home"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("dashboard/",DashboardView.as_view(),name="dashboard"),
    path('login/',LoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("blogadd/",BlogaddView.as_view(),name="blogadd"),
    path("updateblog/<int:id>/",UpdateblogView.as_view(),name="updateblog"),
    path("deleteblog/<int:id>/",DeleteblogView.as_view(),name="deleteblog"),
]