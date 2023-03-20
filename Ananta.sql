-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 20, 2023 at 07:15 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Ananta`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `aadhar` varchar(20) NOT NULL,
  `id` varchar(20) NOT NULL,
  `motive` varchar(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`aadhar`, `id`, `motive`, `date`) VALUES
('123456781234', '21030480041', 'donate plasma', '2023-03-22'),
('234567891011', '21030480029', 'donate blood', '2023-03-25');

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `about` varchar(1000) NOT NULL,
  `pin` varchar(7) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`id`, `name`, `about`, `pin`, `password`) VALUES
('21030480042', 'Survey Hospital, Ranchi', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '834001', 'survey@ranchi'),
('21030480041', 'Sadar Hospital, Ranchi', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '834002', 'sadar@ranchi'),
('21030480029', 'MGM, Ranchi', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '834002', 'mgm@ranchi');

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `aadhar` varchar(15) NOT NULL,
  `about` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `file` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`aadhar`, `about`, `date`, `file`) VALUES
('123456781234', 'blood test', '2023-03-19', '210000001_medreport.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `todo`
--

CREATE TABLE `todo` (
  `email` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `todo`
--

INSERT INTO `todo` (`email`, `title`) VALUES
('deepak@gmail.com', 'Go to gym'),
('ankitaaqgh123@gmail.com', 'hit the gym');

-- --------------------------------------------------------

--
-- Table structure for table `volunteer`
--

CREATE TABLE `volunteer` (
  `aadhar` varchar(15) NOT NULL,
  `name` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_no` varchar(11) NOT NULL,
  `address` varchar(500) NOT NULL,
  `password` varchar(255) NOT NULL,
  `blood` varchar(4) NOT NULL,
  `allergies` varchar(255) NOT NULL,
  `height` varchar(10) NOT NULL,
  `weight` varchar(10) NOT NULL,
  `history` varchar(255) NOT NULL,
  `kin_name` varchar(255) NOT NULL,
  `kin_contact` varchar(11) NOT NULL,
  `donation` varchar(255) NOT NULL,
  `photo` varchar(50) NOT NULL,
  `aadhar_file` varchar(50) NOT NULL,
  `address_file` varchar(50) NOT NULL,
  `report` varchar(50) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `volunteer`
--

INSERT INTO `volunteer` (`aadhar`, `name`, `dob`, `gender`, `email`, `phone_no`, `address`, `password`, `blood`, `allergies`, `height`, `weight`, `history`, `kin_name`, `kin_contact`, `donation`, `photo`, `aadhar_file`, `address_file`, `report`, `score`) VALUES
('123456781234', 'Prem Kumar', '2001-08-09', 'male', 'ankitaaqgh123@gmail.com', '9876543210', 'Rahargora jamshedpur', '123', 'A+', 'strong Smell', '1.75', '75', 'none', 'Takkla', '9123456789', 'Heart, Lungs, Liver, Kidneys, Skin, Bone, ', '123456781234_photo.jpeg', '123456781234_aadhar.jpeg', '123456781234_address.jpeg', '123456781234_report.jpeg', 0),
('234567891011', 'Deepak Kumar', '2002-11-21', 'male', 'deepak@gmail.com', '0987654321', 'jamshedpur, jharkhand', '456', 'o+', 'none', '1.7', '51', 'none', 'sumit', '1234567890', 'Intestines, Tissue, ', '234567891011_photo.pdf', '234567891011_aadhar.pdf', '234567891011_address.pdf', '234567891011_report.pdf', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
