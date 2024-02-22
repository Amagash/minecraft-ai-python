const mineflayer = require('mineflayer')

const bot = mineflayer.createBot({
    host: 'localhost',
    port: 61026,
    username: 'TOTO',
    verbose: true,
})

bot.once('spawn', () => {
    console.log("Hi!")
})
