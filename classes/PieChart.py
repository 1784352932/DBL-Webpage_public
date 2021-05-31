from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class PieChart(JsonFormat):
    def __init__(self):
        super().__init__({'variables_PieChart': []}, "C:\\Users\\20201077\\Desktop\\Doruk Güngör\\Eindhoven\\Computer Science\\Year 1\\Q4\\DBL-Webtech\\Phyton\\Template\\example.json")

    def writeToFile_PieChart(self, data):
        PieChart_format = self.schema

        for key in data:
            PieChart_format['variables'].append({'fromEmail': data[key][0]["fromEmail"],
                'toEmail': data[key][0]["toEmail"], 'sentiment': data[key][0]["sentiment"]})
                
        
        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(PieChart_format, indent=6))