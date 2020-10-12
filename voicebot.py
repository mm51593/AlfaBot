from youtube_dl import YoutubeDL
from musicQueue import MusicQueue

class VoiceBot:
    ''' Voice chat funcionality '''
    
    def __init__(self, client):
        self.client = client        
        ytdl_format_options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'outtmpl': './music_cache/%(id)s-%(title)s',
            'quiet': True,
            'default_search': 'auto'}
        self.ytdl = YoutubeDL(ytdl_format_options)
        return
    
    async def connectToVoiceChannel(self, voiceChannel):
        vclient = await voiceChannel.connect()
        vclient.musicQueue = MusicQueue(self.ytdl, vclient)
        return
        
    async def disconnectFromVoiceChannel(self, voiceConnection):
        await voiceConnection.disconnect()
        return

    async def moveToVoiceChannel(self, voiceClient, voiceChannel):
        ''' retains VoiceClient, unlike disconnect->connect '''
        await voiceClient.move_to(voiceChannel)
        return

    def enqueueSong(self, url, voiceConnection):
        voiceConnection.musicQueue.enqueue(url)
        return

    def getVolume(self, voiceConnection):
        return voiceConnection.musicQueue.volume

    def setVolume(self, voiceConnection, volume):
        try:
            newVolume = int(volume)
        except:
            print("Invalid value") # make this an exception
            return
        return voiceConnection.musicQueue.setVolume(newVolume / 100)

    def stopMusic(self, voiceConnection):
        return voiceConnection.musicQueue.stop()

    def pauseMusic(self, voiceConnection):
        return voiceConnection.musicQueue.pause()

    def resumeMusic(self, voiceConnection):
        return voiceConnection.musicQueue.resume()
        
