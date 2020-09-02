from django.shortcuts import render
from .models import workTable
from rest_framework import viewsets
from .serializers import WorkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

class WorkViewSet(viewsets.ModelViewSet):
    queryset = workTable.objects.all()
    serializer_class = WorkSerializer

    def post(self, request):
        data = request.data
        serializer_class.create(data)





class getWorkTime(APIView):
    def get(self, request):
        q = workTable.objects.all()
        q_serializer = WorkSerializer(q,many=True,context = {'request': request})
        return Response(q_serializer.data)

class searchById(generics.ListAPIView):
    serializer_class = WorkSerializer
    def get_queryset(self):      
        id = self.kwargs['workId']
        print(id)
        return  workTable.objects.filter(workId=id)