""" This is a module for Baidu API users"""
import requests
from aip import AipSpeech
audio_name = 0


def voice(content='hi', app_id='', api_key='', secret_key=''):
    """
    This function uses a Api online to let computer to speak, the data in the test function may be unable to use. url of the API: https://ai.baidu.com/tech/speech/tts_online
    :param content: The content that you want computer to say
    :param app_id: The app id you owned at the https://apis.baidu.com
    :param api_key: The api key you owned at the https://apis.baidu.com
    :param secret_key: The secret key you owned at the https://apis.baidu.com
    :return: None
    """
    global audio_name
    client = AipSpeech(app_id, api_key, secret_key)
    print(client)
    result = client.synthesis(content, 'zh', 1, {'vol': 15, 'per': 1, 'spd': 4})
    mp3name = "voices/audio" + str(audio_name % 2) + '.mp3'
    print(mp3name)
    if not isinstance(result, dict):
        with open(mp3name, 'wb') as fw:
            fw.write(result)
    audio_name += 1


def get_token(url='None', apiKey=None, secretKey=None, ):
    """
    A common function for Baidu API users to create a token
    :param url: A url for the API
    :param apiKey: The api key you owned at the https://apis.baidu.com
    :param secretKey: The secret key you owned at the https://apis.baidu.com
    :return:
    """
    getTokenUrl = url + apiKey + '&client_secret=' + secretKey
    response = requests.get(getTokenUrl)
    data = response.json()
    token = data.get('access_token')
    return token

