# shootingGame
1. Setup django and mysql
2. Run this sql code:
CREATE DATABASE game;

USE game;

CREATE TABLE players (
	id int NOT NULL AUTO_INCREMENT,
	username varchar(16),
	password varchar(255),
	money bigint,
	level int,
	hpLevel int,
	shotgunLevel int,
	pistolLevel int,
	machineGunLevel int,
	sniperLevel int,
	rpgLevel int,
	flamethrowerLevel int,
	knivesLevel int,
	grenadeLevel int,
	shotgunAmmo int,
	machineGunAmmo int,
	sniperAmmo int,
	rpgAmmo int,
	flamethrowerAmmo int,
	knivesAmmo int,
	grenadeAmmo int,
	PRIMARY KEY(id)
);

CREATE TABLE multiplayer21 (
	playerID int,
	playerUsername varchar(15),
	playerPrimaryWeapon int,
	playerDirection int,
	playerX float,
	playerY float,
	ammo int
);
3. run the server
