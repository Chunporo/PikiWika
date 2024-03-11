declare @jsondata nvarchar(max)

select @jsondata = bulkcolumn
from openrowset(bulk 'C:\Users\LENOVO LEGION\Documents\GitHub\PikiWika\json\pokedex_01.json',  single_clob) as j

--print @jsondata
--insert into [pikawiki].[dbo].[Pokemon] (pokemonid, pname, height, weight, hp, attack, defense, specialattack, specialdefense, xp)
select * from openjson(@jsondata)
with 
(
	id int,
	name nvarchar(20),
	height int,
	weight int,
	xp int,
	types nvarchar(max) '$.types.name'
)

BULK INSERT Types
from 'C:\Users\LENOVO LEGION\Documents\GitHub\PikiWika\csv\types.csv'
with (firstrow = 2,
      fieldterminator = ',',
      rowterminator='\n',
      batchsize=10000,
      maxerrors=10);

ALTER TABLE moves
ADD CONSTRAINT fk_movestypes
FOREIGN KEY (type_id) 
REFERENCES Types (typeid)

ALTER TABLE moves
ADD CONSTRAINT fk_move_targetID
FOREIGN KEY (target_id) 
REFERENCES move_targets(id)

ALTER TABLE pokemon_moves
ADD CONSTRAINT fk_pokemonmovemoveid
FOREIGN KEY (move_id)
REFERENCES moves(moveid)

ALTER TABLE pokemon_moves
ADD CONSTRAINT fk_pokemonmove_pokeid
FOREIGN KEY (pokemon_id)
REFERENCES pokemon(pokemonid)

ALTER TABLE pokemon_moves
ADD CONSTRAINT fk_pokemonmove_methodId
FOREIGN KEY (pokemon_move_method_id)
REFERENCES pokemon_move_methods(id)

ALTER TABLE moves
ADD CONSTRAINT fk_moves_type
FOREIGN KEY (type_id) 
REFERENCES Types(typeid)

ALTER TABLE pokemon_types
ADD CONSTRAINT fk_types_typeId
FOREIGN KEY (type_id)
REFERENCES types(typeid)

ALTER TABLE pokemon_types
ADD CONSTRAINT fk_types_pokeId
FOREIGN KEY (pokemon_id)
REFERENCES pokemon(pokemonid)

BULK INSERT pokemon
from 'C:\Users\LENOVO LEGION\Documents\GitHub\PikiWika\csv\pokemon.csv'
with (firstrow = 2,
      fieldterminator = ',',
      rowterminator='\n',
      batchsize=100000,
      maxerrors=10);

-- Drop the unique constraint
ALTER TABLE pokemon
DROP CONSTRAINT UQ__Pokemon__1FC9734C0A08B4C2;

-- Alter the column data type
ALTER TABLE pokemon
ALTER COLUMN pname NVARCHAR(100); -- Change the data type as needed

-- Recreate the unique constraint if necessary
ALTER TABLE pokemon
ADD CONSTRAINT UQ__Pokemon__1FC9734C0A08B4C2 UNIQUE (pname);


-- Drop the foreign key constraint
ALTER TABLE pokemon_moves
DROP CONSTRAINT fk_pokemonmove_pokeid;

-- Perform the ALTER TABLE operation
ALTER TABLE Pokemon
ALTER COLUMN pokemonid INT; -- Modify the column data type or other attributes as needed

-- Recreate the foreign key constraint
ALTER TABLE pokemon_moves
ADD CONSTRAINT fk_pokemonmove_pokeid
FOREIGN KEY (pokeid) REFERENCES Pokemon(pokemonid);

SELECT *
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'Types';

