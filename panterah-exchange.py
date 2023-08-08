import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center; color: pink;'>Panterah Exchange</h1>", unsafe_allow_html=True)


df = pd.read_csv('history-caffe.csv')
df2 = pd.read_csv('history-ape.csv')

with st.container():
    col1, col2 = st.columns([6,2])
    with col1:
        value = round(df['€'][0],2)
        st.subheader(f':violet[Oggi un _caffé_ :coffee:  del Pantera vale:] {value}€')
        st.line_chart(df, x ='Giorno', y='€')

    with col2:    
        value = str(round(df['€'][0],2)) + "€"
        var = str(round(df['Var'][0],2)) + "%"
        delta = round(df['Var'][0]-df['Var'][1],2)
        st.metric('Variazione', value=var, delta=delta)

#####
with st.container():
    col1, col2 = st.columns([6,2])
    with col1:
        value2 = round(df2['€'][0],2)
        st.subheader(f':orange[Oggi un _aperitivo_ :cocktail: del Pantera vale:] {value2}€')
        st.line_chart(df2, x ='Giorno', y='€')

    with col2:    
        value2 = str(round(df2['€'][0],2)) + "€"
        var2 = str(round(df2['Var'][0],2)) + "%"
        delta2 = round(df2['Var'][0]-df2['Var'][1],2)
        st.metric('Variazione', value=var2, delta=delta2)



st.text(f'Ultimo Aggiornamento {df['Giorno'][len(df)]}')
