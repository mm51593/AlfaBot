class functionsBase:
    
    async def shutdown(bot, *args):
        await bot.end()
        return

    async def test(bot, message, *args):
        await bot.sendMessage(message, 'Test')
        return
    
    async def commands(bot, message, *args):
        text = '```Commands: '
        i = 0
        for x in list(bot.commands.keys()):
            if i != 0:
                text += ', '
            text += x
            i += 1
        text += '```'
        await bot.sendMessage(message, text)
