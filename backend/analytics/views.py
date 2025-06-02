from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import UsagePattern
from .serializers import UsagePatternSerializer

class GetAnalysisResults(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        results = UsagePattern.objects.all().order_by('-timestamp')[:10]  # Dernières 10 entrées
        serializer = UsagePatternSerializer(results, many=True)
        return Response(serializer.data)