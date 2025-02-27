from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Handles user login and starts a session"""
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"message": "Login successful"})
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
def logout_view(request):
    """Handles user logout and destroys the session"""
    logout(request)
    return JsonResponse({"message": "Logged out successfully"})

@api_view(['GET'])
def csrf_token(request):
    """Returns CSRF token for frontend authentication"""
    return JsonResponse({"csrfToken": get_token(request)})