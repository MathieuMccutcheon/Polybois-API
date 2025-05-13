from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_boards, get_cards
from .serializers import BoardSerializer, CardSerializer


class BoardsAPIView(APIView):
    def get(self, request):
        boards = get_boards()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    
    
class CardsAPIView(APIView):
    """
    GET /api/boards/{board_id}/cards/ → liste des cartes
    """
    def get(self, request, board_id):
        cards = get_cards(board_id)            # déjà une liste de dicts
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
