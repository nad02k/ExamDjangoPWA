from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from subscriptions.models import PushSubscription

import json
from django.http import JsonResponse

@csrf_exempt
def save_subscription(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            endpoint = data['endpoint']
            keys = data.get('keys', {})

            PushSubscription.objects.update_or_create(
                endpoint=endpoint,
                defaults={'keys': keys}  # si keys est JSONField, ça marche directement
            )

            return JsonResponse({'status': 'success'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    else:
        return JsonResponse({
            'error': 'Invalid request method',
            'allowed_methods': ['POST']
        }, status=405)

def get_vapid_public_key(request):
    return JsonResponse({
        "publicKey": "BExSQxk0YU_KlG_a79QgFRMMwzILI1YohJYXtO8U03hPiREY6EbET6Y_XAH9nQm0ZdC9GUt_LwIeyNExsNE8yvE" #base64url format pas pem
    })


