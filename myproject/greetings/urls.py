from django.urls import path
from . import views  # Import views from the greetings app

urlpatterns = [
    path('', views.welcome, name='welcome'),  # This maps the root URL to the welcome view
    path('greet/<str:username>/', views.greetUser, name='greet_user'),
    path('farewell/<str:username>/', views.farewellUser, name='farewell_user'),
]
