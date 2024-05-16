import boto3
import inspect
import json
import logging
import minecraft_data
import math
from javascript import require, On, AsyncTask, Once
from context.advanced import prompt
from helper.text_handler import *
from vec3 import *

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
block = require('prismarine-block')
item = require('prismarine-item')
windows = require('prismarine-windows')
recipe = require('prismarine-recipe')
mineflayerViewer = require('prismarine-viewer')
inventoryViewer = require('mineflayer-web-inventory')
pvp = require('mineflayer-pvp')
vec3 = require('vec3')

bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 52348,
  'username':'Mistral',
  'verbose': True,
})

bot.loadPlugin(pathfinder.pathfinder)
mcData = require('minecraft-data')(bot.version)
mcd = minecraft_data("1.17")

def dig_block(bot, block):
  bot.dig(block)


@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")
  

@On(bot, "chat")
def handle(this, player_name, message, *args):
    if player_name == bot.username:
        return
    else:
        response = generate_text(message, prompt)
        code = extract_substring(response, "<code>", "</code>")
        reasoning = extract_substring(response, "<scratchpad>", "</scratchpad>")
        logger.info("REASONING BEGINNING: %s REASONING END", reasoning)

        try:
            # WARNING: this is a very dangerous way to execute code! Do you trust AI?
            # Note: the code is executed in the context of the bot entity
            logger.info("CODE BEGINNING: %s CODE END", code)
            exec("{}".format(code))

        except Exception as error:
            logger.info("ERROR BEGINNING: %s ERROR END", error)
            bot.chat(code)
