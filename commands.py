class Commands:
    ''' stores a dictionary of functions '''
    
    def __init__(self):
        self.commands = dict()
        self.loadCommands()
        return

    def loadCommands(self):
        import functionsBase
        self.commandLoader(functionsBase.functionsBase)
        import functionsVoice
        self.commandLoader(functionsVoice.functionsVoice)
        return

    def commandLoader(self, target):
        for x in dir(target):
            if not x.startswith('__'):
                self.commands[x] = getattr(target, x)
        return
