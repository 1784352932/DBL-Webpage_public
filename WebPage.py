from os import link
from flask import Flask, app, render_template, request, jsonify
import pandas as pd
import csv
import os
from Classes.ForceDirectedFormat import ForceDirectedFormat
from Classes.Heatmap import Heatmap
from Classes.PieChart import PieChart
import time

# Bunu silme
app = Flask(__name__, template_folder="Template")

# Root for the main page


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("Base.html")


# Root for the visualizations page
@app.route('/visualizations/', methods=['GET', 'POST'])
def visulizations():
    if request.method == 'POST':
        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')

        csv_filepath = os.path.join('static', file.filename)
        json_filepath = os.path.join(
            'Template', os.path.splitext(file.filename)[0] + '.json')
        file.save(csv_filepath)

        data = {}

        with open(csv_filepath) as csvFile_new:
            csvReader_new = csv.DictReader(csvFile_new)
            for csvRow_new in csvReader_new:
                fromEmail = csvRow_new['fromEmail']
                if (fromEmail not in data):
                    data[fromEmail] = [csvRow_new]
                else:
                    data[fromEmail].append(csvRow_new)

        start = time.time()

        fd_format = ForceDirectedFormat()
        fd_format.writeToFile(data)

        heatmap_format = Heatmap()
        heatmap_format.writeToFile(data)

        PieChart_format = PieChart()
        PieChart_format.writeToFile(data)

        end = time.time()

        print("Time elapsed: %.6f" % (end - start))

        return render_template("AQ.html")

    return render_template("AQ.html")


# Root for the json files
@app.route('/visualizations/<filename>', methods=['GET', 'POST'])
def Enron_anyfile(filename):
    # check if the file exists

    with open('./Template/' + filename + '.json', 'r') as file:
        Json_any_file = file.read()
        return Json_any_file


@app.route('/get-<filename>', methods=['GET', 'POST'])
def getResource(filename):
    # check if the file exists

    with open('./Template/' + filename, 'r') as file:
        return file.read()


#This is important
if __name__ == "__main__":
    app.run(debug=True)
