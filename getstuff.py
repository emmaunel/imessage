# !/usr/bin/python3

"""
Thanks to https://github.com/ginglis13/ for the idea
Gonna customize it later
"""

import requests
import os
import random
from io import open

headers = {'user-agent': 'reddit-{}'.format(os.environ.get('USER', 'cse-20289-sp19'))}

REDDIT_URL = 'https://reddit.com/r/{}/.json'


def handle_url():
    url = REDDIT_URL.format('classiccars')
    results = requests.get(url, headers=headers).json()
    whatiwant = results['data']['children']
    images = []
    for post in whatiwant:
        title = post['data']['title']
        img = post['data']['url']
        source = post['data']['domain']
        images.append((title, img, source))

    return download(images)


def download(images):
    title, img, source = random.choice(images)
    # print(source)

    if source == 'i.imgur.com':
        img = source.replace('.gifv', '.mp4')
        return title, img
    else:
        return title, img


# def dl_content(url, source, title):
#     if source == 'gfycat.com':
#         gfy_url = url.split('/')[-1]
#
#         r = requests.get(GFYCAT.format(gfy_url)).json()
#         gfy_mp4url = r['gfyItem']['mp4Url']
#
#         return gfy_mp4url, title
#
#     elif source == 'i.imgur.com':
#         img_url = url.replace('.gifv', '.mp4')
#         return img_url, title
#
#     else:
#         return url, title

def save2Device(title, img):
    # unknown file type
    if 'v.redd.it' in img:
        print('Error with file type, try again')
        exit(0)

    # if it is a post
    if '.cat' in img:
        print('It is a post')
        exit(0)

    extension = '.jpg'
    for ext in ('mp4', 'png', 'gif', 'jpeg', 'jpg'):
        if ext in img:
            extension = '.' + ext

    # remove previous saved file ???
    # I could do this but It looks like it gets override anyways

    file = 'cat' + extension
    res = requests.get(img)

    # Print title for text msg
    print('Title: {}'.format(title))

    with open(file, 'wb') as file:
        file.write(res.content)


title, img = handle_url()
save2Device(title, img)
