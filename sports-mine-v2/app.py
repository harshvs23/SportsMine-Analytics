from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import plotly.express as px
import numpy as np


app = Flask(__name__)
app.secret_key = "secret key"

def load_ufc():
    df = pd.read_csv(r"C:\Users\LENOVO\Documents\sports\processed\UFC.csv")
    return df

def new_co(odi):
    if odi['Region1'] is not None:
        if odi['Region1'].isupper():
            if (odi.Region1=='ICC'):
                return odi['Region2']
            else:
                return odi['Region1']
                
        elif odi['Region'] is not None:
            if odi['Region'].isupper():
                if odi['Region'] is not "ICC":
                    return odi['Region']
            else:
                return odi['Region2']
        else:
                return odi['Region2']
    else:
        return "NA"

def new_co(t20):
    if t20['Region1'] is not None:
        if t20['Region1'].isupper():
            if (t20.Region1=='ICC'):
                return t20['Region2']
            else:
                return t20['Region1']
                
        elif t20['Region'] is not None:
            if t20['Region'].isupper():
                if t20['Region'] is not "ICC":
                    return t20['Region']
            else:
                return t20['Region2']
        else:
                return t20['Region2']
    else:
        return "NA"
    
def extract_country(player):
    if '(' in player:
        country = player.split('(')[1].strip()
        country = country.replace(')', '')
        country = country.replace('ICC/', '')
        return country
    else:
        country = np.nan
        return country

def clean_player(player):
    if '(' in player:
        player = player.split('(')[0].strip()
    return player

# creating a new column known as final region
def new_co(bowling_odi):
    if bowling_odi['Region1'] is not None:
        if bowling_odi['Region1'].isupper():
            if (bowling_odi.Region1=='ICC'):
                return bowling_odi['Region2']
            else:
                return bowling_odi['Region1']
                
        elif bowling_odi['Region'] is not None:
            if bowling_odi['Region'].isupper():
                if bowling_odi['Region'] is not "ICC":
                    return bowling_odi['Region']
            else:
                return bowling_odi['Region2']
        else:
                return bowling_odi['Region2']
    else:
        return "NA"
# creating a new column known as final region
def new_co(bowling_t20):
    if bowling_t20['Region1'] is not None:
        if bowling_t20['Region1'].isupper():
            if (bowling_t20.Region1=='ICC'):
                return bowling_t20['Region2']
            else:
                return bowling_t20['Region1']
                
        elif bowling_t20['Region'] is not None:
            if bowling_t20['Region'].isupper():
                if bowling_t20['Region'] is not "ICC":
                    return bowling_t20['Region']
            else:
                return bowling_t20['Region2']
        else:
                return bowling_t20['Region2']
    else:
        return "NA"
def extract_country(player):
    if '(' in player:
        country = player.split('(')[1].strip()
        country = country.replace(')', '')
        country = country.replace('ICC/', '')
        return country
    else:
        country = np.nan
        return country

def clean_player(player):
    if '(' in player:
        player = player.split('(')[0].strip()
    return player

   
# creating a new column known as final region
def new_co(fielding_odi):
    if fielding_odi['Region1'] is not None:
        if fielding_odi['Region1'].isupper():
            if (fielding_odi.Region1=='ICC'):
                return fielding_odi['Region2']
            else:
                return fielding_odi['Region1']
                
        elif fielding_odi['Region'] is not None:
            if fielding_odi['Region'].isupper():
                if fielding_odi['Region'] is not "ICC":
                    return fielding_odi['Region']
            else:
                return fielding_odi['Region2']
        else:
                return fielding_odi['Region2']
    else:
        return "NA"
# creating a new column known as final region
def new_co(fielding_t20):
    if fielding_t20['Region1'] is not None:
        if fielding_t20['Region1'].isupper():
            if (fielding_t20.Region1=='ICC'):
                return fielding_t20['Region2']
            else:
                return fielding_t20['Region1']
                
        elif fielding_t20['Region'] is not None:
            if fielding_t20['Region'].isupper():
                if fielding_t20['Region'] is not "ICC":
                    return fielding_t20['Region']
            else:
                return fielding_t20['Region2']
        else:
                return fielding_t20['Region2']
    else:
        return "NA"
def extract_country(player):
    if '(' in player:
        country = player.split('(')[1].strip()
        country = country.replace(')', '')
        country = country.replace('ICC/', '')
        return country
    else:
        country = np.nan
        return country

def clean_player(player):
    if '(' in player:
        player = player.split('(')[0].strip()
    return player


def load_odi():
    odi = pd.read_csv('processed\ODI_data.csv')
    odi = odi.drop(['Unnamed: 0', 'Unnamed: 13'], axis=1)
    #remove ( from column player and split into region column)
    odi[['Player', 'Region']] = odi['Player'].str.split("(", n=1, expand=True)
    #removing ) from region column
    odi['Region'] = odi['Region'].map(lambda x: x.rstrip(')'))
    #split span column into start and end year
    odi[['Start', 'End']] = odi['Span'].str.split("-", n=1, expand=True)
    #split region column into region1 and region2
    odi[['Region1', 'Region']] = odi['Region'].str.split("/", n=1, expand=True)
    #split region1 column into region2
    odi[['Region2', 'Region']] = odi['Region'].str.split("/", n=1, expand=True)
    odi['Final Region'] = odi.apply(new_co, axis=1)
    #drop region1, region2, region columns
    odi = odi.drop(["Region1", "Region2", "Region"], axis=1)
    odi = odi.drop([2148, 949])
    odi=odi[odi['Final Region'].isnull()==False]
    odi["HS"] = odi["HS"].str.replace('*', '')
    #replacing - with 0 in odi data
    odi.replace('-', 0, inplace=True)
    #Change datatype of Runs, Ave, HS, and SR to floats
    odi[['Runs', 'Ave', 'HS', 'SR']] = odi[['Runs', 'Ave', 'HS', 'SR']].astype('float')
    return odi

def load_data2():
    t20 = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\t20.csv')
    #delete unnamed: 0 column
    t20 = t20.drop(['Unnamed: 0', 'Unnamed: 15'], axis=1)
    #remove ( from column player and split into region column)
    t20[['Player', 'Region']] = t20['Player'].str.split("(", n=1, expand=True)
    #removing ) from region column
    t20['Region'] = t20['Region'].map(lambda x: x.rstrip(')'))
    #split span column into start and end year
    t20[['Start', 'End']] = t20['Span'].str.split("-", n=1, expand=True)
    #split region column into region1 and region2
    t20[['Region1', 'Region']] = t20['Region'].str.split("/", n=1, expand=True)
    #split region1 column into region2
    t20[['Region2', 'Region']] = t20['Region'].str.split("/", n=1, expand=True)
    t20['Final Region'] = t20.apply(new_co, axis=1)
    #drop region1, region2, region columns
    t20 = t20.drop(["Region1", "Region2", "Region"], axis=1)
    #Rmoving data of East African Region 
    t20=t20[t20['Final Region'].isnull()==False]
    t20["HS"] = t20["HS"].str.replace('*', '')
    t20.replace('-', 0, inplace=True)
    #Change datatype of Runs, Ave, HS, and SR to floats
    t20[['Runs', 'Ave', 'HS', 'SR']] = t20[['Runs', 'Ave', 'HS', 'SR']].astype('float')
    t20.groupby('Final Region').mean().sort_values('Mat').tail(10)
    return t20

def load_data3():
   
   test = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\test.csv')
   #delete unnamed: 0 column
   test = test.drop(['Unnamed: 0', 'Unnamed: 11'], axis=1)
   #split span column into start and end year
   test[['Start', 'End']] = test['Span'].str.split("-", n=1, expand=True)
   test['Final Region'] = test['Player'].apply(extract_country)
   test['Player'] = test['Player'].apply(clean_player)
   #Rmoving data of East African Region 
   test=test[test['Final Region'].isnull()==False]
   #removing * from HS column
   test["HS"] = test["HS"].str.replace('*', '')
   #replacing - with 0 in t20 data
   test.replace('-', 0, inplace=True)
   #Change datatype of Runs, Ave, HS, and Inns to floats
   test[['Runs', 'Ave', 'HS', 'Inns']] = test[['Runs', 'Ave', 'HS', 'Inns']].astype('float')
   return test
   
   

def load_data4():
    bowling_odi = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\Bowling_ODI.csv')
    #delete unnamed: 0 column
    bowling_odi = bowling_odi.drop(['Unnamed: 0', 'Unnamed: 13'], axis=1)
    #remove ( from column player and split into region column)
    bowling_odi[['Player', 'Region']] = bowling_odi['Player'].str.split("(", n=1, expand=True)
    #removing ) from region column
    bowling_odi['Region'] = bowling_odi['Region'].map(lambda x: x.rstrip(')'))
    #split span column into start and end year
    bowling_odi[['Start', 'End']] = bowling_odi['Span'].str.split("-", n=1, expand=True)
    #split region column into region1 and region2
    bowling_odi[['Region1', 'Region']] = bowling_odi['Region'].str.split("/", n=1, expand=True)
    #split region1 column into region2
    bowling_odi[['Region2', 'Region']] = bowling_odi['Region'].str.split("/", n=1, expand=True)
    #drop region1, region2, region columns
    bowling_odi = bowling_odi.drop(["Region1", "Region2", "Region"], axis=1)
    #Rmoving data of East African Region 
    bowling_odi=bowling_odi[bowling_odi['Final Region'].isnull()==False]
    #replacing - with 0 in t20 data
    bowling_odi.replace('-', 0, inplace=True)
    #Change datatype of Runs, Ave, HS, and SR to floats
    bowling_odi[['Balls', 'Runs', 'Wkts', 'SR']] = bowling_odi[['Balls', 'Runs', 'Wkts', 'SR']].astype('float')
    bowling_odi.groupby('Final Region').mean().sort_values('Mat').tail(10)

    return bowling_odi

def load_data5():
    bowling_t20 = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\Bowling_t20.csv')
    #delete unnamed: 0 column
    bowling_t20 = bowling_t20.drop(['Unnamed: 0', 'Unnamed: 14'], axis=1)
    #remove ( from column player and split into region column)
    bowling_t20[['Player', 'Region']] = bowling_t20['Player'].str.split("(", n=1, expand=True)
    #removing ) from region column
    bowling_t20['Region'] = bowling_t20['Region'].map(lambda x: x.rstrip(')'))
    #split span column into start and end year
    bowling_t20[['Start', 'End']] = bowling_t20['Span'].str.split("-", n=1, expand=True)
    #split region column into region1 and region2
    bowling_t20[['Region1', 'Region']] = bowling_t20['Region'].str.split("/", n=1, expand=True)
    #split region1 column into region2
    bowling_t20[['Region2', 'Region']] = bowling_t20['Region'].str.split("/", n=1, expand=True)
    #drop region1, region2, region columns
    bowling_t20 = bowling_t20.drop(["Region1", "Region2", "Region"], axis=1)
    #Rmoving data of East African Region 
    bowling_t20=bowling_t20[bowling_t20['Final Region'].isnull()==False]
    #replacing - with 0 in t20 data
    bowling_t20.replace('-', 0, inplace=True)
    #Change datatype of Runs, Ave, HS, and SR to floats
    bowling_t20[['Overs', 'Runs', 'Wkts', 'SR']] = bowling_t20[['Overs', 'Runs', 'Wkts', 'SR']].astype('float')
    bowling_t20.groupby('Final Region').mean().sort_values('Mat').tail(10)
    return bowling_t20

def load_data6():
    bowling_test = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\Bowling_test.csv')
    #delete unnamed: 0 column
    bowling_test = bowling_test.drop(['Unnamed: 0', 'Unnamed: 14'], axis=1)
    #split span column into start and end year
    bowling_test[['Start', 'End']] = bowling_test['Span'].str.split("-", n=1, expand=True)
    #Rmoving data of East African Region 
    bowling_test=bowling_test[bowling_test['Final Region'].isnull()==False]
    #replacing - with 0 in t20 data
    bowling_test.replace('-', 0, inplace=True)
    bowling_test.groupby('Final Region').mean().sort_values('Mat').tail(10)
    bowling_test['Final Region'] = bowling_test['Player'].apply(extract_country)
    bowling_test['Player'] = bowling_test['Player'].apply(clean_player) 
    return bowling_test

def load_data7():
    fielding_odi = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\Fielding_ODI.csv')
    #delete unnamed: 0 column
    fielding_odi = fielding_odi.drop(['Unnamed: 0', 'Unnamed: 11'], axis=1)
    #remove ( from column player and split into region column)
    fielding_odi[['Player', 'Region']] = fielding_odi['Player'].str.split("(", n=1, expand=True)
    #removing ) from region column
    fielding_odi['Region'] = fielding_odi['Region'].map(lambda x: x.rstrip(')'))
    #split span column into start and end year
    fielding_odi[['Start', 'End']] = fielding_odi['Span'].str.split("-", n=1, expand=True)
    #split region column into region1 and region2
    fielding_odi[['Region1', 'Region']] = fielding_odi['Region'].str.split("/", n=1, expand=True)
    #split region1 column into region2
    fielding_odi[['Region2', 'Region']] = fielding_odi['Region'].str.split("/", n=1, expand=True)
    #drop region1, region2, region columns
    fielding_odi = fielding_odi.drop(["Region1", "Region2", "Region"], axis=1)
    #Rmoving data of East African Region 
    fielding_odi=fielding_odi[fielding_odi['Final Region'].isnull()==False]
    #replacing - with 0 in t20 data
    fielding_odi.replace('-', 0, inplace=True)
    fielding_odi.groupby('Final Region').mean().sort_values('Mat').tail(10)
    return fielding_odi

def load_data8():
    fielding_t20 = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\Fielding_t20.csv')
    #delete unnamed: 0 column
    fielding_t20 = fielding_t20.drop(['Unnamed: 0', 'Unnamed: 11'], axis=1)
    #remove ( from column player and split into region column)
    fielding_t20[['Player', 'Region']] = fielding_t20['Player'].str.split("(", n=1, expand=True)
    #removing ) from region column
    fielding_t20['Region'] = fielding_t20['Region'].map(lambda x: x.rstrip(')'))
    #split span column into start and end year
    fielding_t20[['Start', 'End']] = fielding_t20['Span'].str.split("-", n=1, expand=True)
    #split region column into region1 and region2
    fielding_t20[['Region1', 'Region']] = fielding_t20['Region'].str.split("/", n=1, expand=True)
    #split region1 column into region2
    fielding_t20[['Region2', 'Region']] = fielding_t20['Region'].str.split("/", n=1, expand=True)
    #drop region1, region2, region columns
    fielding_t20 = fielding_t20.drop(["Region1", "Region2", "Region"], axis=1)
    #Rmoving data of East African Region 
    fielding_t20=fielding_t20[fielding_t20['Final Region'].isnull()==False]
    #replacing - with 0 in t20 data
    fielding_t20.replace('-', 0, inplace=True)
    #Change datatype of Runs, Ave, HS, and SR to floats
    fielding_t20[['Mat', 'Inns', 'Dis', 'Ct']] = fielding_t20[['Mat', 'Inns', 'Dis', 'Ct']].astype('float')
    fielding_t20.groupby('Final Region').mean().sort_values('Mat').tail(10)
    return fielding_t20

def load_data9():
    fielding_test = pd.read_csv(r'C:\Users\LENOVO\Documents\sports\processed\Fielding_test.csv')
    #delete unnamed: 0 column
    fielding_test = fielding_test.drop(['Unnamed: 0', 'Unnamed: 11'], axis=1)
    #split span column into start and end year
    fielding_test[['Start', 'End']] = fielding_test['Span'].str.split("-", n=1, expand=True)
    #Rmoving data of East African Region 
    fielding_test=fielding_test[fielding_test['Final Region'].isnull()==False]
    #replacing - with 0 in t20 data
    fielding_test.replace('-', 0, inplace=True)
    fielding_test.groupby('Final Region').mean().sort_values('Mat').tail(10)
    fielding_test['Final Region'] = fielding_test['Player'].apply(extract_country)
    fielding_test['Player'] = fielding_test['Player'].apply(clean_player)
    return fielding_test




@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/graph/1')
def graph_1():
    odi = load_odi()
    fig1 = px.bar(odi, x="Final Region", y="HS", color="Final Region", title="Matches played by each region"
       , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
       labels={"Final Region": "Region", "HS": "Matches Played"})

    
    fig2 = px.pie(odi, values='HS', names='Final Region', title='Region Wise High Score',
        color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
    
    fig3 = px.bar_polar(odi, r='HS', theta='Final Region', color='Final Region', template='plotly_dark', title='Region Wise High Score',
             color_discrete_sequence=px.colors.sequential.Plasma_r, width=800, height=800)

    fig4 = px.line(odi, x='Final Region', y='HS', color='Final Region', title='Region Wise High Score', 
     color_discrete_sequence=px.colors.sequential.Plasma_r, width=800, height=800,
     labels={'Final Region':'Region', 'HS':'High Score'})
    
    fig5 = px.scatter(odi, x="HS", y="Player", animation_frame="End", animation_group="Final Region",
           size="Runs", color="Final Region", hover_name="Final Region",
           log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000, width=1000, title='High Score vs Player',
           template='plotly_dark')
    
    fig6 = px.scatter_matrix(odi, dimensions=["HS", "Runs", "Ave", "SR"], color="Final Region", 
                  height=1000, width=1000, title='Scatter Matrix', hover_name="Player", hover_data=["Player"])

    return render_template('graph1.html', 
                           fig1= fig1.to_html(),
                           fig2= fig2.to_html(),
                           fig3= fig3.to_html(),
                           fig4= fig4.to_html(),
                           fig5= fig5.to_html(),
                           fig6= fig6.to_html())

@app.route('/ufc')
def load_ufc():
    return render_template('ufc.html')  

@app.route('/football')
def load_foot():
    return render_template('football.html')



@app.route('/cricket', methods=['GET', 'POST'])
def cricket():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'bat_odi':
            odi = load_odi()
            #plotting
            fig1 = px.bar(odi, x="Final Region", y="HS", color="Final Region", title="Matches played by each region",
                     color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig2 = px.pie(odi, values='HS', names='Final Region', title='Region Wise High Score',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig3 = px.bar_polar(odi[:40], r='Runs', theta='Player', color='Player', template='plotly_dark', title='Runs Scored by each player',
                    color_discrete_sequence=px.colors.sequential.Plasma_r, width=1000, height=800)
            fig4 = px.scatter(odi, x="HS", y="Player", animation_frame="End", animation_group="Final Region",
                    size="Runs", color="Final Region", hover_name="Final Region",
                    log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000, width=1000, title='High Score vs Player',
                    template='plotly_dark')
            fig5 = px.sunburst(odi[:100], path=['Final Region','Player'], values='HS')
            fig6 = px.treemap(odi, path=['Final Region', 'Player', 'Mat'], values='Runs',
                    color='Inns', hover_data=['HS'])
            fig7 = px.bar(odi[:50], x="Player", y="100", color="Final Region",
                    pattern_shape="Mat", pattern_shape_sequence=[".", "x", "+"])
            return render_template('cricket.html',
                                choice = "Batting ODI Stats",
                                fig1= fig1.to_html(),
                                fig2= fig2.to_html(),
                                fig3= fig3.to_html(),
                                fig4= fig4.to_html(),
                                fig5= fig5.to_html(),
                                fig6= fig6.to_html(),
                                fig7= fig7.to_html())
        elif choice == 'bat_t20':
            t20 = load_data2()
            fig8 = px.bar(t20, x="Final Region", y="HS", color="Final Region", title="Matches played by each region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig9 = px.pie(t20[:50], values='HS', names='Final Region', title='Region Wise High Score',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig10 = px.scatter(t20, x="HS", y="Player", animation_frame="Start", animation_group="Final Region",
                    size="Runs", color="Final Region", hover_name="Final Region",
                    log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000)
            fig11 = px.sunburst(t20[:100], path=['Final Region','Player'], values='HS', hover_data='Runs')
            fig12 = px.treemap(t20, path=['Final Region', 'Player', 'Mat'], values='Runs',
                    color='Inns', hover_data=['HS'])
            return render_template('cricket.html',
                                   choice = "Batting T20 Stats",
                                    fig8= fig8.to_html(),
                                    fig9= fig9.to_html(),
                                    fig10= fig10.to_html(),
                                    fig11= fig11.to_html(),
                                    fig12= fig12.to_html())

        elif choice == 'bat_test':
            test = load_data3()
            fig13 = px.bar(test, x="Final Region", y="HS", color="Final Region", title="Matches played by each region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig14 = px.pie(test, values='HS', names='Final Region', title='Region Wise High Score',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig15 = px.scatter(test, x="HS", y="Player", animation_frame="End", animation_group="Final Region",
                    size="Runs", color="Final Region", hover_name="Final Region",
                    log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000, width=1000, title='High Score vs Player',
                    template='plotly_dark')
            fig16 = px.sunburst(test[:100], path=['Final Region','Player'], values='HS', hover_data='Runs')
            return render_template('cricket.html',
                                   choice = "Batting Test Stats",
                                    fig13= fig13.to_html(),
                                    fig14= fig14.to_html(),
                                    fig15= fig15.to_html(),
                                    fig16= fig16.to_html())
        elif choice == 'bowl_odi':
            bowling_odi = load_data4()
            fig17 = px.bar(bowling_odi.head(50), x="Player", y="Wkts", color="Player", title="wickets taken by each player in the region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig18 = px.pie(bowling_odi, values='Wkts', names='Final Region', title='wickets taken by each player in the region',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig19 = px.scatter(bowling_odi, x="Wkts", y="Player", animation_frame="End", animation_group="Final Region",
                    size="Runs", color="Final Region", hover_name="Final Region",
                    log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000)
            fig20 = px.sunburst(bowling_odi[:100], path=['Final Region','Player'], values='Wkts', hover_data='Balls')
            fig21 = px.treemap(bowling_odi, path=['Final Region', 'Player', 'Balls'], values='Mat',
                    color='Wkts', hover_data=['Runs'])
            return render_template('cricket.html',
                                   choice = "Bowling ODI Stats",
                                    fig17= fig17.to_html(),
                                    fig18= fig18.to_html(),
                                    fig19= fig19.to_html(),
                                    fig20= fig20.to_html(),
                                    fig21= fig21.to_html())
        elif choice == 'bowl_t20':
            bowling_t20 = load_data5()
            fig22 = px.bar(bowling_t20.head(50), x="Player", y="Wkts", color="Player", title="wickets taken by each player in the region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig23 = px.pie(bowling_t20[:50], values='Wkts', names='Player', title='Percentage of wickets taken by each country ',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig24 = px.scatter(bowling_t20, x="Wkts", y="Player", animation_frame="End", animation_group="Final Region",
                    size="Runs", color="Final Region", hover_name="Final Region",
                    log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000)
            return render_template('cricket.html',
                                   choice = "Bowling T20 Stats",
                                    fig22= fig22.to_html(),
                                    fig23= fig23.to_html(),
                                    fig24= fig24.to_html())
        elif choice == 'bowl_test':
            bowling_test = load_data6()
            fig25 = px.bar(bowling_test, x="Player", y="Wkts", color="Player", title="wickets taken by each player in the region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig26 = px.pie(bowling_test, values='Wkts', names='Final Region', title='Percentage of wickets taken by each country ',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig27 = px.sunburst(bowling_test[:100], path=['Final Region','Player'], values='Wkts', hover_data='Balls')
            fig28 = px.treemap(bowling_test, path=['Final Region', 'Player', 'Balls'], values='Mat',
                  color='Wkts', hover_data=['Runs'])
            return render_template('cricket.html',
                                   choice = "Bowling Test Stats",
                                    fig25= fig25.to_html(),
                                    fig26= fig26.to_html(),
                                    fig27= fig27.to_html(),
                                    fig28= fig28.to_html())
        elif choice == 'fielding_odi':
            fielding_odi = load_data7()
            fig29 = px.bar(fielding_odi, x="Player", y="Dis", color="Player", title="wickets taken by each fielder in the region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig30 = px.pie(fielding_odi, values='Dis', names='Final Region', title='wickets taken by each fielder in the region',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig31 = px.sunburst(fielding_odi[:100], path=['Final Region','Player'], values='Dis', hover_data='Inns')
            fig32 = px.treemap(fielding_odi, path=['Final Region', 'Player', 'Dis'], values='Ct',
                    color='Inns', hover_data=['Ct Wk'])
            fig33 = px.area(fielding_odi, x="Final Region", y="Mat", color="Inns", line_group="Ct")
            return render_template('cricket.html',
                                   choice = "Fielding ODI Stats",
                                    fig29= fig29.to_html(),
                                    fig30= fig30.to_html(),
                                    fig31= fig31.to_html(),
                                    fig32= fig32.to_html(),
                                    fig33= fig33.to_html())
        elif choice == 'fielding_t20':
            fielding_t20 = load_data8()
            fig34 = px.bar(fielding_t20.head(50), x="Player", y="Dis", color="Player", title="wickets taken by each fielder in the region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig35 = px.pie(fielding_t20[:100], values='Dis', names='Final Region', title='wickets taken by each fielder in the region',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig36 = px.scatter(fielding_t20, x="Dis", y="Player", animation_frame="End", animation_group="Final Region",
                    size="Mat", color="Final Region", hover_name="Final Region",
                    log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000)
            fig37 = px.sunburst(fielding_t20[:100], path=['Final Region','Player'], values='Dis', hover_data='Inns')
            fig38 = px.area(fielding_t20, x="Final Region", y="Mat", color="Inns", line_group="Ct Wk")
            return render_template('cricket.html',
                                   choice = "Fielding T20 Stats",
                                    fig34= fig34.to_html(),
                                    fig35= fig35.to_html(),
                                    fig36= fig36.to_html(),
                                    fig37= fig37.to_html(),
                                    fig38= fig38.to_html())
        elif choice == 'fielding_test':
            fielding_test = load_data9()
            fig39 = px.bar(fielding_test.head(50), x="Player", y="Dis", color="Player", title="wickets taken by each fielder in the region"
                    , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
                    labels={"Final Region": "Region", "HS": "Matches Played"})
            fig40 = px.pie(fielding_test[:100], values='Dis', names='Final Region', title='wickets taken by each fielder in the region',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
            fig41 = px.sunburst(fielding_test[:100], path=['Final Region','Player'], values='Dis', hover_data='Inns')
            fig42 = px.area(fielding_test, x="Final Region", y="Mat", color="Inns", line_group="Ct")
            return render_template('cricket.html',
                                   choice = "Fielding Test Stats",
                                    fig39= fig39.to_html(),
                                    fig40= fig40.to_html(),
                                    fig41= fig41.to_html(),
                                    fig42= fig42.to_html())
        

    return render_template('cricket.html')   


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 