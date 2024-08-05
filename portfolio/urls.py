from django.urls import path
from .views import HomePageView, ProjectListView, ProjectDetailView, AboutPageView, ContactFormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]