from os import link
from flask import Flask, app, render_template, request, jsonify
import pandas as pd
import csv
import os
from Classes.ForceDirectedFormat import ForceDirectedFormat
from Classes.Heatmap import Heatmap
from Classes.PieChart import PieChart

from pandas.core.base import DataError



#Bunu silme
app =Flask(__name__,template_folder= "Template")


#Root for the main page
@app.route('/', methods = ['GET', 'POST'])
def homepage():
   return render_template("Base.html")


#Root for the datasets page
@app.route('/data')
def data():
    filename = './static/enron-v1.csv'
    data = pd.read_csv(filename, header=0)
    myData = list(data.values)
    
    return render_template('data.html', myData=myData)


   

#Root for the visualizations page
@app.route('/visualizations/', methods = ['GET', 'POST'])
def visulizations():
    if request.method == 'POST':
      file = request.files['csvfile']
      if not os.path.isdir('static'):
         os.mkdir('static')

      csv_filepath = os.path.join('static', file.filename)
      json_filepath = os.path.join('Template', os.path.splitext(file.filename)[0] + '.json')
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

      fd_format = ForceDirectedFormat()
      fd_format.writeToFile(data)

      heatmap_format = Heatmap()
      heatmap_format.writeToFile_Heatmap(data)

      PieChart_format = PieChart()
      PieChart_format.writeToFile_PieChart(data)
     
     
      return  render_template("AQ.html")
    
    return render_template("AQ.html", message = "Please upload a csv file that is related to the Enron")


#Root for the json files
@app.route('/visualizations/<filename>.csv', methods = ['GET', 'POST'])
def Enron_anyfile(filename):
   #check if the file exists

   with open('C:\\Users\\20201077\\Desktop\\Doruk Güngör\\Eindhoven\\Computer Science\\Year 1\\Q4\\DBL-Webtech\\Phyton\\Template/' + filename + '.json', 'r') as file:
      Json_any_file = file.read()
      return Json_any_file



#This is important
if __name__ == "__main__":
    app.run(debug=True)
