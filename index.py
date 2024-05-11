import boto3
import json
import logging
from javascript import require, On
from context.advanced import prompt
from helper.direction import *


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

bot = mineflayer.createBot({
  'host': 'localhost',
  'port': 56818,
  'username':'Mistral',
  'verbose': True,
  'checkTimeoutInterval': 60 * 10000,
})

bot.loadPlugin(pathfinder.pathfinder)

mcData = require('minecraft-data')(bot.version)

def generate_text(message):
    model_id = "mistral.mistral-large-2402-v1:0"
    message_prompt = prompt.replace("[[MESSAGE]]", message)
    prompt_to_ai = """<s>[INST] {} [/INST]""".format(message_prompt)

    bedrock = boto3.client(service_name="bedrock-runtime")

    body = json.dumps(
        {
            "prompt": prompt_to_ai,
            "max_tokens": 400,
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 50
        }
    )
    logger.info("Generating text with Mistral AI model %s", model_id)

    bedrock = boto3.client(service_name='bedrock-runtime')

    response = bedrock.invoke_model(
        body=body,
        modelId=model_id
    )

    logger.info("Successfully generated text with Mistral AI model %s", model_id)


    response_body = json.loads(response.get("body").read())
    response = response_body.get('outputs')

    return response


@On(bot, 'spawn')
def spawn(*args):
  print("I spawned 👋")
  

@On(bot, "chat")
def handle(this, player_name, message, *args):
    if player_name == bot.username:
        return
    else:
        response = generate_text(message)
        try:
            # WARNING: this is a very dangerous way to execute code! Do you trust AI?
            # Note: the code is executed in the context of the bot entity

            bot.chat("Claude generated the following line of code: {}".format(response))
            eval("{}".format(response))
            print(response)
        except Exception as error:
            print("error: {}".format(error))
            print("{}".format(response))
            bot.chat("ERROR I could not execute that")