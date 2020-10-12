class functionsVoice:
    ''' Voice-related commands '''
    
    
    async def join(bot, message, *args):
        currentConnection = message.guild.voice_client
        newConnection = message.author.voice

        if newConnection:
            newChannel = newConnection.channel
            if currentConnection:
                await bot.voice.moveToVoiceChannel(currentConnection, newChannel)
            else:
                await bot.voice.connectToVoiceChannel(newChannel)
        else:
            print("No target channel")
        return
                
    async def leave(bot, message, *args):
        if message.guild.voice_client:
            await bot.voice.disconnectFromVoiceChannel(message.guild.voice_client)
        return
    
    async def play(bot, message, fullCommand, *args):
        vclient = message.guild.voice_client
        if vclient != None:
            bot.voice.enqueueSong(fullCommand[1], vclient)

    async def volume(bot, message, fullCommand, *args):
        vclient = message.guild.voice_client
        if vclient:
            if len(fullCommand) == 1:
                await bot.sendMessage(message.channel, "Current volume: {}.".format(int(bot.voice.getVolume(vclient) * 100)))
            else:
                bot.voice.setVolume(vclient, fullCommand[1])
        return

    async def stop(bot, message, *args):
        vclient = message.guild.voice_client
        if vclient:
            bot.voice.stopMusic(vclient)
        return

    async def pause(bot, message, *args):
        vclient = message.guild.voice_client
        if vclient:
            bot.voice.pauseMusic(vclient)
        return

    async def resume(bot, message, *args):
        vclient = message.guild.voice_client
        if vclient:
            bot.voice.resumeMusic(vclient)
        return
