
from django.urls import path
from api.views import TestView, UserApiView, UserListCreateAPIView, UserRetrieveUpdateDestrotAPIView, UserViewSets

user_list = UserViewSets.as_view({
    'get': 'list'
})

user_detail = UserViewSets.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('', TestView, name='test'),
    path('api_view_users/', UserApiView.as_view(), name="API_view"),
    path('generic_users/', UserListCreateAPIView.as_view(), name="generic_view"),
    path('generic_users/<int:pk>/', UserRetrieveUpdateDestrotAPIView.as_view(),
         name="generic_view_retrieve"),
    path('viewsets_users/', user_list, name="viewsets_users"),
    path('viewsets_users/<int:pk>/', user_detail, name="viewsets_users_detail"),
]
