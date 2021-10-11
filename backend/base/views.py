from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .courses import courses


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/courses/",
        "/api/courses/create/",
        "/api/courses/upload/",
        "/api/courses/<id>/reviews/",
        "/api/courses/top/",
        "/api/courses/<id>/",
        "/api/courses/delete/<id>/",
        "/api/courses/<update>/<id>",
    ]
    return Response(routes)


@api_view(["GET"])
def getCourses(request):
    return Response(courses)


@api_view(["GET"])
def getCourse(request, pk):
    course = None
    for i in courses:
        if i["_id"] == pk:
            course = i
            break
    return Response(course)
