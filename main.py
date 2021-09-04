from pycoingecko import CoinGeckoAPI
import time
import requests
from pygame import mixer


cg = CoinGeckoAPI()

# load sound
mixer.init()
mixer.music.load('')  # music file location

base_coins_list = cg.get_coins_list()

print('\nProgram initialized at ' + time.strftime('%H:%M'))

time.sleep(25)

# main program loop
while True:
    try:
        current_coins_list = cg.get_coins_list()
        if current_coins_list != base_coins_list:
            mixer.music.play()
            print('\nNew coin(s) released at ' + time.strftime('%H:%M') + '! -----------------------------------------')

            # find new coins
            new_coins_list = [x for x in current_coins_list if x not in base_coins_list]

            # print name
            for coin in new_coins_list:
                print('Name: %s' % coin.get('name'))

            base_coins_list = current_coins_list
    except requests.HTTPError:
        print('error, too many requests')
    time.sleep(25)
