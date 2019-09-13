# -*-coding:utf-8 -*-

from wxpy import *
import os
import random
import time
from zhufu import spring_Festival
from zhufu import Mid_Autumn

bot = Bot(cache_path=True,qr_path='test.jpg')
bot.enable_puid('wxpy_puid.pkl')
my_friends = bot.friends()
for friends in my_friends:
    try:
        msg = Mid_Autumn.belssing[random.randint(0,19)]
        friend = my_friends.search(friends.name)[0]
        friend.send_msg(msg=msg)
        print(friend,msg)
        time.sleep(random.randint(1,6))
    except ResponseError as e:
        pass
print('work done')
