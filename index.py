import boto3
import json
from javascript import require, On
from context.simple import prompt
from helper.direction import *

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')



bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 58917,
  'username':'Claude',
  'verbose': True,
  'checkTimeoutInterval': 60 * 10000,
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

            bot.chat("trying to execute code the following code: {}".format(response))
            eval("{}".format(response))
            print(response)
        except Exception as error:
            print("error: {}".format(error))
            print("{}".format(response))
            bot.chat("I could not execute that: {}".format(response))
