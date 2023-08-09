import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center; color: pink;'>Panterah Exchange</h1>", unsafe_allow_html=True)


df = pd.read_csv('history-caffe.csv')
df2 = pd.read_csv('history-ape.csv')

ultima_riga = len(df)-1
with st.container():
    col1, col2 = st.columns([6,2])
    with col1:
        value = round(df['€'][ultima_riga],2)
        st.subheader(f':violet[Oggi un _caffé_ :coffee:  del Pantera vale:] {value}€')
        st.line_chart(df, x ='Giorno', y='€')

    with col2:    
        value = str(round(df['€'][ultima_riga],2)) + "€"
        var = str(round(df['€'][ultima_riga]-df['€'][ultima_riga-1],2)) + "€"
        delta = str(round(df['Delta'][ultima_riga],2)) + "%"
        st.metric('Variazione', value=delta, delta=var)

#####
with st.container():
    col1, col2 = st.columns([6,2])
    with col1:
        value2 = round(df2['€'][ultima_riga],2)
        st.subheader(f':orange[Oggi un _aperitivo_ :cocktail: del Pantera vale:] {value2}€')
        st.line_chart(df2, x ='Giorno', y='€')

    with col2:    
        value2 = str(round(df2['€'][ultima_riga],2)) + "€"
        var2 = str(round(df2['€'][ultima_riga]-df2['€'][ultima_riga-1],2)) + "€"
        delta2 = str(round(df2['Delta'][ultima_riga],2)) + "%"
        st.metric('Variazione', value=delta2, delta=var2)


ultimo_aggiornamento = df['Giorno'][len(df)-1]
st.text(f'Ultimo Aggiornamento {ultimo_aggiornamento}')
