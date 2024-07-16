from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, CustomLoginView

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomLoginView.as_view(), name='custom_login'),
]
