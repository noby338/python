from wxpy import *

bot = Bot()
friend = bot.friends().search('nobyTest')[0]
friend.send('Hello, WeChat!')