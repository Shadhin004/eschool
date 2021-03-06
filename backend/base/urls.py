from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("courses/", views.getCourses, name="courses"),
    path("courses/<str:pk>/", views.getCourse, name="course"),
]
