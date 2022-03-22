import json
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def getToken(request):
    details = request.data
    post_data = {
        'client_id': details['client_id'],
        'client_secret': details['client_secret'],
        'grant_type': details['grant_type'],
        'resource':details['resource']
    }
    response = requests.post('https://accounts.accesscontrol.windows.net/'+details['tenant_id']+'/tokens/OAuth/2/', data=details)
    content = response.content

    return Response(json.loads(content.decode('utf-8')), status=response.status_code)
    