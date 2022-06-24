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
    #   Create and open connection
    cursor = connection.cursor()
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