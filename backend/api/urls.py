from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentsViewSets)
router.register(r'todos', views.TodoViewset, 'todos')

# router.register(r'users', views.UserViewSets, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
