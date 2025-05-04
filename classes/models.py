class RootClass:
    def __init__(self, name, documentation, attributes: list = None):
        self.name = name
        self.documentation = documentation
        self.attributes = attributes
        self.target_connections = []            # соединения, для которых данный класс target

class NotRootClass(RootClass):
    def __init__(self, name, documentation, attributes: list = None):
        super().__init__(name, documentation, attributes)
        self.source_connections = []            # соединения, для которых данный класс source
