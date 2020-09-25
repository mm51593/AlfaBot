from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

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
        

    async def moveToVoiceChannel(self, voiceClient, voiceChannel):
        # retains VoiceClient, unlike disconnect->connect
        await voiceClient.move_to(voiceChannel)

    async def playMusic(self, url, voiceConnection):
        ytdl_format_options = {'format': 'bestaudio/best', 'outtmpl': './music_cache/%(id)s-%(title)s'}
        ytdl = YoutubeDL(ytdl_format_options)
        try:
            data = ytdl.extract_info(url, download = True)
        except:
            print('data error')
        filename = ytdl.prepare_filename(data)
        voiceConnection.play(FFmpegPCMAudio(filename))
