import requests
import os
import env

fb_client_id = os.getenv('fb_client_id')
# print(fb_client_id)
fb_client_secret = os.getenv('fb_client_secret')
# print(fb_client_secret)
fb_access_token = os.getenv('fb_access_token')
# print(fb_access_token)
fb_access_url = os.getenv('fb_access_url')
# print (fb_access_url)

graph_url = 'https://graph.facebook.com/v19.0/'
def get_comment(ig_media_id = '' , fb_access_token = ''):
    url = graph_url + ig_media_id + '/comments'
    param = dict()
    param['access_token'] = fb_access_token
    response = requests.get(url,param)
    response = response.json()
    return response