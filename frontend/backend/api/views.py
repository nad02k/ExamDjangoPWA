from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class RegisterServiceWorker(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        sw_token = request.data.get('token')
        return Response({"status": "Service Worker Registered"})

class GetAssets(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Return list of assets to cache
        return Response([
            {"url": "/static/main.css", "hash": "abc123"},
            {"url": "/static/app.js", "hash": "def456"}
        ])