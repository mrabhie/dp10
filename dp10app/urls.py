from django.urls import path
from dp10app import views

app_name="dp10app"


urlpatterns=[
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]