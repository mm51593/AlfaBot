class Commands:
    ''' stores a dictionary of functions '''
    
    def __init__(self):
        self.commands = dict()
        self.loadCommands()
        return

    def loadCommands(self):
        import functionsBase
        functionsBase.commandLoader(self.commands)
        return
