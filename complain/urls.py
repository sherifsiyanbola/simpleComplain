from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('dashboard/',views.complainCreateView.as_view(), name="dashboard"),
    path('dashboard/view/', views.complainListView.as_view(), name="complains"),
    path('dashboard/view/detail/<int:pk>/', views.complainDetailView.as_view(), name="detail"),
    path('dashboard/view/complain/<int:pk>/', views.complainView.as_view(), name="viewcomp"),
    path('dashboard/view/complain/view/<int:pk>/', views.complainDeleteView.as_view(), name="delete"),

]