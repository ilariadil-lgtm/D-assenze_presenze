from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsParticipant
from .serializers import (
    ParticipantProfileSerializer,
    UserSerializer,
    RegisterSerializer,
)
from .models import CustomUser


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ParticipantProfileView(APIView):
    """
    Profilo partecipante
    GET  → visualizza profilo
    PUT/PATCH → aggiorna profilo
    """
    permission_classes = [IsAuthenticated, IsParticipant]

    def get(self, request):
        serializer = ParticipantProfileSerializer(request.user)
        return Response({"success": True, "data": serializer.data})

    def patch(self, request):
        serializer = ParticipantProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success": True,
            "message": "Profilo aggiornato con successo.",
            "data": serializer.data
        })

    
    def put(self, request):
        return self.patch(request)


class CurrentUserView(APIView):
    """Utente corrente"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({"success": True, "data": serializer.data})
