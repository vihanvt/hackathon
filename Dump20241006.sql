-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (arm64)
--
-- Host: localhost    Database: hackathon
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data` (
  `Sno` varchar(4) NOT NULL,
  `Company` varchar(1000) NOT NULL,
  `Sector` varchar(1000) NOT NULL,
  `ESG` varchar(20) NOT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES ('1','Infosys Ltd.','IT','A'),('10','Dr. Reddy\'s Laboratories Ltd.','Pharma','B+'),('100','IDBI Bank Ltd','Banks','C'),('11','Kansai Nerolac Paints Ltd','Consumer Goods','B+'),('12','UltraTech Cement Ltd.','Cement','B+'),('13','Larsen & Toubro Ltd.','Construction','B+'),('14','Ambuja Cements Ltd.','Cement','B+'),('15','ITC Ltd.','Consumer Goods','B+'),('16','Hindustan Zinc Ltd.','Metals & Mining','B+'),('17','Asian Paints Ltd.','Consumer Goods','B+'),('18','Wipro Ltd.','IT','B+'),('19','ICICI Lombard General Insurance Company Ltd.','Finance: Non Banking','B+'),('2','Mahindra & Mahindra Ltd.','Automobile','B+'),('20','Havells India Ltd.','Consumer Goods','B+'),('21','Info Edge (India) Ltd.','IT','B+'),('22','Cipla Ltd.','Pharma','B+'),('23','Godrej Consumer Products Ltd.','Consumer Goods','B+'),('24','Tata Steel Ltd.','Metals & Mining','B+'),('25','Hindalco Industries Ltd.','Metals & Mining','B'),('26','Maruti Suzuki India Ltd.','Automobile','B'),('27','Adani Transmission Ltd','Power','B'),('28','Titan Company Ltd.','Consumer Goods','B'),('29','HCL Technologies Ltd.','IT','B'),('3','Tech Mahindra Ltd.','IT','B+'),('30','Page Industries Ltd','Textiles','B'),('31','PI Industries Ltd','Fertilisers & Pesticides','B'),('32','ACC Ltd','Cement','B'),('33','Hero MotoCorp Ltd.','Automobile','B'),('34','Dabur India Ltd.','Consumer Goods','B'),('35','Tata Motors Ltd.','Automobile','B'),('36','Shree Cement Ltd.','Cement','B'),('37','Eicher Motors Ltd.','Automobile','B'),('38','Nestle India Ltd.','Consumer Goods','B'),('39','Biocon Ltd.','Pharma','B'),('4','HDFC Bank Ltd.','Banking: Non Finance','B+'),('40','Divi\'s Laboratories Ltd.','Pharma','B'),('41','JSW Steel Ltd.','Metals & Mining','B'),('42','Piramal Enterprises Ltd.','Pharma','B'),('43','HDFC Bank Ltd.','Banks','B'),('44','IndusInd Bank Ltd.','Banks','B'),('45','ICICI Prudential Life Insurance Company Ltd.','Finance: Non Banking','B'),('46','Whirlpool of India Ltd','Consumer Goods','B'),('47','Axis Bank Ltd.','Banks','B'),('48','Hindustan Unilever Ltd.','Consumer Goods','B'),('49','Grasim Industries Ltd.','Cement','B'),('5','Adani Ports and Special Economic Zone Ltd.','Services','B+'),('50','Vedanta Ltd','Metals & Mining','B'),('51','Colgate Palmolive (India) Ltd.','Consumer Goods','B'),('52','Bharti Airtel Ltd.','Telecom','B'),('53','HDFC Asset Management Company Ltd.','Finance: Non-Banking','B'),('54','Trent Ltd','Consumer Goods','B'),('55','Adani Green Energy Ltd.','Power','B'),('56','Berger Paints India Ltd.','Consumer Goods','B'),('57','United Breweries Ltd.','Consumer Goods','B'),('58','UPL Ltd.','Fertilisers & Pesticides','B'),('59','3M India Ltd','Metals & Mining','B'),('6','Marico Ltd.','Consumer Goods','B+'),('60','Indus Tower Ltd.','Telecom','B'),('61','Oracle Financial Services Software Ltd','IT','B'),('62','Procter & Gamble Hygiene & Health Care Ltd.','Consumer Goods','B'),('63','United Spirits Ltd.','Consumer Goods','B'),('64','HDFC Life Insurance Co. Ltd.','Finance: Non-Banking','B'),('65','Siemens Ltd.','Industrial Manufacturing','B'),('66','Reliance Industries Ltd.','Oil & Gas','B'),('67','Torrent Pharmaceuticals Ltd.','Pharma','B'),('68','Jubilant Foodworks Ltd','Consumer Goods','B'),('69','Pfizer Ltd.','Pharma','B'),('7','Tata Consumer Products Ltd','Consumer Goods','B+'),('70','Avenue Supermarts Ltd.','Consumer Goods','B'),('71','Bajaj Finserv Ltd.','Finance: Non-Banking','B'),('72','Aurobindo Pharma Ltd.','Pharma','B-'),('73','Cadila Healthcare Ltd.','Pharma','B-'),('74','Bosch Ltd.','Automobile','B-'),('75','Alkem Laboratories Ltd.','Pharma','B-'),('76','Bajaj Auto Ltd.','Automobile','B-'),('77','Abbott India Ltd.','Pharma','B-'),('78','DLF Ltd.','Construction','B-'),('79','IPCA Laboratories Ltd','Pharma','B-'),('8','Tata Consultancy Services Ltd.','IT','B+'),('80','ABB India Ltd','Industrial Manufacturing','B-'),('81','Lupin Ltd.','Pharma','B-'),('82','InterGlobe Aviation Ltd.','Services','B-'),('83','Britannia Industries Ltd.','Consumer Goods','B-'),('84','ICICI Bank Ltd.','Banks','B-'),('85','Pidilite Industries Ltd.','Chemicals','B-'),('86','Muthoot Finance Ltd.','Finance: Non-Banking','B-'),('87','Bajaj Finance Ltd.','Finance: Non-Banking','B-'),('88','Honeywell Automation India Ltd','Industrial Manufacturing','B-'),('89','Gillette India Ltd','Consumer Goods','B-'),('9','Larsen & Toubro Infotech Ltd.','IT','B+'),('90','Motherson Sumi Systems Ltd','Automobile','B-'),('91','Indraprastha Gas Ltd.','Oil & Gas','B-'),('92','Sun Pharmaceutical Industries Ltd.','Pharma','B-'),('93','MRF Ltd','Automobile','B-'),('94','Kotak Mahindra Bank Ltd.','Banks','B-'),('95','Yes Bank Ltd.','Banks','B-'),('96','Rajesh Exports Ltd','Consumer Goods','B-'),('97','Bajaj Holdings & Investment Ltd','Finance: Non-Banking','B-'),('98','GlaxoSmithKline Pharmaceuticals Ltd','Pharma','C+'),('99','Bandhan Bank Ltd.','Banks','C+');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stocks`
--

DROP TABLE IF EXISTS `stocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stocks` (
  `Slno` varchar(10) NOT NULL,
  `CompanyName` varchar(50) DEFAULT NULL,
  `StockName` varchar(50) DEFAULT NULL,
  `CMP` int DEFAULT NULL,
  PRIMARY KEY (`Slno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks`
--

LOCK TABLES `stocks` WRITE;
/*!40000 ALTER TABLE `stocks` DISABLE KEYS */;
INSERT INTO `stocks` VALUES ('1','Infosys Ltd.','INFY',1918),('10','Dr. Reddy\'s Laboratories Ltd.','DRREDDY',6633),('100','IDBI Bank Ltd.','IDBI',83),('11','Kansai Nerolac Paints Ltd.','KANSAINER',292),('12','UltraTech Cement Ltd.','ULTRACEMCO',11450),('13','Larsen & Toubro Ltd.','LT',3494),('14','Ambuja Cements Ltd.','AMBUJACEM',611),('15','ITC Ltd.','ITC',504),('16','Hindustan Zinc Ltd.','HINDZINC',517),('17','Asian Paints Ltd.','ASIANPAINT',3072),('18','Wipro Ltd.','WIPRO',534),('19','ICICI Lombard General Insurance Company Ltd.','ICICIGI',2127),('2','Mahindra & Mahindra Ltd.','M&M',3017),('20','Havells India Ltd.','HAVELLS',1934),('21','Info Edge (India) Ltd.','NAUKRI',8199),('22','Cipla Ltd.','CIPLA',1623),('23','Godrej Consumer Products Ltd.','GODREJCP',1343),('24','Tata Steel Ltd.','TATASTEEL',167),('25','Hindalco Industries Ltd.','HINDALCO',748),('26','Maruti Suzuki India Ltd.','MARUTI',12606),('27','Adani Transmission Ltd.','ADANITRANS',3111),('28','Titan Company Ltd.','TITAN',3670),('29','HCL Technologies Ltd.','HCLTECH',1777),('3','Tech Mahindra Ltd.','TECHM',1616),('30','Page Industries Ltd.','PAGEIND',41390),('31','PI Industries Ltd.','PIIND',4587),('32','ACC Ltd.','ACC',2434),('33','Hero MotoCorp Ltd.','HEROMOTOCO',5521),('34','Dabur India Ltd.','DABUR',572),('35','Tata Motors Ltd.','TATAMOTORS',931),('36','Shree Cement Ltd.','SHREECEM',26034),('37','Eicher Motors Ltd.','EICHERMOT',4707),('38','Nestle India Ltd.','NESTLEIND',2598),('39','Biocon Ltd.','BIOCON',346),('4','HDFC Bank Ltd.','HDFCBANK',1658),('40','Divi\'s Laboratories Ltd.','DIVISLAB',5426),('41','JSW Steel Ltd.','JSWSTEEL',1034),('42','Piramal Enterprises Ltd.','PEL',1032),('43','HDFC Bank Ltd.','HDFCBANK',1698),('44','IndusInd Bank Ltd.','INDUSINDBK',1383),('45','ICICI Prudential Life Insurance Company Ltd.','ICICIPRULI',756),('46','Whirlpool of India Ltd.','WHIRLPOOL',2363),('47','Axis Bank Ltd.','AXISBANK',1178),('48','Hindustan Unilever Ltd.','HINDUNILVR',2849),('49','Grasim Industries Ltd.','GRASIM',2745),('5','Adani Ports and Special Economic Zone Ltd.','ADANIPORTS',1414),('50','Vedanta Ltd.','VEDL',7930),('51','Colgate Palmolive (India) Ltd.','COLPAL',3740),('52','Bharti Airtel Ltd.','BHARTIARTL',1641),('53','HDFC Asset Management Company Ltd.','HDFCAMC',4219),('54','Trent Ltd.','TRENT',7353),('55','Adani Green Energy Ltd.','ADANIGREEN',1801),('56','Berger Paints India Ltd.','BERGEPAINT',577),('57','United Breweries Ltd.','UBL',2105),('58','UPL Ltd.','UPL',599),('59','3M India Ltd.','3MINDIA',34330),('6','Marico Ltd.','MARICO',690),('60','Indus Tower Ltd.','INDUSTOWER',372),('61','Oracle Financial Services Software Ltd.','OFSS',10951),('62','Procter & Gamble Hygiene & Health Care Ltd.','PGHH',16754),('63','United Spirits Ltd.','MCDOWELL-N',1531),('64','HDFC Life Insurance Co. Ltd.','HDFCLIFE',709),('65','Siemens Ltd.','SIEMENS',7247),('66','Reliance Industries Ltd.','RELIANCE',2703),('67','Torrent Pharmaceuticals Ltd.','TORNTPHARM',3474),('68','Jubilant Foodworks Ltd.','JUBLFOOD',629),('69','Pfizer Ltd.','PFIZER',5616),('7','Tata Consumer Products Ltd.','TATACONSUM',931),('70','Avenue Supermarts Ltd.','DMART',4738),('71','Bajaj Finserv Ltd.','BAJAJFINSV',7211),('72','Aurobindo Pharma Ltd.','AUROPHARMA',1466),('73','Cadila Healthcare Ltd.','ZYDUSLIFE',136),('74','Bosch Ltd.','BOSCHLTD',36734),('75','Alkem Laboratories Ltd.','ALKEM',6194),('76','Bajaj Auto Ltd.','BAJAJ-AUTO',11774),('77','Abbott India Ltd.','ABBOTINDIA',28105),('78','DLF Ltd.','DLF',845),('79','IPCA Laboratories Ltd.','IPCALAB',1491),('8','Tata Consultancy Services Ltd.','TCS',4252),('80','ABB India Ltd.','ABB',NULL),('81','Lupin Ltd.','LUPIN',2198),('82','InterGlobe Aviation Ltd.','INDIGO',4609),('83','Britannia Industries Ltd.','BRITANNIA',6206),('84','ICICI Bank Ltd.','ICICIBANK',1240),('85','Pidilite Industries Ltd.','PIDILITIND',3209),('86','Muthoot Finance Ltd.','MUTHOOTFIN',1930),('87','Bajaj Finance Ltd.','BAJFINANCE',1885),('88','Honeywell Automation India Ltd.','HONAUT',48223),('89','Gillette India Ltd.','GILLETTE',8528),('9','Larsen & Toubro Infotech Ltd.','LTIM',3494),('90','Motherson Sumi Systems Ltd.','MOTHERSON',201),('91','Indraprastha Gas Ltd.','IGL',549),('92','Sun Pharmaceutical Industries Ltd.','SUNPHARMA',1910),('93','MRF Ltd.','MRF',133409),('94','Kotak Mahindra Bank Ltd.','KOTAKBANK',1809),('95','Yes Bank Ltd.','YESBANK',22),('96','Rajesh Exports Ltd.','RAJESHEXPO',281),('97','Bajaj Holdings & Investment Ltd.','BAJAJHLDNG',10368),('98','GlaxoSmithKline Pharmaceuticals Ltd.','GLAXO',2751),('99','Bandhan Bank Ltd.','BANDHANBNK',187);
/*!40000 ALTER TABLE `stocks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-06  1:37:53
