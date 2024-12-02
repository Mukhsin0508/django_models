from django.http import HttpResponse
from omni_authify.frameworks.django import OmniAuthifyDjango

def facebook_login(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    return auth.login(request)

def facebook_callback(request):
    auth = OmniAuthifyDjango(provider_name='facebook')
    user_info = auth.callback(request)
    print(user_info)

    return HttpResponse(user_info)
