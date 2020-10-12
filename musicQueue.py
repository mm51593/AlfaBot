from discord import FFmpegPCMAudio
from discord import PCMVolumeTransformer

class MusicQueue:
    ''' Manipulates song queueing '''

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

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
            info = self.ytdl.extract_info(self.queue.pop(0), download = False, process = False)
        except Exception as e:
            print(e) # make this an exception

        try:
            data = self.ytdl.extract_info(info['url'], download = False)
        except Exception as e:
            print(e) # make this an exception

        if 'entries' in data:
            data = data['entries'][0]

        #print(data)
        self.current = PCMVolumeTransformer(FFmpegPCMAudio(data['url'], **self.FFMPEG_OPTIONS), self.volume)
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
