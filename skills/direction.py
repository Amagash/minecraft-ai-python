
from javascript import require
pathfinder = require('mineflayer-pathfinder')

def goToPlayer (bot, range_goal, player_name):
    player = bot.players[player_name]
    target = player.entity
    pos = target.position
    bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, range_goal))
