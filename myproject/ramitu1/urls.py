from django.urls import path
from . import views

urlpatterns = [
    path('dimitri/', views.dimitri),
    path('jumpscare/', views.jumpscare ),
]