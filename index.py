import boto3
import json
from javascript import require, On
from context.simple import prompt
from helper.direction import *

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
RANGE_GOAL = 1

bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 58917,
  'username':'Claude',
  'verbose': True,
})

bot.loadPlugin(pathfinder.pathfinder)
# Create a new minecraft-data instance with the bot's version
mcData = require('minecraft-data')(bot.version)


@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")
  

@On(bot, "chat")
def handle(this, player_name, message, *args):
    if player_name == bot.player_name:
        return
    else:
        follow_player(bot, RANGE_GOAL, player_name)

        bedrock = boto3.client(service_name="bedrock-runtime")
        query = "\n\nHuman: {}\n// {} \n\nAssistant:".format(prompt, message)
        print(query)
        body = json.dumps(
            {
                "prompt": query,
                "max_tokens_to_sample": 100,
                "anthropic_version": "bedrock-2023-05-31"
            }
        )
        response = bedrock.invoke_model(body=body, modelId="anthropic.claude-v2:1")
        response_body = json.loads(response.get("body").read())
        response = response_body.get("completion")
        print(response)
        try:
            # WARNING: this is a very dangerous way to execute code! Do you trust AI?
            # Note: the code is executed in the context of the bot entity
            eval("{}".format(response))
        except:
            bot.chat(response)
