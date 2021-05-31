from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class ForceDirectedFormat(JsonFormat):
    def __init__(self):
        super().__init__({'nodes': [], 'links': []}, "C:\\Users\\20201077\\Desktop\\Doruk Güngör\\Eindhoven\\Computer Science\\Year 1\\Q4\\DBL-Webtech\\Phyton\\Template\\ForcedDirectedGraph.json")

    def writeToFile(self, data):
        data_fd_graph = self.schema

        for key in data:
            data_fd_graph['nodes'].append({'id': key, 'group': data[key][0]["fromJobtitle"]})
                
            for item in data[key]:
                data_fd_graph['links'].append({'source': item['fromEmail'], 'target': item['toEmail'], 'sentiment': item['sentiment']})
                if ({'id': item['toEmail'], 'group': item['toJobtitle']} not in data_fd_graph['nodes']):
                    data_fd_graph['nodes'].append({'id': item['toEmail'], 'group': item["toJobtitle"]})

        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(data_fd_graph, indent=6))
      
