import discord

class Bot:
    '''low level client manipulation'''

    def __init__(self, settings):
        self.client = discord.Client()
        self.settings = settings

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
