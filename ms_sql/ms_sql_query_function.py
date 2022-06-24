import pymssql
import pandas
from IPython.display import display

def sql_query(username, password, sql_server, database, query):
    #   Assemble connection string
    connection = pymssql.connect(
        user=username,
        password=password,
        host=sql_server,
        database=database
    )
    #   Create and open connection.  Using the "as+dict=True" allows using the column names instead of indices
    cursor = connection.cursor(as_dict=True)
    cursor.execute(query)
    #   Get data
    data = cursor.fetchall()
    #   Convert data into Pandas DataFrame
    df = pandas.DataFrame(data)
    #   Close connection
    connection.close()
    return df


user = r'lab\martin'
password = r'P@ssw0rd'
sql_host = r'oriondb\orionprod'
database = 'SolarWindsOrion'
query = "SELECT TOP 3 NodeID, Caption, IP_Address FROM [{}].[dbo].[NodesData]".format(database)


results = sql_query(user, password, sql_host, database, query)
display(results)

"""
    The printed results look like:
    
       NodeID      Caption     IP_Address
    0  473        server01       10.1.2.1
    1  489      switch1-01   10.20.27.183
    2  503     router01-01  10.30.127.101

    
    This allows being able to select column by name:
    
    display(results['Caption'][0])
    > 'server01'
    
    
    
    Treat the results like a SQL query without having to perform an actual SQL connection:
    
    caption = 'switch1-01'
    results.loc[results['Caption'] == caption]
    >
       NodeID      Caption     IP_Address
    1  489      switch1-01   10.20.27.183
    
    
    Examples of how to parse:
    https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values
"""