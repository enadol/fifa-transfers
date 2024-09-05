"""Modules providing a function printing python version."""
import pandas as pd
import plotly.express as px
import streamlit as st

#read excel file "transfers_global_FIFA.xlsx" and assign it to a variable called df as DataFrame
df = pd.read_excel("transfers_global_FIFA.xlsx")


#check the first 5 rows of the dataframe to see
# if the new columns are created correctly
print(df.head())

#check the last 5 rows of the dataframe to see
# if the new columns are created correctly
print(df.tail())

#check the data types of the columns of the dataframe
#to see if the new columns are created correctly
print(df.dtypes)

#create function to group and sum by Confederation
#and sort by Transfers Balance in descending order
def group_and_sum(data_source, column_name):
    """Function grouping by Confedaration and summing the values of a column."""
    return data_source.groupby('Confederation')[column_name].sum().sort_values(ascending=False)

#use the function to group and sum the Transfers Spent column
transfers_spent = group_and_sum(df, 'Transfers Spent')

#use the function to group and sum the Transfers received column
transfers_received = group_and_sum(df, 'Transfers received')

#use the function to group and sum the Transfers Balance column
transfers_balance = group_and_sum(df, 'Transfers Balance')

#print the results
print("Fees received:\\n", transfers_received)
print("Fees spent:\\n", transfers_spent)


#visualize the confederations balance with a bar chart
#im plotly
fig = px.bar(transfers_balance, x=transfers_balance.index,\
y=transfers_balance.values, title="Transfers Balance by Confederation")
#change the color of the bars to green if the value is positive and red if the value is negative
fig.update_traces(marker_color=['green' if x >= 0 else 'red' for x in transfers_balance.values], \
marker_line_color='rgb(8,48,107)', marker_line_width=1.5,\
      opacity=0.6, selector=dict({'type':'bar'}))
#change the size of the bars to 0.5
fig.update_traces(width=0.5)

#show in streamlit
st.plotly_chart(fig)
