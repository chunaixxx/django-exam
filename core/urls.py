from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from api.views import CategoryViewSet, NotDoneTodoViewSet, TodoViewSet
from user.views import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('category', CategoryViewSet, basename='categories')
router.register('todo', TodoViewSet, basename='todos')
router.register('not-done-todos', NotDoneTodoViewSet, basename='not-done-todos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
