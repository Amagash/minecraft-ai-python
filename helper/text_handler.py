import boto3
import json
import logging
# from context.advanced import prompt

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
def generate_text(message, prompt):
    model_id = "mistral.mistral-large-2402-v1:0"
    message_prompt = prompt.replace("[[MESSAGE]]", message)
    # print(message_prompt)
    prompt_to_ai = """<s>[INST] {} [/INST]""".format(message_prompt)
    # print(prompt_to_ai)
    bedrock = boto3.client(service_name="bedrock-runtime")

    body = json.dumps(
        {
            "prompt": prompt_to_ai,
            "max_tokens": 500,
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 50
        }
    )
    logger.info("PROMPT BEGINNING: %s PROMPT END", prompt_to_ai)


    response = bedrock.invoke_model(
        body=body,
        modelId=model_id
    )
    # print(response)
    response_body = json.loads(response.get("body").read())
    # print(response_body)
    outputs = response_body.get('outputs')
    # print("OUTPUTS: ", outputs)
    text = outputs[0]['text']
    # print("TEXT: ", text)
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