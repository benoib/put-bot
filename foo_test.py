import json
import itertools
import pynder
import logging
from PIL import Image
import requests
import numpy as np
from StringIO import StringIO
import os


logging.basicConfig(filename='log/process.log', level=logging.DEBUG)
user = 'lbj'

with open('conf_{}.json'.format(user), 'r') as f:
    conf = json.load(f)

path_image = "http://images.gotinder.com/554a331205f4e30d5b5aecff/a976ad9e-4c8c-45a4-b98f-7d2df87b775a.jpg"


def save_image(url=None, save_path=None):
    """Retreives image from url,can save 
    to path (=Name of file).
    Soon: save Image by person."""

    response = requests.get(url)
    #img = np.array(Image.open(StringIO(response.content)))
    if save_path:
        url = save_path
    with open(url, 'w') as f:
        f.write(response.content)
    # return img


def save_user_pictures(user=None):
    """Will save pictures of user if has some"""
    photos_url = user.get_photos()
    base_save_path = user.name
    if len(photos_url) > 0:
        if not os.path.exists(base_save_path):
            os.mkdirs(base_save_path)
        for nb_pict, url in enumerate(photos_url):
            save_path = base_save_path + '/' + nb_pict + '.jpg.'
            save_image(url=url, save_path=save_path)
            print("Saving {} image".format(nb_pict))


FBTOKEN = conf['FACEBOOK_AUTH_TOKEN']
#FBTOKEN = conf['FB_TOKEN']
# FBTOKEN = "EAAGm0PX4ZCpsBADYBHlDExnDK0RoAak9VEzf29MqrmlveXWGhxMrnkeHdIV4ne7JP1NV66vlaXcrbukSAwuqZCvyAdOZB0dEV95sy9IjXTQno2uLd9ZAnXojZBTaBFZCaH7YGgF4FUhFY063Gmprs27k9kqZC0z2jlFZCMT0fXTjM1BLD7o88DSe"

# #FBTOKEN = "YOUR_FB_TOKEN"
FBID = conf['PROFILE_ID']
#FBID = 566627354
# FBID = "dddd55"
#FBTOKEN = "EAAGm0PX4ZCpsBAA9fAZAOZBOZA16Pg7nphCRbovMTZCxZAZCtDzC1Mv9Fy2wgoGRkraFbO52oCh20zwxTDuWvssNPhcEt2jPReIiY65u18ZA5xYjNc2wn6GZC7Fab2esiI9TxPM2c55lcBsgmiNAomiUwxaLTgK56q2gT7TdGi32XnuYcH1NpYpY6ZA3zv1fK36GYZD"
session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)
users = session.nearby_users()


# response = requests.get(path_image)
# img = np.array(Image.open(StringIO(response.content)))
# for user in itertools.islice(users, 5):
#     print user.name


# def handle_matches():
#     log(str(len(session._api.matches())) + ' matches')
#     matches = session._api.matches()
#     for m in matches:
#         message(m)w


# def message(match):
#     ms = match['messages']
#     khaled = session.profile.id
#     if not ms:
#         send(match, 0)
#         return
#     said = False
#     count = 0
#     name = match['person']['name']
#     for m in ms:
#         if m['from'] == khaled:
#             count += 1
#             said = False
#         elif 'dj khaled' in m['message'].lower():
#             said = True
#     if count >= len(messages):
#         log('Finished conversation with ' + name)
#         return
#     if said:
#         send(match, count)
#     else:
#         log('No new messages from ' + name)
