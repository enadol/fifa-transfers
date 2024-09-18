"""Modules providing a function printing python version."""
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(layout="wide", page_title="FIFA Transfer Market Analysis")
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

#create head section and add tag for keywords als metadata
st.markdown("<head><meta name='keywords' content='FIFA, \
    Transfer Market, football, transfers, Analysis, Men's Football,\
     Summer 2024, FIFA Transfer Market Report 2024, FIFA Member Association,\
            Transfers Balance, Transfers Spent, Transfers received,\
            Confederation, Member Association, Data Visualization,\
            Streamlit, Python, Pandas, Plotly, FIFA Transfer Market\
            Analysis, FIFA Transfer Market Report, FIFA Transfer Market \
            Data, FIFA Transfer Market Statistics, FIFA Transfer Market\
            Analysis Tool, FIFA Transfer Market Analysis Dashboard, FIFA \
            Transfer Market Analysis App, FIFA Transfer Market Analysis \
            Web App, FIFA Transfer Market Analysis Tool, FIFA Transfer \
            Market Analysis Dashboard, FIFA Transfer Market Analysis App, \
            FIFA Transfer Market Analysis Web App'></head>", unsafe_allow_html=True)
#add other elements relevant for Search Engine Optimization
st.markdown("<meta name='description' content='This page displays \
            a Transfer Market Analysis of men international football \
             for the summer of 2024. The data used is from the FIFA Transfer \
            Market Report 2024, published by FIFA in september 2024. \
            The data includes the total amount of money spent and received \
            by each FIFA member association (federation) in the summer transfer\
            window of 2024. The data is displayed in a bar chart, which can be \
            filtered by Confederation or Member Association, and by the type of\
            data displayed (Transfers Balance, Transfers Spent, Transfers\
            received).'/>", unsafe_allow_html=True)
st.markdown("<meta name='author' content='Enrique Adolfo López Magallón'/>", unsafe_allow_html=True)
st.markdown("<meta name='viewport' content='width=device-width, \
            initial-scale=1.0'/>", unsafe_allow_html=True)

#add a title to the page. "FIFA TRANSFER MARKET ANALYSIS" in bold and bigger font
st.markdown("<h1 style='text-align: center; color: black;'>\
            FIFA TRANSFER MARKET ANALYSIS</h1>", unsafe_allow_html=True)
#add a subtitle to the page. "SUMMER 2024" in bold and smaller font
st.markdown("<h2 style='text-align: center; color: black;'>\
            MEN'S FOOTBALL - SUMMER 2024</h2>", unsafe_allow_html=True)

#read excel file "transfers_global_FIFA.xlsx" and assign
#  it to a variable called df as DataFrame
df = pd.read_excel("transfers_global_FIFA.xlsx")

#Rename column Transfers received to Transfers Received
#and Transfers spent to Transfers Spent
df.rename(columns={'Transfers received': 'Transfers Received'}, inplace=True)
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
transfers_received = group_and_sum(df, 'Transfers Received')

#use the function to group and sum the Transfers Balance column
transfers_balance = group_and_sum(df, 'Transfers Balance')

#print the results
print("Fees received:", transfers_received)
print("Fees spent:", transfers_spent)
print("Transfers Balance:", transfers_balance)

#make streamlit sidebar with a dropdown menu
#options to choose between graphs:
#"Fees spent", "Fees received", "Balance"
#and a button to show the graph
#the default option is "Balance"
#the default button is "Show Graph"
#the title of the sidebar is "Select a graph"
#the title of the dropdown menu is "Graph type"
#the title of the button is "Show Graph"
#the title of the page is "FIFA TRANSFERS BALANCE BY CONFEDERATION (SUMMER 2024)"
#the page should be wide
with st.sidebar:
    select_data = st.selectbox("Select data", ["Transfers Balance", "Transfers Spent", \
                                               "Transfers Received"], index=2)
    select_filter=st.selectbox("Select filter", ["Per Confederation Aggregate",\
                                                  "Per Confederation Countries"], index=0)
    if select_filter == "Per Confederation Countries":
        select_confederation = st.selectbox("Select Confederation",\
                                             df['Confederation'].unique(), index=0)
    show_graph = st.button("Show Graph")
#if select_filter is "Per Confederation Aggregate", group data by Confederation and sum
# the values of the selected column
#if select_filter is "Per Confederation Countries", filter df
#by Confederation and select the selected column
if select_filter == "Per Confederation Aggregate":
    if select_data == "Transfers Balance":
        data = transfers_balance
    elif select_data == "Transfers Spent":
        data = transfers_spent
    elif select_data == "Transfers Received":
        data = transfers_received
elif select_filter == "Per Confederation Countries":
    if select_confederation:
        if select_data == "Transfers Balance":
            data = df[df['Confederation'] == select_confederation]["Transfers Balance"]
        elif select_data == "Transfers Spent":
            data = df[df['Confederation'] == select_confederation]["Transfers Spent"]
        else:
            data = df[df['Confederation'] == select_confederation]["Transfers Received"]
#create and show graph to be displayed with the filtered data
#the graph should be a bar chart
#the x-axis should be the Confederation or Member Association depending on the filter selected
#the y-axis should be values of the selected column
#the title of the graph should be the selected column
#the title of the x-axis should be the Confederation or Country depending on the filter selected
#the title of the y-axis should be the selected column
#the color of the bars should be green id positive, red if negative value
#the graph should be displayed in the main page of the streamlit app
#the graph should be displayed only if the button "Show Graph" is clicked
if show_graph and select_filter == "Per Confederation Aggregate":
    fig = px.bar(data, x=data.index, y=data.values, title=select_data, color=data.keys())
    #format interactive hover text to show the value of the selected column and the
    #  Confederation or Country depending on the filter selected
    fig.update_traces(hovertemplate='<b>Confederation: %{x}</b><br>%{y:,.0f} (USD)')
    fig.update_layout(xaxis_title="Confederation", yaxis_title=select_data, paper_bgcolor="oldlace")
    st.plotly_chart(fig, use_container_width=True)
elif show_graph and select_filter == "Per Confederation Countries":
    fig = px.bar(df[df['Confederation'] == select_confederation], x='Member Association', \
        y=data.values, title=select_data, color='Member Association')
    #format interactive hover text to show the value of the selected
    # column and the Confederation or Country depending on the filter selected
    fig.update_traces(hovertemplate='<b>Member country: %{x}</b><br>%{y:,.0f} (USD)')
    fig.update_layout(xaxis_title="Member Association", yaxis_title=select_data, \
                      paper_bgcolor="oldlace")
    st.plotly_chart(fig, use_container_width=True)
#add a text area to the page with a title "About" and a short description
#of the page and the data used
st.markdown("<h3 style='text-align: center; color: black; \
    font-size: 20px;'>About this tool</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black; font-size: 12px;'>\
    This page displays a Transfer Market Analysis of men's international football \
    for the summer of 2024. The data used is from the FIFA Transfer Market Report 2024, \
    published by FIFA in september 2024. The data includes the total amount of money \
    spent and received by each FIFA member association (federation) in the summer transfer \
    window of 2024. The data is displayed in a bar chart, which can be filtered by Confederation \
    or Member Association, and by the type of data displayed (Transfers Balance, Transfers Spent, \
    Transfers received). The graph can be interacted with by hovering over the bars to see the exact \
    value of the transfer, and by clicking on the legend to hide or show the data for a specific \
    Confederation or Member Association. Development: Enrique Adolfo López Magallón - \
    @EnriqueALopezM</p>", unsafe_allow_html=True)

#add a link to the source of the data used in the page
st.markdown("<p style='text-align: center; color: black; font-size: 12px;'>Data source: \
<a href='https://inside.fifa.com/legal/football-regulatory/international-transfer-snapshot/men'>\
FIFA Transfer Market Report 2024</a></p>", unsafe_allow_html=True)

st_autorefresh(interval=60 * 60 * 1000, key="dataframerefresh")