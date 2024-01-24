# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 21:23:50 2021

@author: amrit
"""

#when we import hydralit, we automatically get all of Streamlit
import hydralit as hy
import streamlit as st
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.dates as mdates 
import pdfkit
#from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
from streamlit.components.v1 import iframe
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
from csv import reader
from csv import DictReader
#from pages import utils
import calendar
import base64
import plotly.io as pio
#pio.kaleido.scope.default_format = "png"
#import wkhtmltopdf as html
from pdfkit.api import configuration
import glob
from scipy.optimize import fsolve
import csv
#import html_script
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import datetime
import matplotlib.dates as mdates
from PIL import  Image
import hydralit_components as hc
import emoji
import string
import json
import webbrowser
xformatter = mdates.DateFormatter('%H:%M') # for time axis plots
st.set_option('deprecation.showPyplotGlobalUse', False)

icon=Image.open('images/data-analytics.png')
st.set_page_config(page_icon=icon,layout="wide",page_title="kPVIZ : Solar Data Visualization App")




# Title of the main page

display = Image.open('logo.png')
display = np.array(display)
col1, col2,col3 = st.columns((0.1,.6,1.3))
col2.image(display, width = 400)
col3.write(f'<p style="background-color:#003399;color:#FFFFFF;text-align:center;padding:0.7rem;font-size:36px;border-radius:10px 10px 10px 10px;"><b>Solar Data Analytics Dashboard App</b></p>', unsafe_allow_html=True)
app = hy.HydraApp(title='kPVIZ : Solar Data Visualization App',hide_streamlit_markers=True,use_navbar=True, navbar_sticky=True)
#st.write('\n')
#st.write('\n')
#st.write('\n')
#st.write('\n')

@app.addapp(is_home=True)

def home():
    padding_top=0
    m="""<style>
        .appview-container .main .block-container{{
            padding-top: {padding_top}rem;    }}
    </style>
    """

    st.markdown(m, unsafe_allow_html=True)
    def set_bg_hack(main_bg):
        '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
        '''
    # set bg name
        main_bg_ext = "images/home6.png"
        
        st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
#image=Image.open('home.jpg')    
    set_bg_hack('images/home7.png')
    
    
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)


    lottie_banner = load_lottiefile("countryside.json")  # replace link to local lottie file
    lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
    lottie_report=load_lottiefile("stats.json")
    lottie_data=load_lottiefile("sunwise.json")
    lottie_graph=load_lottiefile("graph.json")
    lottie_fin=load_lottiefile("fin.json")
    lottie_stat=load_lottiefile("data3.json")
    lottie_line=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_rWaqBk.json")
    lottie_8760=load_lottiefile("8760_1.json")
    
    p=st.markdown("""
                    <head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.responsive {
  width: 100%;
  height: auto;
}
</style>
</head>
<body> """
                    , unsafe_allow_html=True)  
    
    
    #top row
    col0,col1,col2,col3=st.columns((.1,1.3,1.3,1.3))
    col1.write(f'<p style="background-color:#FFFFFF;color:#0E284A;text-align:left;box-shadow: 1px 1px 1px 2px grey;padding:0.8rem;font-size:4px;border-radius:7px;"><span style="font-size: 10px;">&emsp;</span><br><span style="font-size: 70px;"><b>kPVIZ - <b></span><br><span style="font-size: 30px;">Solar Data <u><i>Dashboard</i></u> App</span><br><span style="font-size: 30px;">&emsp;</span></p>', unsafe_allow_html=True)
    
    #col2.image('images/8760.png')
    
    file_ = open("images/8760 - copy.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
        
    
    col2.write(f'<p style="background-color:#FFFFFF;color:#FFFFFF;text-align:center;box-shadow: 1px 1px 1px 2px grey;padding:0.3rem;border-radius:7px 7px 7px 7px;"><img src="data:image/png;base64,{data_url}" alt="8760" class="responsive"></p>', unsafe_allow_html=True)
    
    #col3 image

    file_ = open("images/laptop_mock.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
      
        
    col3.write(f'<p style="background-color:#FFFFFF;color:#FFFFFF;text-align:center;box-shadow: 1px 1px 1px 2px grey;padding:0.3rem;border-radius:7px 7px 7px 7px;"><img src="data:image/png;base64,{data_url}" alt="laptop_mock" class="responsive"></p>', unsafe_allow_html=True)
    
    #col3.image('images/laptop_mock.png')
    st.write('\n')
    st.write('\n')
    st.write('\n')
   # st.write('\n')
    #st.write('\n')
    
    #button
    col0,col1,col2,col3=st.columns((1.45,0.55,0.55,1.45))
    b = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #22DAE1;
    color:#073274;
    }
</style>""", unsafe_allow_html=True)

    

    url1 = 'https://github.com/amritPVre'

    if col1.button('GitHub Repos'):
        webbrowser.open_new_tab(url1)
        
    url2 = 'https://www.linkedin.com/in/amritmandal/'

    if col2.button('Contact-Linkedin'):
        webbrowser.open_new_tab(url2)
    
    #seprartor
    #st_lottie(
    #lottie_line,speed=1,reverse=False,loop=True,quality="high",height=None,width=None,key=None,)
    st.write(f'<p style="background-color:#9CACC5;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:10px;border-radius:1px;"><b></b></p>', unsafe_allow_html=True)
    st.write('\n')
    
    #Row Three Heading
    col0,col1,col2,col3=st.columns((.1,1.3,1.3,1.3))
    col2.write(f'<p style="background-color:#FFFFFF;color:#0E284A;text-align:center;box-shadow: 1px 1px 1px 1px grey;padding:0.3rem;font-size:4px;border-radius:30px;"><span style="font-size: 40px;"><b><i>Top Features</i><b></span></p>', unsafe_allow_html=True)
    
    #row THREE
    col0,col1,col2,col3=st.columns((.1,1.3,1.3,1.3))
    with col3.container():
        st_lottie(
    lottie_fin,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    #renderer="svg", # canvas
    height=250,
    width=None,
    key=None,
    #background="transparent"
    )
    
    with col2.container():
        st_lottie(
    lottie_graph,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    #renderer="svg", # canvas
    height=250,
    width=None,
    key=None,
    )
    
    
    with col1.container():
        st_lottie(
    lottie_report,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    #renderer="svg", # canvas
    height=250,
    width=None,
    key=None,
    )
    
    #ROW THREE ICONS
    file_ = open("images/project.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
        
        
    col1.write(f'<p style="background-color:#FFFFFF;color:#FFFFFF;text-align:center;padding:0.3rem;font-size:13px;"><a href=""><img src="data:image/png;base64,{data_url}" alt="idea",width=400,height=600></a></p>', unsafe_allow_html=True)
    
    
    file_ = open("images/idea.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
        
        
    col2.write(f'<p style="background-color:#FFFFFF;color:#FFFFFF;text-align:center;padding:0.3rem;font-size:13px;"><a href=""><img src="data:image/png;base64,{data_url}" alt="idea",width=400,height=600></a></p>', unsafe_allow_html=True)
    
    file_ = open("images/cash-flow.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
        
        
    col3.write(f'<p style="background-color:#FFFFFF;color:#FFFFFF;text-align:center;padding:0.3rem;font-size:13px;"><a href=""><img src="data:image/png;base64,{data_url}" alt="idea",width=400,height=600></a></p>', unsafe_allow_html=True)
    
    
    
    col1_text=f"""
        <div id="wb_Text14" style="">
<ul style="font-size:12px;list-style-type:disc;box-shadow: 1px 1px 1px 1px grey;border-radius:7px 7px 7px 7px;padding:0.9rem;line-height: 2.1;">

<li style="margin:0 0 0 18px;"><b>Analytics Dashboard - Hourly to Monthly</b>
</li>
<li style="margin:0 0 0 18px;"><b>Analytics for all Main Solar Parameters</b>
</li>
<li style="margin:0 0 0 18px;"><b>Interactive Visualization of Dataset</b>
</li>
<li style="margin:0 0 0 18px;"><b>Complete EDA of Solar Dataset</b>
</li>
</ul>
</div>
"""
    col1.markdown(col1_text, unsafe_allow_html=True)
    
    
    
    col2_text=f"""
        <div id="wb_Text14" style="">
<ul style="font-size:12px;list-style-type:disc;box-shadow: 1px 1px 1px 1px grey;border-radius:7px 7px 7px 7px;padding:0.9rem;line-height: 2.1;">

<li style="margin:0 0 0 18px;"><b>Interactive Charts - Save as Image Option</b>
</li>
<li style="margin:0 0 0 18px;"><b>Download Daily & Monthly Data as .csv</b>
</li>
<li style="margin:0 0 0 18px;"><b>Graphs - GHI-GII, DC-AC Energy & Amb-PV Temp</b>
</li>
<li style="margin:0 0 0 18px;"><b>Correlation Matrix for Entire Dataset</b>
</li>
</ul>
</div>
"""
    col2.markdown(col2_text, unsafe_allow_html=True)

   
    col3_text=f"""
        <div id="wb_Text14" style="">
<ul style="font-size:12px;list-style-type:disc;box-shadow: 1px 1px 1px 1px grey;border-radius:7px 7px 7px 7px;padding:0.9rem;line-height: 2.1;">

<li style="margin:0 0 0 18px;"><b>Summary Dashboard with Finanacial Detail</b>
</li>
<li style="margin:0 0 0 18px;"><b>Financials Include IRR, NPV, SPP & Net CF</b>
</li>
<li style="margin:0 0 0 18px;"><b>Net CashFlow Statement for 25 Years</b>
</li>
<li style="margin:0 0 0 18px;"><b>Carbon Off-set Analytics</b>
</li>
</ul>
</div>
"""
    col3.markdown(col3_text, unsafe_allow_html=True)
    
    #top banner    
    st_lottie(
    lottie_banner,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    #renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
    )
    
    #st.write('\n')
    #st.write('\n')
    
    
    

@app.addapp(title='Upload Solar Data', icon="📁")
def upload_data():
    col1,col2,col3=st.columns((0.005,2.99,0.005))
    col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>Please Share the Solar Plant Data</b></p>', unsafe_allow_html=True)
    primaryColor = st.get_option("theme.primaryColor")
    s = f"""
    <style>
    div.stButton > button:first-child {{ border: 5px solid {primaryColor};background: linear-gradient(90deg, #2e0088, #3c0392, #4a089d, #570da7, #6513b1, #7218bb, #7f1dc6, #8d22d0);
                                                                                                      color:#ffffff; border-radius:5px 5px 5px 5px; }}
    div.stButton > button:hover {{background: #f95d6a;color:#003f5c}}
                                                                                                      
    <style>
    """
    st.markdown(s, unsafe_allow_html=True)
    Form_header='<p style="font-family:sans-serif; color:#663399; font-size: 16px;">The values in the below form are set as <strong><em>DEFAULT.</em></strong> Please <strong><em>UPDATE</em></strong> with your Project Specific Data</p>'
    st.markdown(Form_header, unsafe_allow_html=True)

          
    with st.form(key='columns_in_form'):
        col1,col2,col3 = st.columns(3)
        DC= col1.number_input('Plant DC Capacity (kWp):',value=12001.00,help='PV System Total Peak Capacity. Like [Total Modules]*[PV Module Watt peak]/[1000]. Ex.-3000*540/1000=1620kWp')
        AC= col1.number_input('Plant AC Capacity (kW):',value=10000.00, help='Total Capacity of All Inverters combined. Like if the plant has 10 nos of 100kW Inverters, then total AC Cap is (10*100)kW or 1000kW')
        Wp= col1.number_input('PV Module Watt Peak (Wp):',value=540.00,help='Mentioned in PV Module Datasheet. Max achievable power of the PV Module')
        co_eff= col1.number_input('PV Module Efficiency (%):',value=20,help='Mentioned in the PV Module Datasheet. ')
        Proj_cost=col1.number_input('Upfront Project Cost (in $ Millions):',value=12,help='Total Investment required to set-up the PV Plant in USD Millions.')
        tariff_type = col2.selectbox(
            "Please Select Power Transcation Type",
            ["Select an Option","PPA_Rate", "Grid Tariff"],
            index=0,help='Please select the type of Power Selling Model to the Utility Grid if it’s a grid-connected project. Like the pv system will only push excess power to grid after self-consumption as NET METERING at a certain pre-defined GRID TARIFF, OR the PV system will send all of it’s generated power to Grid as Utility scale power plant at a certain fixed PPA RATE',
            )
        power_rate=col2.number_input('Power Selling Rate/ Grid Tariff ($/kWh):',value=0.07,help='')
        OnM_Cost=col2.number_input('Yearly O&M Expense as %age of Upfront Project Cost(%):',value=2,help='Cost of Yearly Maintenance like regular cleaning, schedule plant-equipment check-up, Human-resources expenses, repair-damages etc.')
        Tariff_esc=col2.number_input('Yearly Escalation on Power Selling Rate (%):',value=0.5,help='At which rate the GRID TARIFF OR PPA RATE will increase every year')
        OnM_esc=col2.number_input('Yearly Escalation on O&M Expense (%):',value=0.5,help='At which rate the O&M expenses is planned to increase every year.')
        Company=col3.text_input('Your Company Name:',value="Solar Company")
        contact_person=col3.text_input('Your Full Name:',value="John Doe")
        e_mail_id=col3.text_input('Your e-mail id:')
        Country=col3.text_input('Country You are From:')
        
        col1,col2, col3,col4,col5,col6,col7 = st.columns(7)
        submitted = col4.form_submit_button('SUBMIT')
            
    if submitted==True:
        st.balloons()
        col1,col2, col3 = st.columns((0.92,1.16,0.92))
        col2.success("🎉 Your Inputs Have Been Saved! Now Please Upload Hourly Solar Data")
        st.write("\n")
        d1={'DC_Cap':[DC],
           'AC_Cap':[AC],
           'PV_Wp':[Wp],
           'Power_eff':[co_eff],
           'Proj_Cost':[Proj_cost],
           'Electricity_Tariff':[tariff_type],
           'Power_rate':[power_rate],
           'OnM':[OnM_Cost],
           'Tariff_Esc':[Tariff_esc],
           'OnM_Esc':[OnM_esc],
           'Company_Name':[Company],
           'Company_representative':[contact_person],
           'email_id':[e_mail_id],
           'Country':[Country]
           
           }
        dstore={'DC_Cap':[DC],
           'AC_Cap':[AC],
           'PV_Wp':[Wp],
           'Proj_Cost':[Proj_cost],
           'Electricity_Tariff':[tariff_type],
           'Power_rate':[power_rate],
           'OnM':[OnM_Cost],
           'Tariff_Esc':[Tariff_esc],
           'OnM_Esc':[OnM_esc],
           'Company_Name':[Company],
           'Company_representative':[contact_person],
           'email_id':[e_mail_id],
           'Country':[Country]
           
           }
        d1 = pd.DataFrame(data=d1)
        d1.to_csv('data/d1.csv', index=False)
        dstore=pd.DataFrame(data=dstore)
        
    
    else:
        
        col1, col2, col3=st.columns(3)
        Please_submit='<span style="color:#663399;font-family:Arial;font-size:22px;"><strong><em>Click </em></strong></span><span style="background-color:#2F6179;color:#FFFFFF;font-family:Arial;font-size:22px;"><strong><em>SUBMIT</em></strong></span><span style="color:#663399;font-family:Arial;font-size:22px;"><strong><em> to save form responses.</em></strong></span>'
        col2.markdown(Please_submit, unsafe_allow_html=True)
        col1, col2, col3=st.columns((0.5,2,0.5))
        Sample_data='<span style="color:#44546A;font-family:Arial;font-size:16px;"><strong><u>If You Donot Have Sufficient Data, Then Please Click Below to Evaluate the App WIth Pre-defined Data</u></strong></span>'
        col2.markdown(Sample_data, unsafe_allow_html=True)
        col1,col2,col3,col4,col5,col6,col7=st.columns(7)
        if col4.button("Sample Data"):
            data0=pd.read_csv('data/sample_data.csv')
            st.dataframe(data0)
        st.write("\n")
        return
        
    # Upload the dataset and save as csv
    col1, col2, col3=st.columns(3)
    col2.markdown("### Upload Hourly Solar Data file to Start") 
    st.write("\n")
    
    # Code to read a single file 
    col1,col2,col3=st.columns((0.75,1.5,0.75))
    uploaded_file = col2.file_uploader("Choose a file", type = ['csv', 'xlsx'])
    global data
    col1,col2,col3,col4,col5,col6,col7=st.columns(7)
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)
    pre_col=['date','GlobHor','GlobInc','DiffHor','EArray','E_Grid','T_Amb','TArray', 'IArray','UArray','ArrayON']
    instrc='<span style="color:#663399;font-family:Arial;font-size:29px;"><strong><em>Please Update your Data File as Per <a href="https://www.youtube.com/watch?v=elwW9ehCyT8&t=17s">Instruction</a></em></strong></span>'
    st.write('\n')
    st.write('\n')
    if col3.button("Load Data"):
        columns=data.columns.values.tolist()
        def commonelem_set(z, x):
            one = set(z)
            two = set(x)
            if (one == two):
                return ("There are common elements in both lists:", one & two)
            else:
                return (0)
  
        z = commonelem_set(pre_col, columns)
        if z==0:
            st.markdown(instrc, unsafe_allow_html=True)
        else:
            st.dataframe(data) 
            data.to_csv('data/main_data.csv', index=False)
        
    else:
        if col5.button("Sample Data"):
            data=pd.read_csv('data/sample_data.csv')
            st.dataframe(data)
            
    col1,col2,col3=st.columns((.75,1.5,.75))
    st.write('\n')
    st.write('\n')
    col2.write(f'<p style="background-color:#633A8F;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:7px 7px 7px 7px;">Format of Data Table : The Dataset <b>MUST</b> Contain These Below Columns</p>', unsafe_allow_html=True)
    ref_df=pd.DataFrame({'Columns Syntax':'Meaning of Column Syntax in Data file', 'date':'Date in dd/mm/yyyy hh:mm format', 'GlobHor':'Global Horizontal Irradiance (W/m\u00b2)',
                         'DiffHor': 'Diffuse horizontal Irradiance(W/m\u00b2)','GlobInc':'Global Irradiance on Module Surface(W/m\u00b2)',
                         'T_Amb':'Ambient Temperature (\u00b0C)','TArray':'PV Array Temperature(\u00b0C)',
                         'EArray':'DC Power(kW)','E_Grid':'AC Power Output(kW)',
                         'IArray':'Total DC System Current(A)','UArray':'DC String Voltage (V)',
                         'ArrayON':'System Operating Hours (Should be 1 for Hourly Values'
                         
                         },index =[0])
    ref_df=ref_df.set_index('Columns Syntax')
    pd.set_option("display.max_colwidth", -1)
    st.table(ref_df)
    
@app.addapp(title='EDA Dashboard', icon="💹")
def EDA():
    col1,col2,col3=st.columns((0.005,2.99,0.005))
    col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>Exploratory Data Analysis of Solar Data</b></p>', unsafe_allow_html=True)
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
        df=pd.read_csv('data/sample_data.csv')
        d=pd.read_csv('data/sample_d1.csv')
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)

        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        
        corrMatrix = df.corr()
        plt.figure(figsize=(21,7))
        fig_corr = sns.heatmap(corrMatrix,cmap="YlGnBu", annot=True).set(title=f'__Corelation Matrix Plot__')
        #plt.savefig("output.png")
        st.pyplot()
        st.write('\n')
        st.write('\n')
        
        col1,col2=st.columns((.72,1.28))
        corr_plot=f"""
        <div id="wb_Text14" style="">
<ul style="font-size:15px;list-style-type:disc;">
<li style="margin:0 0 0 24px;">Each square shows the correlation between the variables on each axis. Correlation ranges from -1 to +1. 
</li>
<li style="margin:0 0 0 24px;">Values closer to zero means there is no linear trend between the two variables. 
</li>
<li style="margin:0 0 0 24px;">The close to 1 the correlation is the more positively correlated they are.
</li>
<li style="margin:0 0 0 24px;">A correlation closer to -1 is similar, but instead of both increasing one variable will decrease as the other increases. 
</li>
<li style="margin:0 0 0 24px;">The diagonals are all 1, because those squares are correlating each variable to itself. 
</li>
<li style="margin:0 0 0 24px;">For the rest the larger the number and darker the color the higher the correlation between the two variables. 
</li>
</ul>
<p style="font-size:15px;">&nbsp;</p>
</div>
"""
        col2.markdown(corr_plot, unsafe_allow_html=True)
        #head='<span style="background-color:#44546A;color:#FFFFFF;font-family:Arial;font-size:32px;line-height:33px;"><strong>Corelation Matrix Plot of Solar <br>Project Related Parameters&nbsp;&nbsp;&nbsp;&nbsp;:</strong></span>'
        col1.markdown(f'<p style="background-color:#265A88;color:#FFFFFF;text-align:center;padding:0.7rem;font-size:36px;border-radius:10px 10px 10px 10px;"><b>Corelation Matrix Plot of Solar Project Related Parameters :</b></p>', unsafe_allow_html=True)
        st.markdown("----------------------------------------")

        col1,col2,col3=st.columns((0.05,2.9,0.05))
        
        fig = px.scatter_matrix(df1,
                                dimensions=["GlobInc", "GlobHor", "T_Amb", "TArray", "EArray", "E_Grid"],
                                color="E_Grid")
        fig.update_layout(title_text="<b>Statistical Analysis: Pair Plots for All The Input Parameters</b>", title_x=.7,
                  width=1260,
                  height=720)
        col2.plotly_chart(fig)
        col2.info(f'Pair Plot is an important tool for EDA. It helps to understand the distribution of a single variable and the relationship among TWO variables. Its a very very useful method for Trend Analysis like Operational Data of Solar PV Plants. Here, all the parameters plotted against each other. The COLOR Bar on right is for AC Power Output. And the Entire plotting is donw with in corelation with AC Power O/P because this is the main component in the entire analysis that means overall performance of any solar PV plant.')
        
    else:
        df=pd.read_csv('data/main_data.csv')
        d=pd.read_csv('data/d1.csv')
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        
        corrMatrix = df.corr()
        plt.figure(figsize=(21,7))
        fig_corr = sns.heatmap(corrMatrix,cmap="YlGnBu", annot=True).set(title=f'Corelation Matrix Plot')
        #plt.savefig("output.png")
        st.pyplot()
        st.write('\n')
        st.write('\n')
        
        col1,col2=st.columns((.72,1.28))
        corr_plot=f"""
        <div id="wb_Text14" style="">
<ul style="font-size:15px;list-style-type:disc;">
<li style="margin:0 0 0 24px;">Each square shows the correlation between the variables on each axis. Correlation ranges from -1 to +1. 
</li>
<li style="margin:0 0 0 24px;">Values closer to zero means there is no linear trend between the two variables. 
</li>
<li style="margin:0 0 0 24px;">The close to 1 the correlation is the more positively correlated they are.
</li>
<li style="margin:0 0 0 24px;">A correlation closer to -1 is similar, but instead of both increasing one variable will decrease as the other increases. 
</li>
<li style="margin:0 0 0 24px;">The diagonals are all 1, because those squares are correlating each variable to itself. 
</li>
<li style="margin:0 0 0 24px;">For the rest the larger the number and darker the color the higher the correlation between the two variables. 
</li>
</ul>
<p style="font-size:15px;">&nbsp;</p>
</div>
"""
        col2.markdown(corr_plot, unsafe_allow_html=True)
        #head='<span style="background-color:#44546A;color:#FFFFFF;font-family:Arial;font-size:32px;line-height:33px;"><strong>Corelation Matrix Plot of Solar <br>Project Related Parameters&nbsp;&nbsp;&nbsp;&nbsp;:</strong></span>'
        col1.markdown(f'<p style="background-color:#265A88;color:#FFFFFF;text-align:center;padding:0.7rem;font-size:36px;border-radius:10px 10px 10px 10px;"><b>Corelation Matrix Plot of Solar Project Related Parameters :</b></p>', unsafe_allow_html=True)
        st.markdown("----------------------------------------")

        col1,col2,col3=st.columns((0.05,2.9,0.05))
        
        fig = px.scatter_matrix(df1,
                                dimensions=["GlobInc", "GlobHor", "T_Amb", "TArray", "EArray", "E_Grid"],
                                color="E_Grid")
        fig.update_layout(title_text="<b>Statistical Analysis: Pair Plots for All The Input Parameters</b>", title_x=.7,
                  width=1260,
                  height=720)
        col2.plotly_chart(fig)
        
        col2.info(f'Pair Plot is an important tool for EDA. It helps to understand the distribution of a single variable and the relationship among TWO variables. Its a very very useful method for Trend Analysis like Operational Data of Solar PV Plants. Here, all the parameters plotted against each other. The COLOR Bar on right is for AC Power Output. And the Entire plotting is donw with in corelation with AC Power O/P because this is the main component in the entire analysis that means overall performance of any solar PV plant.')
 

@app.addapp(title='Hourly Analytics',icon='⏳')
def hourly():
    col1,col2,col3=st.columns((0.005,2.99,0.005))
    col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>Hourly Solar Data Analytics</b></p>', unsafe_allow_html=True)
    def info(url):
        st.markdown(f'<p style="background:#06a2bf;color:#06a2bf;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
        df=pd.read_csv('data/sample_data.csv')
        d=pd.read_csv('data/sample_d1.csv')
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        #Metrics-Backend
        df1_sum=df1.sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.0%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        
        cols1,cols2,cols4,cols5=st.columns(4)
        cols1.metric(label="Peak GHI(W/m\u00b2)",value="{:.2f}".format(df1.GlobHor.max()))
        cols2.metric(label="Peak GII(W/m\u00b2)",value="{:.2f}".format(df1.GlobInc.max()))
        #cols3.markdown(" ")
        cols4.metric(label="Ambient Temperature(\u00b0C)",value="Max: "+str(float("{:.1f}".format(df1.T_Amb.max())))+"\u00b0C",delta = "Min: "+str(float(df1.T_Amb.min()))+"\u00b0C", delta_color = 'inverse')
        cols5.metric(label="Module Temperature(\u00b0C)",value = "Max: "+str(float("{:.2f}".format(df1.TArray.max())))+"\u00b0C", delta = "Min: "+str(float("{:.2f}".format(df1.TArray.min())))+"\u00b0C", delta_color = 'inverse')
        
        #st.info('Info message')
        peak_ghi=value="{:.2f}".format(df1.GlobHor.max())
        peak_gii=value="{:.2f}".format(df1.GlobInc.max())
        Amb_max=value="{:.1f}".format(df1.T_Amb.max())
        Amb_min=value="{:.1f}".format(df1.T_Amb.min())
        Tpv_max=value="{:.2f}".format(df1.TArray.max())
        Tpv_min="{:.2f}".format(df1.TArray.min())
        
        
        
        
        

        
        col1,col2=st.columns(2)
        #Irradiance Graph
        fig1 = px.line(df1, y=["GlobInc", "GlobHor"],title='Hourly Solar Irradiance (W/m\u00b2) GII & GHI',width=620,height=460)
        fig1.update_layout(title_text='<b>Hourly Solar Irradiance (W/m\u00b2) GII & GHI</b>', title_x=0.5,
                   xaxis_title="Time (in HH:MM)",yaxis_title="Irradiance (W/m\u00b2)")
        col1.plotly_chart(fig1)
        
        #Temperature Graph
        fig2 = px.line(df1, y=["TArray", "T_Amb"],title='Hourly Temperature Distribution (\u00b0C) : Ambient & Module Temperature',width=620,height=460)
        fig2.update_layout(title_text='<b>Hourly Temperature Distribution (\u00b0C) : Ambient & Module Temperature</b>', title_x=0.5,
                   xaxis_title="Time",yaxis_title="Temperature (\u00b0C)")
        col2.plotly_chart(fig2)
        
        col1,col2=st.columns(2)
        col1.info(f'The __Hourly GHI Vs GII Plot__ shows the Comparison between Global Horizontal Irradiance(GHI) & Global Irradiance on Inclined/Module Surface(GII). The Values are available for 365 days with **ONE** hour interval, including operational & non-operational hours. Here, the highest value ever achieved in a year for **GHI** is **{peak_ghi}/w/m\u00b2** and for **GII** is **{peak_gii}/w/m\u00b2**')
        col2.info(f'The __Ambient & PV Array Surface Hourly Temperature Distribution__ through out the year plotted in this chart. The values of both Ambient(Operating & Non-Operating hours) & PV temperature (Only Operating Hours) are in __**ONE**__ Hour interval. Highest Ambient Temperature reached to __**{Amb_max}\u00b0C**__ & **{Tpv_max}\u00b0C** for PV Surface. Whereas the Lowest values were __**{Amb_min}\u00b0C**__ &  __**{Tpv_min}\u00b0C**__ respectively')
        
        #st.markdown("----------------------------------------")
        
        cols1,cols2,cols4,cols5=st.columns(4)
        cols1.metric(label="Max DC Power(kW)",value="{:.2f}".format(df1.EArray.max()))
        cols2.metric(label="Max AC Power(kW)",value="{:.2f}".format(df1.E_Grid.max()))
        #cols3.markdown(" ")
        cols4.metric(label="Total Plant Running Hours",value="{:.0f}".format(df1_sum.ArrayON))
        cols5.metric(label="Yearly Avg Amb Temperature(\u00b0C)",value ="{:.2f}".format(dfTamb.T_Amb.max())+"\u00b0C")
        
        
        max_p_DC=value="{:.2f}".format(df1.EArray.max())
        max_p_AC=value="{:.2f}".format(df1.E_Grid.max())
        max_p_delta=value="{:.2f}".format(df1.EArray.max()-df1.E_Grid.max())
        st.write(max_p_AC)
        
        colx,coly=st.columns(2)
        #E_Grid & EArray Graph
        figx = px.line(df1, y=["EArray", "E_Grid"],title='Hourly DC & AC Power(kW) Generation Over the Year',width=620,height=460)
        figx.update_layout(title_text='<b>Hourly DC & AC Power(kW) Generation Over the Year</b>', title_x=0.5,
                   xaxis_title="Time",yaxis_title="Power (kW)")
        colx.plotly_chart(figx)
        
        #E_Grid Vs GII Graph
        figy = px.scatter(df1,x="GlobInc", y="E_Grid",title='Hourly AC Power(kW) Vs GII (W/m\u00b2) Plot',width=620,height=460,color='TArray')
        figy.update_layout(title_text='<b>Hourly AC Power(kW) Vs GII (W/m\u00b2) Plot</b>', title_x=0.5,
                   xaxis_title="GII (W/m\u00b2)",yaxis_title="E_Grid (kW)")
        coly.plotly_chart(figy)
 
        col1,col2=st.columns(2)
        col1.info(f'**Hourly DC & AC Power(kW) Generation** for the entire time period in **ONE** Hour interval shows the Delta between them as power loss during the DC to AC conversion, Transmission & Down-time of the PV System. Any anomaly in AC side of the system can be very easily detected from this graph. The delta between **MAX** DC to AC power was **{max_p_delta}kW** which occured at the same time stamp.')
        col2.info(f'Above Pair Plot between **Hourly AC Power Production & GII** indicates the corelation between them. Higher the Value of GII, the Power generation Also incrases proportionately. If AC Power shows **0** even though there is a GII value exists for thatmoment, that means the PV Plant is **Under Maintenance** **OR** there must be certain **Power failure** on the **AC Side** of the System.')
 
    
    
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        colDC, colAC=st.columns(2)
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        #DC Power Distribution over the year
        figDC = px.scatter(df3x, x="TIME", y="EArray", title=f"<b>DC Power: Daily Distribution</b>", color = "DATE_STR",width=620,height=460)
        figDC.update_traces(marker=dict(size=5, opacity=0.7), selector=dict(mode='markers'))
        figDC.update_layout( title_x=0.5,xaxis_title="TIME OF THE DAY",yaxis_title="DC Power (kW)")
        colDC.plotly_chart(figDC)
        
        #DC Power Distribution over the year
        figAC = px.scatter(df3x, x="TIME", y="E_Grid", title=f"{'<b>AC Power: Daily Distribution</b>':^50}", color = "DATE_STR",width=620,height=460)
        figAC.update_traces(marker=dict(size=5, opacity=0.7), selector=dict(mode='markers'))
        figAC.update_layout( title_x=0.5,xaxis_title="TIME OF THE DAY",yaxis_title="AC Power (kW)")
        colAC.plotly_chart(figAC)
        
        
        col1,col2=st.columns(2)
        col1.info('The Daily Distribution Plot of **DC Power** depicts the concentration of DC Power Generation at Certain Hours of The Day. Here, It can be seen the most of Peak Generation happen during **10AM to 2PM** every day. Hence, this period is the **Peak Generation Hours** of the PV System.')
        col2.info('Similar to the **Daily DC Power Distribution Plot**, here the **AC Power Distribution** also shows the same kind of concentration in Power Generation. Here also, the Peak Generating Hours are **10AM to 2PM** every day. So, the **Peak Generation Hours** same for both **DC** & **AC** Power Generation.')
        
        
        

        
    else:
        df=pd.read_csv('data/main_data.csv')
        d=pd.read_csv('data/d1.csv')
        
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.0%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        
        cols1,cols2,cols4,cols5=st.columns(4)
        cols1.metric(label="Peak GHI(W/m\u00b2)",value="{:.2f}".format(df1.GlobHor.max()))
        cols2.metric(label="Peak GII(W/m\u00b2)",value="{:.2f}".format(df1.GlobInc.max()))
        #cols3.markdown(" ")
        cols4.metric(label="Ambient Temperature(\u00b0C)",value="Max: "+str(float("{:.1f}".format(df1.T_Amb.max())))+"\u00b0C",delta = "Min: "+str(float(df1.T_Amb.min()))+"\u00b0C", delta_color = 'inverse')
        cols5.metric(label="Module Temperature(\u00b0C)",value = "Max: "+str(float("{:.2f}".format(df1.TArray.max())))+"\u00b0C", delta = "Min: "+str(float("{:.2f}".format(df1.TArray.min())))+"\u00b0C", delta_color = 'inverse')
        
        #st.info('Info message')
        peak_ghi=value="{:.2f}".format(df1.GlobHor.max())
        peak_gii=value="{:.2f}".format(df1.GlobInc.max())
        Amb_max=value="{:.1f}".format(df1.T_Amb.max())
        Amb_min=value="{:.1f}".format(df1.T_Amb.min())
        Tpv_max=value="{:.2f}".format(df1.TArray.max())
        Tpv_min="{:.2f}".format(df1.TArray.min())
        
        
        
        
        

        
        col1,col2=st.columns(2)
        #Irradiance Graph
        fig1 = px.line(df1, y=["GlobInc", "GlobHor"],title='Hourly Solar Irradiance (W/m\u00b2) GII & GHI',width=620,height=460)
        fig1.update_layout(title_text='<b>Hourly Solar Irradiance (W/m\u00b2) GII & GHI</b>', title_x=0.5,
                   xaxis_title="Time (in HH:MM)",yaxis_title="Irradiance (W/m\u00b2)")
        col1.plotly_chart(fig1)
        
        #Temperature Graph
        fig2 = px.line(df1, y=["TArray", "T_Amb"],title='Hourly Temperature Distribution (\u00b0C) : Ambient & Module Temperature',width=620,height=460)
        fig2.update_layout(title_text='<b>Hourly Temperature Distribution (\u00b0C) : Ambient & Module Temperature</b>', title_x=0.5,
                   xaxis_title="Time",yaxis_title="Temperature (\u00b0C)")
        col2.plotly_chart(fig2)
        
        col1,col2=st.columns(2)
        col1.info(f'The __Hourly GHI Vs GII Plot__ shows the Comparison between Global Horizontal Irradiance(GHI) & Global Irradiance on Inclined/Module Surface(GII). The Values are available for 365 days with **ONE** hour interval, including operational & non-operational hours. Here, the highest value ever achieved in a year for **GHI** is **{peak_ghi}/w/m\u00b2** and for **GII** is **{peak_gii}/w/m\u00b2**')
        col2.info(f'The __Ambient & PV Array Surface Hourly Temperature Distribution__ through out the year plotted in this chart. The values of both Ambient(Operating & Non-Operating hours) & PV temperature (Only Operating Hours) are in __**ONE**__ Hour interval. Highest Ambient Temperature reached to __**{Amb_max}\u00b0C**__ & **{Tpv_max}\u00b0C** for PV Surface. Whereas the Lowest values were __**{Amb_min}\u00b0C**__ &  __**{Tpv_min}\u00b0C**__ respectively')
        
        #st.markdown("----------------------------------------")
        
        cols1,cols2,cols4,cols5=st.columns(4)
        cols1.metric(label="Max DC Power(kW)",value="{:.2f}".format(df1.EArray.max()))
        cols2.metric(label="Max AC Power(kW)",value="{:.2f}".format(df1.E_Grid.max()))
        #cols3.markdown(" ")
        cols4.metric(label="Total Plant Running Hours",value="{:.0f}".format(df1_sum.ArrayON))
        cols5.metric(label="Yearly Avg Amb Temperature(\u00b0C)",value ="{:.2f}".format(dfTamb.T_Amb.max())+"\u00b0C")
        
        
        max_p_DC=value="{:.2f}".format(df1.EArray.max())
        max_p_AC=value="{:.2f}".format(df1.E_Grid.max())
        max_p_delta=value="{:.2f}".format(df1.EArray.max()-df1.E_Grid.max())
        st.write(max_p_AC)
        
        colx,coly=st.columns(2)
        #E_Grid & EArray Graph
        figx = px.line(df1, y=["EArray", "E_Grid"],title='Hourly DC & AC Power(kW) Generation Over the Year',width=620,height=460)
        figx.update_layout(title_text='<b>Hourly DC & AC Power(kW) Generation Over the Year</b>', title_x=0.5,
                   xaxis_title="Time",yaxis_title="Power (kW)")
        colx.plotly_chart(figx)
        
        #E_Grid Vs GII Graph
        figy = px.scatter(df1,x="GlobInc", y="E_Grid",title='Hourly AC Power(kW) Vs GII (W/m\u00b2) Plot',width=620,height=460,color='TArray')
        figy.update_layout(title_text='<b>Hourly AC Power(kW) Vs GII (W/m\u00b2) Plot</b>', title_x=0.5,
                   xaxis_title="GII (W/m\u00b2)",yaxis_title="E_Grid (kW)")
        coly.plotly_chart(figy)
 
        col1,col2=st.columns(2)
        col1.info(f'**Hourly DC & AC Power(kW) Generation** for the entire time period in **ONE** Hour interval shows the Delta between them as power loss during the DC to AC conversion, Transmission & Down-time of the PV System. Any anomaly in AC side of the system can be very easily detected from this graph. The delta between **MAX** DC to AC power was **{max_p_delta}kW** which occured at the same time stamp.')
        col2.info(f'Above Pair Plot between **Hourly AC Power Production & GII** indicates the corelation between them. Higher the Value of GII, the Power generation Also incrases proportionately. If AC Power shows **0** even though there is a GII value exists for thatmoment, that means the PV Plant is **Under Maintenance** **OR** there must be certain **Power failure** on the **AC Side** of the System.')
 
    
    
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        colDC, colAC=st.columns(2)
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        #DC Power Distribution over the year
        figDC = px.scatter(df3x, x="TIME", y="EArray", title=f"<b>DC Power: Daily Distribution</b>", color = "DATE_STR",width=620,height=460)
        figDC.update_traces(marker=dict(size=5, opacity=0.7), selector=dict(mode='markers'))
        figDC.update_layout( title_x=0.5,xaxis_title="TIME OF THE DAY",yaxis_title="DC Power (kW)")
        colDC.plotly_chart(figDC)
        
        #DC Power Distribution over the year
        figAC = px.scatter(df3x, x="TIME", y="E_Grid", title=f"{'<b>AC Power: Daily Distribution</b>':^50}", color = "DATE_STR",width=620,height=460)
        figAC.update_traces(marker=dict(size=5, opacity=0.7), selector=dict(mode='markers'))
        figAC.update_layout( title_x=0.5,xaxis_title="TIME OF THE DAY",yaxis_title="AC Power (kW)")
        colAC.plotly_chart(figAC)
        
        
        col1,col2=st.columns(2)
        col1.info('The Daily Distribution Plot of **DC Power** depicts the concentration of DC Power Generation at Certain Hours of The Day. Here, It can be seen the most of Peak Generation happen during **10AM to 2PM** every day. Hence, this period is the **Peak Generation Hours** of the PV System.')
        col2.info('Similar to the **Daily DC Power Distribution Plot**, here the **AC Power Distribution** also shows the same kind of concentration in Power Generation. Here also, the Peak Generating Hours are **10AM to 2PM** every day. So, the **Peak Generation Hours** same for both **DC** & **AC** Power Generation.')
        
@app.addapp(title='Daily Analytics',icon='☀')
def Daily():
    col1,col2,col3=st.columns((0.005,2.99,0.005))
    col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>Daily Solar Data Analytics</b></p>', unsafe_allow_html=True)
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
        df=pd.read_csv('data/sample_data.csv')
        d=pd.read_csv('data/sample_d1.csv')
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.0%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        
        
        
        col1,col2,col3,col4,col5=st.columns(5)
        
        month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"] # Add aditional months
        month_choice = col3.selectbox(label = "Select your month", options = month_name) # Give user to select

        cola,colb,colc,cold,cole=st.columns((1,1.1,1,0.9,1))
        st.markdown("----------------------------------------")
    # Convert month name to value
        st.write(df1)
        df1['month'] = pd.DatetimeIndex(df1['date']).month
        month_obj = datetime.datetime.strptime(month_choice, "%B")
        sel = month_obj.month # Get the month value

        # Get that particular month and display to the user
        dfB = df1[df1["month"] == sel]
        st.write(dfB) # You can add the other coloumns as well
        
        dfBs=dfB.resample('D', on='date').sum()
        st.write(dfBs)
        
       
        
        dfBs['date'] = dfBs.index
        st.write(dfBs)
        
        dfBav=dfB[dfB["TArray"] != 0.0].resample('D', on='date').mean()
        dfBav['date'] = dfBav.index
        st.write(dfBav)
        
        dfBavD=dfBav.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS','month','date'], axis = 1)
        #st.write(dfBavD)
        dfBsD=dfBs.drop(['T_Amb','TArray','UArray','IArray','HOURS','MINUTES','MINUTES_PASS','month','date'], axis = 1)
        #st.write(dfBsD)
        dfBD=pd.concat([dfBsD,dfBavD], axis=1, sort= False)
        #st.write(dfBD)
        
        def convert_df(df):
            #Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        csv = convert_df(dfBD)
        
        download=colc.download_button(label=f"⬇️ Download {month_choice} Data",
                   data=csv,
                   file_name=f'{month_choice}_Summary.csv',
                   mime='text/csv',
                   )
        
        
        
        #Monthly Metrics
        #Metrics Backend
        dfBs_sum=dfBs.sum(axis=0, skipna=True)
        Tmod=dfBav.TArray.mean()
        
        
        col1.metric(label="Total Plant DC Capacity (kWp)",value="{:.0f}".format(d.DC_Cap.max()))
        col5.metric(label="Total Plant AC Capacity (kW)",value="{:.0f}".format(d.AC_Cap.max()),delta = "DC/AC Ratio: ""{:.2%}".format(d.DC_Cap.max()/d.AC_Cap.max()), delta_color = 'off')
        
     
        #Charts 
         
        colx,coly=st.columns(2)
        
        figx = go.Figure(data=[
            go.Bar(name='GlobHor', x=dfBs['date'], y=dfBs['GlobHor'],marker_color='#ff7f0e'),
            go.Bar(name='GlobInc', x=dfBs['date'], y=dfBs['GlobInc'],marker_color='#1f77b4')
            ])
        # Change the bar mode
        figx.update_layout(title_text='<b>Daily Global Horizontal & Inclined Plane Irradiations</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Irradiation (kWh/m\u00b2)",width=620,height=460,
            barmode='group')
        colx.plotly_chart(figx)
        
        
        irr_delta=value="{:.2f}".format((dfBs_sum.GlobInc-dfBs_sum.GlobHor)/1000)
        
        
        col1,col2=st.columns(2)
        col1.info(f'Similar to the **Hourly GII & GHI Plot**, this Plot shows the sum of Hourly values of each day for the **{month_choice}**. The Difference between Monthly GHI & GII during Operation is **{irr_delta} kWh/m\u00b2**')
        col2.info(f'Above Chart shows the **Daily Average Temperature of PV Array** during the Operational Hours. This value is very important to assess Daily **Temperature-Corrected PR** of PV System.')
        
        
        
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total Monthly GHI (kWh/m\u00b2)", value="{:.2f}".format(dfBs_sum.GlobHor/1000))
        col2.metric(label="Total Monthly GII (kWh/m\u00b2)", value="{:.2f}".format(dfBs_sum.GlobInc/1000))
        col3.metric(label="Monthly PR (%)", value="{:.0%}".format(dfBs_sum.E_Grid*1000/dfBs_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Monthly Usuable Energy (MWh)", value="{:.2f}".format(dfBs_sum.E_Grid/1000))
        col5.metric(label="Monthly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        
        figy = go.Figure(data=[
            go.Bar(name='Average Module Temperature', x=dfBav['date'], y=dfBav['TArray'],marker_color='#673AB7')
            ])
        # Change the bar mode
        figy.update_layout(title_text='<b>Daily Average Module Temperature During Operation</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Temperature (\u00b0C)",width=620,height=460,barmode='group')
        coly.plotly_chart(figy)
        
        
        
        
        #Bar Charts
        colx1,coly1=st.columns(2)
        
        figx1 = px.bar(dfBs, x='date', y='EArray',
             hover_data=['EArray', 'GlobInc'], color=dfBav['TArray'])
        figx1.update_layout(title_text='<b>Daily DC Energy Yield</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Energy (kWh)",width=620,height=460)
        colx1.plotly_chart(figx1)
        
        
        figy1 = px.bar(dfBs, x='date', y='E_Grid',
             hover_data=['E_Grid', 'GlobInc'], color='GlobInc')
        figy1.update_layout(title_text='<b>Daily AC Energy Yield</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Energy (kWh)",width=620,height=460)
        coly1.plotly_chart(figy1)
        
        EArray_month=value="{:.2f}".format(dfBs_sum.EArray/1000)
        Egrid_month=value="{:.2f}".format(dfBs_sum.E_Grid/1000)
        
        col1,col2=st.columns(2)
        col1.info(f'**Daily DC Energy Yield** Plot presents sum value of **Hourly DC Power Generation**. The Monthly DC Energy Yield for **{month_choice}** is **{EArray_month} MWh**. Further to this, as you hover over the plot, there are other values like **Daily GII** & **Daily Avg PV Temperature** corresponding to that day. The **Color** bar on the **right** indicates the **corelation** intensity of Daily Avg **PV Temperature** with **DC Energy** Yield.')
        col2.info(f'Similar to the plot on left, this plot represents the **Daily AC Energy** Data for the **{month_choice}**, which is **{Egrid_month} MWh**. in this plot, the corelation between **AC Energy Generation** & **Daily GII** has been shown. The **Color bar** on the **right** side shows the **intensity scale** of GII over the Daily AC Energy Production. Higher the **GII**, so the **AC Energy Production** will higher for that day.')
        
        
        
        
    else:
        df=pd.read_csv('data/main_data.csv')
        d=pd.read_csv('data/d1.csv')
        
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.0%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        
        
        
        col1,col2,col3,col4,col5=st.columns(5)
        
        month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"] # Add aditional months
        month_choice = col3.selectbox(label = "Select your month", options = month_name) # Give user to select

        cola,colb,colc,cold,cole=st.columns((1,1.1,1,0.9,1))
        st.markdown("----------------------------------------")
    # Convert month name to value
        df1['month'] = pd.DatetimeIndex(df1['date']).month
        month_obj = datetime.datetime.strptime(month_choice, "%B")
        sel = month_obj.month # Get the month value

        # Get that particular month and display to the user
        dfB = df1[df1["month"] == sel]
        #st.write(dfB) # You can add the other coloumns as well
        
        dfBs=dfB.resample('D', on='date').sum()
        #st.write(dfBs)
        
       
        
        dfBs['date'] = dfBs.index
        #st.write(dfBs)
        
        dfBav=dfB[dfB["TArray"] != 0.0].resample('D', on='date').mean()
        dfBav['date'] = dfBav.index
        #st.write(dfBav)
        
        dfBavD=dfBav.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS','month','date'], axis = 1)
        #st.write(dfBavD)
        dfBsD=dfBs.drop(['T_Amb','TArray','UArray','IArray','HOURS','MINUTES','MINUTES_PASS','month','date'], axis = 1)
        #st.write(dfBsD)
        dfBD=pd.concat([dfBsD,dfBavD], axis=1, sort= False)
        #st.write(dfBD)
        
        def convert_df(df):
            #Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        csv = convert_df(dfBD)
        
        download=colc.download_button(label=f"⬇️ Download {month_choice} Data",
                   data=csv,
                   file_name=f'{month_choice}_Summary.csv',
                   mime='text/csv',
                   )
        
        
        
        #Monthly Metrics
        #Metrics Backend
        dfBs_sum=dfBs.sum(axis=0, skipna=True)
        Tmod=dfBav.TArray.mean()
        
        
        col1.metric(label="Total Plant DC Capacity (kWp)",value="{:.0f}".format(d.DC_Cap.max()))
        col5.metric(label="Total Plant AC Capacity (kW)",value="{:.0f}".format(d.AC_Cap.max()),delta = "DC/AC Ratio: ""{:.2%}".format(d.DC_Cap.max()/d.AC_Cap.max()), delta_color = 'off')
        
     
        #Charts 
         
        colx,coly=st.columns(2)
        
        figx = go.Figure(data=[
            go.Bar(name='GlobHor', x=dfBs['date'], y=dfBs['GlobHor'],marker_color='#ff7f0e'),
            go.Bar(name='GlobInc', x=dfBs['date'], y=dfBs['GlobInc'],marker_color='#1f77b4')
            ])
        # Change the bar mode
        figx.update_layout(title_text='<b>Daily Global Horizontal & Inclined Plane Irradiations</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Irradiation (kWh/m\u00b2)",width=620,height=460,
            barmode='group')
        colx.plotly_chart(figx)
        
        
        irr_delta=value="{:.2f}".format((dfBs_sum.GlobInc-dfBs_sum.GlobHor)/1000)
        
        
        col1,col2=st.columns(2)
        col1.info(f'Similar to the **Hourly GII & GHI Plot**, this Plot shows the sum of Hourly values of each day for the **{month_choice}**. The Difference between Monthly GHI & GII during Operation is **{irr_delta} kWh/m\u00b2**')
        col2.info(f'Above Chart shows the **Daily Average Temperature of PV Array** during the Operational Hours. This value is very important to assess Daily **Temperature-Corrected PR** of PV System.')
        
        
        
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total Monthly GHI (kWh/m\u00b2)", value="{:.2f}".format(dfBs_sum.GlobHor/1000))
        col2.metric(label="Total Monthly GII (kWh/m\u00b2)", value="{:.2f}".format(dfBs_sum.GlobInc/1000))
        col3.metric(label="Monthly PR (%)", value="{:.0%}".format(dfBs_sum.E_Grid*1000/dfBs_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Monthly Usuable Energy (MWh)", value="{:.2f}".format(dfBs_sum.E_Grid/1000))
        col5.metric(label="Monthly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        
        figy = go.Figure(data=[
            go.Bar(name='Average Module Temperature', x=dfBav['date'], y=dfBav['TArray'],marker_color='#673AB7')
            ])
        # Change the bar mode
        figy.update_layout(title_text='<b>Daily Average Module Temperature During Operation</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Temperature (\u00b0C)",width=620,height=460,barmode='group')
        coly.plotly_chart(figy)
        
        
        
        
        #Bar Charts
        colx1,coly1=st.columns(2)
        
        figx1 = px.bar(dfBs, x='date', y='EArray',
             hover_data=['EArray', 'GlobInc'], color=dfBav['TArray'])
        figx1.update_layout(title_text='<b>Daily DC Energy Yield</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Energy (kWh)",width=620,height=460)
        colx1.plotly_chart(figx1)
        
        
        figy1 = px.bar(dfBs, x='date', y='E_Grid',
             hover_data=['E_Grid', 'GlobInc'], color='GlobInc')
        figy1.update_layout(title_text='<b>Daily AC Energy Yield</b>', title_x=0.5,
                   xaxis_title="Days",yaxis_title="Energy (kWh)",width=620,height=460)
        coly1.plotly_chart(figy1)
        
        EArray_month=value="{:.2f}".format(dfBs_sum.EArray/1000)
        Egrid_month=value="{:.2f}".format(dfBs_sum.E_Grid/1000)
        
        col1,col2=st.columns(2)
        col1.info(f'**Daily DC Energy Yield** Plot presents sum value of **Hourly DC Power Generation**. The Monthly DC Energy Yield for **{month_choice}** is **{EArray_month} MWh**. Further to this, as you hover over the plot, there are other values like **Daily GII** & **Daily Avg PV Temperature** corresponding to that day. The **Color** bar on the **right** indicates the **corelation** intensity of Daily Avg **PV Temperature** with **DC Energy** Yield.')
        col2.info(f'Similar to the plot on left, this plot represents the **Daily AC Energy** Data for the **{month_choice}**, which is **{Egrid_month} MWh**. in this plot, the corelation between **AC Energy Generation** & **Daily GII** has been shown. The **Color bar** on the **right** side shows the **intensity scale** of GII over the Daily AC Energy Production. Higher the **GII**, so the **AC Energy Production** will higher for that day.')
        
        
@app.addapp(title='Monthly Analytics',icon='🌤')
def Monthly():
    col1,col2,col3=st.columns((0.005,2.99,0.005))
    col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>Monthly Solar Data Analytics</b></p>', unsafe_allow_html=True)
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
        df=pd.read_csv('data/sample_data.csv')
        d=pd.read_csv('data/sample_d1.csv')
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        #st.write(df3x)
        df1ms=df1[df1["TArray"] != 0.0].resample('M', on='date').sum()
        df1msd=df1ms.drop(['T_Amb','TArray', 'IArray','UArray','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1msd)
        df1mm=df1[df1["TArray"] != 0.0].resample('M', on='date').mean()
        df1mmd=df1mm.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','T_Amb', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mmd)
        df1mtamb=df1.resample('M', on='date').mean()
        df1mtambd=df1mtamb.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','TArray', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mtambd)
        
        
        
        df1msd['GlobInc']=pd.eval('df1msd.GlobInc/1000')
        df1msd['GlobHor']=pd.eval('df1msd.GlobHor/1000')
        df1msd['DiffHor']=pd.eval('df1msd.DiffHor/1000')
        df1msd['EArray']=pd.eval('df1msd.EArray/1000')
        df1msd['E_Grid']=pd.eval('df1msd.E_Grid/1000')
        
        #Monthly Sum Dataframe
        df1msd['date'] = df1msd.index
        df1msd['month'] = df1msd['date'].dt.month
        df1msd['month'] = df1msd['month'].apply(lambda x: calendar.month_abbr[x])
        df1msd = df1msd.set_index(['month'])
        
        df1msd.loc['Yearly']= df1msd[['GlobInc','GlobHor','DiffHor','EArray','E_Grid','ArrayON']].sum()
        df1msd['PR']= pd.eval('df1msd.E_Grid*1000/df1msd.GlobInc/d.DC_Cap.max()')
        df1msd=df1msd.drop(['date'],axis=1)
        
        
        #st.write(df1msd)
        #Monthly Average Temp Dataframe
        df1msT=pd.concat([df1mmd,df1mtambd ], axis=1, sort= False)
        df1msT['date'] = df1msT.index
        df1msT['month'] = df1msT['date'].dt.month
        df1msT['month'] = df1msT['month'].apply(lambda x: calendar.month_abbr[x])
        df1msT = df1msT.set_index(['month'])
        df1msT=df1msT.drop(['date'],axis=1)
        df1msT.loc['Yearly']= df1msT.mean()
        
        df1msF=pd.concat([df1msd,df1msT ], axis=1, sort= False)
        
        
        
        
        #Charts
        df1msdC=df1msd.drop(['Yearly'])
        
        #st.write(df1msdC)
        colx,coly=st.columns(2)
        
        figx = go.Figure(data=[
            go.Bar(name='GlobHor',x=df1msdC.index, y=df1msdC['GlobHor']),
            go.Bar(name='GlobInc',x=df1msdC.index, y=df1msdC['GlobInc'])
            ])
        # Change the bar mode
        figx.update_layout(title_text='<b>Monthly Global Horizontal & Inclined Plane Irradiations</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Irradiation (kWh/m\u00b2)",width=620,height=460,
            barmode='group')
        colx.plotly_chart(figx)
        
        
        figy = go.Figure(data=[
            go.Bar(name='EArray',x=df1msdC.index, y=df1msdC['EArray'],marker_color='#5A30F0'),
            go.Bar(name='E_Grid',x=df1msdC.index, y=df1msdC['E_Grid'],marker_color='lightsalmon')
            ])
        # Change the bar mode
        figy.update_layout(title_text='<b>Monthly DC & AC Energy Yield of PV Plant</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Energy Yield (MWh)",width=620,height=460,
            barmode='group')
        
        coly.plotly_chart(figy)
        
        
        col1,col2=st.columns(2)
        #Temperature Chart
        df1msTC=df1msT.drop(['Yearly'])
        fig1 = px.line(df1msTC,x=df1msTC.index, y=["TArray", "T_Amb"],title='Monthly Avg Ambient & PV Module Surface Temperature (\u00b0C)',width=620,height=460)
        fig1.update_layout(title_text='<b>Monthly Avg Ambient & PV Module Surface Temperature (\u00b0C)</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Temperature (\u00b0C)")
        col1.plotly_chart(fig1)
        
        fig2 = px.bar(df1msdC, x=df1msdC.index, y='PR',
             hover_data=['E_Grid', 'PR'], color='E_Grid')
        fig2.update_layout(title_text='<b>Monthly Performance Ratio</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Ratio (%)",width=620,height=460)
        col2.plotly_chart(fig2)
        
        col1,col2=st.columns(2)
        col1.info(f'The Above plot shows **Monthly Avg Ambient & PV Surface Temperatures** for the enitre time period. The Ambient Temperature calculated by averaging out the entire day+night(24 hours) time values whereas the PV Surface temperature derived from avg temp values of only Operating Hours. PV Surface temperature values will always be **Higher** than the Ambient Temperature at any given time during the operation.')
        col2.info(f'**Performance Ratio (PR)** for all the months plotted above. This is again a corealation Mapping Plot where the Corealation has been established between **Monthly PR** & the **Monthly Energy Output**. On the right, The **E_Grid** (Energy Output) Scale added. When the **PR** is **lower**, the **E_Grid** is **higher** and vice versa. AC Energy Output is **highly** corelated with **GII** and **moderately** corelated with **Ambient Temperature**')
        
        
        
        st.markdown("----------------------------------------")
        
        #Download Summary Data
        col1,col2,col3=st.columns((1.1,1,.9))
        def convert_df(df):
            #Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        csv = convert_df(df1msF)
        col2=col2.download_button(label="⬇️ Download Solar Plant Summary",
                   data=csv,
                   file_name='Solar_Plant_Summary.csv',
                   mime='text/csv',
                   )
        
        df1msF=df1msF.style.format({'GlobHor': "{:.2f}",'GlobInc': "{:.2f}",
                                    'DiffHor': "{:.2f}",'EArray': "{:.2f}",'E_Grid': "{:.2f}",'ArrayON':"{:.0f}",
                                    'PR': "{:.2%}",'T_Amb': "{:.2f}",'TArray': "{:.2f}"})
        
        st.table(df1msF)
        
        
        
        
        
        
    else:
        df=pd.read_csv('data/main_data.csv')
        d=pd.read_csv('data/d1.csv')
        
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        col3.metric(label="Annual PR (%)", value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        st.markdown("----------------------------------------")
        #st.write(df3x)
        df1ms=df1[df1["TArray"] != 0.0].resample('M', on='date').sum()
        df1msd=df1ms.drop(['T_Amb','TArray', 'IArray','UArray','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1msd)
        df1mm=df1[df1["TArray"] != 0.0].resample('M', on='date').mean()
        df1mmd=df1mm.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','T_Amb', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mmd)
        df1mtamb=df1.resample('M', on='date').mean()
        df1mtambd=df1mtamb.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','TArray', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mtambd)
        
        
        
        df1msd['GlobInc']=pd.eval('df1msd.GlobInc/1000')
        df1msd['GlobHor']=pd.eval('df1msd.GlobHor/1000')
        df1msd['DiffHor']=pd.eval('df1msd.DiffHor/1000')
        df1msd['EArray']=pd.eval('df1msd.EArray/1000')
        df1msd['E_Grid']=pd.eval('df1msd.E_Grid/1000')
        
        #Monthly Sum Dataframe
        df1msd['date'] = df1msd.index
        df1msd['month'] = df1msd['date'].dt.month
        df1msd['month'] = df1msd['month'].apply(lambda x: calendar.month_abbr[x])
        df1msd = df1msd.set_index(['month'])
        
        df1msd.loc['Yearly']= df1msd[['GlobInc','GlobHor','DiffHor','EArray','E_Grid','ArrayON']].sum()
        df1msd['PR']= pd.eval('df1msd.E_Grid*1000/df1msd.GlobInc/d.DC_Cap.max()')
        df1msd=df1msd.drop(['date'],axis=1)
        
        
        #st.write(df1msd)
        #Monthly Average Temp Dataframe
        df1msT=pd.concat([df1mmd,df1mtambd ], axis=1, sort= False)
        df1msT['date'] = df1msT.index
        df1msT['month'] = df1msT['date'].dt.month
        df1msT['month'] = df1msT['month'].apply(lambda x: calendar.month_abbr[x])
        df1msT = df1msT.set_index(['month'])
        df1msT=df1msT.drop(['date'],axis=1)
        df1msT.loc['Yearly']= df1msT.mean()
        
        df1msF=pd.concat([df1msd,df1msT ], axis=1, sort= False)
        
        
        
        
        #Charts
        df1msdC=df1msd.drop(['Yearly'])
        
        #st.write(df1msdC)
        colx,coly=st.columns(2)
        
        figx = go.Figure(data=[
            go.Bar(name='GlobHor',x=df1msdC.index, y=df1msdC['GlobHor']),
            go.Bar(name='GlobInc',x=df1msdC.index, y=df1msdC['GlobInc'])
            ])
        # Change the bar mode
        figx.update_layout(title_text='<b>Monthly Global Horizontal & Inclined Plane Irradiations</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Irradiation (kWh/m\u00b2)",width=620,height=460,
            barmode='group')
        colx.plotly_chart(figx)
        
        
        figy = go.Figure(data=[
            go.Bar(name='EArray',x=df1msdC.index, y=df1msdC['EArray'],marker_color='#5A30F0'),
            go.Bar(name='E_Grid',x=df1msdC.index, y=df1msdC['E_Grid'],marker_color='lightsalmon')
            ])
        # Change the bar mode
        figy.update_layout(title_text='<b>Monthly DC & AC Energy Yield of PV Plant</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Energy Yield (MWh)",width=620,height=460,
            barmode='group')
        
        coly.plotly_chart(figy)
        
        
        col1,col2=st.columns(2)
        #Temperature Chart
        df1msTC=df1msT.drop(['Yearly'])
        fig1 = px.line(df1msTC,x=df1msTC.index, y=["TArray", "T_Amb"],title='Monthly Avg Ambient & PV Module Surface Temperature (\u00b0C)',width=620,height=460)
        fig1.update_layout(title_text='<b>Monthly Avg Ambient & PV Module Surface Temperature (\u00b0C)</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Temperature (\u00b0C)")
        col1.plotly_chart(fig1)
        
        fig2 = px.bar(df1msdC, x=df1msdC.index, y='PR',
             hover_data=['E_Grid', 'PR'], color='E_Grid')
        fig2.update_layout(title_text='<b>Monthly Performance Ratio</b>', title_x=0.5,
                   xaxis_title="Months",yaxis_title="Ratio (%)",width=620,height=460)
        col2.plotly_chart(fig2)
        
        col1,col2=st.columns(2)
        col1.info(f'The Above plot shows **Monthly Avg Ambient & PV Surface Temperatures** for the enitre time period. The Ambient Temperature calculated by averaging out the entire day+night(24 hours) time values whereas the PV Surface temperature derived from avg temp values of only Operating Hours. PV Surface temperature values will always be **Higher** than the Ambient Temperature at any given time during the operation.')
        col2.info(f'**Performance Ratio (PR)** for all the months plotted above. This is again a corealation Mapping Plot where the Corealation has been established between **Monthly PR** & the **Monthly Energy Output**. On the right, The **E_Grid** (Energy Output) Scale added. When the **PR** is **lower**, the **E_Grid** is **higher** and vice versa. AC Energy Output is **highly** corelated with **GII** and **moderately** corelated with **Ambient Temperature**')
        
        
        
        st.markdown("----------------------------------------")
        
        #Download Summary Data
        col1,col2,col3=st.columns((1.1,1,.9))
        def convert_df(df):
            #Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        csv = convert_df(df1msF)
        col2=col2.download_button(label="⬇️ Download Solar Plant Summary",
                   data=csv,
                   file_name='Solar_Plant_Summary.csv',
                   mime='text/csv',
                   )
        
        df1msF=df1msF.style.format({'GlobHor': "{:.2f}",'GlobInc': "{:.2f}",
                                    'DiffHor': "{:.2f}",'EArray': "{:.2f}",'E_Grid': "{:.2f}",'ArrayON':"{:.0f}",
                                    'PR': "{:.2%}",'T_Amb': "{:.2f}",'TArray': "{:.2f}"})
        
        st.table(df1msF)
        
        
        
@app.addapp(title='Summary',icon='📘')
def project_summary():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
        df=pd.read_csv('data/sample_data.csv')
        d=pd.read_csv('data/sample_d1.csv')
        
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        if not os.path.exists("images"):
            os.mkdir("images")
            df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        #col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        #col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        #col3.metric(label="Annual PR (%)", value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        #col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        #col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        #st.markdown("----------------------------------------")
        #st.write(df3x)
        df1ms=df1[df1["TArray"] != 0.0].resample('M', on='date').sum()
        df1msd=df1ms.drop(['T_Amb','TArray', 'IArray','UArray','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1msd)
        df1mm=df1[df1["TArray"] != 0.0].resample('M', on='date').mean()
        df1mmd=df1mm.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','T_Amb', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mmd)
        df1mtamb=df1.resample('M', on='date').mean()
        df1mtambd=df1mtamb.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','TArray', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mtambd)
        
        
        
        df1msd['GlobInc']=pd.eval('df1msd.GlobInc/1000')
        df1msd['GlobHor']=pd.eval('df1msd.GlobHor/1000')
        df1msd['DiffHor']=pd.eval('df1msd.DiffHor/1000')
        df1msd['EArray']=pd.eval('df1msd.EArray/1000')
        df1msd['E_Grid']=pd.eval('df1msd.E_Grid/1000')
        
        #Monthly Sum Dataframe
        df1msd['date'] = df1msd.index
        df1msd['month'] = df1msd['date'].dt.month
        df1msd['month'] = df1msd['month'].apply(lambda x: calendar.month_abbr[x])
        df1msd = df1msd.set_index(['month'])
        
        df1msd.loc['Yearly']= df1msd[['GlobInc','GlobHor','DiffHor','EArray','E_Grid','ArrayON']].sum()
        df1msd['PR']= pd.eval('df1msd.E_Grid*1000/df1msd.GlobInc/d.DC_Cap.max()')
        df1msd=df1msd.drop(['date'],axis=1)
        
        
        #st.write(df1msd)
        #Monthly Average Temp Dataframe
        df1msT=pd.concat([df1mmd,df1mtambd ], axis=1, sort= False)
        df1msT['date'] = df1msT.index
        df1msT['month'] = df1msT['date'].dt.month
        df1msT['month'] = df1msT['month'].apply(lambda x: calendar.month_abbr[x])
        df1msT = df1msT.set_index(['month'])
        df1msT=df1msT.drop(['date'],axis=1)
        df1msT.loc['Yearly']= df1msT.mean()
        
        df1msF=pd.concat([df1msd,df1msT ], axis=1, sort= False)
        
        
        
        
        #Charts
        df1msdC=df1msd.drop(['Yearly'])
        
        
        
        
        sns.set_theme(style="whitegrid")
        #df = sns.load_dataset("df1msdC")
        ax = sns.barplot(x=df1msdC.index, y=df1msdC['E_Grid'], data=df1msdC).set(title='Monthly AC Energy Injected to Grid', ylabel='AC Energy(kWh)')
        plt.savefig("Monthly_E_Grid.png")
        #st.pyplot()
        
        
        df1msdc1=df1msdC
        df1msdc1 = pd.DataFrame({
            'Months': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
            'GlobInc': df1msdC['GlobInc'],
            'GlobHor': df1msdC['GlobHor']
            })
        
        #st.write(df1msdc1)
        
        
        
        fig, ax1 = plt.subplots(figsize=(6.4, 4.8))
        tidy = df1msdc1.melt(id_vars='Months').rename(columns=str.title)
        sns.barplot(x='Months', y='Value', hue='Variable', data=tidy, ax=ax1,palette = 'magma').set(title='Monthly GII(GlobInc) & GHI(GlobHor) Values (kWh/mm\u00b2)', ylabel='Irradiation (kWh/mm\u00b2/month)')
        plt.savefig("Monthly_GHI_GII.png")
        #st.pyplot()
        
        #st.markdown("----------------------------------------")
        
        
    #-----------------------------------------
        DC=d.DC_Cap.max()
        AC=d.AC_Cap.max()
        PV_Wp=d.PV_Wp.max()
        P_eff=d.Power_eff.max()
        Proj_Cost=d.Proj_Cost.max()
        E_Tariff=d.Power_rate.max()
        OnM=d.OnM.max()
        Tariff_esc=d.Tariff_Esc.max()
        OnM_esc=d.OnM_Esc.max()
        Electricity_Tariff=d.Electricity_Tariff.max()
        Company_Name=d.Company_Name.max()
        Company_representative=d.Company_representative.max()
        email_id=d.email_id.max()
        Country=d.Country.max()
    
    
        #st.write(DC, AC,PV_Wp,P_eff,Proj_Cost,E_Tariff, OnM, Tariff_esc, OnM_esc,Electricity_Tariff)
    
        E_Grid=format(df1_sum.E_Grid/1000)
        #st.write(E_Grid)
        FinData={'Year':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]}
        FinD=pd.DataFrame(FinData)
    
        FinD['Yearly_Yield_kWh']=pd.eval('(df1_sum.E_Grid)*((1-0.007)**FinD.Year)')
        FinD['Yearly_Gross_Income_$']=pd.eval('FinD.Yearly_Yield_kWh*E_Tariff*((1+Tariff_esc/100)**FinD.Year)')
        FinD['Yearly_OnM_Expense_$']=pd.eval('Proj_Cost*(10**6)*(OnM/100)*((1+OnM_esc/100)**FinD.Year)')
        FinD['Gross_Income_After_OnM']=FinD['Yearly_Gross_Income_$']-FinD['Yearly_OnM_Expense_$']
        FinD['Gross_Cash_Flow_$']=FinD['Yearly_Gross_Income_$']-FinD['Yearly_OnM_Expense_$']

        new_row=pd.DataFrame({'Year':0,'Yearly_Yield_kWh':0,'Yearly_Gross_Income_$':0,
                         'Yearly_OnM_Expense_$':0,'Gross_Income_After_OnM':0, 'Gross_Cash_Flow_$':Proj_Cost*(-1)*10**6
                          },index =[0])
        FinD1=pd.concat([new_row, FinD]).reset_index(drop = True)
        
        FinD1['cumsum_Cash_Flow_$']=FinD1['Gross_Cash_Flow_$'].cumsum()
        #st.dataframe(FinD1)
    
    
        #Paybackk Period Calculation
        def payback():
            final_full_year = FinD1[FinD1['cumsum_Cash_Flow_$'] < 0].index.values.max()
            fractional_yr = -FinD1['cumsum_Cash_Flow_$'][final_full_year]/FinD1['Gross_Cash_Flow_$'][final_full_year + 1]
            period = final_full_year + fractional_yr
            return round(period, 1)
    
        #st.write("Payback Period : ", payback(), "Years")
        PBP=payback()
    
        #Cash Flow Chart for 25 Years 
        sns.set_theme(style="whitegrid")
        fig, ax = plt.subplots(figsize=(6.4,4.8))
        ax = sns.barplot(x=FinD1.Year, y=FinD1['cumsum_Cash_Flow_$'], data=FinD1,ax=ax,palette = 'Spectral').set(title='Cumulative Cash Flow for 25 Years',ylabel='Cumulative Cash Flow ($)')
    
        plt.savefig("Cashflow_25.png")
        #st.pyplot()
    
        cash_flow = FinD1['Gross_Cash_Flow_$'].values
        FinD1['Time'] = [i for i in range(26)]
        t = FinD1['Time'].values
    
        def npv(irr, cashfs, t):  
            x =  np.sum(cashfs / (1 + irr) ** t)
            return round(x, 3)
    
        def irr(cashfs, t, x0, **kwargs):
            y = (fsolve(npv, x0=x0, args=(cashfs, t), **kwargs)).item()
            return round(y*100, 4)
    
        FinD1_sum=FinD1.sum(axis=0, skipna=True)
        #st.write(FinD1_sum['Yearly_OnM_Expense_$'])
        LCOE=value='{:.3f}'.format((FinD1_sum['Yearly_OnM_Expense_$']+Proj_Cost)/FinD1_sum.Yearly_Yield_kWh)
    
    
        CO2=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(0.709/1000))
        Cars=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(0.154/1000))
        Houses=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(0.129/1000))
        Trees=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(11.7/1000))
    
    
    
        #st.write(LCOE, CO2,Cars,Houses,Trees)
    
        NPV=npv(irr=0.10, cashfs=cash_flow, t=t)
        IRR=irr(cashfs=cash_flow, t=t, x0=0.10)
        Gross_25=value='{:.2f}'.format(FinD1_sum['Gross_Income_After_OnM']/10**6)
        PR=value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max())
        Spec_E=value='{:.0f}'.format(FinD.Yearly_Yield_kWh.max()/DC)
        OnM_25=value='{:.2f}'.format(FinD1_sum['Yearly_OnM_Expense_$']/10**6)
    
        #st.write("NPV : $", NPV)
        #st.write("IRR : ", IRR,'%')
        #st.write(Gross_25,Spec_E)

        new_column = pd.DataFrame({'DC_Cap':DC,'AC_Cap':AC,'PV_Wp':PV_Wp,'Power_eff':P_eff,
                               'Proj_Cost':Proj_Cost,'Electricity_Tariff':Electricity_Tariff,
                               'OnM':OnM,'E_tariff':E_Tariff,'Tariff_esc':Tariff_esc,'OnM_esc':OnM_esc,
                               'Company_Name':Company_Name,'Company_representative':Company_representative,
                               'email_id':email_id,'Country':Country,
        'E_Grid':E_Grid,'PR':PR,'Spec_E':Spec_E,'Gross_25':Gross_25,
                               'LCOE':LCOE,'PBP':PBP,'IRR':IRR,
                               'CO2':CO2,'Cars':Cars,'Houses':Houses,'Trees':Trees,'NPV':NPV
                               },index =[0])
    
    
        new_column.to_csv('data/d2.csv')
    
    
    
        #-------------------PDF Report-----------------------
       
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.9rem;font-size:4px;border-radius:4px;"><span style="font-size: 36px;"><b>SOLAR DATA ANALYTICS - SUMMARY<b></span><br><span style="font-size: 18px;">{Company_Name}&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;||&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Presented By {Company_representative}</span></p>', unsafe_allow_html=True)
        
        st.write('\n')
        st.write('\n')
        #st.write('\n')
        st.write(f'<p style="background-color:#5981B5;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:10px;border-radius:1px;"><b></b></p>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        
        #E_grid, DC, AC Capacity, Annual PR
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        
        
        col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Plant DC Capacity</b></p>', unsafe_allow_html=True)
        col3.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Annual Energy Yield</b></p>', unsafe_allow_html=True)
        col4.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Annual PR</b></p>', unsafe_allow_html=True)
        col5.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Plant AC Capacity</b></p>', unsafe_allow_html=True)
        
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        DC_m=value=str(float("{:.2f}".format(DC)))+" kWp"
        PR_m=PR
        E_Grid_m=value=str(float(format(E_Grid)))+" MWh"
        AC_m=value=str(float("{:.2f}".format(AC)))+" kW"
        
        col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{DC_m}</b></p>', unsafe_allow_html=True)
        col3.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{E_Grid_m}</b></p>', unsafe_allow_html=True)
        col4.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{PR_m}</b></p>', unsafe_allow_html=True)
        col5.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{AC_m}</b></p>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        #Project cost, SPec Yield, Gross income
        col1,col2,col3,col4,col5=st.columns((0.1,1.6,1.6,1.6,0.1))
        
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Gross Solar Income after 25 Years:<br>USD ${Gross_25} Millions</b></p>', unsafe_allow_html=True)
        col3.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Specific Energy Yield:<br>{Spec_E} kWh/kWp/Yr</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Upfront Project Cost:<br>USD ${Proj_Cost} Millions</b></p>', unsafe_allow_html=True)
        
        #GII,GHI Graph, E_grid Graph, Tariff, O&M and Escalations
        col1,col2,col3,col4,col5=st.columns((0.2,1.65,0.1,1.65,0.2))
        col2.image('Monthly_E_Grid.png')
        col4.image('Monthly_GHI_GII.png')
        
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:7px 7px 0px 0px;"><b>{Electricity_Tariff}: ${E_Tariff} USD/kWh</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:7px 7px 0px 0px;"><b>Yearly O&M Cost: {OnM}% of Total Project Cost</b></p>', unsafe_allow_html=True)
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:0px 0px 7px 7px;"><b>Year-On-Year Escalation: {Tariff_esc}%</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:0px 0px 7px 7px;"><b>Year-On-Year Escalation: {OnM_esc}%</b></p>', unsafe_allow_html=True)
        
        #Cashflow Graph
        col1,col2,col3=st.columns((0.75,1.5,0.75))
        col2.image('Cashflow_25.png')
        NPV_m=value="{:.3f}".format(NPV/(10**6))
        
        col1,col2,col3,col4,col5=st.columns((0.55,1.2,1.5,1.2,0.55))
        st.write('\n')
        st.write('\n')
        col4.markdown(f'<p style="background-color:#498AAA;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Net Present Value (NPV):<br>USD $ ({(NPV_m)}) Millions</b></p>', unsafe_allow_html=True)
        col2.markdown(f'<p style="background-color:#DC765A;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Total O&M Expenses in 25 Years:<br>USD $ {OnM_25} Millions</b></p>', unsafe_allow_html=True)
        st.write('\n')
        #LCOE, PBP, IRR
        col1,col2,col3,col4,col5=st.columns((0.1,1.6,1.6,1.6,0.1))
        
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:3px;"><b>LCOE:<br>${LCOE} USD/kWh</b></p>', unsafe_allow_html=True)
        col3.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:3px;"><b>Simple Payback Period:<br>{PBP} Years</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:3px;"><b>Internal Rate of Return:<br>{IRR}%</b></p>', unsafe_allow_html=True)
        
        #Carbon Offset
        col1,col2,col3,col4=st.columns(4)
        
        
        #divider
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:4px;border-radius:1px;"><b></b></p>', unsafe_allow_html=True)
        #images
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        file_ = open("images/co2-cloud.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col2.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        file_ = open("images/car.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col3.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        file_ = open("images/green-home.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col4.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        file_ = open("images/park.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col5.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        
        #text
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        col2.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{CO2}</b><br>Tonnes of CO2 Offset per Year</p>', unsafe_allow_html=True)
        col3.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{Cars}</b><br>Cars Taken off from the Road</p>', unsafe_allow_html=True)
        col4.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{Houses}</b><br>Houses Energy Met per Year</p>', unsafe_allow_html=True)
        col5.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{Trees}</b><br>Tree Seedlings grown in 10 Years</p>', unsafe_allow_html=True)
       
        #divider
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:4px;border-radius:1px;"><b></b></p>', unsafe_allow_html=True)
        
        #Footer
        file_ = open("images/linkedin.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        
        file_ = open("images/github.png", "rb")
        contents = file_.read()
        data_url1 = base64.b64encode(contents).decode("utf-8")
        file_.close()
        
        
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.3rem;font-size:13px;border-radius:7px 7px 7px 7px;">DEVELOPED BY AMRIT MANDAL&emsp;&emsp;|&emsp;&emsp;<b>Contact @ </b><a href="https://www.linkedin.com/in/amritmandal/"><img src="data:image/png;base64,{data_url}" alt="co2"></a></p>', unsafe_allow_html=True)
        
    else:
        df=pd.read_csv('data/main_data.csv')
        d=pd.read_csv('data/d1.csv')
        
        df.E_Grid[df.E_Grid.lt(0)] = 0
        df['date'] = pd.to_datetime(df['date'])
        df1 = df.set_index(['date'])
        
        if not os.path.exists("images"):
            os.mkdir("images")
        
        df3x=df1
        df3x['date'] = df3x.index
        # adding separate time and date columns
        df3x["DATE"] = pd.to_datetime(df3x['date']).dt.date # add new column with date
        df3x["TIME"] = pd.to_datetime(df3x['date']).dt.time # add new column with time
        # add hours and minutes for ml models
        df3x['HOURS'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.hour
        df3x['MINUTES'] = pd.to_datetime(df3x['TIME'],format='%H:%M:%S').dt.minute
        df3x['MINUTES_PASS'] = df3x['MINUTES'] + df3x['HOURS']*60

        # add date as string column
        df3x["DATE_STR"] = df3x["DATE"].astype(str) # add column with date as string
        
        
        
        #Metrics-Backend
        df1_sum = df1.select_dtypes(include=[np.number]).sum(axis=0, skipna=True)
        dfd=df[df["E_Grid"] != 0.0].resample('D', on='date').mean()
        Tmod=dfd.TArray.mean()
        dfTamb=df.resample('Y', on='date').mean()
        
      
        #Metrics-Frontend
        col1,col2,col3,col4,col5=st.columns(5)
        #col1.metric(label="Total GHI (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobHor/1000))
        #col2.metric(label="Total GII (kWh/m\u00b2/year)", value="{:.2f}".format(df1_sum.GlobInc/1000))
        #col3.metric(label="Annual PR (%)", value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max()))
        #col4.metric(label="Yearly Energy Yield (MWh/year)", value="{:.2f}".format(df1_sum.E_Grid/1000))
        #col5.metric(label="Yearly Avg PV Temperature (\u00b0C)", value="{:.2f}".format(Tmod))
        
        #st.markdown("----------------------------------------")
        #st.write(df3x)
        df1ms=df1[df1["TArray"] != 0.0].resample('M', on='date').sum()
        df1msd=df1ms.drop(['T_Amb','TArray', 'IArray','UArray','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1msd)
        df1mm=df1[df1["TArray"] != 0.0].resample('M', on='date').mean()
        df1mmd=df1mm.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','T_Amb', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mmd)
        df1mtamb=df1.resample('M', on='date').mean()
        df1mtambd=df1mtamb.drop(['GlobHor','GlobInc','DiffHor','EArray','E_Grid','TArray', 'IArray','UArray','ArrayON','HOURS','MINUTES','MINUTES_PASS'], axis = 1)
        #st.write(df1mtambd)
        
        
        
        df1msd['GlobInc']=pd.eval('df1msd.GlobInc/1000')
        df1msd['GlobHor']=pd.eval('df1msd.GlobHor/1000')
        df1msd['DiffHor']=pd.eval('df1msd.DiffHor/1000')
        df1msd['EArray']=pd.eval('df1msd.EArray/1000')
        df1msd['E_Grid']=pd.eval('df1msd.E_Grid/1000')
        
        #Monthly Sum Dataframe
        df1msd['date'] = df1msd.index
        df1msd['month'] = df1msd['date'].dt.month
        df1msd['month'] = df1msd['month'].apply(lambda x: calendar.month_abbr[x])
        df1msd = df1msd.set_index(['month'])
        
        df1msd.loc['Yearly']= df1msd[['GlobInc','GlobHor','DiffHor','EArray','E_Grid','ArrayON']].sum()
        df1msd['PR']= pd.eval('df1msd.E_Grid*1000/df1msd.GlobInc/d.DC_Cap.max()')
        df1msd=df1msd.drop(['date'],axis=1)
        
        
        #st.write(df1msd)
        #Monthly Average Temp Dataframe
        df1msT=pd.concat([df1mmd,df1mtambd ], axis=1, sort= False)
        df1msT['date'] = df1msT.index
        df1msT['month'] = df1msT['date'].dt.month
        df1msT['month'] = df1msT['month'].apply(lambda x: calendar.month_abbr[x])
        df1msT = df1msT.set_index(['month'])
        df1msT=df1msT.drop(['date'],axis=1)
        df1msT.loc['Yearly']= df1msT.mean()
        
        df1msF=pd.concat([df1msd,df1msT ], axis=1, sort= False)
        
        
        
        
        #Charts
        df1msdC=df1msd.drop(['Yearly'])
        
        
        
        
        sns.set_theme(style="whitegrid")
        #df = sns.load_dataset("df1msdC")
        ax = sns.barplot(x=df1msdC.index, y=df1msdC['E_Grid'], data=df1msdC).set(title='Monthly AC Energy Injected to Grid', ylabel='AC Energy(kWh)')
        plt.savefig("Monthly_E_Grid.png")
        #st.pyplot()
        
        
        df1msdc1=df1msdC
        df1msdc1 = pd.DataFrame({
            'Months': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
            'GlobInc': df1msdC['GlobInc'],
            'GlobHor': df1msdC['GlobHor']
            })
        
        #st.write(df1msdc1)
        
        
        
        fig, ax1 = plt.subplots(figsize=(6.4, 4.8))
        tidy = df1msdc1.melt(id_vars='Months').rename(columns=str.title)
        sns.barplot(x='Months', y='Value', hue='Variable', data=tidy, ax=ax1,palette = 'magma').set(title='Monthly GII(GlobInc) & GHI(GlobHor) Values (kWh/mm\u00b2)', ylabel='Irradiation (kWh/mm\u00b2/month)')
        plt.savefig("Monthly_GHI_GII.png")
        #st.pyplot()
        
        #st.markdown("----------------------------------------")
        
        
    #-----------------------------------------
        DC=d.DC_Cap.max()
        AC=d.AC_Cap.max()
        PV_Wp=d.PV_Wp.max()
        P_eff=d.Power_eff.max()
        Proj_Cost=d.Proj_Cost.max()
        E_Tariff=d.Power_rate.max()
        OnM=d.OnM.max()
        Tariff_esc=d.Tariff_Esc.max()
        OnM_esc=d.OnM_Esc.max()
        Electricity_Tariff=d.Electricity_Tariff.max()
        Company_Name=d.Company_Name.max()
        Company_representative=d.Company_representative.max()
        email_id=d.email_id.max()
        Country=d.Country.max()
    
    
        #st.write(DC, AC,PV_Wp,P_eff,Proj_Cost,E_Tariff, OnM, Tariff_esc, OnM_esc,Electricity_Tariff)
    
        E_Grid=format(df1_sum.E_Grid/1000)
        #st.write(E_Grid)
        FinData={'Year':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]}
        FinD=pd.DataFrame(FinData)
    
        FinD['Yearly_Yield_kWh']=pd.eval('(df1_sum.E_Grid)*((1-0.007)**FinD.Year)')
        FinD['Yearly_Gross_Income_$']=pd.eval('FinD.Yearly_Yield_kWh*E_Tariff*((1+Tariff_esc/100)**FinD.Year)')
        FinD['Yearly_OnM_Expense_$']=pd.eval('Proj_Cost*(10**6)*(OnM/100)*((1+OnM_esc/100)**FinD.Year)')
        FinD['Gross_Income_After_OnM']=FinD['Yearly_Gross_Income_$']-FinD['Yearly_OnM_Expense_$']
        FinD['Gross_Cash_Flow_$']=FinD['Yearly_Gross_Income_$']-FinD['Yearly_OnM_Expense_$']

        new_row=pd.DataFrame({'Year':0,'Yearly_Yield_kWh':0,'Yearly_Gross_Income_$':0,
                         'Yearly_OnM_Expense_$':0,'Gross_Income_After_OnM':0, 'Gross_Cash_Flow_$':Proj_Cost*(-1)*10**6
                          },index =[0])
        FinD1=pd.concat([new_row, FinD]).reset_index(drop = True)
        
        FinD1['cumsum_Cash_Flow_$']=FinD1['Gross_Cash_Flow_$'].cumsum()
        #st.dataframe(FinD1)
    
    
        #Paybackk Period Calculation
        def payback():
            final_full_year = FinD1[FinD1['cumsum_Cash_Flow_$'] < 0].index.values.max()
            fractional_yr = -FinD1['cumsum_Cash_Flow_$'][final_full_year]/FinD1['Gross_Cash_Flow_$'][final_full_year + 1]
            period = final_full_year + fractional_yr
            return round(period, 1)
    
        #st.write("Payback Period : ", payback(), "Years")
        PBP=payback()
    
        #Cash Flow Chart for 25 Years 
        sns.set_theme(style="whitegrid")
        fig, ax = plt.subplots(figsize=(6.4,4.8))
        ax = sns.barplot(x=FinD1.Year, y=FinD1['cumsum_Cash_Flow_$'], data=FinD1,ax=ax,palette = 'Spectral').set(title='Cumulative Cash Flow for 25 Years',ylabel='Cumulative Cash Flow ($)')
    
        plt.savefig("Cashflow_25.png")
        #st.pyplot()
    
        cash_flow = FinD1['Gross_Cash_Flow_$'].values
        FinD1['Time'] = [i for i in range(26)]
        t = FinD1['Time'].values
    
        def npv(irr, cashfs, t):  
            x =  np.sum(cashfs / (1 + irr) ** t)
            return round(x, 3)
    
        def irr(cashfs, t, x0, **kwargs):
            y = (fsolve(npv, x0=x0, args=(cashfs, t), **kwargs)).item()
            return round(y*100, 4)
    
        FinD1_sum=FinD1.sum(axis=0, skipna=True)
        #st.write(FinD1_sum['Yearly_OnM_Expense_$'])
        LCOE=value='{:.3f}'.format((FinD1_sum['Yearly_OnM_Expense_$']+Proj_Cost)/FinD1_sum.Yearly_Yield_kWh)
    
    
        CO2=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(0.709/1000))
        Cars=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(0.154/1000))
        Houses=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(0.129/1000))
        Trees=value='{:.0f}'.format(FinD1_sum.Yearly_Yield_kWh*(11.7/1000))
    
    
    
        #st.write(LCOE, CO2,Cars,Houses,Trees)
    
        NPV=npv(irr=0.10, cashfs=cash_flow, t=t)
        IRR=irr(cashfs=cash_flow, t=t, x0=0.10)
        Gross_25=value='{:.2f}'.format(FinD1_sum['Gross_Income_After_OnM']/10**6)
        PR=value="{:.2%}".format(df1_sum.E_Grid*1000/df1_sum.GlobInc/d.DC_Cap.max())
        Spec_E=value='{:.0f}'.format(FinD.Yearly_Yield_kWh.max()/DC)
        OnM_25=value='{:.2f}'.format(FinD1_sum['Yearly_OnM_Expense_$']/10**6)
    
        #st.write("NPV : $", NPV)
        #st.write("IRR : ", IRR,'%')
        #st.write(Gross_25,Spec_E)

        new_column = pd.DataFrame({'DC_Cap':DC,'AC_Cap':AC,'PV_Wp':PV_Wp,'Power_eff':P_eff,
                               'Proj_Cost':Proj_Cost,'Electricity_Tariff':Electricity_Tariff,
                               'OnM':OnM,'E_tariff':E_Tariff,'Tariff_esc':Tariff_esc,'OnM_esc':OnM_esc,
                               'Company_Name':Company_Name,'Company_representative':Company_representative,
                               'email_id':email_id,'Country':Country,
        'E_Grid':E_Grid,'PR':PR,'Spec_E':Spec_E,'Gross_25':Gross_25,
                               'LCOE':LCOE,'PBP':PBP,'IRR':IRR,
                               'CO2':CO2,'Cars':Cars,'Houses':Houses,'Trees':Trees,'NPV':NPV
                               },index =[0])
    
    
        new_column.to_csv('data/d2.csv')
    
    
    
        #-------------------PDF Report-----------------------
       
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.9rem;font-size:4px;border-radius:4px;"><span style="font-size: 36px;"><b>SOLAR DATA ANALYTICS - SUMMARY<b></span><br><span style="font-size: 18px;">{Company_Name}&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;||&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Presented By {Company_representative}</span></p>', unsafe_allow_html=True)
        
        st.write('\n')
        st.write('\n')
        #st.write('\n')
        st.write(f'<p style="background-color:#5981B5;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:10px;border-radius:1px;"><b></b></p>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        
        #E_grid, DC, AC Capacity, Annual PR
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        
        
        col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Plant DC Capacity</b></p>', unsafe_allow_html=True)
        col3.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Annual Energy Yield</b></p>', unsafe_allow_html=True)
        col4.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Annual PR</b></p>', unsafe_allow_html=True)
        col5.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:20px;border-radius:6px 6px 0px 0px;"><b>Plant AC Capacity</b></p>', unsafe_allow_html=True)
        
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        DC_m=value=str(float("{:.2f}".format(DC)))+" kWp"
        PR_m=PR
        E_Grid_m=value=str(float(format(E_Grid)))+" MWh"
        AC_m=value=str(float("{:.2f}".format(AC)))+" kW"
        
        col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{DC_m}</b></p>', unsafe_allow_html=True)
        col3.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{E_Grid_m}</b></p>', unsafe_allow_html=True)
        col4.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{PR_m}</b></p>', unsafe_allow_html=True)
        col5.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.6rem;font-size:30px;border-radius:0px 0px 6px 6px;"><b>{AC_m}</b></p>', unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        #Project cost, SPec Yield, Gross income
        col1,col2,col3,col4,col5=st.columns((0.1,1.6,1.6,1.6,0.1))
        
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Gross Solar Income after 25 Years:<br>USD ${Gross_25} Millions</b></p>', unsafe_allow_html=True)
        col3.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Specific Energy Yield:<br>{Spec_E} kWh/kWp/Yr</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Upfront Project Cost:<br>USD ${Proj_Cost} Millions</b></p>', unsafe_allow_html=True)
        
        #GII,GHI Graph, E_grid Graph, Tariff, O&M and Escalations
        col1,col2,col3,col4,col5=st.columns((0.2,1.65,0.1,1.65,0.2))
        col2.image('Monthly_E_Grid.png')
        col4.image('Monthly_GHI_GII.png')
        
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:7px 7px 0px 0px;"><b>{Electricity_Tariff}: ${E_Tariff} USD/kWh</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:7px 7px 0px 0px;"><b>Yearly O&M Cost: {OnM}% of Total Project Cost</b></p>', unsafe_allow_html=True)
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:0px 0px 7px 7px;"><b>Year-On-Year Escalation: {Tariff_esc}%</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:0px 0px 7px 7px;"><b>Year-On-Year Escalation: {OnM_esc}%</b></p>', unsafe_allow_html=True)
        
        #Cashflow Graph
        col1,col2,col3=st.columns((0.75,1.5,0.75))
        col2.image('Cashflow_25.png')
        NPV_m=value="{:.3f}".format(NPV/(10**6))
        
        col1,col2,col3,col4,col5=st.columns((0.55,1.2,1.5,1.2,0.55))
        st.write('\n')
        st.write('\n')
        col4.markdown(f'<p style="background-color:#498AAA;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Net Present Value (NPV):<br>USD $ ({(NPV_m)}) Millions</b></p>', unsafe_allow_html=True)
        col2.markdown(f'<p style="background-color:#DC765A;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:20px;border-radius:3px;"><b>Total O&M Expenses in 25 Years:<br>USD $ {OnM_25} Millions</b></p>', unsafe_allow_html=True)
        st.write('\n')
        #LCOE, PBP, IRR
        col1,col2,col3,col4,col5=st.columns((0.1,1.6,1.6,1.6,0.1))
        
        col2.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:3px;"><b>LCOE:<br>${LCOE} USD/kWh</b></p>', unsafe_allow_html=True)
        col3.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:3px;"><b>Simple Payback Period:<br>{PBP} Years</b></p>', unsafe_allow_html=True)
        col4.markdown(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:3px;"><b>Internal Rate of Return:<br>{IRR}%</b></p>', unsafe_allow_html=True)
        
        #Carbon Offset
        col1,col2,col3,col4=st.columns(4)
        
        
        #divider
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:4px;border-radius:1px;"><b></b></p>', unsafe_allow_html=True)
        #images
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        file_ = open("images/co2-cloud.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col2.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        file_ = open("images/car.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col3.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        file_ = open("images/green-home.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col4.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        file_ = open("images/park.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        col5.markdown(
        f'<p style="text-align:center;"><img src="data:image/png;base64,{data_url}" alt="co2"></p>',
        unsafe_allow_html=True,)
        
        
        #text
        col1,col2,col3,col4,col5,col6=st.columns((0.1,1.45,1.45,1.45,1.45,0.1))
        col2.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{CO2}</b><br>Tonnes of CO2 Offset per Year</p>', unsafe_allow_html=True)
        col3.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{Cars}</b><br>Cars Taken off from the Road</p>', unsafe_allow_html=True)
        col4.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{Houses}</b><br>Houses Energy Met per Year</p>', unsafe_allow_html=True)
        col5.write(f'<p style="background-color:#FFFFFF;color:#1F306B;text-align:center;padding:0.6rem;font-size:22px;border-radius:0px 0px 6px 6px;"><b>{Trees}</b><br>Tree Seedlings grown in 10 Years</p>', unsafe_allow_html=True)
       
        #divider
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.1rem;font-size:4px;border-radius:1px;"><b></b></p>', unsafe_allow_html=True)
        
        #Footer
        file_ = open("images/linkedin.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        
        file_ = open("images/github.png", "rb")
        contents = file_.read()
        data_url1 = base64.b64encode(contents).decode("utf-8")
        file_.close()
        
        
        st.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.3rem;font-size:13px;border-radius:7px 7px 7px 7px;">DEVELOPED BY AMRIT MANDAL&emsp;&emsp;|&emsp;&emsp;<b>Contact @ </b><a href="https://www.linkedin.com/in/amritmandal/"><img src="data:image/png;base64,{data_url}" alt="co2"></a></p>', unsafe_allow_html=True)
@app.addapp(title='Tutorial',icon='🗺')
def tutorialNo ():
    col1,col2,col3=st.columns((0.005,2.99,0.005))
    col2.write(f'<p style="background-color:#1F306B;color:#FFFFFF;text-align:center;padding:0.4rem;font-size:26px;border-radius:7px 7px 7px 7px;"><b>Guide to kPVIZ Including Data Upload Methods for PVSyst & Helioscope</b></p>', unsafe_allow_html=True)
    
    col1,col2,col3=st.columns((.5,2,.5))
    col2.header('Guide to Prepare PVSyst Data to be Uploaded into kPVIZ')
    with col2.expander(f"Guide for PVSyst_6.8 OR Higher Version"):
        #Step-1
     st.write("""
         <p><span style="text-decoration: underline;"><strong>STEP-1:</strong></span> First, Open PVSyst from your system. Then Under the Grid-Connected Tab, Create your PV System Design. Now, After setting the parameters of System, detailed losses, Near Shadings and other values, Now, Click on the "<em><strong>Advanced Simul.</strong></em>" Option on the right side as shown in the below picture.</p>
     """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture2.png")
     #Step-2
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-2:</strong></span> Now after you click on "<em><strong>Advanced Simul.</strong></em>", a new window will open as shown here. In this window, select <em><strong>"Output File"</strong></em> Option.</p>
              """,unsafe_allow_html=True)
     st.image("tuts/pvsyst/Picture3.png") 
    
     #Step-3
     st.write('\n')
     st.write("""
             <p><span style="text-decoration: underline;"><strong>STEP-3:</strong></span> As you click on <em><strong>"Output File"</strong></em> Option, again another window will open. Inside this window, first, on the Top left corner, select <em><strong>"File Name"</strong></em> and if you wish to change the output csv file, then please go ahead otherwise let other parameters <em><strong>unchanged</strong></em> on the <strong><em>left tab</em></strong> as shown below.&nbsp;</p>
              """,unsafe_allow_html=True)
     st.image("tuts/pvsyst/Picture4.png") 
     st.write('\n')
     #step-4
     st.write('\n')
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-4:</strong></span> Now under the Simulation variables section under the same tab as previous step, first, <strong>select</strong> <em><strong>GlobInc</strong></em> under <em><strong>InColl</strong></em> group, and <em><strong>un-check Globeff</strong></em> parameter.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture5.png") 
     st.write('\n')
     #step-5
     st.write('\n')
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-5:</strong></span> Next, Under the <em><strong>MetData</strong></em> group, select <em><strong>GlobHor, DiffHor</strong></em> and <em><strong>T_Amb</strong></em>. Follow the picture below for reference.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture6.png") 
     st.write('\n')
     
     
     #step-6
     st.write('\n')
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-6</strong></span>: Next, Under the <strong>Array</strong> group, select <em><strong>EArray, TArray, IArray, UArray</strong></em> and<em><strong> ArrayOn</strong></em> parameters.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture7.png") 
     st.write('\n')
     
     #step-7
     st.write('\n')
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-7:</strong></span> Similarly, Under the <strong>System</strong> group, Select only<strong><em> E_Grid</em></strong> parameter and in <em><strong>NormFac</strong></em> group, <strong>Un-check</strong> the <em><strong>PR</strong></em> Parameters.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture8.png") 
     st.write('\n')
     
     
     #step-8
     st.write('\n')
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-8:</strong></span> Now, all the parameters selection is done &amp; ready to be saved in the <em><strong>output .csv</strong></em> file. The <strong>selected parameters</strong> can be seen on the<strong><em> right side tab</em></strong> of the same window. Click on <em><span style="text-decoration: underline;"><strong>OK</strong></span></em> and exit this window.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture9.png") 
     st.write('\n')
     
     
     #step-9
     st.write('\n')
     st.write("""
              <p><strong><span style="text-decoration: underline;">STEP-9:</span></strong> Back to the "<em><strong>Advanced Simul.</strong></em>" window, click on <em><strong>Simulation</strong></em> on the <em>bottom left corner</em> of the window and <em><strong>start</strong></em> the project simulation. It'll take few seconds to complete the simulation.&nbsp;</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture10.png") 
     st.write('\n')
     
     
     #step-10
     st.write('\n')
     st.write("""
             <p><span style="text-decoration: underline;"><strong>STEP-10:</strong></span> After the simulation done, your <em><strong>output.csv</strong></em> file is ready and the path to file is now showing in your pvsyst window. Else, you can directly go to <em>path/users/(your_user_name)/pvsyst7.0_Data/UserHourly</em> folder.</p> 
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture11.png")
     st.write('\n')
     st.write('**NEXT**')
     st.image("tuts/pvsyst/Picture12.png")
     st.write('\n')
     st.write('**NEXT**')
     st.image("tuts/pvsyst/Picture13.png")
     st.write('\n')
     
     #step-11
     st.write('\n')
     st.write("""
             <p><span style="text-decoration: underline;"><strong>STEP-11:</strong></span> Now, open the Folder and select your recently generated <em><strong>hourly data csv file</strong></em> for your grid-connected project. Open the .csv file and follow the <em><strong>next steps for Data cleaning</strong></em>.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture14.jpg") 
     st.write('\n')
     
     
     #step-12
     st.write('\n')
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-12:</strong></span> Now as shown in the below picture, first select the first 10 rows and simply delete them.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture15.jpg") 
     st.write('\n')
     
     #step-13
     st.write('\n')
     st.write("""
              <p><span style="text-decoration: underline;"><strong>STEP-13:</strong></span> Again, after the deleting first 10 rows, now delete the unit rows and the row below it. And save the .csv file.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/pvsyst/Picture16.png") 
     st.write('\n')
     
     #Uploading data into kPVIZ
    col1,col2,col3=st.columns((.5,2,.5))
    col2.header('Guide to Upload Data & Explore kPVIZ')
    with col2.expander(f"Step by Step Guide to Upload Data & Explore kPVIZ"):
        #Step-1
     st.write("""
         <p><span style="text-decoration: underline;"><strong>STEP-1:</strong></span> First, Go to the <em><strong>"Upload Your Data"</strong></em> Page. You'll see a <em><strong>Form</strong></em> at the top. Please Fill up all the inputs with correct values and info inside the form. After completing the form, click on <em><strong>"SUBMIT"</strong></em>.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/kpviz_1.png")
     st.write('\n')
     st.image("tuts/kpviz_2.png")
     #Step-2
     st.write("""
              <p><strong><span style="text-decoration: underline;">STEP-2:</span></strong> After you click <em><strong>"SUBMIT"</strong></em> button on the form, you'll see a <em><strong>"Data Upload"</strong></em> option pop-up on that window. Now, upload your <em>PVSyst/Helioscope</em> data as per the previous instructions for <span style="text-decoration: underline;"><a href="#guide-to-prepare-pvsyst-data-to-be-uploaded-into-kpviz"><strong>PVSyst</strong></a></span> / <span style="text-decoration: underline;"><strong><a href="kpviz.herokkuapp.com/#">Helioscope</a></strong></span>.</p>
              """,unsafe_allow_html=True)
     st.image("tuts/kpviz_2.png") 
    
     #Step-3
     st.write('\n')
     st.write("""
             <p><strong><span style="text-decoration: underline;">STEP-3</span></strong>: After you upload the <em><strong>.csv/xlsx</strong></em> file into the app, Now Click on <em><strong>Load Data</strong></em> option. Now, you are good to go!!</p>
              """,unsafe_allow_html=True)
     st.image("tuts/kpviz_3.png") 
     st.write('\n')
     #step-4
     st.write('\n')
     st.write("""
              <p><strong><span style="text-decoration: underline;">STEP-4:</span></strong> After you upload your Solar Data, now the kPVIZ App will analyze your data and create <strong><em>EDA plots, Hourly Plots, Daily Plots for any specific month, and Monthly Data plots.</em></strong> Navigate through the <em><strong>Top Horizontal Menu Bar</strong></em> to explore the kPVIZ app.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/kpviz_4.png") 
     st.write('\n')
     #step-5
     st.write('\n')
     st.write("""
              <p><strong><span style="text-decoration: underline;">STEP-5:</span></strong> As you can see in the below picture, the graphs are highly interactive and you can save the plots as image format into your local system directly.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/kpviz_5.png") 
     st.write('\n')
     
     
     #step-6
     st.write('\n')
     st.write("""
              <p><strong><span style="text-decoration: underline;">STEP-6:</span></strong> On the <em><strong>Summary Report</strong></em> Page, You'll find the High Quality One Page <em><span style="text-decoration: underline;"><strong>Techno-Commercial Summary</strong></span></em> Details of your Solar Project.</p>
              """,unsafe_allow_html=True)
     st.write('\n')
     st.image("tuts/kpviz_6.png") 
     st.write('\n')
     


#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()
