import boto3
import inspect
import json
import logging
import math
from context.simple import prompt
from javascript import require, On, AsyncTask, Once
from helper.text_handler import *
from vec3 import *

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
mineflayer = require('mineflayer')

bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 52348,
  'username':'Mistral',
  'verbose': True,
})

@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")
  

@On(bot, "chat")
def handle(this, player_name, message, *args):
    if player_name == bot.username:
        return
    else:
        # print(message)
        response = generate_text(message, prompt)
        code = response.lstrip()
        try:
            # WARNING: this is a very dangerous way to execute code! Do you trust AI?
            # Note: the code is executed in the context of the bot entity
            print("TRYING TO EXEC: ", code)
            eval("{}".format(code))
        except Exception as error:
          bot.chat(code)
          logger.info("ERROR BEGINNING: %s ERROR END", error)
