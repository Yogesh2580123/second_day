from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student_app.views import StudentViewSet

router = DefaultRouter()
router.register('post', StudentViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
