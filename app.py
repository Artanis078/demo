# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:59:05 2022

@author: 
"""

# streamlit run C:\PBI\Streamlit\derby01.py

import streamlit as st
import pandas as pd
import numpy as np


#choix du fichier excel
#excel_file = 'C:\PBI\Streamlit\DerbyStreamlit.xlsx'
#sheet_name = 'IGRF'

st.set_page_config(page_title = "StatsXX",
                   page_icon = ":telescope:",
                   layout = "centered"
                   )


# ---- READ EXCEL ----
@st.cache
def get_data_from_excel(filename,datasheet):
    
    df = pd.read_excel(
        io = filename,
        engine = 'openpyxl',
        sheet_name = datasheet,
        usecols='A:D',
        )

    
    #df.colums = ['Cable Length','Theta','No.']
    #df["hour"] = pd.to_datetime(df["Time"],format="%H:%M:%S").dt.hour
    return df

# recupe nom equipe 1
def equipe01(filename,datasheet):
    
    E1 = pd.read_excel(
        io = filename,
        engine = 'openpyxl',
        sheet_name = datasheet,
        nrows=0,
        usecols='A',
        )
    
    return E1



df = get_data_from_excel('C:\PBI\Streamlit\DerbyStreamlit.xlsx','01')
Home_team = equipe01('C:\PBI\Streamlit\DerbyStreamlit.xlsx','01')
#df = df.drop(index = 0)

#df.ix[10,'B']

print (df.head())
#df = pd.read_excel(excel_file,
 #                  sheet_name=sheet_name,
  #                 usecols='B,C')

# AFFICHER UNE CELLULE
#-------------------------
#import openpyxl
#wb = openpyxl.load_workbook(‘workbook.xlsx’)
#sheet = wb[‘data’]
#C1 = sheet[‘C1’] # read direct value in cell C1
#C1 = sheet.cell(row=1,column=3) # or this has the same effect

#print(C1.value)
#------------------------------




#Titre page
st.title('TITRE')

#st.subheader('paragraphe')
st.subheader('Equipe')



# ----SIDEBAR----
st.sidebar.header("Liste Graphique")




st.dataframe(Home_team)
# conversion suite bug version pour afficher texte
test = df.astype(str)
#st.dataframe(test,  width=1900 , height=630)
st.table(test)
#st.dataframe(df)
