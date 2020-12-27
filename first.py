#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings

st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("This is mine")
st.write("Hello i am new here")

df = pd.read_csv('tips.csv')
tips = df.head(10)
st.table(tips)

st.header("Visualisation Using Seaborn")
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()

st.subheader("Joinplot")
sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
st.pyplot()

