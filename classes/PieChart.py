from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class PieChart(JsonFormat):
    def __init__(self):
        super().__init__([], "C:\\Users\\20201077\\Desktop\\Doruk Güngör\\Eindhoven\\Computer Science\\Year 1\\Q4\\DBL-Webtech\\Phyton\\Template\\pie_chart.json")

    def writeToFile(self, data):
        PieChart_format = self.schema

        for key in data:
            PieChart_format.append({'fromEmail': data[key][0]["fromEmail"],
                'toEmail': data[key][0]["toEmail"], 'fromJobtitle': data[key][0]["fromJobtitle"], 
                'toJobtitle': data[key][0]["toJobtitle"]})
                
        
        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(PieChart_format, indent=6))
