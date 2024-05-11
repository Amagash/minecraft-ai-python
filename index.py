import boto3
import json
import logging
from javascript import require, On
from context.advanced import prompt
from helper.text_handler import *




mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
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

@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")
  

@On(bot, "chat")
def handle(this, player_name, message, *args):
    if player_name == bot.username:
        return
    else:
        bot.chat("hello")
        code = """bot.pathfinder.setGoal(pathfinder.goals.GoalNear(0, 0, -1))"""
        eval("{}".format(code))
        # response = generate_text(message)
        # code = extract_substring(response, "<code>", "</code>")

#         try:
#             # WARNING: this is a very dangerous way to execute code! Do you trust AI?
#             # Note: the code is executed in the context of the bot entity
#             print(f"Running: {code}")
#             eval("{}".format(code))
#             # if code != "":
#             #     code = code.strip()
#             #     for code_line in code.split('\n'):
#             #         print(f"Running: {code_line}")
#             #         eval("{}".format(code_line))
#         except Exception as error:
#             print("error: {}".format(error))
#             bot.chat("I could not execute that: {}".format(code))
#             # message_with_error = f"I got the following error: {error} with the following code {code} solve the issue."
#             # new_code = generate_text(message_with_error)
#             # handle(this, player_name, new_code)


# if __name__ == "__main__":
#     # message = "move forward 1 step."
#     # response = generate_text(message)
#     # code = code_extract(response)

#     # code = """bot.pathfinder.setGoal(new bot.GoalBlock(bot.entity.position.offset(0, 0, -1)))
#     # """
#     # code = """bot.pathfinder.setGoal(pathfinder.goals.GoalBlock(bot.entity.position.offset(0, 0, -1)))
#     # """
#     code = """bot.chat("hello")"""
#     eval("{}".format(code))
