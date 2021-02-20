DROP SCHEMA IF EXISTS `lostpropertyhub`;
CREATE USER 'lostpropertyhub'@'%' IDENTIFIED BY 'jL0xxwMjNuJB5c5E';
CREATE SCHEMA IF NOT EXISTS `lostpropertyhub` DEFAULT CHARACTER SET utf8;
GRANT ALL PRIVILEGES ON `lostpropertyhub`.* TO `lostpropertyhub`@`%`;
USE `lostpropertyhub`;

DROP TABLE IF EXISTS `Users`;
CREATE TABLE IF NOT EXISTS `Users` (
  `idUser` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `pwd` VARCHAR(50) NOT NULL,
  `mail` VARCHAR(50) NOT NULL,
  `tel` VARCHAR(50),
  `address` VARCHAR(100),
  `isAdmin` BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (`idUser`)
);

DROP TABLE IF EXISTS `Tickets`;
CREATE TABLE `Tickets` (
    `idTicket` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `userId` INT UNSIGNED NOT NULL,
    `tstamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `type` TEXT NOT NULL,
    `object` TEXT NOT NULL,
    `description` TEXT NOT NULL,
    `brand` TEXT NOT NULL,
    `color` TEXT NOT NULL,
    `details` TEXT NOT NULL,
    `date` TEXT NOT NULL,
    `place` TEXT NOT NULL,
    `reviewed` BOOLEAN DEFAULT 0,
    `revby` INT UNSIGNED DEFAULT NULL,
    PRIMARY KEY (`idTicket`),
    FOREIGN KEY (`userId`) REFERENCES `Users` (`idUser`) ON DELETE CASCADE,
    FOREIGN KEY (`revby`) REFERENCES `Users` (`idUser`) ON DELETE SET NULL
);

