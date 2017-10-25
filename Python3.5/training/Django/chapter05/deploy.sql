-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: deploy
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_2dd61047ad92e291_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_2dd61047ad92e291_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_66b8ff6e892d40bb_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_4b5fe96a3a82930a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add my file',7,'add_myfile'),(20,'Can change my file',7,'change_myfile'),(21,'Can delete my file',7,'delete_myfile'),(22,'Can add area info',8,'add_areainfo'),(23,'Can change area info',8,'change_areainfo'),(24,'Can delete area info',8,'delete_areainfo'),(25,'Can add person',9,'add_person'),(26,'Can change person',9,'change_person'),(27,'Can delete person',9,'delete_person');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$UoF0ToGmZOid$GqPpv6RLhj7Q3XijE7kbc6efmVnuTX0yJY8FRjVTcDA=','2017-10-15 12:27:50.617909',1,'python','','','123@123.com',1,1,'2017-10-15 12:27:44.097007');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_62f80535ec4aa327_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_62f80535ec4aa327_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6079b81116ead62c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_4948b3ef7a340eeb_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_4948b3ef7a340eeb_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_613beff4f0d5b7d4_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_areainfo`
--

DROP TABLE IF EXISTS `deploy_areainfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_areainfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area_name` varchar(50) NOT NULL,
  `area_code` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_areainfo`
--

LOCK TABLES `deploy_areainfo` WRITE;
/*!40000 ALTER TABLE `deploy_areainfo` DISABLE KEYS */;
INSERT INTO `deploy_areainfo` VALUES (1,'东城区','110101'),(2,'西城区','110102'),(3,'崇文区','110103'),(4,'宣武区','110104'),(5,'朝阳区','110105'),(6,'丰台区','110106'),(7,'石景山区','110107'),(8,'海淀区','110108'),(9,'门头沟区','110109'),(10,'房山区','110111'),(11,'通州区','110112'),(12,'顺义区','110113'),(13,'昌平区','110114'),(14,'大兴区','110115'),(15,'怀柔区','110116'),(16,'平谷区','110117'),(17,'密云县','110228'),(18,'延庆县','110229'),(19,'和平区','120101'),(20,'河东区','120102'),(21,'河西区','120103'),(22,'南开区','120104'),(23,'河北区','120105'),(24,'红桥区','120106'),(25,'塘沽区','120107'),(26,'汉沽区','120108'),(27,'大港区','120109'),(28,'东丽区','120110'),(29,'西青区','120111'),(30,'津南区','120112'),(31,'北辰区','120113'),(32,'武清区','120114'),(33,'宝坻区','120115'),(34,'宁河县','120221'),(35,'静海县','120223'),(36,'蓟　县','120225'),(37,'市辖区','130101'),(38,'长安区','130102'),(39,'桥东区','130103'),(40,'桥西区','130104'),(41,'新华区','130105'),(42,'井陉矿区','130107'),(43,'东城区','110101'),(44,'西城区','110102'),(45,'崇文区','110103'),(46,'宣武区','110104'),(47,'朝阳区','110105'),(48,'丰台区','110106'),(49,'石景山区','110107'),(50,'海淀区','110108'),(51,'门头沟区','110109'),(52,'房山区','110111'),(53,'通州区','110112'),(54,'顺义区','110113'),(55,'昌平区','110114'),(56,'大兴区','110115'),(57,'怀柔区','110116'),(58,'平谷区','110117'),(59,'密云县','110228'),(60,'延庆县','110229'),(61,'和平区','120101'),(62,'河东区','120102'),(63,'河西区','120103'),(64,'南开区','120104'),(65,'河北区','120105'),(66,'红桥区','120106'),(67,'塘沽区','120107'),(68,'汉沽区','120108'),(69,'大港区','120109'),(70,'东丽区','120110'),(71,'西青区','120111'),(72,'津南区','120112'),(73,'北辰区','120113'),(74,'武清区','120114'),(75,'宝坻区','120115'),(76,'宁河县','120221'),(77,'静海县','120223'),(78,'蓟　县','120225'),(79,'市辖区','130101'),(80,'长安区','130102'),(81,'桥东区','130103'),(82,'桥西区','130104'),(83,'新华区','130105'),(84,'井陉矿区','130107'),(85,'东城区','110101'),(86,'西城区','110102'),(87,'崇文区','110103'),(88,'宣武区','110104'),(89,'朝阳区','110105'),(90,'丰台区','110106'),(91,'石景山区','110107'),(92,'海淀区','110108'),(93,'门头沟区','110109'),(94,'房山区','110111'),(95,'通州区','110112'),(96,'顺义区','110113'),(97,'昌平区','110114'),(98,'大兴区','110115'),(99,'怀柔区','110116'),(100,'平谷区','110117'),(101,'密云县','110228'),(102,'延庆县','110229'),(103,'和平区','120101'),(104,'河东区','120102'),(105,'河西区','120103'),(106,'南开区','120104'),(107,'河北区','120105'),(108,'红桥区','120106'),(109,'塘沽区','120107'),(110,'汉沽区','120108'),(111,'大港区','120109'),(112,'东丽区','120110'),(113,'西青区','120111'),(114,'津南区','120112'),(115,'北辰区','120113'),(116,'武清区','120114'),(117,'宝坻区','120115'),(118,'宁河县','120221'),(119,'静海县','120223'),(120,'蓟　县','120225'),(121,'市辖区','130101'),(122,'长安区','130102'),(123,'桥东区','130103'),(124,'桥西区','130104'),(125,'新华区','130105'),(126,'井陉矿区','130107');
/*!40000 ALTER TABLE `deploy_areainfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_myfile`
--

DROP TABLE IF EXISTS `deploy_myfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_myfile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_myfile`
--

LOCK TABLES `deploy_myfile` WRITE;
/*!40000 ALTER TABLE `deploy_myfile` DISABLE KEYS */;
INSERT INTO `deploy_myfile` VALUES (1,'index.html'),(2,'index.html'),(3,'index.html'),(4,'search_index.json');
/*!40000 ALTER TABLE `deploy_myfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_person`
--

DROP TABLE IF EXISTS `deploy_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_name` varchar(30) NOT NULL,
  `person_age` int(11) NOT NULL,
  `person_sex` varchar(5) NOT NULL,
  `person_area_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deploy_per_person_area_id_1de7398085e7752f_fk_deploy_areainfo_id` (`person_area_id`),
  CONSTRAINT `deploy_per_person_area_id_1de7398085e7752f_fk_deploy_areainfo_id` FOREIGN KEY (`person_area_id`) REFERENCES `deploy_areainfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_person`
--

LOCK TABLES `deploy_person` WRITE;
/*!40000 ALTER TABLE `deploy_person` DISABLE KEYS */;
INSERT INTO `deploy_person` VALUES (1,'Trump',10,'nan',3);
/*!40000 ALTER TABLE `deploy_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_418a9795e817f58b_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_2e9c823def6c9e06_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_418a9795e817f58b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_2e9c823def6c9e06_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-10-15 13:39:14.730894','1','Trump',1,'',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_72cdc66e5b37cbff_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'deploy','areainfo'),(7,'deploy','myfile'),(9,'deploy','person'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-10-15 11:18:50.394410'),(2,'auth','0001_initial','2017-10-15 11:18:52.379025'),(3,'admin','0001_initial','2017-10-15 11:18:52.695150'),(4,'contenttypes','0002_remove_content_type_name','2017-10-15 11:18:52.904955'),(5,'auth','0002_alter_permission_name_max_length','2017-10-15 11:18:53.001512'),(6,'auth','0003_alter_user_email_max_length','2017-10-15 11:18:53.080313'),(7,'auth','0004_alter_user_username_opts','2017-10-15 11:18:53.092637'),(8,'auth','0005_alter_user_last_login_null','2017-10-15 11:18:53.139835'),(9,'auth','0006_require_contenttypes_0002','2017-10-15 11:18:53.144479'),(10,'sessions','0001_initial','2017-10-15 11:18:53.507686'),(11,'deploy','0001_initial','2017-10-15 11:50:31.467271'),(12,'deploy','0002_areainfo','2017-10-15 12:55:56.498537'),(13,'deploy','0003_auto_20171015_2118','2017-10-15 13:36:22.324789'),(14,'deploy','0004_person','2017-10-15 13:36:22.562466');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('df8xj1menz7wzj2m7u9oi99yh93zemu5','NDFkNDNjMTY2M2IyYjNlYjI2YmY1MzA3MGE4ZGZlNzZlZTI4ODZiNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYWU1YjY4MGRhYTE0ZTI4Zjg4NjExYjA3MmQ0ZGY2MjRmZWJiZTciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-10-29 12:27:50.651415');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-17  7:54:23
