import discord
from commands import Commands 
from voicebot import VoiceBot

class Bot:
    '''low level client manipulation'''

    def __init__(self, settings):
        self.client = discord.Client()
        self.settings = settings
        self.commands = Commands().commands
        self.voice = VoiceBot(self.client)

        @self.client.event
        async def on_message(message):
            if message.content.startswith(self.settings.prefix):
                if message.author != self.client.user:
                    fullCommand = self.messageTrimmer(message)
                    if fullCommand[0] in self.commands:
                        await self.commands[fullCommand[0]](self, message, fullCommand)
            return

        @self.client.event
        async def on_ready():
            print("Ready!")
            return

    def start(self):
        print("Starting...")
        self.client.run(self.settings.token)
        return

    async def end(self):
        print("Shutting down...")
        await self.client.logout()
        return

    async def sendMessage(self, message, messageText):
        await message.channel.send(messageText)
        return

    def messageTrimmer(self, message):
        msgtxt = message.content[len(self.settings.prefix):].strip().split(' ', 1)
        return msgtxt
