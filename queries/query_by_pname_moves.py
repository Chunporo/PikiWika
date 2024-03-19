import pyodbc
import pandas as pd

# Set your database connection details
server = 'LAPTOP-DN3PCHGN\SQLEXPRESS01'
database = 'Pikawiki'
driver = 'ODBC Driver 17 for SQL Server'  # Adjust the driver according to your setup

# Establish the database connection with Windows Authentication
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'
connection = pyodbc.connect(connection_string)

# Function to get Pokemon moves by name
def get_pokemon_moves_by_name(pokemon_name, version_group_id=20):
    # Query to get Pokemon information by name
    query = """
    SELECT 
        PM.level,
        M.mname AS "Move Name",
        T.Tname AS "Type",
        M.power,
        M.accuracy
    FROM
        pokemon
    JOIN
        pokemon_moves PM ON PM.pokemon_id = pokemon.pokemonid
    JOIN
        moves M ON M.moveid = PM.move_id
    JOIN
        Types T ON T.typeid = M.type_id
    WHERE
        pokemon.pname = ? AND PM.pokemon_move_method_id = 1 AND PM.version_group_id = ?
    ORDER BY
        PM.level ASC;
    """
    
    # Execute the query and fetch results into a DataFrame
    df = pd.read_sql_query(query, connection, params=(pokemon_name, version_group_id))
    
    return df

# Example: Query Pokemon information by name with the default version_group_id = 20
pokemon_name_to_query = 'Pikachu'
pokemon_moves_df = get_pokemon_moves_by_name(pokemon_name_to_query)

# Print the DataFrame
print(pokemon_moves_df)

# Close the database connection
connection.close()
