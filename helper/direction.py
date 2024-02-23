import threading
import time
from javascript import require
pathfinder = require('mineflayer-pathfinder')

def go_to_player (bot, range_goal, player_name):
    """
    A method to go to the player.
    """
    player = bot.players[player_name]
    target = player.entity
    pos = target.position
    bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, range_goal))

def follow_player(bot, range_goal, player_name):
    bot.go_to_playerInterval = set_interval(go_to_player, 2, bot=bot, range_goal=range_goal, player_name=player_name)

def set_interval(func, sec, **kwargs):
    while True:
        func(bot=kwargs['bot'], range_goal=kwargs['range_goal'], player_name=kwargs['player_name'])
        time.sleep(sec)
    