##we cretaed this to keep the url of each app

from django.urls import path
from .views import test_view,homepage_view

urlpatterns = [
    
    path("about/",test_view ),
    path("",homepage_view ),
    ###homepage_view is a function
]