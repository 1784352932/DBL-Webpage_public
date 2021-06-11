''' 
6. fix performance issues!!!
'''
from Classes.JsonFormat import JsonFormat
import os
import json
from pathlib import Path


class ForceDirectedFormat(JsonFormat):
    def __init__(self):
        super().__init__({'nodes': [], 'links': []},  "./Template/ForcedDirectedGraph.json")

    def writeToFile(self, data):
        data_fd_graph = self.schema

        data_fd_graph_full = []

        for key in data:
            to_append = {
                'id': key, 'group': data[key][0]["fromJobtitle"], 'fromId': data[key][0]['fromId']}

            if (to_append not in data_fd_graph['nodes']):
                data_fd_graph['nodes'].append(to_append)

            for item in data[key]:
                to_append = {
                    'source': item['fromEmail'], 'target': item['toEmail']}

                if to_append not in data_fd_graph['links']:
                    data_fd_graph['links'].append(to_append)

                data_fd_graph_full.append(to_append)

                to_append = {
                    'id': item['toEmail'], 'group': item['toJobtitle'], 'fromId': item['toId']}

                if (to_append not in data_fd_graph['nodes']):
                    data_fd_graph['nodes'].append(to_append)

        for i in range(len(data_fd_graph['links'])):
            item = data_fd_graph['links'][i]
            curr_connections = list(filter(
                lambda x: x['source'] == item['source'] and x['target'] == item['target'], data_fd_graph_full))

            data_fd_graph['links'][i]['emails_count'] = len(curr_connections)

        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(data_fd_graph, indent=6))
