from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', views.PostCreateView.as_view()),
    path('<int:id>/', views.PostDetailView.as_view()),
]

urlpatterns += router.urls
