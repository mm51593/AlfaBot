def commandLoader(commandDict):
    commandDict['shutdown'] = shutdown
    return

async def shutdown(bot, *args):
    await bot.end()
    return
