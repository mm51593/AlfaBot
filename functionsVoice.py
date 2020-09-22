class functionsVoice:
    ''' Voice-related commands '''
    
    async def join(bot, message, *args):
        for channel in message.channel.guild.voice_channels:
            for member in channel.members:
                if member == message.author:
                    await bot.voice.connectToVoiceChannel(channel)
                    return
