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

def get_pokemon_moves_by_name(pokemon_name, cursor):
    # Query to get Pokemon information by name
    query = """
    SELECT 
        PM.level,
        M.mname AS "Move Name",
        T.Tname AS "Type",
        M.power,
        M.accuracy,
        M.generation_id
    FROM
        pokemon
    JOIN
        pokemon_moves PM ON PM.pokemon_id = pokemon.pokemonid
    JOIN
        moves M ON M.moveid = PM.move_id
    JOIN
        Types T ON T.typeid = M.type_id
    WHERE
        pokemon.pname = ?
    """
    
    # Execute the query
    cursor.execute(query, (pokemon_name,))
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Create a DataFrame from the results
    if not results:
        print("No results found for the given Pokemon name.")
    else:
    # Create a DataFrame from the results
        columns = [column[0] for column in cursor.description]  # Extract column names from cursor.description
        pokemon_df = pd.DataFrame(results, columns=columns)

    # Print the DataFrame
    print(pokemon_df)

# Example: Query Pokemon information by name
pokemon_name_to_query = 'Ekans'
pokemon_df = get_pokemon_moves_by_name(pokemon_name_to_query, cursor)


# Close the database connection
cursor.close()
connection.close()
