from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class ForceDirectedFormat(JsonFormat):
    def __init__(self):
        super().__init__({'nodes': [], 'links': []}, "C:\\Users\\20201077\\Desktop\\Doruk Güngör\\Eindhoven\\Computer Science\\Year 1\\Q4\\DBL-Webtech\\Phyton\\Template\\example.json")

    def writeToFile(self, data):
        data_fd_graph = self.schema

        for key in data:
            data_fd_graph['nodes'].append({'id': key, 'fromJobtitle': data[key][0]["fromJobtitle"],
                'toJobtitle': data[key][0]["toJobtitle"]})
                
            for item in data[key]:
                data_fd_graph['links'].append({'source': item['fromEmail'], 'target': item['toEmail'], 'sentiment': item['sentiment']})
        
        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(data_fd_graph, indent=6))
      