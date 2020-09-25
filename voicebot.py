from youtube_dl import YoutubeDL
from musicQueue import MusicQueue

class VoiceBot:
    ''' Voice chat funcionality '''
    
    def __init__(self, client):
        self.client = client
        self.connections = dict()        
        ytdl_format_options = {
            'format': 'bestaudio/best',
            'outtmpl': './music_cache/%(id)s-%(title)s',
            'quiet': True}
        self.ytdl = YoutubeDL(ytdl_format_options)
        return
    
    async def connectToVoiceChannel(self, voiceChannel):
        self.connections[voiceChannel.guild] = await voiceChannel.connect()
        self.connections[voiceChannel.guild].musicQueue = MusicQueue(self.ytdl, self.connections[voiceChannel.guild])
        return
        
    async def disconnectFromVoiceChannel(self, voiceConnection):
        await voiceConnection.disconnect()
        del self.connections[voiceConnection.guild]
        return

    async def moveToVoiceChannel(self, voiceClient, voiceChannel):
        ''' retains VoiceClient, unlike disconnect->connect '''
        await voiceClient.move_to(voiceChannel)
        return

    async def enqueueSong(self, url, voiceConnection):
        voiceConnection.musicQueue.enqueue(url)
        return
