const mineflayer = require('mineflayer')

const bot = mineflayer.createBot({
    host: 'localhost',
    port: 61026,
    username: 'JS',
    verbose: true,
})

bot.once('spawn', () => {
    console.log("Hi!")
})
