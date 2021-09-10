# call with -u in terminal

# hide pygame start prompt
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''

from pycoingecko import CoinGeckoAPI
import time
import requests
from pygame import mixer
from pathlib import Path


cg = CoinGeckoAPI()

# load sound for alarm
path = Path(__file__).parent / 'alarm.wav'  # get sound path
mixer.init()
mixer.music.load(str(path))  # .wav alarm file location
mixer.music.set_volume(0.5)

# get list of all coins info
while True:
    try:
        base_coins_list = cg.get_coins_list()
        break
    except requests.HTTPError:
        print('API overloaded, retrying in 60 sec...')
        time.sleep(60)

print('\ntip: Hold CTRL and click a url to open in the browser')
print('\nProgram initialized at ' + time.strftime('%H:%M'))

time.sleep(31)

# main program loop, check if a new coin released
while True:
    try:
        # check if new coins released
        current_coins_list = cg.get_coins_list()

        if current_coins_list != base_coins_list:
            mixer.music.play()
            print('\n\nNew coin(s) released at ' + time.strftime('%H:%M') + '! -----------------------------------------')

            # separate new coins to another list
            new_coins_list = [x for x in current_coins_list if x not in base_coins_list]

            # print new coin(s) name(s)
            for coin in new_coins_list:
                print('Name: %s' % coin.get('name'))
                # you can change url to 'https://www.coingecko.com/en/coins/%s\n' to go to the site in english
                print('url: https://www.coingecko.com/pt/moedas/%s\n' % coin.get('id'))

            base_coins_list = current_coins_list
    except requests.HTTPError:
        pass

    time.sleep(31)
