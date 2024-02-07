import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import xlwings as xw
from PIL import Image


st.set_page_config(page_title="IIT",layout="wide",initial_sidebar_state='expanded')

def main_page():
    st.title("DATA ANALYSIS")
    st.header(":red[USING PYTHON]")
    st.subheader("PROJECT DASHBOARD")
    st.markdown("---")
   
   
   
   

def page2():
    df=pd.read_excel(io='final.xlsx',engine='openpyxl',sheet_name='Sheet1',usecols='A:K',nrows=3323)
   
    cate=st.sidebar.multiselect('Charts based on Type:',options=df["Type"].unique(),default=df["Type"].unique())

    dep=st.sidebar.multiselect('Charts based on Department:',options=df["DepartmentCode"].unique(),default=df["DepartmentCode"].unique())
   
   

    st.sidebar.subheader('Admin')
   
   
def page3():
        st.title("DATA ANALYSIS")
        st.header("USING PYTHON")
        st.subheader("PROJECT DESCRIPTION")
        st.markdown("-----")
        df__name=pd.read_excel(io='final.xlsx',engine='openpyxl',sheet_name='Sheet1',usecols='A:I',nrows=3323)
        df__name.dropna(inplace=True)
       
       
        pie_chart=px.pie(df__name,title="Chart on Type of Projects done:",values="Year",names="Type")
        st.plotly_chart(pie_chart)

def page4():
        st.title("DATA ANALYSIS")
        st.header("USING PYTHON")
        st.subheader("PROJECT DESCRIPTION")
        st.markdown("---")
        st.header("Table and Pie-Chart based on Type:")
        dfname=pd.read_excel(io='final.xlsx',engine='openpyxl',sheet_name='Sheet1',usecols='A:I',nrows=3323)
        dfname.dropna(inplace=True)
        
        dfname = pd.read_excel(io='final.xlsx', engine='openpyxl', sheet_name='Sheet1', usecols='A:I', nrows=3323)
        dfname.dropna(inplace=True)

        namess = dfname["Type"].unique()
        type_counts = dfname["Type"].value_counts()
        values = type_counts.values.tolist()  # Convert counts to a list
        names = type_counts.index.tolist()    # Convert types to a list

        pfms = px.pie(dfname,values=values, names=names, title="Type-wise:")
        st.plotly_chart(pfms)
       
        
       
def page5():
        st.title("DATA ANALYSIS")
        st.header(":red USING PYTHON")
        st.subheader("PROJECT DESCRIPTION")
        st.markdown("---")
        st.header("Table and Pie-Chart based on Department:")
        dfname1 = pd.read_excel(io='final.xlsx', engine='openpyxl', sheet_name='Sheet1', usecols='A:H', nrows=3323)
        dfname1.dropna(inplace=True)

        namess = dfname1["DepartmentCode"].unique()
        type_counts = dfname1["DepartmentCode"].value_counts()
        values = type_counts.values.tolist()  # Convert counts to a list
        names = type_counts.index.tolist()    # Convert departments to a list

        pfms1 = px.pie(values=values, names=names, title="Department-wise:")
        st.plotly_chart(pfms1)        
 
def page6():
        st.title("DATA ANALYSIS")
        st.header(":red USING PYTHON")
        st.subheader("PROJECT DESCRIPTION")
        st.markdown("---")
        st.header("Table and Pie-Chart based on Year:")
        dfname2=pd.read_excel(io='final.xlsx',engine='openpyxl',sheet_name='Sheet1',usecols='A:H',nrows=3323)
        dfname2.dropna(inplace=True)
     
        years_unique = dfname2["Year"].unique()
        year_counts = dfname2["Year"].value_counts()
        values = year_counts.values.tolist()  # Convert counts to a list
        names = year_counts.index.tolist()    # Convert years to a list

        pms1 = px.pie(values=values, names=names, title="Year-wise:")
        st.plotly_chart(pms1)
 
 
def page7():
        st.title("DATA ANALYSIS")
        st.header(":red USING PYTHON")
        st.subheader("PROJECT DESCRIPTION")
        st.markdown("---")
        st.header("Table and Pie-Chart based on PI:")
        dfname3=pd.read_excel(io='final.xlsx',engine='openpyxl',sheet_name='Sheet1',usecols='A:H',nrows=3323)
        dfname3.dropna(inplace=True)
       
        pi_unique = dfname3["PI"].unique()
        pi_counts = dfname3["PI"].value_counts()
        values = pi_counts.values.tolist()  # Convert counts to a list
        names = pi_counts.index.tolist()    # Convert PI names to a list

        pm1 = px.pie(values=values, names=names, title="PI-wise:")
        st.plotly_chart(pm1)
         
 
page_names_to_funcs = {
    "MAIN PAGE": main_page,
    "DETAILS": page2,
    "OVERALL": page3,
    "TYPE": page4,
    "DEPARTMENT":page5,
    "YEAR":page6,
    "PI":page7    
    }

st.sidebar.header('Main Menu')
selected_page = st.sidebar.selectbox("DOMAIN", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
if(st.sidebar.button("ADMIN LOGIN")):
    name = st.text_input("Enter Your name", "Type Here ...")
    id1=st.text_input("Enter Your ID", "Type Here ...")
    uploaded_file = st.file_uploader("Choose a file")
