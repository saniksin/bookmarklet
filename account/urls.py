from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # предыдущий url входа
    # path('login/', views.user_login, name='login'),

    # # url-адреса для входа и выхода
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # # url-адреса для смены пароля
    # path('password-change/', 
    #      auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password-change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),

    # # url-адрес для сброса пароля
    # path('password-reset/', 
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('password-reset/complete',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),

    #Заменяет все что вышел было
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
]
