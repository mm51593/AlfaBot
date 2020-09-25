from discord import FFmpegPCMAudio
from discord import PCMVolumeTransformer

class MusicQueue:
    ''' Manipulates song queueing '''

    def __init__(self, ytdl, voiceConnection):
        self.queue = []
        self.voice = voiceConnection
        self.ytdl = ytdl
        self.volume = 0.5
        self.current = None
        return

    def enqueue(self, url):
        try:
            data = self.ytdl.extract_info(url, download = False)
        except Exception as e: 
            print(e) # make this an exception
        self.queue.append(self.ytdl.prepare_filename(data))

        if not self.current:
            self.playNext()
        return

    def playNext(self):
        self.current = PCMVolumeTransformer(FFmpegPCMAudio(self.queue.pop(0)), self.volume)
        self.voice.play(self.current, after = self.finalise)
        return

    def finalise(self, E):
        if E:
            print('Playback error')
        else:
            if self.queue:
                self.playNext()
            else:
                self.current = None
        return

    def setVolume(self, newVolume):
        self.volume = newVolume
        self.current.volume = newVolume
        return

    def stop(self):
        self.queue.clear()
        if self.voice.is_playing():
            self.voice.stop()
        return
