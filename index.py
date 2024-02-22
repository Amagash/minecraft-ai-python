import boto3
import json
from javascript import require, On

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 58917,
  'username':'Claude',
  'verbose': True,
})

# Create a new minecraft-data instance with the bot's version
mcData = require('minecraft-data')(bot.version)

@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")

@On(bot, "chat")
def handle(this, username, message, *args):
    if username == bot.username:
        return
    else:
        bedrock = boto3.client(service_name="bedrock-runtime")
        body = json.dumps(
            {
                "prompt": "\n\nHuman: {} \n\nAssistant:".format(message),
                "max_tokens_to_sample": 100,
                "anthropic_version": "bedrock-2023-05-31"
            }
        )
        response = bedrock.invoke_model(body=body, modelId="anthropic.claude-v2:1")
        response_body = json.loads(response.get("body").read())
        response = response_body.get("completion")
        bot.chat(response)
        response = "bot.setControlState('jump', True)"
        try:
            eval("{}".format(response))
        except:
            bot.chat(response)
