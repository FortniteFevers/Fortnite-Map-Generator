import os
import PIL
import requests
import tweepy
import time
from PIL import Image
from colorama import *
init()
print("Starting program...")
url = 'https://media.fortniteapi.io/images/map.png'
r = requests.get(url, allow_redirects=True)
open('map.png', 'wb').write(r.content)
print(Fore.GREEN+"Opened map.png")
response = requests.get('https://benbotfn.tk/api/v1/status')
version = response.json()['currentFortniteVersionNumber']
print(Fore.BLUE+"Retrived version number..")
img=Image.open('map.png')
img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
img.save('smallmap.png')
os.remove('map.png')

auth = tweepy.OAuthHandler('API', 'API-SECRET')
auth.set_access_token('ACESS', 'ACESS-SECRET')
api = tweepy.API(auth)

api.update_with_media('smallmap.png', 'Battle Royale map for v'+str(version))
print(Fore.GREEN+"Tweeted image!")
time.sleep(2)
print("Finnished program. Closing in 5 seconds.")
time.sleep(5)
