def get_token(request):
    import requests
    from urllib.parse import urlparse
    from config.settings.base import env
    parsed_url = urlparse(env("KOBOTOOLBOX_KF_API_URL"))
    api_url = f'{parsed_url.scheme}://{parsed_url.netloc}/'
    token = requests.get(f"{api_url}/token/?format=json", cookies=request.COOKIES).json()['token']

    return token
