def commandLoader(commandDict):
    commandDict['shutdown'] = shutdown
    return

async def shutdown(bot):
    await bot.end()
    return
