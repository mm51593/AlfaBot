from discord import FFmpegPCMAudio

class VoiceBot:
    ''' Voice chat funcionality '''
    
    def __init__(self, client):
        self.client = client
        self.connections = dict()
        return
    
    async def connectToVoiceChannel(self, voiceChannel):
        self.connections[voiceChannel.guild] = await voiceChannel.connect()
        
    async def disconnectFromVoiceChannel(self, voiceConnection):
        await voiceConnection.disconnect()
        del self.connections[voiceConnection.guild]
        

    # TODO: move_to functionality

    async def playMusic(self, voiceConnection):
        source = FFmpegPCMAudio(r'D:\Users\Maks\Music\y2mate.com - Persona Q2 OST_ Pull the Trigger (Kotone Shiomi Battle Theme)_NLyznZmzPgA.mp3')
        voiceConnection.play(source)
