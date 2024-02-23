import threading
import time
from javascript import require
pathfinder = require('mineflayer-pathfinder')

from helper.interval import Interval

interval = None

def go_to_player (bot, player_name):
    """
    A method to go to the player.
    """
    player = bot.players[player_name]
    target = player.entity
    pos = target.position
    bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, 1))

def follow_player(bot, player_name):
    global interval
    interval = Interval(2, go_to_player, bot=bot, player_name=player_name)

def set_interval(func, sec, **kwargs):
    while True:
        func(bot=kwargs['bot'], player_name=kwargs['player_name'])
        time.sleep(sec)
    
def stop_following_player():
    global interval
    interval.stop()