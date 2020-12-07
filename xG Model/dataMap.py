'''
   MAIN DATA VISUALIZATION SCRIPT
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns
import pandas as pd
from dataControl import teamSort
from perfMeasures import playerSeasonEval
#from dataViz import pitchCreator
import matplotlib.colors as mcolors
pd.options.plotting.backend = "plotly"

plt.style.use('fivethirtyeight')

import gspread
import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets 

gc = pygsheets.authorize(service_file= 'andrabi-analytics.json')
Oxy = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSUi7dv_9At8t7pN9UX0J1V_-jfvUJ-SShjKII-GLS2BsUKbDgYHn_-YO9_lt2-onCJ-3ug1XLhvwXI/pub?output=csv' # read in xG data from Google spreadsheet

df = pd.read_csv(Oxy)

df = teamSort(df)
#print(df)

df = playerSeasonEval(df)

df = pd.DataFrame(df.loc[df['aG'] >= 2])
print(df)


fig = df.plot.scatter(x="aG", y="Total_Shots")
fig.show()


name = df['Player']
print(name)
aG = df['aG']
print(aG)
shots = df['Total_Shots']
print(shots)

fig, ax = plt.subplots()
ax.scatter(shots, aG)

#for i, txt in enumerate(name):
#    ax.annotate(txt, (shots[i], aG[i]))

plt.title('Seasonal xG v aG per Qualified Player')
plt.xlabel('Seasonal xG')
plt.ylabel('Seasonal aG')

plt.show()