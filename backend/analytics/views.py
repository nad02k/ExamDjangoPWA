from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import UsagePattern

class GetAnalysisResults(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        results = UsagePattern.objects.all().order_by('-timestamp')[:10]  # Les 10 derniers
        data = [
            {
                "cluster": r.cluster_id,
                "description": r.description,
                "timestamp": r.timestamp
            } for r in results
        ]
        return Response(data)