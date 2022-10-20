from django.urls import path, include

from app.views import todoapi



urlpatterns = [
    path('api/',todoapi.as_view()), 

]