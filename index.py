import boto3
import json
import logging
import minecraft_data
from javascript import require, On
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

bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 59714,
  'username':'Mistral',
  'verbose': True,
})

bot.loadPlugin(pathfinder.pathfinder)
mcData = require('minecraft-data')(bot.version)
mcd = minecraft_data(bot.version)

@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")
  

@On(bot, "chat")
def handle(this, player_name, message, *args):
    if player_name == bot.username:
        return
    else:
        response = generate_text(message)
        code = extract_substring(response, "<code>", "</code>")
        reasoning = extract_substring(response, "<scratchpad>", "</scratchpad>")
        logger.info("REASONING BEGINNING: %s REASONING END", reasoning)

        # dirt_block = bot.findBlock({
        #   matching: mcdata.blocks.dirt.id,
        #   maxDistance: 128
        # })

        # print(dirt_block)

        try:
            # WARNING: this is a very dangerous way to execute code! Do you trust AI?
            # Note: the code is executed in the context of the bot entity
            logger.info("CODE BEGINNING: %s CODE END", code)
            exec("{}".format(code))

        except Exception as error:
            # print("error: {}".format(error))
            # bot.chat("I could not execute that: {}".format(code))
            # message_with_error = f"I got the following error: {error} with the following code {code} solve the issue."
            logger.info("ERROR BEGINNING: %s ERROR END", error)
            bot.chat("Sorry I did not understand, can you repeat that ?")
            # new_code = generate_text(message)
            # handle(this, player_name, new_code)


# if __name__ == "__main__":
#     # message = "move forward 1 step."
#     # response = generate_text(message)
#     # code = code_extract(response)

#     # code = """bot.pathfinder.setGoal(new bot.GoalBlock(bot.entity.position.offset(0, 0, -1)))
#     # """
#     # code = """bot.pathfinder.setGoal(pathfinder.goals.GoalBlock(bot.entity.position.offset(0, 0, -1)))
#     # """
#     player = bot.players[player_name]
#     print(player)
