/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 8.2.0 : Database - secure_atm
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`secure_atm` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `secure_atm`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add atm_card',7,'add_atm_card'),(26,'Can change atm_card',7,'change_atm_card'),(27,'Can delete atm_card',7,'delete_atm_card'),(28,'Can view atm_card',7,'view_atm_card'),(29,'Can add block_details',8,'add_block_details'),(30,'Can change block_details',8,'change_block_details'),(31,'Can delete block_details',8,'delete_block_details'),(32,'Can view block_details',8,'view_block_details'),(33,'Can add branch',9,'add_branch'),(34,'Can change branch',9,'change_branch'),(35,'Can delete branch',9,'delete_branch'),(36,'Can view branch',9,'view_branch'),(37,'Can add complaints',10,'add_complaints'),(38,'Can change complaints',10,'change_complaints'),(39,'Can delete complaints',10,'delete_complaints'),(40,'Can view complaints',10,'view_complaints'),(41,'Can add customer',11,'add_customer'),(42,'Can change customer',11,'change_customer'),(43,'Can delete customer',11,'delete_customer'),(44,'Can view customer',11,'view_customer'),(45,'Can add feedbacks',12,'add_feedbacks'),(46,'Can change feedbacks',12,'change_feedbacks'),(47,'Can delete feedbacks',12,'delete_feedbacks'),(48,'Can view feedbacks',12,'view_feedbacks'),(49,'Can add login',13,'add_login'),(50,'Can change login',13,'change_login'),(51,'Can delete login',13,'delete_login'),(52,'Can view login',13,'view_login'),(53,'Can add authorized_person',14,'add_authorized_person'),(54,'Can change authorized_person',14,'change_authorized_person'),(55,'Can delete authorized_person',14,'delete_authorized_person'),(56,'Can view authorized_person',14,'view_authorized_person'),(57,'Can add transactions',15,'add_transactions'),(58,'Can change transactions',15,'change_transactions'),(59,'Can delete transactions',15,'delete_transactions'),(60,'Can view transactions',15,'view_transactions');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'Secure_ATM_app','atm_card'),(8,'Secure_ATM_app','block_details'),(9,'Secure_ATM_app','branch'),(10,'Secure_ATM_app','complaints'),(11,'Secure_ATM_app','customer'),(12,'Secure_ATM_app','feedbacks'),(13,'Secure_ATM_app','login'),(14,'Secure_ATM_app','authorized_person'),(15,'Secure_ATM_app','transactions');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'Secure_ATM_app','0001_initial','2024-01-15 07:25:55.423185'),(2,'Secure_ATM_app','0002_authorized_person_transactions_delete_deposit','2024-01-15 07:25:55.658855'),(3,'contenttypes','0001_initial','2024-01-15 07:25:55.721372'),(4,'auth','0001_initial','2024-01-15 07:25:56.537493'),(5,'admin','0001_initial','2024-01-15 07:25:56.804097'),(6,'admin','0002_logentry_remove_auto_add','2024-01-15 07:25:56.819737'),(7,'admin','0003_logentry_add_action_flag_choices','2024-01-15 07:25:56.837916'),(8,'contenttypes','0002_remove_content_type_name','2024-01-15 07:25:56.946080'),(9,'auth','0002_alter_permission_name_max_length','2024-01-15 07:25:57.008630'),(10,'auth','0003_alter_user_email_max_length','2024-01-15 07:25:57.071586'),(11,'auth','0004_alter_user_username_opts','2024-01-15 07:25:57.071586'),(12,'auth','0005_alter_user_last_login_null','2024-01-15 07:25:57.138637'),(13,'auth','0006_require_contenttypes_0002','2024-01-15 07:25:57.138637'),(14,'auth','0007_alter_validators_add_error_messages','2024-01-15 07:25:57.150181'),(15,'auth','0008_alter_user_username_max_length','2024-01-15 07:25:57.197092'),(16,'auth','0009_alter_user_last_name_max_length','2024-01-15 07:25:57.260016'),(17,'auth','0010_alter_group_name_max_length','2024-01-15 07:25:57.322551'),(18,'auth','0011_update_proxy_permissions','2024-01-15 07:25:57.339207'),(19,'auth','0012_alter_user_first_name_max_length','2024-01-15 07:25:57.401165'),(20,'sessions','0001_initial','2024-01-15 07:25:57.464106'),(21,'Secure_ATM_app','0003_customer_amount','2024-01-22 08:44:03.852022');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('vpv8vepri63ce3heifo9iabwp01a85pr','MDFmMjJkZmMwZmRlYmY1Y2NmMDc1ZDVlOGRkODMxMmE5MzBkNjE3NDp7ImxvZyI6ImxvIiwibGlkIjo0fQ==','2024-02-05 06:38:55.713618'),('n1aqofaltwbw5cyzkm0zig5fxfigdvkv','NDIwNTk5NWUxODIzMmQ2Y2UzYWJjY2UyZThiMDNmMWFjOWZiMDE4ODp7ImxvZyI6IiJ9','2024-01-29 09:01:55.754727');

/*Table structure for table `secure_atm_app_atm_card` */

DROP TABLE IF EXISTS `secure_atm_app_atm_card`;

CREATE TABLE `secure_atm_app_atm_card` (
  `id` int NOT NULL AUTO_INCREMENT,
  `request_date` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `card_no` varchar(200) NOT NULL,
  `cvv` varchar(200) NOT NULL,
  `exp_date` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_atm_card_USER_id_93fec918` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_atm_card` */

insert  into `secure_atm_app_atm_card`(`id`,`request_date`,`status`,`card_no`,`cvv`,`exp_date`,`USER_id`) values (1,'10-01-2024','approved','23456','231','12/24',2);

/*Table structure for table `secure_atm_app_authorized_person` */

DROP TABLE IF EXISTS `secure_atm_app_authorized_person`;

CREATE TABLE `secure_atm_app_authorized_person` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_authorized_person_USER_id_f8289f3a` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_authorized_person` */

insert  into `secure_atm_app_authorized_person`(`id`,`name`,`image`,`USER_id`) values (1,'Fathima','/static/images/2024-01-22 152330.png',2);

/*Table structure for table `secure_atm_app_block_details` */

DROP TABLE IF EXISTS `secure_atm_app_block_details`;

CREATE TABLE `secure_atm_app_block_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `ATM_CARD_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_block_details_ATM_CARD_id_93fe0f45` (`ATM_CARD_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_block_details` */

insert  into `secure_atm_app_block_details`(`id`,`date`,`status`,`ATM_CARD_id`) values (1,'12-01-2024','Unblocked',1);

/*Table structure for table `secure_atm_app_branch` */

DROP TABLE IF EXISTS `secure_atm_app_branch`;

CREATE TABLE `secure_atm_app_branch` (
  `id` int NOT NULL AUTO_INCREMENT,
  `branch_name` varchar(200) NOT NULL,
  `ifsc` varchar(200) NOT NULL,
  `pincode` int NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` bigint NOT NULL,
  `LOGIN_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_branch_LOGIN_id_23af629f` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_branch` */

insert  into `secure_atm_app_branch`(`id`,`branch_name`,`ifsc`,`pincode`,`email`,`phone`,`LOGIN_id`) values (1,'fsdfhfd','3456346',436336,'vbnvbnc',5446,1);

/*Table structure for table `secure_atm_app_complaints` */

DROP TABLE IF EXISTS `secure_atm_app_complaints`;

CREATE TABLE `secure_atm_app_complaints` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `complaint` varchar(200) NOT NULL,
  `reply` varchar(200) NOT NULL,
  `reply_date` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_complaints_USER_id_052716d8` (`USER_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_complaints` */

/*Table structure for table `secure_atm_app_customer` */

DROP TABLE IF EXISTS `secure_atm_app_customer`;

CREATE TABLE `secure_atm_app_customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` bigint NOT NULL,
  `image` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `account_no` varchar(200) NOT NULL,
  `BRANCH_id` int NOT NULL,
  `LOGIN_id` int NOT NULL,
  `amount` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_customer_BRANCH_id_4b02450b` (`BRANCH_id`),
  KEY `Secure_ATM_app_customer_LOGIN_id_eb3c2874` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_customer` */

insert  into `secure_atm_app_customer`(`id`,`name`,`email`,`phone`,`image`,`gender`,`account_no`,`BRANCH_id`,`LOGIN_id`,`amount`) values (2,'Ribin','ribinak76@gmail.com',6753874586,'/static/images/123.jpg','Male','7668797896',1,4,'0');

/*Table structure for table `secure_atm_app_feedbacks` */

DROP TABLE IF EXISTS `secure_atm_app_feedbacks`;

CREATE TABLE `secure_atm_app_feedbacks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `feedback` varchar(200) NOT NULL,
  `rating` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_feedbacks_USER_id_d38660bd` (`USER_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_feedbacks` */

/*Table structure for table `secure_atm_app_login` */

DROP TABLE IF EXISTS `secure_atm_app_login`;

CREATE TABLE `secure_atm_app_login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_login` */

insert  into `secure_atm_app_login`(`id`,`username`,`password`,`usertype`) values (1,'branch','123','branch'),(2,'sss','ss','user'),(5,'admin','admin','admin'),(4,'user','123','user');

/*Table structure for table `secure_atm_app_transactions` */

DROP TABLE IF EXISTS `secure_atm_app_transactions`;

CREATE TABLE `secure_atm_app_transactions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `time` varchar(200) NOT NULL,
  `amount` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `USER_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Secure_ATM_app_transactions_USER_id_119836cd` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `secure_atm_app_transactions` */

insert  into `secure_atm_app_transactions`(`id`,`date`,`time`,`amount`,`type`,`USER_id`) values (1,'pending','pending','pending','pending',2),(2,'pending','pending','pending','pending',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
