from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostCreateView.as_view()),
    path('<int:id>/', views.PostDetailView.as_view()),

]
