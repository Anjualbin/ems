from django.urls import path
from employee import views

urlpatterns=[
    path("userhome",views.User_home.as_view(),name="userhome"),
    path("signin",views.Login.as_view(),name="signin"),
    path("signout",views.Signout.as_view(),name="signout"),
]