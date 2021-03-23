from django.shortcuts import render, get_object_or_404
from api.serializers import UserSerializer
from api.models import User
# resframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

# Create your views here.


@api_view(['GET', 'POST'])
def TestView(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            'success': True,
            'message': 'Get request success!',
            'data': serializer.data
        })
    if request.method == 'POST':
        return Response({
            'success': True,
            'message': 'Post request success!',
        })

    return Response({
        'success': False,
        'message': 'Invalid request'

    })


# APIview
class UserApiView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            'success': True,
            'message': 'Get request success!',
            'data': serializer.data
        })

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Post request success!',
                'data': serializer.data
            })

    def put(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            users = User.objects.get(pk=request.data.get('id'))
            if users:
                serializer = UserSerializer(users, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'APIview updated users post',
                        'data': serializer.data
                    })
        return Response({
            'success': False,
            'message': 'APIview put request fulfilled',
        })

    def delete(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            users = User.objects.get(pk=request.data.get('id'))
            if users:
                users.delete()
                return Response({
                    'success': True,
                    'messgae': 'delete user success!'
                })
        return Response({
            'success': False,
            'message': 'delete request fulfilled'
        })


# Generic view
class UserListCreateAPIView(generics.ListCreateAPIView):
    # GET,POST
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestrotAPIView(generics.RetrieveUpdateDestroyAPIView):
    # GET:PK ,PUT,PATCH,DELETE
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSet
class UserViewSets(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    #GET : PK
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        if pk is not None:
            users = get_object_or_404(queryset, pk=pk)
            serializer = UserSerializer(users)
            return Response(serializer.data)
