-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 11, 2016 at 05:34 PM
-- Server version: 5.6.21
-- PHP Version: 5.5.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `linkedin`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE IF NOT EXISTS `company` (
`id` int(11) NOT NULL,
  `CompanyID` varchar(111) DEFAULT NULL,
  `Name` varchar(72) DEFAULT NULL,
  `Description` varchar(2042) DEFAULT NULL,
  `Specialties` varchar(274) DEFAULT NULL,
  `Address1` varchar(116) DEFAULT NULL,
  `Address2` varchar(51) DEFAULT NULL,
  `Locality` varchar(45) DEFAULT NULL,
  `Region` varchar(25) DEFAULT NULL,
  `PostalCode` varchar(23) DEFAULT NULL,
  `Country` varchar(21) DEFAULT NULL,
  `Website` varchar(131) DEFAULT NULL,
  `Industry` varchar(36) DEFAULT NULL,
  `Type` varchar(23) DEFAULT NULL,
  `CompanySize` varchar(21) DEFAULT NULL,
  `Founded` varchar(255) DEFAULT NULL,
  `Followers` varchar(255) DEFAULT NULL,
  `RecentUpdates` varchar(5180) DEFAULT NULL,
  `RecentUpdatesLinks` varchar(500) DEFAULT NULL,
  `EmployeesOnLinkedIn` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `education`
--

CREATE TABLE IF NOT EXISTS `education` (
`id` int(11) NOT NULL,
  `LinkedInURL` varchar(83) DEFAULT NULL,
  `Institute` varchar(99) DEFAULT NULL,
  `Degree` varchar(160) DEFAULT NULL,
  `Years` varchar(16) DEFAULT NULL,
  `Description` varchar(876) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `experience`
--

CREATE TABLE IF NOT EXISTS `experience` (
`id` int(11) NOT NULL,
  `ProfileID` varchar(83) DEFAULT NULL,
  `CompanyID` varchar(111) DEFAULT NULL,
  `CompanyName` varchar(100) DEFAULT NULL,
  `Position` varchar(100) DEFAULT NULL,
  `StartDate` varchar(14) DEFAULT NULL,
  `EndDate` varchar(14) DEFAULT NULL,
  `Location` varchar(44) DEFAULT NULL,
  `Description` varchar(2008) DEFAULT NULL,
  `Type` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `hrefs`
--

CREATE TABLE IF NOT EXISTS `hrefs` (
`id` int(11) NOT NULL,
  `href` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE IF NOT EXISTS `profile` (
`id` int(11) NOT NULL,
  `PublicURL` varchar(800) DEFAULT NULL,
  `ProfileID` int(1) DEFAULT NULL,
  `FirstName` varchar(20) DEFAULT NULL,
  `LastName` varchar(800) DEFAULT NULL,
  `fullname` varchar(800) DEFAULT NULL,
  `Current` varchar(800) DEFAULT NULL,
  `Previous` varchar(800) DEFAULT NULL,
  `Connections` int(50) DEFAULT NULL,
  `Certification` varchar(500) DEFAULT NULL,
  `Groups` varchar(800) DEFAULT NULL,
  `Summery` varchar(2054) DEFAULT NULL,
  `Location` varchar(500) DEFAULT NULL,
  `Industry` varchar(500) DEFAULT NULL,
  `Language` varchar(500) DEFAULT NULL,
  `Headline` varchar(255) DEFAULT NULL,
  `Website` varchar(255) DEFAULT NULL,
  `Education` varchar(255) DEFAULT NULL,
  `Interests` varchar(2000) NOT NULL,
  `Organisations` varchar(2000) NOT NULL,
  `Skills` varchar(996) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `company`
--
ALTER TABLE `company`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `education`
--
ALTER TABLE `education`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `experience`
--
ALTER TABLE `experience`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `hrefs`
--
ALTER TABLE `hrefs`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `education`
--
ALTER TABLE `education`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `experience`
--
ALTER TABLE `experience`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hrefs`
--
ALTER TABLE `hrefs`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
