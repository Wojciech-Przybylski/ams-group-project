-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: cinema
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actors`
--

DROP TABLE IF EXISTS `actors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `actor` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_actors_actor` (`actor`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actors`
--

LOCK TABLES `actors` WRITE;
/*!40000 ALTER TABLE `actors` DISABLE KEYS */;
INSERT INTO `actors` VALUES (17,'Angelina Jolie'),(19,'Anne Hathaway'),(2,'Brad Pitt'),(23,'Charlize Theron'),(13,'Cillian Murphy'),(7,'Dwayne Johnson'),(18,'Emma Stone'),(27,'Florence Pugh'),(11,'Harrison Ford'),(16,'Jennifer Aniston'),(15,'Jennifer Lawrence'),(9,'Johnny Depp'),(21,'Julia Roberts'),(3,'Leonardo DiCaprio'),(26,'Margot Robbie'),(10,'Matt Damon'),(25,'Meryl Streep'),(22,'Mila Kunis'),(12,'Morgan Freeman'),(24,'Natalie Portman'),(5,'Robert Downey Jr.'),(28,'Ryan Gosling'),(8,'Samuel L. Jackson'),(20,'Sandra Bullock'),(14,'Scarlett Johansson'),(1,'Tom Cruise'),(6,'Tom Hanks'),(29,'Will Ferrell'),(4,'Will Smith');
/*!40000 ALTER TABLE `actors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `movie_id` int NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_bookings_movie_id` (`movie_id`),
  KEY `ix_bookings_user_id` (`user_id`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings_items`
--

DROP TABLE IF EXISTS `bookings_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `booking_id` int NOT NULL,
  `showing_id` int NOT NULL,
  `ticket_type_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_bookings_items_booking_id` (`booking_id`),
  KEY `ix_bookings_items_showing_id` (`showing_id`),
  KEY `ix_bookings_items_ticket_type_id` (`ticket_type_id`),
  CONSTRAINT `bookings_items_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`id`),
  CONSTRAINT `bookings_items_ibfk_2` FOREIGN KEY (`showing_id`) REFERENCES `showings` (`id`),
  CONSTRAINT `bookings_items_ibfk_3` FOREIGN KEY (`ticket_type_id`) REFERENCES `ticket_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings_items`
--

LOCK TABLES `bookings_items` WRITE;
/*!40000 ALTER TABLE `bookings_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookings_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_item`
--

DROP TABLE IF EXISTS `cart_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `showing_id` int NOT NULL,
  `ticket_type_id` int NOT NULL,
  `quantity` int NOT NULL,
  `cart_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `showing_id` (`showing_id`),
  KEY `ticket_type_id` (`ticket_type_id`),
  KEY `cart_id` (`cart_id`),
  CONSTRAINT `cart_item_ibfk_1` FOREIGN KEY (`showing_id`) REFERENCES `showings` (`id`),
  CONSTRAINT `cart_item_ibfk_2` FOREIGN KEY (`ticket_type_id`) REFERENCES `ticket_type` (`id`),
  CONSTRAINT `cart_item_ibfk_3` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_item`
--

LOCK TABLES `cart_item` WRITE;
/*!40000 ALTER TABLE `cart_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment_thread`
--

DROP TABLE IF EXISTS `comment_thread`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment_thread` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_comment_thread_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_thread`
--

LOCK TABLES `comment_thread` WRITE;
/*!40000 ALTER TABLE `comment_thread` DISABLE KEYS */;
INSERT INTO `comment_thread` VALUES (1,'Mission Impossible'),(3,'The Dark Knight'),(4,'The Godfather'),(2,'The Matrix');
/*!40000 ALTER TABLE `comment_thread` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comment_thread_id` int NOT NULL,
  `user_id` int NOT NULL,
  `comment` varchar(200) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_comments_user_id` (`user_id`),
  KEY `ix_comments_comment_thread_id` (`comment_thread_id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`comment_thread_id`) REFERENCES `comment_thread` (`id`),
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,1,1,'This is a comment','2023-09-12 13:16:48'),(2,1,1,'This is another comment','2023-09-12 13:16:48'),(3,1,1,'This is a third comment','2023-09-12 13:16:48');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `directors`
--

DROP TABLE IF EXISTS `directors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `directors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `director` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_directors_director` (`director`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directors`
--

LOCK TABLES `directors` WRITE;
/*!40000 ALTER TABLE `directors` DISABLE KEYS */;
INSERT INTO `directors` VALUES (1,'Christopher Nolan'),(9,'Clint Eastwood'),(6,'David Fincher'),(13,'Greta Gerwig'),(11,'Guy Ritchie'),(5,'James Cameron'),(3,'Martin Scorsese'),(10,'Peter Jackson'),(4,'Quentin Tarantino'),(7,'Ridley Scott'),(12,'Ron Howard'),(2,'Steven Spielberg'),(8,'Tim Burton');
/*!40000 ALTER TABLE `directors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `genre` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_genres_genre` (`genre`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (1,'Action'),(11,'Adventure'),(12,'Animation'),(13,'Biography'),(2,'Comedy'),(10,'Crime'),(14,'Documentary'),(8,'Drama'),(15,'Family'),(9,'Fantasy'),(16,'History'),(3,'Horror'),(17,'Music'),(18,'Musical'),(19,'Mystery'),(4,'Romance'),(5,'Sci-Fi'),(20,'Sport'),(6,'Thriller'),(21,'War'),(7,'Western');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_actors`
--

DROP TABLE IF EXISTS `movie_actors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_actors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int NOT NULL,
  `actor_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_movie_actors_actor_id` (`actor_id`),
  KEY `ix_movie_actors_movie_id` (`movie_id`),
  CONSTRAINT `movie_actors_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_actors_ibfk_2` FOREIGN KEY (`actor_id`) REFERENCES `actors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_actors`
--

LOCK TABLES `movie_actors` WRITE;
/*!40000 ALTER TABLE `movie_actors` DISABLE KEYS */;
INSERT INTO `movie_actors` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,3),(5,2,4),(6,2,5),(7,3,5),(8,3,6),(9,3,7),(10,4,8),(11,4,9),(12,4,10),(13,5,5),(14,5,13),(15,5,27),(16,6,26),(17,6,28),(18,6,29);
/*!40000 ALTER TABLE `movie_actors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_directors`
--

DROP TABLE IF EXISTS `movie_directors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_directors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int NOT NULL,
  `director_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_movie_directors_movie_id` (`movie_id`),
  KEY `ix_movie_directors_director_id` (`director_id`),
  CONSTRAINT `movie_directors_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_directors_ibfk_2` FOREIGN KEY (`director_id`) REFERENCES `directors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_directors`
--

LOCK TABLES `movie_directors` WRITE;
/*!40000 ALTER TABLE `movie_directors` DISABLE KEYS */;
INSERT INTO `movie_directors` VALUES (1,1,1),(2,2,5),(3,3,1),(4,4,3),(5,5,1),(6,6,13);
/*!40000 ALTER TABLE `movie_directors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_genres`
--

DROP TABLE IF EXISTS `movie_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_movie_genres_movie_id` (`movie_id`),
  KEY `ix_movie_genres_genre_id` (`genre_id`),
  CONSTRAINT `movie_genres_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_genres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_genres`
--

LOCK TABLES `movie_genres` WRITE;
/*!40000 ALTER TABLE `movie_genres` DISABLE KEYS */;
INSERT INTO `movie_genres` VALUES (1,1,1),(2,2,5),(3,3,1),(4,4,10),(5,5,13),(6,6,2),(7,6,8);
/*!40000 ALTER TABLE `movie_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `description` varchar(2048) NOT NULL,
  `image` varchar(30) NOT NULL,
  `release_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_movies_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Mission Impossible','A secret agent is sent to Sydney, to find and destroy a genetically modified disease called \'Chimera\'.','images/mission_impossible.jpeg','1996-05-22 00:00:00'),(2,'The Matrix','A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.','images/the_matrix.jpg','1999-03-31 00:00:00'),(3,'The Dark Knight','When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.','images/the_dark_knight.jpg','2008-07-14 00:00:00'),(4,'The Godfather','The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.','images/the_godfather.jpg','1972-03-24 00:00:00'),(5,'Oppenheimer','A look at the life of J. Robert Oppenheimer, the physicist tasked with developing the first atomic bomb.','images/oppenheimer.jpeg','2023-07-21 00:00:00'),(6,'Barbie','Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.','images/barbie.jpeg','2023-07-21 00:00:00');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_details`
--

DROP TABLE IF EXISTS `payment_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `card_name` varchar(30) NOT NULL,
  `user_id` int NOT NULL,
  `card_number` varchar(16) NOT NULL,
  `expiry_date` varchar(5) NOT NULL,
  `security_code` varchar(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_payment_details_card_number` (`card_number`),
  KEY `ix_payment_details_user_id` (`user_id`),
  CONSTRAINT `payment_details_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_details`
--

LOCK TABLES `payment_details` WRITE;
/*!40000 ALTER TABLE `payment_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `showings`
--

DROP TABLE IF EXISTS `showings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `showings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int NOT NULL,
  `screen_number` int NOT NULL,
  `date` datetime NOT NULL,
  `seats_available` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_showings_movie_id` (`movie_id`),
  CONSTRAINT `showings_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `showings`
--

LOCK TABLES `showings` WRITE;
/*!40000 ALTER TABLE `showings` DISABLE KEYS */;
INSERT INTO `showings` VALUES (1,1,1,'2023-10-01 12:00:00',10),(2,1,1,'2023-10-01 15:00:00',100),(3,1,2,'2023-10-01 18:00:00',100),(4,1,2,'2023-10-01 21:00:00',100),(5,2,5,'2023-10-11 12:00:00',100),(6,2,5,'2023-10-11 15:00:00',100),(7,2,6,'2023-10-11 18:00:00',100),(8,2,6,'2023-10-11 21:00:00',100),(9,3,9,'2023-10-21 12:00:00',100),(10,3,9,'2023-10-21 15:00:00',100),(11,3,10,'2023-10-21 18:00:00',100),(12,3,10,'2023-10-21 21:00:00',100),(13,4,13,'2023-10-31 12:00:00',100),(14,4,13,'2023-10-31 15:00:00',100),(15,4,14,'2023-10-31 18:00:00',100),(16,4,14,'2023-10-31 21:00:00',100),(17,5,17,'2023-11-01 12:00:00',100),(18,5,17,'2023-11-01 15:00:00',100),(19,5,18,'2023-11-01 18:00:00',100),(20,5,18,'2023-11-01 21:00:00',100),(21,6,21,'2023-11-11 12:00:00',100),(22,6,21,'2023-11-11 15:00:00',100),(23,6,22,'2023-11-11 18:00:00',100),(24,6,22,'2023-11-11 21:00:00',100);
/*!40000 ALTER TABLE `showings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_type`
--

DROP TABLE IF EXISTS `ticket_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticket_type` varchar(30) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_ticket_type_ticket_type` (`ticket_type`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_type`
--

LOCK TABLES `ticket_type` WRITE;
/*!40000 ALTER TABLE `ticket_type` DISABLE KEYS */;
INSERT INTO `ticket_type` VALUES (1,'Adult',10),(2,'Child',5);
/*!40000 ALTER TABLE `ticket_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(512) NOT NULL,
  `email` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`),
  UNIQUE KEY `ix_user_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'james','$2b$12$KuCn0V6.EgNZhMaSW.7B0OLWhMjclFFeCvRq1bEpnZWhsab/94pF6','james@qa.com',0),(2,'admin','$2b$12$UIG5IA/.Gi2rsFsCrniUh.HKYUz4we2YXJgnvGQdyGfKhJ28dBTZe','admin@qa.com',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-12 15:50:56
