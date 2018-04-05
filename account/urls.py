from django.urls import path, re_path, include
from .views import LoginAPI, RegisterAPI, ChangePasswordAPI, LoginView, RegisterView, ChangePasswordView, logout_view, IndexView



urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login_api'),
    path('api/register', RegisterAPI.as_view(), name='register_api'),
    path('api/change_password', ChangePasswordAPI.as_view(), name='change_password_api'),

    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('change_password', ChangePasswordView.as_view(), name='change_password'),
    path('logout', logout_view, name='logout'),

    re_path(r'^api-auth/', include('rest_framework.urls'))
]
