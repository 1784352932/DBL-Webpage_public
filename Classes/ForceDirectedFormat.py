from Classes.JsonFormat import JsonFormat
import os
import json
from pathlib import Path
import pandas as pd


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
                    'source': item['fromEmail'], 'target': item['toEmail'], 'emails_count': 0}

                data_fd_graph['links'].append(to_append)

                data_fd_graph_full.append(to_append)

                to_append = {
                    'id': item['toEmail'], 'group': item['toJobtitle'], 'fromId': item['toId']}

                data_fd_graph['nodes'].append(to_append)

        data_fd_graph['nodes'] = set(frozenset(d.items()) for d in data_fd_graph['nodes'])
        data_fd_graph['nodes'] = [dict(s) for s in data_fd_graph['nodes']]

        df = pd.DataFrame(data_fd_graph['links']).groupby(['source', 'target'])['emails_count'].agg('count').reset_index()

        data_fd_graph['links'] = (df.to_dict('r'))

        with open(self.filepath, "w") as jsonFile:
            jsonFile.write(json.dumps(data_fd_graph, indent=6))
