from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user-create'),
    path('login/', LoginView.as_view(), name='login-user-create'),
]