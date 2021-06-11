from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class Heatmap(JsonFormat):
    def __init__(self):
        super().__init__([], "./Template/heatmap.json")

    def writeToFile(self, data):
        Heatmap_format = self.schema

        for key in data:
            for i in range(len(data[key])):
                to_append = {'fromId': data[key][i]["fromId"], 'toId': data[key][i]["toId"], 'sentiment': data[key][i]["sentiment"]}

                if to_append not in Heatmap_format:
                    Heatmap_format.append(to_append)
    
        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(Heatmap_format, indent=6))
      
