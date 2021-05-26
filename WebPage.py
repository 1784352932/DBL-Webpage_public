from os import link
from flask import Flask, app, render_template, request
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
   if request.method == 'POST':
      file = request.files['csvfile']
      if not os.path.isdir('static'):
         os.mkdir('static')
      filepath = os.path.join('static', file.filename)
      file.save(filepath)
      return "The uploaded file is: " + file.filename + render_template("Base.html")
   return render_template("Base.html")


@app.route('/data')
def data():
    filename = './static/enron-v1.csv'
    data = pd.read_csv(filename, header=0)
    myData = list(data.values)
    
    return render_template('data.html', myData=myData)

@app.route('/visualizations/Template/Forced_graph.json', methods = ['GET', 'POST'])
def Enron_force():
   with open("./Template/Forced_graph.json") as file:
      enron_data = file.read()
      return enron_data
   

@app.route('/visualizations/Template/Enron_3d_scatter.json', methods = ['GET', 'POST'])
def Enron_3d():
   with open("./Template/3d_scatter.json") as file:
      enron_data_3d_SCATTER = file.read()
      return enron_data_3d_SCATTER



@app.route('/visualizations/Template/Enron.json', methods = ['GET', 'POST'])
def Enron():
   with open("./Template/Enron.json") as file:
      enron_data = file.read()
      return enron_data


   
   
#Bunu silme
@app.route('/visualizations/')
def visulizations():
   return render_template("AQ.html")


#Bunu silme
if __name__ == "__main__":
    app.run(debug=True)

#Data Process Section
df_enron = pd.read_csv(csv_file_path)

DataFrame = str #This should be changed into a different type.
Visulization = str #This should be changed into a different type.

def user_choose_fromId(df:DataFrame, lb:int, ub:int) -> DataFrame:
    """Returns the Dataframe of the fromId choosen by the user.
    
    Assumptions:
    * lb > 0
    * ub > 0 & ub <= 149
    """
    df_user_choose_fromId = df.copy()
    user_choose_fromId_bool = (df_user_choose_fromId['fromId'] <= ub) & (df_user_choose_fromId['fromId'] >= lb)
    df_user_choose_fromId = df_user_choose_fromId[user_choose_fromId_bool].reset_index(drop=True)
    return df_user_choose_fromId

def user_choose_toId(df:DataFrame, lb:int, ub:int) -> DataFrame:
    """Returns the Dataframe of the toId choosen by the user.
    
    Assumptions:
    * lb > 0
    * ub > 0 & ub <= 149
    """
    df_user_choose_toId = df.copy()
    user_choose_toId_bool = (df_user_choose_toId['toId'] <= ub) & (df_user_choose_toId['toId'] >= lb)
    df_user_choose_toId = df_user_choose_toId[user_choose_toId_bool].reset_index(drop=True)
    return df_user_choose_toId

def user_choose_fromJobtitle(df:DataFrame, title:str) -> DataFrame:
    """Returns the Dataframe of the fromJobtitle choosen by the user.
    
    Assumptions:
    * JobTitle must be valid.
    """
    if title == 'ALL':
        return df
    else:
        title_list = list(df['fromJobtitle'])
        assert title in title_list, "Please provide a valid job title, or the string Unknown."
    
        df_user_choose_fromJobtitle = df.copy()
        user_choose_fromJobtitle_bool = df_user_choose_fromJobtitle['fromJobtitle'] == title
        df_user_choose_fromJobtitle = df_user_choose_fromJobtitle[user_choose_fromJobtitle_bool].reset_index(drop=True)
        return df_user_choose_fromJobtitle

def user_choose_toJobtitle(df:DataFrame, title:str) -> DataFrame:
    """Returns the Dataframe of the toJobtitle choosen by the user.
    
    Assumptions:
    * JobTitle must be valid.
    """
    if title == 'ALL':
        return df
    else:    
        title_list = list(df['toJobtitle'])
        assert title in title_list, "Please provide a valid job title, or the string Unknown."
    
        df_user_choose_toJobtitle = df.copy()
        user_choose_toJobtitle_bool = df_user_choose_toJobtitle['toJobtitle'] == title
        df_user_choose_toJobtitle = df_user_choose_toJobtitle[user_choose_toJobtitle_bool].reset_index(drop=True)
        return df_user_choose_toJobtitle

def user_choose_messageType(df:DataFrame, message_type:str) -> DataFrame:
    """Returns the Dataframe of the message type choosen by the user.
    
    Assumptions:
    * messageType must be either TO or CC.
    """
    if message_type == 'ALL':
        return df
    else:    
        type_list = list(df['messageType'])
        assert message_type in type_list, "Please provide a valid message type, TO or CC."
    
        df_user_choose_messageType = df.copy()
        user_choose_messageType_bool = df_user_choose_messageType['messageType'] == message_type
        df_user_choose_messageType = df_user_choose_messageType[user_choose_messageType_bool].reset_index(drop=True)
        return df_user_choose_messageType

def user_choose_sentiment(df:DataFrame, lb:float, ub:float) -> DataFrame:
    """Returns the Dataframe of the sentiment range choosen by the user.
    
    Assumptions:
    * lb >= -1 * lb < 1
    * ub > -1 & ub <= 1
    """
    df_user_choose_sentiment = df.copy()
    user_choose_sentiment_bool = (df_user_choose_sentiment['sentiment'] <= ub) & (df_user_choose_sentiment['sentiment'] >= lb)
    df_user_choose_sentiment = df_user_choose_sentiment[user_choose_sentiment_bool].reset_index(drop=True)
    return df_user_choose_sentiment


def user_choose_data (df_original: DataFrame = df_enron) -> DataFrame:
    """Returns a modified dataframe, according to the options that user choose, from the original dataframe.
    """
    lb_fromId = int(input('Please provide the lower bound of the range of fromId that you want to investigate. (Min: 0, Max: 149) : '))
    ub_fromId = int(input('Please provide the upper bound of the range of fromId that you want to investigate. (Min: 0, Max: 149) : '))
    df_mod_fromId = user_choose_fromId(df_original, lb_fromId, ub_fromId)
    
    lb_toId = int(input('Please provide the lower bound of the range of toId that you want to investigate. (Min: 0, Max: 149) : '))
    ub_toId = int(input('Please provide the upper bound of the range of toId that you want to investigate. (Min: 0, Max: 149) : '))
    df_mod_toId = user_choose_toId(df_mod_fromId, lb_toId, ub_toId)
    
    title_fromJobtitle = input('Please provide sender’s job title that you want to investigate, type "ALL" if you want to investigate all.: ')
    df_mod_fromJobtitle = user_choose_fromJobtitle(df_mod_toId, title_fromJobtitle)

    title_toJobtitle = input('Please provide receiver’s job title that you want to investigate, type "ALL" if you want to investigate all.: ')
    df_mod_toJobtitle = user_choose_fromJobtitle(df_mod_fromJobtitle, title_toJobtitle)
    
    message_type = input('Please provide the message type, type "ALL" if you want to investigate all. (toward:"TO", cc: "CC"): ')
    df_mod_final = user_choose_messageType(df_mod_toJobtitle, message_type)
    
    return df_mod_fromId


