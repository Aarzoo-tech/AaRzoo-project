from django.urls.conf import path
from contest.views import *
urlpatterns=[
    path('home-page',home),
    path('registration',newuser),
    path('save-user',saveuser),
    path('login',user_login),
    path('logout',user_logout),
    path('get-contest',contest),
    path('contest-result',contest_result),
]