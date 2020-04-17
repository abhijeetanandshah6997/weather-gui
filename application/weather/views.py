import requests
from django.conf import settings
from django.shortcuts import render, redirect


def home(request):
    access_token_header = {
        'api-token': settings.API_TOKEN,
        'Accept': 'application/json',
        'user-email': settings.USER_EMAIL,
    }
    response_access_token = requests.get(settings.GET_ACCESS_TOKEN, headers=access_token_header)
    if response_access_token.status_code == 200:
        access_token = response_access_token.json()["auth_token"]
        api_request_header = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}',
        }
        response_countries = requests.get(settings.COUNTRY_API, headers=api_request_header)
        if response_countries.status_code == 200:
            countries = list()
            for country in response_countries.json():
                countries.append(country["country_name"])
            data = {
                'countries': countries,
                'access_token': access_token,
            }
            return render(request, 'weather/home.html', data)
    return redirect("error")


def error(request):
    return render(request, 'weather/error.html')
