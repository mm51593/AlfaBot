class functionsVoice:
    ''' Voice-related commands '''
    
    
    async def join(bot, message, *args):
        currentConnection = bot.voice.connections.get(message.guild)
        for channel in message.channel.guild.voice_channels:
            for member in channel.members:
                if member == message.author:
                    if currentConnection != None:
                        if currentConnection.channel == channel:
                            return
                        else:
                            await bot.commands['leave'](bot, message)
                    await bot.voice.connectToVoiceChannel(channel)
                    return
                
    async def leave(bot, message, *args):
        if bot.voice.connections.get(message.guild) != None:
            await bot.voice.disconnectFromVoiceChannel(bot.voice.connections[message.guild])

    
    async def play(bot, message, *args):
        vclient = bot.voice.connections.get(message.guild)
        if vclient != None:
            await bot.voice.playMusic(vclient)
