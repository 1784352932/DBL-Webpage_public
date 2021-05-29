from os import link
from flask import Flask, app, render_template, request, jsonify
import pandas as pd
import csv,json
import os
#import panel as pn
#import chart_studio.plotly as py
import plotly.graph_objs as go



csv_file_path = './static/enron-v1.csv'


json_file_path = './Template/Enron.json'

json_new_enron = './Template/Forced_graph.json'

json_3d_scatter = './Template/3d_scatter.json'



data = {}
with open(csv_file_path) as csvFile:
   csvReader = csv.DictReader(csvFile)
   for csvRow in csvReader:
      date = csvRow['date']
      data[date] = csvRow

#add a route to the dictionary

root = {}
root['node'] = data

edge = {}
edge['link'] = root
      
with open(json_file_path, "w") as jsonFile:
   Enron_json = jsonFile.write(json.dumps(data, indent=4))


cols_list = ["fromEmail", "toEmail", "sentiment", "fromJobtitle", "toJobtitle"]
df_new = pd.read_csv(csv_file_path, usecols=cols_list)

#df_new.to_csv(r'C:\Users\20201077\Desktop\Doruk Güngör\Eindhoven\Computer Science\Year 1\Q4\DBL-Webtech\Phyton\static\scatter_3d.csv')

csv_3d = './static/scatter_3d.csv'

new_data = {}
with open(csv_3d) as csvFile_1:
   csvReader_1 = csv.DictReader(csvFile_1)
   for csvRow_1 in csvReader_1:
      fromEmail = csvRow_1['fromEmail']
      new_data[fromEmail] = csvRow_1


with open(json_3d_scatter, "w") as jsonFile:
   Enron_3d_Json = jsonFile.write(json.dumps(new_data, indent=4))



#Bunu silme
app =Flask(__name__,template_folder= "Template")


#Bunu silme
@app.route('/', methods = ['GET', 'POST'])
def homepage():
   return render_template("Base.html")

@app.route('/data')
def data():
    filename = './static/enron-v1.csv'
    data = pd.read_csv(filename, header=0)
    myData = list(data.values)
    
    return render_template('data.html', myData=myData)


   

#Bunu silme
@app.route('/visualizations/', methods = ['GET', 'POST'])
def visulizations():
    if request.method == 'POST':
      file = request.files['csvfile']
      if not os.path.isdir('static'):
         os.mkdir('static')
      filepath = os.path.join('Template', os.path.splitext(file.filename)[0] + '.json')
      file.save(filepath)
      data_new = {}
      with open(filepath) as csvFile_new:
          csvReader_new = csv.DictReader(csvFile_new)
          for csvRow_new in csvReader_new:
              fromEmail = csvRow_new['fromEmail']
              data_new[fromEmail] = csvRow_new

      with open(filepath, "w") as jsonFile:
         Json_any_file = jsonFile.write(json.dumps(data_new, indent=4))
         return "The uploaded file is: " + file.filename + render_template("AQ.html")
    
    return render_template("AQ.html")



@app.route('/visualizations/<filename>.csv', methods = ['GET', 'POST'])
def Enron_anyfile(filename):
   #check if the file exists

   with open('./Template/' + filename + '.json', 'r') as file:
      Json_any_file = file.read()
      return Json_any_file





@app.route('/test')
def test():
   return render_template("Test.html")

#Bunu silme
if __name__ == "__main__":
    app.run(debug=True)
