from django.urls import path
from .views import BoardsAPIView, CardsAPIView

urlpatterns = [
    path('boards/',               BoardsAPIView.as_view(), name='boards-list'),
    path('boards/<int:board_id>/cards/', CardsAPIView.as_view(),  name='cards-list'),
]