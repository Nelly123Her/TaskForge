from django.urls import path
from .views import login_view, logout_view, csrf_token

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('csrf/', csrf_token, name='csrf'),
]
