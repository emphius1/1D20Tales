-- Schema for Game Mechanics

CREATE TABLE IF NOT EXISTS `Characters` (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `backstory` TEXT,
  `traits` TEXT,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Inventory` (
  `id` INT AUTO_INCREMENT,
  `character_id` INT,
  `item_name` VARCHAR(255) NOT NULL,
  `item_description` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`character_id`) REFERENCES `Characters`(`id`)
);

CREATE TABLE IF NOT EXISTS `Skills` (
  `id` INT AUTO_INCREMENT,
  `character_id` INT,
  `skill_name` VARCHAR(255) NOT NULL,
  `skill_level` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`character_id`) REFERENCES `Characters`(`id`)
);

CREATE TABLE IF NOT EXISTS `Enemies` (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `strategy` TEXT,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Combat` (
  `id` INT AUTO_INCREMENT,
  `character_id` INT,
  `enemy_id` INT,
  `narrative` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`character_id`) REFERENCES `Characters`(`id`),
  FOREIGN KEY (`enemy_id`) REFERENCES `Enemies`(`id`)
);