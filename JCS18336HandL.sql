-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 30, 2018 at 03:40 PM
-- Server version: 10.2.7-MariaDB
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `JCS18336HandL`
--

-- --------------------------------------------------------

--
-- Table structure for table `Beverages`
--

CREATE TABLE `Beverages` (
  `Drink` char(128) NOT NULL,
  `Price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Beverages`
--

INSERT INTO `Beverages` (`Drink`, `Price`) VALUES
('1d', 12),
('aa aa', 11),
('asd', 12),
('Coke', 1.5),
('Fanta', 1.5),
('Iced tea', 1.5),
('Mountain Dew', 1.5),
('Pepsi', 1.5),
('qwe', -1),
('testing', 12),
('water', 1.5),
('wqe', 12);

-- --------------------------------------------------------

--
-- Table structure for table `Employees`
--

CREATE TABLE `Employees` (
  `ID` int(11) NOT NULL,
  `DOB` date NOT NULL,
  `BaseSalary` int(128) NOT NULL,
  `Name` varchar(128) NOT NULL,
  `Position` varchar(128) DEFAULT NULL,
  `Warning` int(32) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Employees`
--

INSERT INTO `Employees` (`ID`, `DOB`, `BaseSalary`, `Name`, `Position`, `Warning`) VALUES
(12346, '1995-05-24', 10, 'Sosage', 'Cleaner', 5),
(12349, '1993-04-09', 5, 'xiao huang', 'Restroom CEO', 0),
(12351, '1995-09-08', 5, 'big huang', 'Kitchen CEO', 0),
(12353, '1997-04-01', 1, 'Little Lau', 'Toilet Cleaner', 5),
(12354, '1994-09-29', 2, 'Xiao Horse', 'Waitress', 1),
(12355, '1955-10-28', 2000, 'William Gates', 'Restaurant Manager', 0),
(12358, '1998-09-09', 2, 'ManFenNan', 'chef', 0),
(12364, '1980-05-23', 12, 'Weimin', 'Mascot', 2),
(12369, '1998-01-01', 3, 'huan', 'gg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `Expenses`
--

CREATE TABLE `Expenses` (
  `Date` date NOT NULL,
  `Electricity` int(32) NOT NULL DEFAULT 0,
  `Gas` int(32) NOT NULL DEFAULT 0,
  `Water` int(32) NOT NULL DEFAULT 0,
  `Salary` int(32) NOT NULL DEFAULT 0,
  `Rent` int(32) NOT NULL DEFAULT 0,
  `CostofGood` int(32) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Expenses`
--

INSERT INTO `Expenses` (`Date`, `Electricity`, `Gas`, `Water`, `Salary`, `Rent`, `CostofGood`) VALUES
('2016-02-01', 1300, 1400, 110, 4000, 321, 300),
('2017-01-09', 1460, 1460, 100, 4000, 3000, 231),
('2018-03-07', 1500, 1500, 110, 4000, 3000, 230),
('2018-03-19', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `Foods`
--

CREATE TABLE `Foods` (
  `No` int(8) NOT NULL,
  `Ingredients` text NOT NULL,
  `FoodName` char(128) NOT NULL,
  `Price` double NOT NULL,
  `Popularity` int(32) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Foods`
--

INSERT INTO `Foods` (`No`, `Ingredients`, `FoodName`, `Price`, `Popularity`) VALUES
(100, 'Glass noodles,Carrot,White cabbage ,etc', 'Spring Roll', 2.25, 3),
(101, 'Chicken, ginger, garlic, soy sauce, rice vinegar,Shaoxing wine or sherry, sugar, sesame oil, scallions, hot chili peppers, batter', 'General Tso\'s chicken', 8, 5),
(102, 'Sugar,Soy Source, Pork...', 'Sweet & Sour Pork', 7.5, 2),
(103, 'Sesame, more sesame, broccoli, chichken', 'Sesame chicken', 8, 5);

-- --------------------------------------------------------

--
-- Table structure for table `Goods`
--

CREATE TABLE `Goods` (
  `Type` char(128) NOT NULL,
  `Price` double NOT NULL,
  `Quantity` int(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Goods`
--

INSERT INTO `Goods` (`Type`, `Price`, `Quantity`) VALUES
('Ham', 3, 12),
('Pork', 2, 10),
('Rice', 16, 4),
('Sausage', 2, 100),
('Soy Sauce', 5, 10);

-- --------------------------------------------------------

--
-- Table structure for table `LunchSpecials`
--

CREATE TABLE `LunchSpecials` (
  `Name` char(128) NOT NULL,
  `Price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `LunchSpecials`
--

INSERT INTO `LunchSpecials` (`Name`, `Price`) VALUES
('Fried Chicken Wings', 7),
('Happy Familiy', 12),
('Kung Pao Triple Delight', 11),
('Szechuan Beef', 6.5);

-- --------------------------------------------------------

--
-- Table structure for table `Transactions`
--

CREATE TABLE `Transactions` (
  `Order#` int(8) NOT NULL,
  `Date` date NOT NULL,
  `Cashier` char(128) NOT NULL,
  `FoodOrdered` text NOT NULL,
  `Earning` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Transactions`
--

INSERT INTO `Transactions` (`Order#`, `Date`, `Cashier`, `FoodOrdered`, `Earning`) VALUES
(4321, '2015-02-13', 'Zeng', '2 Egg Roll, 3 General Tso\'s Chicken Wings , 5 Sesame Chicken', 300),
(4322, '2016-03-11', 'Lau', '2 Kung Pao Chicken,3 Chicken With Cashew Nuts,4 Chicken Chow Mein, 5 Wor Sue Gai (Yellow Gravy),1 Chicken With Broccoli', 415.36),
(4323, '2017-01-01', 'Gates', '2 Beef With Broccoli,3 Vegetables With Bean Curd, 2 Spinach With Garlic,etc.', 250.15),
(4324, '2018-03-06', 'Zeng', 'Sesame Chicken, Kung Pao Chicken, Hunan Chicken, Cheese Wontan', 123),
(4325, '2018-03-19', 'Zeng', 'sesame chicken, garlic sauce fish', 8),
(4326, '2018-03-29', 'JIM', '1 Coke, 2 Shaomai', 20);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Beverages`
--
ALTER TABLE `Beverages`
  ADD PRIMARY KEY (`Drink`);

--
-- Indexes for table `Employees`
--
ALTER TABLE `Employees`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Expenses`
--
ALTER TABLE `Expenses`
  ADD PRIMARY KEY (`Date`);

--
-- Indexes for table `Foods`
--
ALTER TABLE `Foods`
  ADD PRIMARY KEY (`No`),
  ADD KEY `FoodName` (`FoodName`,`Price`);

--
-- Indexes for table `Goods`
--
ALTER TABLE `Goods`
  ADD PRIMARY KEY (`Type`);

--
-- Indexes for table `LunchSpecials`
--
ALTER TABLE `LunchSpecials`
  ADD PRIMARY KEY (`Name`),
  ADD KEY `Name` (`Name`,`Price`);

--
-- Indexes for table `Transactions`
--
ALTER TABLE `Transactions`
  ADD PRIMARY KEY (`Order#`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Employees`
--
ALTER TABLE `Employees`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12370;
--
-- AUTO_INCREMENT for table `Foods`
--
ALTER TABLE `Foods`
  MODIFY `No` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;
--
-- AUTO_INCREMENT for table `Transactions`
--
ALTER TABLE `Transactions`
  MODIFY `Order#` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4327;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
