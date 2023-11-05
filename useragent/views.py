from django.shortcuts import render
from django_user_agents.utils import get_user_agent

def welcome(request):
    return render(request, 'useragent/welcome.html')

def user_agent(request):
    user_agent = get_user_agent(request)
    return render(request, 'useragent/user_agent.html', {'user_agent': user_agent})

def user_agent_info(request):
    user_agent = get_user_agent(request)
    if user_agent.is_pc:
        dispositivo = "PC"
    elif user_agent.is_mobile:
        dispositivo = "Móvil"
    elif user_agent.is_tablet:
        dispositivo = "Tablet"
    elif user_agent.is_bot:
        dispositivo = "Bot"
    else:
        dispositivo = "Dispositivo no reconocido"

    tactil = user_agent.is_touch_capable
    host = request.get_host()
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'useragent/user_agent_info.html',
                   {'dispositivo': dispositivo, 'tactil': tactil,
                     'host': host, 'ip': ip})
    