import pyodbc
import pandas as pd

# Set your database connection details
server = 'LAPTOP-DN3PCHGN\SQLEXPRESS01'
database = 'Pikawiki'
driver = 'ODBC Driver 17 for SQL Server'  # Adjust the driver according to your setup

# Establish the database connection with Windows Authentication
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

def get_pokedex():
    query = """
    SELECT
        P.pname,
        P.height,
        P.weight,
        P.xp,
        P.hp,
        P.attack,
        P.defense,
        P.specialattack,
        P.specialdefense,
        P.speed
    FROM
        Pokemon P
    """
    cursor.execute(query)
    
    # Fetch all the results
    results = cursor.fetchall()
    
    # Create a DataFrame
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(results, columns=columns)
    
    return df

# Example usage
pokedex_df = get_pokedex()
print(pokedex_df)
