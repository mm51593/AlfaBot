class VoiceBot:
    ''' Voice chat funcionality '''
    
    def __init__(self, client):
        self.client = client
        return
    
    async def connectToVoiceChannel(self, voiceChannel):
        await voiceChannel.connect()
        
