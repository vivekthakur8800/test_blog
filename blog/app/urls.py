from django.urls import path
from app.views import Home,SignupView,DashboardView,LoginView,LogoutView,BlogaddView,UpdateblogView,DeleteblogView,SearchView
from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns=[
    path("",Home.as_view(),name="home"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("dashboard/",DashboardView.as_view(),name="dashboard"),
    path('login/',LoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("blogadd/",BlogaddView.as_view(),name="blogadd"),
    path("updateblog/<int:id>/",UpdateblogView.as_view(),name="updateblog"),
    path("deleteblog/<int:id>/",DeleteblogView.as_view(),name="deleteblog"),
    path("search/",SearchView.as_view(),name="search"),
    path("passwordchange/",PasswordChangeView.as_view(template_name="app/changepassword.html",success_url="/dashboard/"),name="passwordchange"),
    path("passwordreset/",PasswordResetView.as_view(template_name="app/passwordreset.html"),name="passwordreset"),
    path("password_reset/done/",PasswordResetDoneView.as_view(template_name="app/passwordresetdone.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name="app/passwordresetconfirm.html"),name="password_reset_confirm"),
    path("reset/done/",PasswordResetCompleteView.as_view(template_name="app/passwordresetcomplete.html"),name="password_reset_complete"),
]