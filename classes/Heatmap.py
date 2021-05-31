from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class Heatmap(JsonFormat):
    def __init__(self):
        super().__init__({'variables': []}, "C:\\Users\\20201077\\Desktop\\Doruk Güngör\\Eindhoven\\Computer Science\\Year 1\\Q4\\DBL-Webtech\\Phyton\\Template\\example.json")

    def writeToFile_Heatmap(self, data):
        Heatmap_format = self.schema

        for key in data:
            Heatmap_format['variables'].append({'fromEmail': data[key][0]["fromEmail"],
                'toEmail': data[key][0]["toEmail"], 'sentiment': data[key][0]["sentiment"]})
                
        
        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(Heatmap_format, indent=6))
      