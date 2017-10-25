-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: model
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
  KEY `auth_group__permission_id_1c8710e6bf99a8ca_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1c8710e6bf99a8ca_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_6d041d3162d8405_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
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
  CONSTRAINT `auth__content_type_id_6c23e55393350e04_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add book info',7,'add_bookinfo'),(20,'Can change book info',7,'change_bookinfo'),(21,'Can delete book info',7,'delete_bookinfo'),(22,'Can add hero info',8,'add_heroinfo'),(23,'Can change hero info',8,'change_heroinfo'),(24,'Can delete hero info',8,'delete_heroinfo'),(25,'Can add place',9,'add_place'),(26,'Can change place',9,'change_place'),(27,'Can delete place',9,'delete_place'),(28,'Can add restaurant',10,'add_restaurant'),(29,'Can change restaurant',10,'change_restaurant'),(30,'Can delete restaurant',10,'delete_restaurant'),(31,'Can add new place',11,'add_newplace'),(32,'Can change new place',11,'change_newplace'),(33,'Can delete new place',11,'delete_newplace'),(34,'Can add student',12,'add_student'),(35,'Can change student',12,'change_student'),(36,'Can delete student',12,'delete_student'),(37,'Can add superman',13,'add_superman'),(38,'Can change superman',13,'change_superman'),(39,'Can delete superman',13,'delete_superman'),(40,'Can add dormitory',14,'add_dormitory'),(41,'Can change dormitory',14,'change_dormitory'),(42,'Can delete dormitory',14,'delete_dormitory'),(43,'Can add member',15,'add_member'),(44,'Can change member',15,'change_member'),(45,'Can delete member',15,'delete_member'),(46,'Can add book desc',16,'add_bookdesc'),(47,'Can change book desc',16,'change_bookdesc'),(48,'Can delete book desc',16,'delete_bookdesc'),(49,'Can add area info',17,'add_areainfo'),(50,'Can change area info',17,'change_areainfo'),(51,'Can delete area info',17,'delete_areainfo');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
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
  KEY `auth_user_groups_group_id_4056dac6c169c085_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_4056dac6c169c085_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_100736bf30ef89a7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  KEY `auth_user_u_permission_id_2f37bcdce8e73800_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_2f37bcdce8e73800_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_2ac0da0ed679bead_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  KEY `djang_content_type_id_57bf8d2f87d48e04_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_419bfbfccbbdd6a8_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_57bf8d2f87d48e04_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_419bfbfccbbdd6a8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
  UNIQUE KEY `django_content_type_app_label_542a23029cefb59e_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(17,'model','areainfo'),(16,'model','bookdesc'),(7,'model','bookinfo'),(14,'model','dormitory'),(8,'model','heroinfo'),(15,'model','member'),(11,'model','newplace'),(9,'model','place'),(10,'model','restaurant'),(12,'model','student'),(13,'model','superman'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-10-14 00:19:33.950555'),(2,'auth','0001_initial','2017-10-14 00:19:34.666255'),(3,'admin','0001_initial','2017-10-14 00:19:34.873950'),(4,'contenttypes','0002_remove_content_type_name','2017-10-14 00:19:34.990945'),(5,'auth','0002_alter_permission_name_max_length','2017-10-14 00:19:35.173981'),(6,'auth','0003_alter_user_email_max_length','2017-10-14 00:19:35.323699'),(7,'auth','0004_alter_user_username_opts','2017-10-14 00:19:35.332845'),(8,'auth','0005_alter_user_last_login_null','2017-10-14 00:19:35.397132'),(9,'auth','0006_require_contenttypes_0002','2017-10-14 00:19:35.400853'),(10,'model','0001_initial','2017-10-14 00:19:35.806532'),(11,'sessions','0001_initial','2017-10-14 00:19:35.886863'),(12,'model','0002_newplace_student','2017-10-14 01:59:41.652815'),(13,'model','0003_dormitory_member_superman','2017-10-14 02:48:39.536970'),(14,'model','0004_auto_20171014_1054','2017-10-14 02:54:58.008196'),(15,'model','0005_bookdesc','2017-10-14 12:10:04.631260'),(16,'model','0006_areainfo','2017-10-14 13:51:20.667005'),(17,'model','0007_auto_20171014_2204','2017-10-14 14:04:34.918341');
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
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_areainfo`
--

DROP TABLE IF EXISTS `model_areainfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_areainfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area_name` varchar(30) NOT NULL,
  `area_parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `model_areai_area_parent_id_2dc4319b11395ad1_fk_model_areainfo_id` (`area_parent_id`),
  CONSTRAINT `model_areai_area_parent_id_2dc4319b11395ad1_fk_model_areainfo_id` FOREIGN KEY (`area_parent_id`) REFERENCES `model_areainfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_areainfo`
--

LOCK TABLES `model_areainfo` WRITE;
/*!40000 ALTER TABLE `model_areainfo` DISABLE KEYS */;
INSERT INTO `model_areainfo` VALUES (1,'北京',NULL),(2,'河北',NULL),(3,'海淀区',1),(4,'昌平区',1),(5,'顺义区',1),(6,'房山区',1),(7,'朝阳区',1),(8,'丰台区',1),(9,'石家庄',2),(10,'唐山',2),(11,'保定',2),(12,'邢台',2),(13,'邯郸',2),(14,'秦皇岛',2);
/*!40000 ALTER TABLE `model_areainfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_bookdesc`
--

DROP TABLE IF EXISTS `model_bookdesc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_bookdesc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_title` varchar(20) NOT NULL,
  `book_read` int(11) NOT NULL,
  `book_comment` int(11) NOT NULL,
  `book_isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_bookdesc`
--

LOCK TABLES `model_bookdesc` WRITE;
/*!40000 ALTER TABLE `model_bookdesc` DISABLE KEYS */;
INSERT INTO `model_bookdesc` VALUES (1,'射雕英雄传',10,10,1),(2,'天龙八部',20,20,0),(3,'笑傲江湖',30,30,1),(4,'雪山飞狐',40,40,0);
/*!40000 ALTER TABLE `model_bookdesc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_bookinfo`
--

DROP TABLE IF EXISTS `model_bookinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_bookinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_title` varchar(50) NOT NULL,
  `book_comment` int(11) NOT NULL,
  `book_read` int(11) NOT NULL,
  `book_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_bookinfo`
--

LOCK TABLES `model_bookinfo` WRITE;
/*!40000 ALTER TABLE `model_bookinfo` DISABLE KEYS */;
INSERT INTO `model_bookinfo` VALUES (1,'射雕英雄传',47,28,1),(2,'天龙八部',79,57,0),(3,'笑傲江湖',79,52,1),(4,'雪山飞狐',29,61,0);
/*!40000 ALTER TABLE `model_bookinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_dormitory`
--

DROP TABLE IF EXISTS `model_dormitory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_dormitory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dormitory_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_dormitory`
--

LOCK TABLES `model_dormitory` WRITE;
/*!40000 ALTER TABLE `model_dormitory` DISABLE KEYS */;
INSERT INTO `model_dormitory` VALUES (2,''),(3,''),(4,''),(5,'205'),(6,'401');
/*!40000 ALTER TABLE `model_dormitory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_heroinfo`
--

DROP TABLE IF EXISTS `model_heroinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_heroinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hero_name` varchar(50) NOT NULL,
  `hero_sex` tinyint(1) NOT NULL,
  `hero_desc` longtext NOT NULL,
  `hero_delete` tinyint(1) NOT NULL,
  `hero_book_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `model_heroinf_hero_book_id_3dd4f762629931a1_fk_model_bookinfo_id` (`hero_book_id`),
  CONSTRAINT `model_heroinf_hero_book_id_3dd4f762629931a1_fk_model_bookinfo_id` FOREIGN KEY (`hero_book_id`) REFERENCES `model_bookinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_heroinfo`
--

LOCK TABLES `model_heroinfo` WRITE;
/*!40000 ALTER TABLE `model_heroinfo` DISABLE KEYS */;
INSERT INTO `model_heroinfo` VALUES (1,'郭靖',1,'降龙十八掌',0,1),(2,'黄蓉',0,'打狗棍法',0,1),(3,'黄药师',1,'弹指神通',0,1),(4,'欧阳锋',1,'蛤蟆功',0,1),(5,'梅超风',0,'九阴白骨爪',0,1),(6,'乔峰',1,'降龙十八掌',0,2),(7,'段誉',1,'六脉神剑',0,2),(8,'虚竹',1,'天山六阳掌',0,2),(9,'王语嫣',0,'神仙姐姐',0,2),(10,'令狐冲',1,'独孤九剑',0,3),(11,'任盈盈',0,'弹琴',0,3),(12,'岳不群',1,'华山剑法',0,3),(13,'东方不败',1,'葵花宝典',0,3),(14,'胡斐',1,'胡家刀法',0,4),(15,'苗若兰',0,'黄衣',0,4),(16,'程灵素',0,'医术',0,4),(17,'袁紫衣',0,'六合拳',0,4);
/*!40000 ALTER TABLE `model_heroinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_member`
--

DROP TABLE IF EXISTS `model_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_name` varchar(50) NOT NULL,
  `member_dormitory_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `model_member_dormitory_id_4b2832c30d416be3_fk_model_dormitory_id` (`member_dormitory_id`),
  CONSTRAINT `model_member_dormitory_id_4b2832c30d416be3_fk_model_dormitory_id` FOREIGN KEY (`member_dormitory_id`) REFERENCES `model_dormitory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_member`
--

LOCK TABLES `model_member` WRITE;
/*!40000 ALTER TABLE `model_member` DISABLE KEYS */;
INSERT INTO `model_member` VALUES (1,'喜羊羊',NULL),(2,'灰太狼',2);
/*!40000 ALTER TABLE `model_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_place`
--

DROP TABLE IF EXISTS `model_place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_place` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `place_name` varchar(50) NOT NULL,
  `place_address` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_place`
--

LOCK TABLES `model_place` WRITE;
/*!40000 ALTER TABLE `model_place` DISABLE KEYS */;
INSERT INTO `model_place` VALUES (1,'上海市','浦东新区航头镇'),(2,'南京市','雨花台区铁心桥街道');
/*!40000 ALTER TABLE `model_place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_restaurant`
--

DROP TABLE IF EXISTS `model_restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_restaurant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `res_name` varchar(100) NOT NULL,
  `res_place_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `res_place_id` (`res_place_id`),
  CONSTRAINT `model_restaurant_res_place_id_2200dc71ce4061c7_fk_model_place_id` FOREIGN KEY (`res_place_id`) REFERENCES `model_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_restaurant`
--

LOCK TABLES `model_restaurant` WRITE;
/*!40000 ALTER TABLE `model_restaurant` DISABLE KEYS */;
INSERT INTO `model_restaurant` VALUES (1,'肯德基',1),(2,'必胜客',2);
/*!40000 ALTER TABLE `model_restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_student`
--

DROP TABLE IF EXISTS `model_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` tinyint(1) NOT NULL,
  `age` int(11) NOT NULL,
  `activity` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_student`
--

LOCK TABLES `model_student` WRITE;
/*!40000 ALTER TABLE `model_student` DISABLE KEYS */;
/*!40000 ALTER TABLE `model_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_superman`
--

DROP TABLE IF EXISTS `model_superman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model_superman` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `description` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `age` int(11) NOT NULL,
  `height` decimal(5,2) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `profile` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_superman`
--

LOCK TABLES `model_superman` WRITE;
/*!40000 ALTER TABLE `model_superman` DISABLE KEYS */;
/*!40000 ALTER TABLE `model_superman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_custom_place`
--

DROP TABLE IF EXISTS `my_custom_place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `my_custom_place` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `place_name` varchar(50) NOT NULL,
  `place_address` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_custom_place`
--

LOCK TABLES `my_custom_place` WRITE;
/*!40000 ALTER TABLE `my_custom_place` DISABLE KEYS */;
/*!40000 ALTER TABLE `my_custom_place` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-17  7:54:42
