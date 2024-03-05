USE Pikawiki;

CREATE TABLE Pokemon
(
	pokemonid INT,
	pname CHAR(20) UNIQUE NOT NULL,
	hp INT NOT NULL,
	attack INT NOT NULL,
	defense INT NOT NULL,
	specialattack INT NOT NULL,
	specialdefense INT NOT NULL,
	speed INT NOT NULL,
	PRIMARY KEY(pokemonid)
);

CREATE TABLE Types
(
	typeid INT IDENTITY(1,1),
	tname CHAR(10) UNIQUE NOT NULL,
	PRIMARY KEY(typeid) 
);

CREATE TABLE Moves
( 	
	moveid INT IDENTITY(1,1),
	mname CHAR(20) UNIQUE NOT NULL,
	description CHAR(200) NOT NULL,
	category INT NOT NULL,
	power INT,
	accuracy INT,
	PRIMARY KEY (moveid) 
);

CREATE TABLE Abilities
(
	abilityid INT IDENTITY(1,1),
	aname CHAR(20) UNIQUE NOT NULL,
	effect VARCHAR(3000) NOT NULL,
	PRIMARY KEY (abilityid)
);

CREATE TABLE learns
(
	pokemonid INT,
	moveid INT,
	atlevel INT,
	PRIMARY KEY (pokemonid, moveid),
	FOREIGN KEY (pokemonid) REFERENCES Pokemon(pokemonid),
	FOREIGN KEY (moveid) REFERENCES Moves(moveid)
);

CREATE TABLE possesses
(	
	pokemonid INT,
	abilityid INT,
	PRIMARY KEY (pokemonid, abilityid),
	FOREIGN KEY (pokemonid) REFERENCES Pokemon(pokemonid),
	FOREIGN KEY (abilityid) REFERENCES Abilities(abilityid)
);

CREATE TABLE has
(
	pokemonid INT,
	typeid INT,
	PRIMARY KEY(pokemonid, typeid),
	FOREIGN KEY (pokemonid) REFERENCES Pokemon(pokemonid),
	FOREIGN KEY (typeid) REFERENCES Types(typeid)
);

CREATE TABLE is_of
(
	moveid INT,
	typeid INT,
	effectiveness REAL,
	PRIMARY KEY(moveid, typeid),
	FOREIGN KEY (moveid) REFERENCES Moves(moveid),
	FOREIGN KEY (typeid) REFERENCES Types(typeid)
);

CREATE TABLE attacking
(
	typeid1 INT,
	typeid2 INT,
	PRIMARY KEY(typeid1, typeid2),
	FOREIGN KEY (typeid1) REFERENCES Types(typeid),
	FOREIGN KEY (typeid2) REFERENCES Types(typeid)
);

CREATE TABLE defending
(
	typeid1 INT,
	typeid2 INT,
	effectiveness REAL,
	PRIMARY KEY(typeid1, typeid2),
	FOREIGN KEY (typeid1) REFERENCES Types(typeid),
	FOREIGN KEY (typeid2) REFERENCES Types(typeid)
);
