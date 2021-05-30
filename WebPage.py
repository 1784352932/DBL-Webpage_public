from os import link
from flask import Flask, app, render_template, request, jsonify
import pandas as pd
import csv,json
import os



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
         Json_any_file = jsonFile.write(json.dumps( data_new, indent=6))
         return "The uploaded file is: " + file.filename + render_template("AQ.html")
    
    return render_template("AQ.html")



@app.route('/visualizations/<filename>.csv', methods = ['GET', 'POST'])
def Enron_anyfile(filename):
   #check if the file exists

   with open('./Template/' + filename + '.json', 'r') as file:
      Json_any_file = file.read()
      return Json_any_file



#Bunu silme
if __name__ == "__main__":
    app.run(debug=True)
