from django.core.serializers import serialize
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework import status

from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from serializers.task_serializer import TaskCreateSerializer
from models import Task



def greetings(request):
    name = "Corina"
    return HttpResponse(f"<h1> Hello, {name}  </h1>")


@api_view(['POST'])
def create_task(request: Request):
    row_data = request.data
    serializer = TaskCreateSerializer(data=row_data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            data=serializer.data,
            status=201
        )
    else:
        return Response(
            data=serializer.errors,
            status=400
        )