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
        self.queue.append(url)
        
        if not self.current:
            self.playNext()
        return

    def playNext(self):
        try:
            data = self.ytdl.extract_info(self.queue.pop(0), download = False)
        except Exception as e:
            print(e) # make this an exception

        self.current = PCMVolumeTransformer(FFmpegPCMAudio(data['url']), self.volume)
        self.voice.play(self.current, after = self.finalise)
        print('playing')
        return

    def finalise(self, E):
        if E:
            print('Playback error')
        else:
            print('finished')
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
        if self.voice.is_playing() or self.voice.is_paused():
            self.voice.stop()
        return

    def pause(self):
        if self.voice.is_playing():
            self.voice.pause()
        return

    def resume(self):
        if self.voice.is_paused():
            self.voice.resume()
        return
