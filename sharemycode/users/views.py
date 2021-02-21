from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
import json

from django.contrib.auth.models import User
def main(request):
    to_json = {
        'is_authenticated': request.user.is_authenticated,
        'is_staff':request.user.is_staff,
        'is_superuser':request.user.is_superuser
    }
    return HttpResponse(json.dumps(to_json))

