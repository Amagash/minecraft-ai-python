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
  'port': 59714,
  'username':'Mistral',
  'verbose': True,
#   'checkTimeoutInterval': 60 * 10000,
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
    outputs = response_body.get('outputs')
    text = outputs[0]['text']
    print (text)
    return text

def extract_substring(text, trigger_str, end_str):
    last_trigger_index = text.rfind(trigger_str)

    if last_trigger_index == -1:
        return ""

    next_end_index = text.find(end_str, last_trigger_index)

    if next_end_index == -1:
        return ""

    substring = text[last_trigger_index + len(trigger_str):next_end_index]

    return substring

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
        try:
            # WARNING: this is a very dangerous way to execute code! Do you trust AI?
            # Note: the code is executed in the context of the bot entity
            if code != "":
                code = code.strip()
                for code_line in code.split('\n'):
                    print(f"Running: {code_line}")
                    eval("{}".format(code_line))
        except Exception as error:
            print("error: {}".format(error))
            bot.chat("I could not execute that: {}".format(code))


# if __name__ == "__main__":
#     message = "move forward 1 step."
#     response = generate_text(message)
#     code = code_extract(response)