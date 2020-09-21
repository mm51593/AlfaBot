class functionsBase:
    
    async def shutdown(bot, *args):
        await bot.end()
        return

    async def test(bot, message, *args):
        await bot.sendMessage(message, 'Test')
        return
