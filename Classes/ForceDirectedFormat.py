from Classes.JsonFormat import JsonFormat
import os, json
from pathlib import Path

class ForceDirectedFormat(JsonFormat):
    def __init__(self):
        super().__init__({'nodes': [], 'links': []},  "./Template/ForcedDirectedGraph.json")

    def writeToFile(self, data):
        data_fd_graph = self.schema

        for key in data:
            data_fd_graph['nodes'].append({'id': key, 'group': data[key][0]["fromJobtitle"]})#, 'fromId': data[key][0]['fromId']})
                
            for item in data[key]:
                to_append = {'source': item['fromEmail'], 'target': item['toEmail']}

                if to_append not in [{i:data_item[i] for i in data_item if i != 'email_count'} for data_item in data_fd_graph['links']]:
                    data_fd_graph['links'].append(to_append)
                    data_fd_graph['links'][data_fd_graph['links'].index(to_append)]['email_count'] = len([link_item for link_item in data_fd_graph['links'] if {i: link_item[i] for i in link_item if i != 'emails_count'} == to_append])
                
                to_append = {'id': item['toEmail'], 'group': item['toJobtitle']}#, 'fromId': item['toId']}

                if (to_append not in data_fd_graph['nodes']):
                    data_fd_graph['nodes'].append(to_append)
                

        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(data_fd_graph, indent=6))
      
