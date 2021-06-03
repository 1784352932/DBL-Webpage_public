from os import link


class JsonFormat():
    def __init__(self, schema, filepath):
        self.filepath = filepath
        self.schema = schema

    def writeToFile(self, data):
        pass