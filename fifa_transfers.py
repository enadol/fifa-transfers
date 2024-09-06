"""Modules providing a function printing python version."""
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
#add a title to the page. "FIFA TRANSFER MARKET ANALYSIS" in bold and bigger font
st.markdown("<h1 style='text-align: center; color: black;'>\
            FIFA TRANSFER MARKET ANALYSIS</h1>", unsafe_allow_html=True)
#add a subtitle to the page. "SUMMER 2024" in bold and smaller font
st.markdown("<h2 style='text-align: center; color: black;'>\
            SUMMER 2024</h2>", unsafe_allow_html=True)

#read excel file "transfers_global_FIFA.xlsx" and assign
#  it to a variable called df as DataFrame
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
<<<<<<< HEAD
    graph_type = st.selectbox("Select analysis", ["Balance", "Fees spent", "Fees received"], index=0)
    conf_type=st.selectbox(df['Confederation'].unique(), index=0)
    show_conf_graph = st.button("Show Confederations Totals")
    show_members_graph = st.button("Show Confederations per members")

#if the confederations button is clicked, show the graph for confederations
if show_conf_graph:
    if graph_type == "Balance":
        #visualize the confederations balance with a bar chart
        #im plotly. Change yaxis label to "Amount (USD)"
        fig = px.bar(transfers_balance, x=transfers_balance.index, y=transfers_balance.values, \
        labels={'x':'Confederation', 'y':'Amount (USD)'},\
        title="TRANSFERS BALANCE BY CONFEDERATION (SUMMER 2024)", width=1000, height=600)
        #change the color of the bars to green if the value
        #is positive and red if the value is negative
        fig.update_traces(marker_color=['green' if x >= 0 else \
                    'red' for x in transfers_balance.values], \
        marker_line_color='rgb(8,48,107)', marker_line_width=1.5,\
              opacity=0.6, selector=dict({'type':'bar'}))
        #change the size of the bars to 0.5
        fig.update_layout(bargap=0.5)
        #change the background color to white
        fig.update_layout(plot_bgcolor='white')
        #change the font color to black
        fig.update_layout(font_color='black')
        #change the title font size to 20
        fig.update_layout(title_font_size=20)
        #change the title font color to black
        fig.update_layout(title_font_color='black')
        #change the xaxis font size to 15
        fig.update_layout(xaxis_tickfont_size=15)
        #change the yaxis font size to 15
        fig.update_layout(yaxis_tickfont_size=15)
        #change the xaxis title font size to 20
        fig.update_layout(xaxis_title_font_size=20)
        #change the yaxis title font size to 20
        fig.update_layout(yaxis_title_font_size=20)
        #change the xaxis title font color to black
        fig.update_layout(xaxis_title_font_color='black')
        #change the yaxis title font color to black
        fig.update_layout(yaxis_title_font_color='black')
        #change the xaxis tick angle to 45 degrees
        fig.update_layout(xaxis_tickangle=45)
        fig.add_annotation(text="Source: FIFA", xref="paper", \
        yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=12))
        #show the graph
        st.plotly_chart(fig, use_container_width=True)
    elif graph_type == "Fees spent":
        #visualize the fees spent with a bar chart
        #im plotly. Change yaxis label to "Amount (USD)
        fig = px.bar(transfers_spent, x=transfers_spent.index, y=transfers_spent.values, \
        labels={'x':'Confederation', 'y':'Amount (USD)'},\
         title="FEES SPENT BY CONFEDERATION (SUMMER 2024)", width=1000, height=600)
        #change the color of the bars to green if the value
        #is positive and red if the value is negative
        fig.update_traces(marker_color=['green' if x >= 0 else \
                    'red' for x in transfers_spent.values], \
        marker_line_color='rgb(8,48,107)', marker_line_width=1.5,\
              opacity=0.6, selector=dict({'type':'bar'}))
        #change the size of the bars to 0.5
        fig.update_layout(bargap=0.5)
        #change the background color to white
        fig.update_layout(plot_bgcolor='white')
        #change the font color to black
        fig.update_layout(font_color='black')
        #change the title font size to 20
        fig.update_layout(title_font_size=20)
        #change the title font color to black
        fig.update_layout(title_font_color='black')
        #change the xaxis font size to 15
        fig.update_layout(xaxis_tickfont_size=15)
        #change the yaxis font size to 15
        fig.update_layout(yaxis_tickfont_size=15)
        #change the xaxis title font size to 20
        fig.update_layout(xaxis_title_font_size=20)
        #change the yaxis title font size to 20
        fig.update_layout(yaxis_title_font_size=20)
        #change the xaxis title font color to black
        fig.update_layout(xaxis_title_font_color='black')
        #change the yaxis title font color to black
        fig.update_layout(yaxis_title_font_color='black')
        #change the xaxis tick angle to 45 degrees
        fig.update_layout(xaxis_tickangle=45)
        fig.add_annotation(text="Source: FIFA", xref="paper", \
        yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=12))
        #show the graph
        st.plotly_chart(fig, use_container_width=True)
    else:
        #graph for fees received
        #visualize the fees received with a bar chart
        #im plotly. Change yaxis label to "Amount (USD)
        fig = px.bar(transfers_received, x=transfers_received.index, y=transfers_received.values, \
                     labels={'x':'Confederation', 'y':'Amount (USD)'},\
                     title="FEES RECEIVED BY CONFEDERATION (SUMMER 2024)", width=1000, height=600)
        #change the color of the bars to green if the value
        #is positive and red if the value is negative
        fig.update_traces(marker_color=['green' if x >= 0 else \
                    'red' for x in transfers_received.values], \
        marker_line_color='rgb(8,48,107)', marker_line_width=1.5,\
              opacity=0.6, selector=dict({'type':'bar'}))
        #change the size of the bars to 0.5
        fig.update_layout(bargap=0.5)
        #change the background color to white
        fig.update_layout(plot_bgcolor='white')
        #change the font color to black
        fig.update_layout(font_color='black')
        #change the title font size to 20
        fig.update_layout(title_font_size=20)
        #change the title font color to black
        fig.update_layout(title_font_color='black')
        #change the xaxis font size to 15
        fig.update_layout(xaxis_tickfont_size=15)
        #change the yaxis font size to 15
        fig.update_layout(yaxis_tickfont_size=15)
        #change the xaxis title font size to 20
        fig.update_layout(xaxis_title_font_size=20)
        #change the yaxis title font size to 20
        fig.update_layout(yaxis_title_font_size=20)
        #change the xaxis title font color to black
        fig.update_layout(xaxis_title_font_color='black')
        #change the yaxis title font color to black
        fig.update_layout(yaxis_title_font_color='black')
        #change the xaxis tick angle to 45 degrees
        fig.update_layout(xaxis_tickangle=45)

    if show_members_graph:
        df_filtered=df['Confederation'==show_members_graph]
        #graph for fees received by member association
        #visualize the fees received by member association with a bar chart
        #im plotly. Change yaxis label to "Amount (USD)
        fig = px.bar(transfers_received_by_member_association, x=transfers_received_by_member_association.index, y=transfers_received_by_member_association.values, \
                     labels={'x':'Member Association', 'y':'Amount (USD)'},\
                     title="FEES RECEIVED BY MEMBER ASSOCIATION (SUMMER 2024)", width=1000, height=600)
        #change the color of the bars to green if the value
        #is positive and red if the value is negative
        fig.update_traces(marker_color=['green' if x >= 0 else \
                    'red' for x in transfers_received_by_member_association.values], \
        marker_line_color='rgb(8,48,107)', marker_line_width=1.5,\
              opacity=0.6, selector=dict({'type':'bar'}))
        #change the size of the bars to 0.5
        fig.update_layout(bargap=0.5)
        #change the background color to white
        fig.update_layout(plot_bgcolor='white')
        #change the font color to black
        fig.update_layout(font_color='black')
        #change the title font size to 20
        fig.update_layout(title_font_size=20)
        #change the title font color to black
        fig.update_layout(title_font_color='black')
        #change the xaxis font size to 15
        fig.update_layout(xaxis_tickfont_size=15)
        #change the yaxis font size to 15
        fig.update_layout(yaxis_tickfont_size=15)
        #change the xaxis title font size to 20
        fig.update_layout(xaxis_title_font_size=20)
        #change the yaxis title font size to 20
        fig.update_layout(yaxis_title_font_size=20)
        #change the xaxis title font color to black
        fig.update_layout(xaxis_title_font_color='black')
        #change the yaxis title font color to black
        fig.update_layout(yaxis_title_font_color='black')
        #change the xaxis tick angle to 45 degrees
        fig.update_layout(xaxis_tickangle=45)
        #add annotation in bottom right position
        #font smaller. "Source: FIFA"
        fig.add_annotation(text="Source: FIFA", xref="paper", \
        yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=12))
        #show the graph
        st.plotly_chart(fig, use_container_width=True)
       
#add annotation in bottom right position
#font smaller. "Source: FIFA"
        fig.add_annotation(text="Source: FIFA", xref="paper", \
        yref="paper", x=1, y=-0.15, showarrow=False, font=dict(size=12))
#show the graph
        st.plotly_chart(fig, use_container_width=True)

#if the show_members is clicked, show Member Assocation graphs

=======
    select_data = st.selectbox("Select data", ["Transfers Balance", "Transfers Spent", \
                                               "Transfers received"], index=2)
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
    elif select_data == "Transfers received":
        data = transfers_received
elif select_filter == "Per Confederation Countries":
    if select_confederation:
        if select_data == "Transfers Balance":
            data = df[df['Confederation'] == select_confederation]["Transfers Balance"]
        elif select_data == "Transfers Spent":
            data = df[df['Confederation'] == select_confederation]["Transfers Spent"]
        else:
            data = df[df['Confederation'] == select_confederation]["Transfers received"]
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
    fig.update_layout(xaxis_title="Confederation", yaxis_title=select_data)
    st.plotly_chart(fig, use_container_width=True)
elif show_graph and select_filter == "Per Confederation Countries":
    fig = px.bar(df[df['Confederation'] == select_confederation], x='Member Association', \
        y=data.values, title=select_data, color='Member Association')
    #format interactive hover text to show the value of the selected 
    # column and the Confederation or Country depending on the filter selected
    fig.update_traces(hovertemplate='<b>Member country: %{x}</b><br>%{y:,.0f} (USD)')
    fig.update_layout(xaxis_title="Member Association", yaxis_title=select_data)
    st.plotly_chart(fig, use_container_width=True)
>>>>>>> 1bffee487e620c7f76eae7b06229d088081a5e60
