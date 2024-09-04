"""Modules providing a function printing python version."""
import pandas as pd
import plotly.express as px

#read excel file "transfers_global_FIFA.xlsx" and assign it to a variable called df as DataFrame
df = pd.read_excel("transfers_global_FIFA.xlsx")

#create columns 'Transfers Spent' and 'Transfers received'. Take the
#columns Transfer fees spent and Transfer fees received
# eliminate '.', if present, change "bn" to "000000000" else "m" to "000000" and else "k" to "000".
# Then change the data type to int
# make this a function
def convert_to_int(x):
    """Function converting columns with 'bn', 'm', 'k' to int."""
    if '.' in str(x):
        x = x.replace('.', '')
    if 'bn' in str(x):
        x = int(float(x.replace('bn', '')) * 1000000000)
    elif 'm' in str(x):
        x = int(float(x.replace('m', '')) * 1000000)
    elif 'k' in str(x):
        x = int(float(x.replace('k', '')) * 1000)
    else:
        x = int(x)
    return x

df['Transfers Spent'] = df['Transfer fees spent'].apply(convert_to_int)
df['Transfers received'] = df['Transfer fees received'].apply(convert_to_int)

#sum Transfers Spent
print("Total Transfers Spent: ", df['Transfers Spent'].sum())

#sum Transfers received
print("Total Transfers received: ", df['Transfers received'].sum())

#create a new dataframe without the colums
#Transfer fees spent and Transfer fees received
df_new = df.drop(['Transfer fees spent', 'Transfer fees received'], axis=1)

#on df_new create a new column 'Transfers Balance' which is
#the difference between the Transfers received and Transfers Spent columns
df_new['Transfers Balance'] = df_new['Transfers received'] - df_new['Transfers Spent']

#check the first 5 rows of the dataframe to see
# if the new columns are created correctly
print(df_new.head())

#check the last 5 rows of the dataframe to see
# if the new columns are created correctly
print(df_new.tail())

#check the data types of the columns of the dataframe 
#to see if the new columns are created correctly
print(df_new.dtypes)

#create function to group and sum by Confederation
#and sort by Transfers Balance in descending order
def group_and_sum(data_source, column_name):
    """Function grouping by Confedaration and summing the values of a column."""
    return data_source.groupby('Confederation')[column_name].sum().sort_values(ascending=False)

#use the function to group and sum the Transfers Balance column
transfers_balance = group_and_sum(df_new, 'Transfers Balance')

#use the function to group and sum the Transfers Spent column
transfers_spent = group_and_sum(df_new, 'Transfers Spent')

#use the function to group and sum the Transfers received column
transfers_received = group_and_sum(df_new, 'Transfers received')

#print the results
print("Transfers Balance:\\n", transfers_balance)

#visualize the confederations results with a bar chart
#im plotly
fig = px.bar(transfers_balance, x=transfers_balance.index,\
y=transfers_balance.values, title="Transfers Balance by Confederation")
fig.show()

