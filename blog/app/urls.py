from django.urls import path
from app.views import Home,SignupView
urlpatterns=[
    path("",Home.as_view(),name="home"),
    path("signup/",SignupView.as_view(),name="signup"),
]