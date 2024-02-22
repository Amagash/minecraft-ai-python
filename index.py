import boto3
import json
from javascript import require, On

mineflayer = require('mineflayer')

bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 61026,
  'username':'TITI',
  'verbose': True,
})

@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")

@On(bot, "chat")
def handle(this, username, message, *args):
    if username == bot.username:
        return
    else:
        bot.chat("hi!")