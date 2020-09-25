from discord import FFmpegPCMAudio

class MusicQueue:
    ''' Manipulates song queueing '''

    def __init__(self, ytdl, voiceConnection):
        self.queue = []
        self.voice = voiceConnection
        self.ytdl = ytdl
        return

    def enqueue(self, url):
        try:
            data = self.ytdl.extract_info(url, download = False)
        except Exception as e: 
            print(e) # make this an exception
        self.queue.append(self.ytdl.prepare_filename(data))

        if len(self.queue) == 1:
            self.playNext()
        return

    def playNext(self):
        self.voice.play(FFmpegPCMAudio(self.queue[0]), after = self.finalise)
        return

    def finalise(self, E):
        if E:
            print('Playback error')
        else:
            self.queue.pop(0)
            if len(self.queue) > 0:
                self.playNext()
        return
