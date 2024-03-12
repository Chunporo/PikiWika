import pyodbc

# Set your database connection details
server = 'your_server_name'
database = 'Pikawiki'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'  # Adjust the driver according to your setup

# Establish the database connection
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

def get_pokemon_info_by_name(pokemon_name):
    # Query to get Pokemon information by name
    query = f"""
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
        P.speed,
        T.tname AS type
    FROM
        Pokemon P
    JOIN
        has H ON P.pokemonid = H.pokemonid
    JOIN
        Types T ON H.typeid = T.typeid
    WHERE
        P.pname = ?
    """
    # Execute the query
    cursor.execute(query, pokemon_name)
    
    # Fetch the result
    result = cursor.fetchone()
    
    if result:
        print(f"Pokemon Name: {result.pname}")
        print(f"Height: {result.height} Weight: {result.weight}")
        print(f"XP: {result.xp} HP: {result.hp}")
        print(f"Attack: {result.attack} Defense: {result.defense}")
        print(f"Special Attack: {result.specialattack} Special Defense: {result.specialdefense}")
        print(f"Speed: {result.speed}")
        print(f"Type: {result.type}")
    else:
        print(f"No Pokemon found with the name '{pokemon_name}'")

# Example: Query Pokemon information by name
pokemon_name_to_query = 'Pikachu'
get_pokemon_info_by_name(pokemon_name_to_query)

# Close the database connection
cursor.close()
connection.close()
