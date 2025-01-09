import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as pa


plt.figure(figsize=(11,8))
covid = pd.read_csv("StatewiseTestingDetails.csv")

print(covid)
state=covid[(covid["State"]=="West Bengal") | (covid["State"]=="Maharashtra")]
state=state 
#print(state)
#covid_grouped=covid.groupby()
'''
#MAtplotlib
plt.plot(state["Date"],state["Positive"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
'''

#Plotly
#grouped_positive=covid.groupby("State").agg({
#    "Positive":"sum"
#}).reset_index()

#ma_mah=covid[covid["State"]=="Maharashtra"]["Positive"].max()
#print(ma_mah)

fig=pa.line(covid,x="Date",y="Positive", hover_name="State", color="State",title="Trend of Positive Covid-19 Cases Over Time")
fig.show()
fig=pa.bar(covid,x="State",y="Positive", hover_name="Date", color="State",title="Covid-19 Positive Cases Across State")
fig.show()



