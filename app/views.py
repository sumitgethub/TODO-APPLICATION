from django.shortcuts import render
from rest_framework.views import APIView
from app.models import Todo
from app.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
# Create your views here.

class todoapi(APIView):
        permission_classes = [IsAuthenticated]
        def get(self, request):
            user = request.user

            try:
                snippit = Todo.objects.filter(user=user)
            except snippit.DoesNotExist:
                return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
            

            serializer = TodoSerializer(snippit, many=True)

            return Response(serializer.data)

        def post(self, request):
            data = request.data
            user = request.user
            title = data.get('title')
            body = data.get('body')

            payload = {
                "user": user.id,
                "title": title,
                "body": body

            }

            serializer = TodoSerializer(data=payload)

            if not serializer.is_valid():
                return Response(serializer.errors)
        
            serializer.save()
            return Response(serializer.data)
        
        def patch(self, request):
            data = request.data
            try:
                sneppit = Todo.objects.get(id=data.get('todo'))
            except Exception:
                return Response({'error': 'todo not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = TodoSerializer(sneppit, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors)
            serializer.save()
            return Response(serializer.data)

        def delete(self, request):
            """
                delete single shipping address
            """
            data = request.data

            sneppit = Todo.objects.get(id=data.get('todo'))
            sneppit.delete()

            return Response({'msg': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
