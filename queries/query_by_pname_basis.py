import pyodbc

# Set your database connection details
server = 'LAPTOP-DN3PCHGN\SQLEXPRESS01'
database = 'Pikawiki'
driver = 'ODBC Driver 17 for SQL Server'  # Adjust the driver according to your setup

# Establish the database connection with Windows Authentication
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

def get_pokemon_info_by_name(pokemon_name):
    # Query to get Pokemon information by name
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
        P.speed,
        T.tname AS type,
        STRING_AGG(A.aname, ', ') AS abilities 
    FROM
        Pokemon P
    JOIN
        pokemon_types H ON P.pokemonid = H.pokemon_id
    JOIN
        Types T ON H.type_id = T.typeid
    JOIN
        possesses ON possesses.pokemonid = P.pokemonid
    JOIN
        abilities A ON possesses.abilityid = A.abilityid
    WHERE
        P.pname = ?
    GROUP BY
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
        T.tname
    """
    
    # Execute the query
    cursor.execute(query, pokemon_name)
    
    # Fetch the first result
    result = cursor.fetchone()
    
    if result:
        print(f"Pokemon Name: {result.pname}")
        print(f"Height: {result.height} Weight: {result.weight}")
        print(f"XP: {result.xp} HP: {result.hp}")
        print(f"Attack: {result.attack} Defense: {result.defense}")
        print(f"Special Attack: {result.specialattack} Special Defense: {result.specialdefense}")
        print(f"Speed: {result.speed}")
        print(f"Type: {result.type}")
        print(f"Abilities: {result.abilities}")
        print("-" * 20)
    else:
        print(f"No Pokemon found with the name '{pokemon_name}'")


# Example: Query Pokemon information by name
pokemon_name_to_query = 'Ekans'
get_pokemon_info_by_name(pokemon_name_to_query)

# Close the database connection
cursor.close()
connection.close()
