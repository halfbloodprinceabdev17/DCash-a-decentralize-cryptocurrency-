import pandas as pd
import mysql.connector

# Connect to MySQL
def sql_load():
    cnx = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='crypto')

    # Specify the table name and the query to fetch the data
    table_name = 'blockchain'
    query = f'SELECT * FROM {table_name}'

    # Load data into a DataFrame
    df = pd.read_sql(query, cnx)

    # Save DataFrame to a CSV file
    csv_file = 'data.csv'
    df.to_csv(csv_file, index=False)

    # Close the MySQL connection
    cnx.close()

    #print(f'Data successfully exported to {csv_file}.')
