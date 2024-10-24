from django.http import JsonResponse
from firebase_admin import auth

def register_user(request):
    if request.method == 'POST':
        data = request.POST
        try:
            user = auth.create_user(
                email=data['email'],
                password=data['password']
            )
            return JsonResponse({'message': 'User created sucessfully', 'uid': user.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)