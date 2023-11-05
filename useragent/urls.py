from django.urls import path
from useragent import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('user-agent/', views.user_agent, name='user_agent'),
    path('user-agent/info/', views.user_agent_info, name='user_agent_info'),
]