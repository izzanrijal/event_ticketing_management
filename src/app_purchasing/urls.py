from django.urls import path
from . import views

urlpatterns = [
path("event/", views.page_event),
path('checkout/', views.page_checkout),
]