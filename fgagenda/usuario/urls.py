from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar/', SignupManagerView.as_view(), name='cadastrar'),
    path('login/', LoginView.as_view(), name='login')
]