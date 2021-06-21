from django.urls import path
from django.conf.urls import include, url
from newsletter_sub.views import *
from .views import HomeHandler, NewsletterHandler, DashboardHandler
urlpatterns = [
   path('', HomeHandler.as_view()), 
   path('subscribe/', NewsletterHandler.as_view()), 
   path('subscribers/',DashboardHandler.as_view()) 
]
