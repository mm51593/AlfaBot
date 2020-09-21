import discord
from commands import Commands 

class Bot:
    '''low level client manipulation'''

    def __init__(self, settings):
        self.client = discord.Client()
        self.settings = settings
        self.commands = Commands().commands

        @self.client.event
        async def on_ready():
            print("Ready!")
            return
        return

    def start(self):
        print("Starting...")
        self.client.run(self.settings.token)
        return

    async def end(self):
        print("Shutting down...")
        await self.client.logout()
        return

    def messageTrimmer(self, message):
        msgtxt = message.content[len(self.settings.prefix):].strip().split(' ', 1)
        return msgtxt
