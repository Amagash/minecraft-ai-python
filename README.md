# minecraft-ai-python

A proof of concept for controlling a bot in Minecraft with an AI. 

## Requirements

- Clone this project on your local machine
```shell
git clone https://github.com/Amagash/minecraft-ai-python.git
```
- [Minecraft](https://www.minecraft.net/en-us/get-minecraft) (Java Edition) version 1.17
- Node.js version 14+
- Python 3.8+
- An [AWS](https://us-east-1.console.aws.amazon.com/) account 

You can access mineflayer in Python in addition to any other JavaScript package by first installing the javascript pip package:
```shell
pip install javascript
```

## How to use

### Start the Minecraft server

Here is how to start the Minecraft server:

1. Choose a host computer. This computer should be fast enough to play Minecraft, while running a server for other players as well.
2. Launch the game and click **Single Player**.
3. Create a new world or open an existing one. 
4. Inside that world, press the Esc key, and click **Open to LAN**. 
5. Choose a game mode to set for the other players.
6. Choose **Creative mode** that allows you to fly and place an infinite number of blocks.
7. Click **Start LAN World**, and you'll see a message that a local game has been hosted.
8. Take note of the port number.
9. In index.py replace the port number with the one you just noted.
    ```python
    bot = mineflayer.createBot({
    'host': 'localhost',
    'port': [PORT_NUMBER],
    'username':'Claude',
    'verbose': True,
    })
    ```

### Launch the bot

From your terminal, run the following commands:

```
npm install
python index.py
```

In a few seconds, you should see a message that the bot is running, and you should see the bot pop up in Minecraft.

### Sending commands

Inside the Minecraft client, press the `T` key to open the chat box. You can now chat with your bot connected to your AI.

## Disclaimer

This is a proof of concept. It is not intended to be used in production.
