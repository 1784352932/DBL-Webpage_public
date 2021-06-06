from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class Heatmap(JsonFormat):
    def __init__(self):
        super().__init__([], "./Template/heatmap.json")

    def writeToFile(self, data):
        Heatmap_format = self.schema

        for key in data:
            Heatmap_format.append({'fromId': data[key][0]["fromId"],
                'toId': data[key][0]["toId"], 'sentiment': data[key][0]["sentiment"]})
                
        
        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(Heatmap_format, indent=6))
      
