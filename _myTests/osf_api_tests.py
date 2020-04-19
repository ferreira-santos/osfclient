# -*- coding: utf-8 -*-
"""
Created on Thu May 18 19:11:47 2017

@author: F. Ferreira-Santos
"""

# Helpful sites: 
    
# JSON formatter  --  https://jsonformatter.curiousconcept.com/
# OSF API v2  --  https://osf.io/y9jdt/wiki/home/
# OSF API v2 documentation -- https://developer.osf.io/
# OSF project I made for testing: https://osf.io/rqu7n/wiki/home/

# OAuth documentation/tutorial -- https://www.oauth.com/oauth2-servers/oauth2-clients/mobile-and-native-apps/
# OSF OAuth Python code -- https://github.com/abought/osf_oauth2_demo

# FOR VISUAL STUDIO and C#
# https://www.visualstudio.com/en-us/docs/integrate/get-started/auth/oauth
# http://deanhume.com/home/blogpost/a-simple-guide-to-using-oauth-with-c-/49


import requests
import json

#from the URL of your OSF profile
user_id = 'ctukj'

#from https://osf.io/settings/tokens/ --> manually generated token
personal_access_token = '1XJ9DpqlqVIoFuD8FuTJ71wpZymdLLTvzGb6VGKNqAviZ5Yv5oVV4GBVyOrXHxQdJemr8n'


response = requests.get(
        url = "https://api.osf.io/v2/?format=api",
        headers={
                #"Authorization": "Bearer " + personal_access_token,
                "Content-Type": "application/vnd.api+json",
            },
        )


response = requests.get(
        url = "https://accounts.osf.io/?format=api",
        headers={
                #"Authorization": "Bearer " + personal_access_token,
                "Content-Type": "application/vnd.api+json",
            },
        )


def send_request_user():
    # Request (1)
    # GET https://api.osf.io/v2/nodes/d92en/files/

    try:
        response = requests.get(
            url="https://api.osf.io/v2/users/" + user_id + "/",
            headers={
                "Authorization": "Bearer " + personal_access_token,
                "Content-Type": "application/vnd.api+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')




#API Test project --- rqu7n
project_id = "rqu7n"

def send_request_nodes(project_id):
    # Request (2)
    # GET https://api.osf.io/v2/nodes/d92en/files/

    try:
        response = requests.get(
            url="https://api.osf.io/v2/users/" + user_id + "/nodes/?filter[id]=" + project_id,
            headers={
                "Authorization": "Bearer " + personal_access_token,
                "Content-Type": "application/vnd.api+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        # PRINTS the node information for the project_id
        
        response_json = json.loads(response.content)
        # response_json['data'][0]['id']
        # response_json['data'][0]['attributes']['tags']
        
        # GET wiki info
        response_wikis = requests.get(
            url=response_json['data'][0]['relationships']['wikis']['links']['related']['href'],
            headers={
                "Authorization": "Bearer " + personal_access_token,
                "Content-Type": "application/vnd.api+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response_wikis.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response_wikis.content))
        # PRINTS the wiki information for the project_id
        
        response_wikis_json = json.loads(response_wikis.content)
        # response_wikis_json['data'][0]['links']['download']
        
        response_wikis_download = requests.get(
            url=response_wikis_json['data'][0]['links']['download'],
            headers={
                "Authorization": "Bearer " + personal_access_token,
                "Content-Type": "application/vnd.api+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response_wikis_download.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response_wikis_download.content))     
        # PRINTS the wiki CONTENTS for the project_id
        
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
