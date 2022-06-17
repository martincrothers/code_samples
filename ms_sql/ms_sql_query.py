import pymssql

host = r'oriondb\orionprod'
user = r'lab\martin'
password = r'P@ssw0rd'
database = 'SolarWindsOrion'

connection = pymssql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

query = "SELECT TOP 2 [NodeID], [Caption], [IP_Address] FROM [{}].[dbo].[NodesData]".format(database)

cursor = connection.cursor()
cursor.execute(query)

for row in cursor:
    print(row[0])

connection.close()

