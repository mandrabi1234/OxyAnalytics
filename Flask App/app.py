# Example: setting up Python server using Flask
import os
from flask import Flask, jsonify, request, abort, render_template

import pygsheets

import pandas as pd


app = Flask(__name__)

gc = pygsheets.authorize(service_file= 'andrabi-analytics.json')
gsheet = gc.open("xG Stats").sheet1

# Access Google Spreadsheet
sh = gc.open('xG Stats')

#--Declare and initialize variables for each individual worksheet within Google Spreadsheet--#

wks = sh[0] # First worksheet: raw_xG 

wks1 = sh[1] # Second worksheet: Season_team

wks2 = sh[2] # Third worksheet: Season-player

wks3 = sh[3] # Fourth worksheet: Game_team

wks4 = sh[4] # Fifth worksheet: Game_player 

wks5 = sh[5] # Sixth worksheet: Season_GK

wks6 = sh[6]

wks7 = sh[7]

wks10 = sh[9]

seasonTeam = pd.DataFrame(wks1.get_all_records())      # Returns a list of dictionaries

seasonPlayer = pd.DataFrame(wks2.get_all_records())

gameTeam = pd.DataFrame(wks3.get_all_records())

metricIndex = pd.DataFrame(wks7.get_all_records())

gamePlayer = pd.DataFrame(wks4.get_all_records())

gkSeason = pd.DataFrame(wks5.get_all_records())

gameOpp = pd.DataFrame(wks10.get_all_records())      # Returns a list of dictionaries




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index1():
    return render_template('index.html')


#---Analysis Page Route---#
@app.route('/analysis')
def games():
    return render_template('analysis.html')

#---About Page Route---#
@app.route('/about')
def analysis():
    return render_template('about.html')

#---Contact Page Route---#
@app.route('/contact')
def season():
    return render_template('contact.html')

#---Analysis Home Routes---#
@app.route('/analysis-home')
def analysisHome():
    return render_template('analysis-home.html')

@app.route('/externalReference')
def externalReference():
    return render_template('externalReference.html')

@app.route('/analysis-home/metric_index')
def metric_index():
    offense = metricIndex.loc[metricIndex['ID'] == 'O']
    defense = metricIndex.loc[metricIndex['ID'] == 'D']
    overall = metricIndex.loc[metricIndex['ID'] == 'Ov']
    return render_template('metricIndex.html',tables=[overall.to_html(classes='overall'), offense.to_html(classes = 'offense'), defense.to_html(classes = 'defense')],
    titles = ['na', 'Overall Metrics', 'Offensive Metrics', 'Defensive Metrics'])   

     

@app.route('/analysis-season')
def analysisSeason():
    return render_template('analysis-season.html')

#---Player Breakdown ROUTES---#
@app.route('/analysis-season/playerBreakdown')
def playerBreakdown():
    goalKeepers = seasonPlayer.loc[seasonPlayer['position']=='GK']
    defenders = seasonPlayer.loc[seasonPlayer['position']=='D']
    midfielders = seasonPlayer.loc[seasonPlayer['position'] == 'M']
    forwards = seasonPlayer.loc[seasonPlayer['position'] == 'F']
    return render_template('analysis-season-playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

@app.route('/analysis-season/teamBreakdown')
def teamBreakdown():

    return render_template('analysis-season-teamBreakdown.html',tables=[gameTeam.to_html(classes='game')],
    titles = ['na'])

@app.route('/analysis-season/team-SeasonBreakdown')
def teamSeasonBreakdown():

    return render_template('analysis-season-teamSeasonBreakdown.html',tables=[seasonTeam.to_html(classes='game')],
    titles = ['na'])


@app.route('/analysis-season/teamVisuals')
def teamVisuals():
    return render_template('analysis-season-teamVisuals.html')


@app.route('/analysis-season/oppBreakdown')
def oppBreakdown():

    return render_template('analysis-season-oppBreakdown.html',tables=[gameOpp.to_html(classes='game')],
    titles = ['na'])


#---p90 Evaluation Routes---#
@app.route('/analysis-game')
def analysisGame():
    return render_template('analysis-game1.html')


@app.route('/analysis-game/team/playerBreakdown')
def analysisGame_Breakdown():
    seasonPlayer.set_index(['Player'], inplace=True)
    seasonPlayer.index.name=None
    goalKeepers = seasonPlayer.loc[seasonPlayer['position']=='GK']
    defenders = seasonPlayer.loc[seasonPlayer['position']=='D']
    midfielders = seasonPlayer.loc[seasonPlayer['position'] == 'M']
    forwards = seasonPlayer.loc[seasonPlayer['position'] == 'F']
    return render_template('test.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

#--Game 1 Analytics Routes--#
@app.route('/analysis-game/team-game1')
def analysisGame1():
    return render_template('analysis-game1.html')

@app.route('/analysis-game/team-game1-playerBreakdown')
def game1_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 1])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game1_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Game 2 Analytics Routes--#
@app.route('/analysis-game/team-game2')
def analysisGame2():
    return render_template('analysis-game2.html')

@app.route('/analysis-game/team-game2-playerBreakdown')
def game2_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 2])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game2_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])



#--Game 3 Analytics Routes--#
@app.route('/analysis-game/team-game3')
def analysisGame3():
    return render_template('analysis-game3.html')

@app.route('/analysis-game/team-game3-playerBreakdown')
def game3_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 3])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game3_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])




#--Game 4 Analytics Routes--#
@app.route('/analysis-game/team-game4')
def analysisGame4():
    return render_template('analysis-game4.html')

@app.route('/analysis-game/team-game4-playerBreakdown')
def game4_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 4])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game4_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Game 5 Analytics Routes--#
@app.route('/analysis-game/team-game5')
def analysisGame5():
    return render_template('analysis-game5.html')

@app.route('/analysis-game/team-game5-playerBreakdown')
def game5_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 5])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game5_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

#--Game 6 Analytics Routes--#
@app.route('/analysis-game/team-game6')
def analysisGame6():
    return render_template('analysis-game6.html')

@app.route('/analysis-game/team-game6-playerBreakdown')
def game6_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 6])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game6_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Game 7 Analytics Routes--#
@app.route('/analysis-game/team-game7')
def analysisGame7():
    return render_template('analysis-game7.html')

@app.route('/analysis-game/team-game7-playerBreakdown')
def game7_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 7])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game7_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

#--Game 8 Analytics Routes--#
@app.route('/analysis-game/team-game8')
def analysisGame8():
    return render_template('analysis-game8.html')

@app.route('/analysis-game/team-game8-playerBreakdown')
def game8_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 8])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game8_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

#--Game 9 Analytics Routes--#
@app.route('/analysis-game/team-game9')
def analysisGame9():
    return render_template('analysis-game9.html')

@app.route('/analysis-game/team-game9-playerBreakdown')
def game9_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 9])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game9_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

#--Game 10 Analytics Routes--#
@app.route('/analysis-game/team-game10')
def analysisGame10():
    return render_template('analysis-game10.html')

@app.route('/analysis-game/team-game10-playerBreakdown')
def game10_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 10])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game10_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

#--Game 11 Analytics Routes--#
@app.route('/analysis-game/team-game11')
def analysisGame11():
    return render_template('analysis-game11.html')

@app.route('/analysis-game/team-game11-playerBreakdown')
def game11_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 11])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game11_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Game 12 Analytics Routes--#
@app.route('/analysis-game/team-game12')
def analysisGame12():
    return render_template('analysis-game12.html')

@app.route('/analysis-game/team-game12-playerBreakdown')
def game12_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 12])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game12_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])

#--Game 13 Analytics Routes--#
@app.route('/analysis-game/team-game13')
def analysisGame13():
    return render_template('analysis-game13.html')

@app.route('/analysis-game/team-game13-playerBreakdown')
def game13_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 13])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game13_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Game 14 Analytics Routes--#
@app.route('/analysis-game/team-game14')
def analysisGame14():
    return render_template('analysis-game14.html')

@app.route('/analysis-game/team-game14-playerBreakdown')
def game14_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 14])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game14_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Game 15 Analytics Routes--#
@app.route('/analysis-game/team-game15')
def analysisGame15():
    return render_template('analysis-game15.html')

@app.route('/analysis-game/team-game15-playerBreakdown')
def game15_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 15])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game15_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Game 16 Analytics Routes--#
@app.route('/analysis-game/team-game16')
def analysisGame16():
    return render_template('analysis-game16.html')

@app.route('/analysis-game/team-game16-playerBreakdown')
def game16_playerBreakdown():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['ID'] == 16])
    goalKeepers = playerStat.loc[playerStat['position']=='GK']
    defenders = playerStat.loc[playerStat['position']=='D']
    midfielders = playerStat.loc[playerStat['position'] == 'M']
    forwards = playerStat.loc[playerStat['position'] == 'F']
    return render_template('game16_playerBreakdown.html',tables=[goalKeepers.to_html(classes='goalKeepers'), defenders.to_html(classes='defenders'), midfielders.to_html(classes='midfielders'), forwards.to_html(classes='forwards')],
    titles = ['na', 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'])


#--Player Stats Routes--#
# Ben Harding - GK, 00
@app.route('/analysis-home/playerBreakdown-benHarding')
def playerBreakdown_benHarding():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Ben Harding'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Ben Harding']


    return render_template('gameBreakdown_bHarding.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')], 
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

@app.route('/analysis-season/bHarding_visual')
def bHarding_visuals():
    return render_template('dataViz-bHarding.html')

# Jacob Gitin - GK, 0
@app.route('/analysis-home/playerBreakdown-jacobGitin')
def playerBreakdown_jacobGitin():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Jacob Gitin'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Jacob Gitin']


    return render_template('gameBreakdown_jGitin.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Scott Drazan - GK, 01
@app.route('/analysis-home/playerBreakdown-scottDrazan')
def playerBreakdown_scottDrazan():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Scott Drazan'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]

    return render_template('gameBreakdown_sDrazan.html',tables=[gkSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Riley Mccabe - D, 02
@app.route('/analysis-home/playerBreakdown-rileyMccabe')
def playerBreakdown_rileyMccabe():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Riley Mccabe'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Riley Mccabe']


    return render_template('gameBreakdown_rMccabe.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Spencer Shearer - M, 03
@app.route('/analysis-home/playerBreakdown-spencerShearer')
def playerBreakdown_spencerShearer():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Spencer Shearer'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Spencer Shearer']


    return render_template('gameBreakdown_sShearer.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Ryan Wilson - M, 04
@app.route('/analysis-home/playerBreakdown-ryanWilson')
def playerBreakdown_ryanWilson():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Ryan Wilson'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Ryan Wilson']


    return render_template('gameBreakdown_rWilson.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# David Paine - D, 05
@app.route('/analysis-home/playerBreakdown-davidPaine')
def playerBreakdown_davidPaine():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Daivd Paine'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'David Paine']


    return render_template('gameBreakdown_dPaine.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na','Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Nicolas Eble - M, 06
@app.route('/analysis-home/playerBreakdown-nicEble')
def playerBreakdown_nicEble():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Nicolas Eble'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Nicolas Eble']


    return render_template('gameBreakdown_nEble.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Matthew Teplitz - F, 07
@app.route('/analysis-home/playerBreakdown-mattTeplitz')
def playerBreakdown_mattTeplitz():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Matthew Teplitz'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Matthew Teplitz']


    return render_template('gameBreakdown_mTeplitz.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Ben Simon - M, 08
@app.route('/analysis-home/playerBreakdown-benSimon')
def playerBreakdown_benSimon():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Ben Simon'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Ben Simon']


    return render_template('gameBreakdown_bSimon.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Marcus Blumenfeld - F, 09
@app.route('/analysis-home/playerBreakdown-marcBlumenfeld')
def playerBreakdown_marcBlumenfeld():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Marcus Blumenfeld'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Marcus Blumenfeld']


    return render_template('gameBreakdown_mBlumenfeld.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Jasper Brannon - M, 10
@app.route('/analysis-home/playerBreakdown-jasperBrannon')
def playerBreakdown_jasperBrannon():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Jasper Brannon'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Jasper Brannon']


    return render_template('gameBreakdown_jBrannon.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Matthew Anzalone - D, 11
@app.route('/analysis-home/playerBreakdown-mattAnzalone')
def playerBreakdown_mattAnzalone():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Matthew Anzalone'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Matthew Anzalone']


    return render_template('gameBreakdown_mAnzalone.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Sean Kim - F, 12
@app.route('/analysis-home/playerBreakdown-seanKim')
def playerBreakdown_seanKim():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Sean Kim'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Sean Kim']


    return render_template('gameBreakdown_sKim.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Jack Meeker - D, 13
@app.route('/analysis-home/playerBreakdown-jackMeeker')
def playerBreakdown_jackMeeker():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Jack Meeker'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Jack Meeker']


    return render_template('gameBreakdown_jMeeker.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Adrian Paredes - M, 14
@app.route('/analysis-home/playerBreakdown-adrianParedes')
def playerBreakdown_adrianParedes():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Adrian Paredes'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Adrian Paredes']


    return render_template('gameBreakdown_aParedes.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

@app.route('/analysis-season/aParedes_visual')
def aParedes_visual():
    return render_template('dataViz-aParedes.html')


# Logan Myers - M, 16
@app.route('/analysis-home/playerBreakdown-loganMyers')
def playerBreakdown_loganMyers():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Logan Myers'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Logan Myers']


    return render_template('gameBreakdown_lMyers.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Tyler Wray - F, 17
@app.route('/analysis-home/playerBreakdown-tylerWray')
def playerBreakdown_tylerWray():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Tyler Wray'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Tyler Wray']


    return render_template('gameBreakdown_tWray.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Jake Foster - M, 18
@app.route('/analysis-home/playerBreakdown-jakeFoster')
def playerBreakdown_jakeFoster():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Jake Foster'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Jake Foster']


    return render_template('gameBreakdown_jFoster.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Joey Schwartz - M, 19
@app.route('/analysis-home/playerBreakdown-joeySchwartz')
def playerBreakdown_joeySchwartz():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Joey Schwartz'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Joey Schwartz']


    return render_template('gameBreakdown_jSchwartz.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Jazz Henry - F, 20
@app.route('/analysis-home/playerBreakdown-jazzHenry')
def playerBreakdown_jazzHenry():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Jazz Henry'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Jazz Henry']


    return render_template('gameBreakdown_jHenry.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na','Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Teagan Jarvis - F, 21
@app.route('/analysis-home/playerBreakdown-teaganJarvis')
def playerBreakdown_teaganJarvis():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Teagan Jarvis'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Teagan Jarvis']


    return render_template('gameBreakdown_tJarvis.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Tye Hernandez - M, 22
@app.route('/analysis-home/playerBreakdown-tyeHernandez')
def playerBreakdown_tyeHernandez():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Tye Hernandez'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Tye Hernandez']


    return render_template('gameBreakdown_tHernandez.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Miles Robertson - D, 23
@app.route('/analysis-home/playerBreakdown-milesRobertson')
def playerBreakdown_milesRobertson():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Miles Robertson'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Miles Robertson']


    return render_template('gameBreakdown_mRobertson.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Caleb Jordening - F, 24
@app.route('/analysis-home/playerBreakdown-calebJorden')
def playerBreakdown_calebJorden():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Caleb Jordening'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Caleb Jordening']


    return render_template('gameBreakdown_cJordening.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Neython Streitz - D, 25
@app.route('/analysis-home/playerBreakdown-neythonStreitz')
def playerBreakdown_neythonStreitz():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Neython Streitz'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Neython Streitz']


    return render_template('gameBreakdown_nStreitz.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Ben Tucker - D, 27
@app.route('/analysis-home/playerBreakdown-benTucker')
def playerBreakdown_benTucker():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Ben Tucker'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Ben Tucker']


    return render_template('gameBreakdown_bTucker.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])

# Luke Haas - GK, 30
@app.route('/analysis-home/playerBreakdown-lukeHaas')
def playerBreakdown_lukeHaas():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Luke Haas'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Luke Haas']


    return render_template('gameBreakdown_lHaas.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Eric DaCosta - D, 31
@app.route('/analysis-home/playerBreakdown-ericDacosta')
def playerBreakdown_ericDacosta():
    playerStat = pd.DataFrame(gamePlayer.loc[gamePlayer['Player'] == 'Eric Dacosta'])
    game1 = playerStat.loc[playerStat['ID']== 1]
    game2 = playerStat.loc[playerStat['ID']== 2]
    game3 = playerStat.loc[playerStat['ID'] == 3]
    game4 = playerStat.loc[playerStat['ID'] == 4]
    game5 = playerStat.loc[playerStat['ID'] == 5]
    game6 = playerStat.loc[playerStat['ID'] == 6]
    game7 = playerStat.loc[playerStat['ID'] == 7]
    game8 = playerStat.loc[playerStat['ID'] == 8]
    game9 = playerStat.loc[playerStat['ID'] == 9]
    game10 = playerStat.loc[playerStat['ID'] == 10]
    game11 = playerStat.loc[playerStat['ID'] == 11]
    game12 = playerStat.loc[playerStat['ID'] == 12]
    game13 = playerStat.loc[playerStat['ID'] == 13]
    game14 = playerStat.loc[playerStat['ID'] == 14]
    game15 = playerStat.loc[playerStat['ID'] == 15]
    game16 = playerStat.loc[playerStat['ID'] == 16]
    playerSeason = seasonPlayer.loc[seasonPlayer['Player'] == 'Eric Dacosta']


    return render_template('gameBreakdown_eDacosta.html',tables=[playerSeason.to_html(classes = 'playerStat'), game1.to_html(classes='game1'), game2.to_html(classes='game2'), game3.to_html(classes='game3'), game4.to_html(classes='game4'), 
    game5.to_html(classes='game5'), game6.to_html(classes='game6'), game7.to_html(classes='game7'), game8.to_html(classes='game8'), game9.to_html(classes='game9'), game10.to_html(classes='game10'), 
    game11.to_html(classes='game11'), game12.to_html(classes='game12'), game13.to_html(classes='game13'), game14.to_html(classes='game14'), game15.to_html(classes='game15'), game16.to_html(classes='game16')],
    titles = ['na', 'Seasonal', 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7', 'Game 8', 'Game 9', 'Game 10', 'Game 11', 'Game 12', 'Game 13', 'Game 14', 'Game 15', 'Game 16'])


# Player Selection Page
@app.route('/analysis-home/playerSelection')
def playerSelection():
    return render_template('playerSelection.html')


if __name__ == '__main__':
 app.run(debug=True, use_reloader=True)