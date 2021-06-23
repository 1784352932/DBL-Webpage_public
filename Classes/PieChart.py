from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class PieChart(JsonFormat):
    def __init__(self):
        super().__init__([], "./Template/pie_chart.json")

    def writeToFile(self, data):
        PieChart_format = self.schema

        for key in data:
            for i in range(len(data[key])):
                to_append = {'fromEmail': data[key][i]["fromEmail"],
                    'toEmail': data[key][i]["toEmail"], 'fromJobtitle': data[key][i]["fromJobtitle"], 
                    'toJobtitle': data[key][i]["toJobtitle"]}

                PieChart_format.append(to_append)

        PieChart_format = set(frozenset(d.items()) for d in PieChart_format)
        PieChart_format = [dict(s) for s in PieChart_format]
        
        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(PieChart_format, indent=6))
