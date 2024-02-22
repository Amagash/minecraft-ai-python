
from javascript import require
pathfinder = require('mineflayer-pathfinder')


def goToPlayer (bot, range_goal, username):
    player = bot.players[username]
    print("Target", player)
    target = player.entity
    pos = target.position
    movements = pathfinder.Movements(bot)
    bot.pathfinder.setMovements(movements)
    bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, range_goal))
