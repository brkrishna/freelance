-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 16, 2014 at 01:26 PM
-- Server version: 5.5.38
-- PHP Version: 5.3.10-1ubuntu3.14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `crm`
--

-- --------------------------------------------------------

--
-- Table structure for table `bf_activities`
--

DROP TABLE IF EXISTS `bf_activities`;
CREATE TABLE IF NOT EXISTS `bf_activities` (
  `activity_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL DEFAULT '0',
  `activity` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `created_on` datetime NOT NULL,
  `deleted` tinyint(12) NOT NULL DEFAULT '0',
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=149 ;

--
-- Dumping data for table `bf_activities`
--

INSERT INTO `bf_activities` (`activity_id`, `user_id`, `activity`, `module`, `created_on`, `deleted`) VALUES
(1, 1, 'logged in from: 127.0.0.1', 'users', '2014-10-14 05:03:45', 0),
(2, 1, 'App settings saved from: 127.0.0.1', 'core', '2014-10-14 05:04:10', 0),
(3, 1, 'App settings saved from: 127.0.0.1', 'core', '2014-10-14 05:04:23', 0),
(4, 1, 'Created Module: UOM : 127.0.0.1', 'modulebuilder', '2014-10-14 05:16:15', 0),
(5, 1, 'Created Module: Product : 127.0.0.1', 'modulebuilder', '2014-10-14 05:19:16', 0),
(6, 1, 'Created Module: Vendors : 127.0.0.1', 'modulebuilder', '2014-10-14 05:25:49', 0),
(7, 1, 'Created Module: Document Types : 127.0.0.1', 'modulebuilder', '2014-10-14 05:28:00', 0),
(8, 1, 'logged in from: 127.0.0.1', 'users', '2014-10-14 05:39:49', 0),
(9, 1, 'created a new Editor: Ramakrishna', 'users', '2014-10-14 05:50:46', 0),
(10, 2, 'logged in from: 127.0.0.1', 'users', '2014-10-14 05:51:20', 0),
(11, 1, 'logged in from: 127.0.0.1', 'users', '2014-10-14 05:51:42', 0),
(12, 1, 'modified user: admin', 'users', '2014-10-14 06:00:58', 0),
(13, 1, 'Created Module: Purchase Orders : 127.0.0.1', 'modulebuilder', '2014-10-14 06:20:31', 0),
(14, 1, 'logged in from: 127.0.0.1', 'users', '2014-10-14 09:14:26', 0),
(15, 1, 'Created Module: Containers : 127.0.0.1', 'modulebuilder', '2014-10-14 09:29:21', 0),
(16, 1, 'Created Module: Purchase Order Documents : 127.0.0.1', 'modulebuilder', '2014-10-14 09:34:13', 0),
(17, 1, 'Created Module: PO Transactions : 127.0.0.1', 'modulebuilder', '2014-10-14 09:42:02', 0),
(18, 1, 'Created Module: Customers : 127.0.0.1', 'modulebuilder', '2014-10-14 09:48:28', 0),
(19, 1, 'modified user: Ramakrishna', 'users', '2014-10-14 09:54:04', 0),
(20, 1, 'App settings saved from: 127.0.0.1', 'core', '2014-10-14 09:54:50', 0),
(21, 1, 'App settings saved from: 127.0.0.1', 'core', '2014-10-14 09:54:50', 0),
(22, 1, 'App settings saved from: 127.0.0.1', 'core', '2014-10-14 09:55:32', 0),
(23, 1, 'modified user: Ramakrishna', 'users', '2014-10-14 09:56:35', 0),
(24, 2, 'logged in from: 127.0.0.1', 'users', '2014-10-14 09:56:56', 0),
(25, 2, 'logged in from: 127.0.0.1', 'users', '2014-10-14 09:58:09', 0),
(26, 2, 'logged in from: 127.0.0.1', 'users', '2014-10-14 09:58:43', 0),
(27, 2, 'logged in from: 127.0.0.1', 'users', '2014-10-14 09:59:26', 0),
(28, 2, 'Created record with ID: 1 : 127.0.0.1', 'uom', '2014-10-14 09:59:39', 0),
(29, 2, 'Created record with ID: 2 : 127.0.0.1', 'uom', '2014-10-14 09:59:49', 0),
(30, 2, 'Created record with ID: 3 : 127.0.0.1', 'uom', '2014-10-14 09:59:56', 0),
(31, 1, 'Migrate Type: vendors_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 10:43:42', 0),
(32, 1, 'Migrate module: vendors Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 10:43:42', 0),
(33, 1, 'Migrate Type: vendors_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 10:43:49', 0),
(34, 1, 'Migrate module: vendors Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 10:43:49', 0),
(35, 1, 'Created record with ID: 1 : 127.0.0.1', 'vendors', '2014-10-14 10:44:18', 0),
(36, 2, 'logged in from: 127.0.0.1', 'users', '2014-10-14 11:27:27', 0),
(37, 1, 'modified user: Ramakrishna', 'users', '2014-10-14 11:28:10', 0),
(38, 1, 'modified user: Ramakrishna', 'users', '2014-10-14 11:28:50', 0),
(39, 1, 'created a new Contributor: Karthik', 'users', '2014-10-14 11:43:52', 0),
(40, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 11:44:10', 0),
(41, 1, 'Updated record with ID: 1 : 127.0.0.1', 'vendors', '2014-10-14 11:54:03', 0),
(42, 1, 'Created record with ID: 1 : 127.0.0.1', 'product', '2014-10-14 11:55:14', 0),
(43, 1, 'Created record with ID: 2 : 127.0.0.1', 'product', '2014-10-14 11:55:27', 0),
(44, 1, 'Created Module: Samples : 127.0.0.1', 'modulebuilder', '2014-10-14 12:03:38', 0),
(45, 3, 'Created record with ID: 1 : 127.0.0.1', 'samples', '2014-10-14 12:31:33', 0),
(46, 3, 'Created record with ID: 2 : 127.0.0.1', 'samples', '2014-10-14 12:36:23', 0),
(47, 1, 'created a new User: Alekhya', 'users', '2014-10-14 12:42:59', 0),
(48, 4, 'logged in from: 127.0.0.1', 'users', '2014-10-14 12:43:11', 0),
(49, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 12:44:07', 0),
(50, 1, 'App settings saved from: 127.0.0.1', 'core', '2014-10-14 12:44:17', 0),
(51, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 12:44:34', 0),
(52, 3, 'Updated record with ID: 2 : 127.0.0.1', 'samples', '2014-10-14 12:47:08', 0),
(53, 4, 'logged in from: 127.0.0.1', 'users', '2014-10-14 12:51:58', 0),
(54, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 12:52:20', 0),
(55, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 13:26:53', 0),
(56, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 14:02:53', 0),
(57, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 14:04:00', 0),
(58, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 14:04:09', 0),
(59, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 14:04:25', 0),
(60, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 14:50:48', 0),
(61, 3, 'Updated record with ID: 2 : 127.0.0.1', 'samples', '2014-10-14 16:24:27', 0),
(62, 1, 'modified user: Alekhya', 'users', '2014-10-14 16:25:58', 0),
(63, 4, 'logged in from: 127.0.0.1', 'users', '2014-10-14 16:26:06', 0),
(64, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-14 16:32:58', 0),
(65, 1, 'Created Module: Inquiries : 127.0.0.1', 'modulebuilder', '2014-10-14 16:46:17', 0),
(66, 1, 'Migrate Type: inquiries_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 16:49:18', 0),
(67, 1, 'Migrate module: inquiries Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 16:49:18', 0),
(68, 1, 'Migrate Type: inquiries_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:49:25', 0),
(69, 1, 'Migrate module: inquiries Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:49:25', 0),
(70, 1, 'Created record with ID: 2 : 127.0.0.1', 'vendors', '2014-10-14 16:51:58', 0),
(71, 1, 'Migrate Type: inquiries_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:54:14', 0),
(72, 1, 'Migrate module: inquiries Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:54:14', 0),
(73, 1, 'Migrate Type: inquiries_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 16:54:37', 0),
(74, 1, 'Migrate module: inquiries Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 16:54:37', 0),
(75, 1, 'Migrate Type: inquiries_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:54:43', 0),
(76, 1, 'Migrate module: inquiries Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:54:43', 0),
(77, 1, 'Migrate Type: purchase_orders_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 16:56:58', 0),
(78, 1, 'Migrate module: purchase_orders Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 16:56:58', 0),
(79, 1, 'Migrate Type: purchase_orders_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:57:06', 0),
(80, 1, 'Migrate module: purchase_orders Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 16:57:06', 0),
(81, 1, 'Migrate Type: customers_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 17:19:12', 0),
(82, 1, 'Migrate module: customers Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 17:19:12', 0),
(83, 1, 'Migrate Type: customers_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 17:19:17', 0),
(84, 1, 'Migrate module: customers Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 17:19:17', 0),
(85, 1, 'Created record with ID: 1 : 127.0.0.1', 'customers', '2014-10-14 17:19:40', 0),
(86, 1, 'Updated record with ID: 1 : 127.0.0.1', 'customers', '2014-10-14 17:23:20', 0),
(87, 1, 'Updated record with ID: 1 : 127.0.0.1', 'customers', '2014-10-14 17:23:31', 0),
(88, 1, 'Created record with ID: 1 : 127.0.0.1', 'purchase_orders', '2014-10-14 17:31:45', 0),
(89, 1, 'Migrate Type: containers_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 18:18:39', 0),
(90, 1, 'Migrate module: containers Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 18:18:39', 0),
(91, 1, 'Migrate Type: containers_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 18:18:48', 0),
(92, 1, 'Migrate module: containers Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 18:18:48', 0),
(93, 1, 'Migrate Type: containers_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 18:31:00', 0),
(94, 1, 'Migrate module: containers Version: 0 from: 127.0.0.1', 'migrations', '2014-10-14 18:31:01', 0),
(95, 1, 'Migrate Type: containers_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 18:31:06', 0),
(96, 1, 'Migrate module: containers Version: 2 from: 127.0.0.1', 'migrations', '2014-10-14 18:31:06', 0),
(97, 1, 'Created record with ID: 1 : 127.0.0.1', 'containers', '2014-10-14 18:31:45', 0),
(98, 1, 'Created record with ID: 2 : 127.0.0.1', 'containers', '2014-10-14 18:40:08', 0),
(99, 1, 'logged in from: 127.0.0.1', 'users', '2014-10-15 06:13:38', 0),
(100, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-15 06:17:40', 0),
(101, 1, 'Created record with ID: 1 : 127.0.0.1', 'document_types', '2014-10-15 07:04:43', 0),
(102, 1, 'Created record with ID: 2 : 127.0.0.1', 'document_types', '2014-10-15 07:05:15', 0),
(103, 1, 'Created record with ID: 3 : 127.0.0.1', 'document_types', '2014-10-15 07:05:37', 0),
(104, 1, 'Created record with ID: 4 : 127.0.0.1', 'document_types', '2014-10-15 07:05:43', 0),
(105, 1, 'Migrate Type: purchase_order_documents_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-15 07:10:13', 0),
(106, 1, 'Migrate module: purchase_order_documents Version: 0 from: 127.0.0.1', 'migrations', '2014-10-15 07:10:13', 0),
(107, 1, 'Migrate Type: purchase_order_documents_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-15 07:10:20', 0),
(108, 1, 'Migrate module: purchase_order_documents Version: 2 from: 127.0.0.1', 'migrations', '2014-10-15 07:10:20', 0),
(109, 1, 'Created record with ID: Array : 127.0.0.1', 'purchase_order_documents', '2014-10-15 08:19:13', 0),
(110, 1, 'logged in from: 127.0.0.1', 'users', '2014-10-15 08:44:04', 0),
(111, 1, 'Created record with ID: Array : 127.0.0.1', 'purchase_order_documents', '2014-10-15 09:07:02', 0),
(112, 1, 'Migrate Type: purchase_order_documents_ Uninstalled Version: 0 from: 127.0.0.1', 'migrations', '2014-10-15 09:27:46', 0),
(113, 1, 'Migrate module: purchase_order_documents Version: 0 from: 127.0.0.1', 'migrations', '2014-10-15 09:27:46', 0),
(114, 1, 'Migrate Type: purchase_order_documents_ to Version: 2 from: 127.0.0.1', 'migrations', '2014-10-15 09:27:53', 0),
(115, 1, 'Migrate module: purchase_order_documents Version: 2 from: 127.0.0.1', 'migrations', '2014-10-15 09:27:53', 0),
(116, 1, 'Created record with ID: 1 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 09:28:08', 0),
(117, 3, 'logged in from: 127.0.0.1', 'users', '2014-10-15 10:04:25', 0),
(118, 4, 'logged in from: 127.0.0.1', 'users', '2014-10-15 10:46:46', 0),
(119, 1, 'Created record with ID: 3 : 127.0.0.1', 'containers', '2014-10-15 10:51:08', 0),
(120, 1, 'Created record with ID: 4 : 127.0.0.1', 'containers', '2014-10-15 10:51:57', 0),
(121, 1, 'Created record with ID: 5 : 127.0.0.1', 'containers', '2014-10-15 10:52:36', 0),
(122, 1, 'Created record with ID: 6 : 127.0.0.1', 'containers', '2014-10-15 10:53:09', 0),
(123, 1, 'Created record with ID: 7 : 127.0.0.1', 'containers', '2014-10-15 10:53:37', 0),
(124, 1, 'Created record with ID: 2 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:55:10', 0),
(125, 1, 'Created record with ID: 3 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:55:27', 0),
(126, 1, 'Created record with ID: 4 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:56:22', 0),
(127, 1, 'Created record with ID: 5 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:56:45', 0),
(128, 1, 'Created record with ID: 6 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:57:14', 0),
(129, 1, 'Created record with ID: 7 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:57:54', 0),
(130, 1, 'Created record with ID: 8 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:58:18', 0),
(131, 1, 'Created record with ID: 9 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:58:34', 0),
(132, 1, 'Created record with ID: 10 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 10:59:19', 0),
(133, 1, 'Created record with ID: 11 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:00:28', 0),
(134, 1, 'Created record with ID: 12 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:00:59', 0),
(135, 1, 'Created record with ID: 13 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:01:28', 0),
(136, 1, 'Created record with ID: 14 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:01:52', 0),
(137, 1, 'Created record with ID: 15 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:02:17', 0),
(138, 1, 'Created record with ID: 16 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:02:18', 0),
(139, 1, 'Created record with ID: 17 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:02:44', 0),
(140, 1, 'Created record with ID: 18 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:03:00', 0),
(141, 1, 'Created record with ID: 19 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:03:22', 0),
(142, 1, 'Created record with ID: 20 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:03:40', 0),
(143, 1, 'Created record with ID: 21 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:04:06', 0),
(144, 1, 'Created record with ID: 22 : 127.0.0.1', 'purchase_order_documents', '2014-10-15 11:04:22', 0),
(145, 1, 'Updated record with ID: 1 : 127.0.0.1', 'product', '2014-10-15 11:08:07', 0),
(146, 1, 'Updated record with ID: 2 : 127.0.0.1', 'product', '2014-10-15 11:08:21', 0),
(147, 4, 'logged in from: 127.0.0.1', 'users', '2014-10-15 11:36:30', 0),
(148, 1, 'logged in from: 127.0.0.1', 'users', '2014-10-15 11:40:39', 0);

-- --------------------------------------------------------

--
-- Table structure for table `bf_containers`
--

DROP TABLE IF EXISTS `bf_containers`;
CREATE TABLE IF NOT EXISTS `bf_containers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `po_ref` varchar(255) NOT NULL,
  `container_no` varchar(255) NOT NULL,
  `seal` varchar(255) NOT NULL,
  `origin` varchar(2) NOT NULL,
  `batch_nos` varchar(255) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` decimal(18,3) NOT NULL,
  `uom_id` int(11) NOT NULL,
  `status` varchar(255) NOT NULL,
  `started_on` date NOT NULL DEFAULT '0000-00-00',
  `arrived_on` date NOT NULL DEFAULT '0000-00-00',
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `bf_containers`
--

INSERT INTO `bf_containers` (`id`, `po_ref`, `container_no`, `seal`, `origin`, `batch_nos`, `product_id`, `quantity`, `uom_id`, `status`, `started_on`, `arrived_on`, `deleted`, `created_on`, `modified_on`) VALUES
(1, 'RS-SB-OVCO-201409', 'OOLU0448435', 'OOLCNK0062', 'PH', '142170', 2, 56.000, 1, 'In Transit', '2014-10-01', '0000-00-00', 0, '2014-10-14 18:31:45', '0000-00-00 00:00:00'),
(2, 'RS-SB-OVCO-201409', 'OOLU2180465', 'OOLDDG1190', 'PH', '142490', 2, 28.000, 1, 'In Transit', '2014-10-01', '0000-00-00', 0, '2014-10-14 18:40:08', '0000-00-00 00:00:00'),
(3, 'RS-SB-OVCO-201409', 'TCLU2993635', 'CBC87795', 'PH', '15189', 2, 1.000, 1, 'In Transit', '2014-10-01', '0000-00-00', 0, '2014-10-15 10:51:08', '0000-00-00 00:00:00'),
(4, 'RS-SB-OVCO-201409', 'KKTU7618462', 'CAV42559', 'PH', '1425', 2, 1.000, 1, 'In Transit', '2014-10-01', '0000-00-00', 0, '2014-10-15 10:51:57', '0000-00-00 00:00:00'),
(5, 'RS-SB-OVCO-201409', 'EMCU146112-8', 'EMCBSV3493', 'LK', 'O140814FL, O140817FL, O140821FL, O140825FL, O140828FL ', 1, 2.000, 1, 'In Transit', '2014-10-01', '0000-00-00', 0, '2014-10-15 10:52:36', '0000-00-00 00:00:00'),
(6, 'RS-SB-OVCO-201409', 'TTHU5619064', 'AP40024427', 'PH', '140915', 1, 1.000, 1, 'In Transit', '2014-10-01', '0000-00-00', 0, '2014-10-15 10:53:09', '0000-00-00 00:00:00'),
(7, 'RS-SB-OVCO-201409', 'APZU4887232', 'AP40024496', 'PH', '140915', 1, 1.000, 1, 'In Transit', '2014-10-01', '0000-00-00', 0, '2014-10-15 10:53:37', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `bf_countries`
--

DROP TABLE IF EXISTS `bf_countries`;
CREATE TABLE IF NOT EXISTS `bf_countries` (
  `iso` char(2) NOT NULL DEFAULT 'US',
  `name` varchar(80) NOT NULL,
  `printable_name` varchar(80) NOT NULL,
  `iso3` char(3) DEFAULT NULL,
  `numcode` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`iso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bf_countries`
--

INSERT INTO `bf_countries` (`iso`, `name`, `printable_name`, `iso3`, `numcode`) VALUES
('AD', 'ANDORRA', 'Andorra', 'AND', 20),
('AE', 'UNITED ARAB EMIRATES', 'United Arab Emirates', 'ARE', 784),
('AF', 'AFGHANISTAN', 'Afghanistan', 'AFG', 4),
('AG', 'ANTIGUA AND BARBUDA', 'Antigua and Barbuda', 'ATG', 28),
('AI', 'ANGUILLA', 'Anguilla', 'AIA', 660),
('AL', 'ALBANIA', 'Albania', 'ALB', 8),
('AM', 'ARMENIA', 'Armenia', 'ARM', 51),
('AN', 'NETHERLANDS ANTILLES', 'Netherlands Antilles', 'ANT', 530),
('AO', 'ANGOLA', 'Angola', 'AGO', 24),
('AQ', 'ANTARCTICA', 'Antarctica', NULL, NULL),
('AR', 'ARGENTINA', 'Argentina', 'ARG', 32),
('AS', 'AMERICAN SAMOA', 'American Samoa', 'ASM', 16),
('AT', 'AUSTRIA', 'Austria', 'AUT', 40),
('AU', 'AUSTRALIA', 'Australia', 'AUS', 36),
('AW', 'ARUBA', 'Aruba', 'ABW', 533),
('AZ', 'AZERBAIJAN', 'Azerbaijan', 'AZE', 31),
('BA', 'BOSNIA AND HERZEGOVINA', 'Bosnia and Herzegovina', 'BIH', 70),
('BB', 'BARBADOS', 'Barbados', 'BRB', 52),
('BD', 'BANGLADESH', 'Bangladesh', 'BGD', 50),
('BE', 'BELGIUM', 'Belgium', 'BEL', 56),
('BF', 'BURKINA FASO', 'Burkina Faso', 'BFA', 854),
('BG', 'BULGARIA', 'Bulgaria', 'BGR', 100),
('BH', 'BAHRAIN', 'Bahrain', 'BHR', 48),
('BI', 'BURUNDI', 'Burundi', 'BDI', 108),
('BJ', 'BENIN', 'Benin', 'BEN', 204),
('BM', 'BERMUDA', 'Bermuda', 'BMU', 60),
('BN', 'BRUNEI DARUSSALAM', 'Brunei Darussalam', 'BRN', 96),
('BO', 'BOLIVIA', 'Bolivia', 'BOL', 68),
('BR', 'BRAZIL', 'Brazil', 'BRA', 76),
('BS', 'BAHAMAS', 'Bahamas', 'BHS', 44),
('BT', 'BHUTAN', 'Bhutan', 'BTN', 64),
('BV', 'BOUVET ISLAND', 'Bouvet Island', NULL, NULL),
('BW', 'BOTSWANA', 'Botswana', 'BWA', 72),
('BY', 'BELARUS', 'Belarus', 'BLR', 112),
('BZ', 'BELIZE', 'Belize', 'BLZ', 84),
('CA', 'CANADA', 'Canada', 'CAN', 124),
('CC', 'COCOS (KEELING) ISLANDS', 'Cocos (Keeling) Islands', NULL, NULL),
('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF THE', 'Congo, the Democratic Republic of the', 'COD', 180),
('CF', 'CENTRAL AFRICAN REPUBLIC', 'Central African Republic', 'CAF', 140),
('CG', 'CONGO', 'Congo', 'COG', 178),
('CH', 'SWITZERLAND', 'Switzerland', 'CHE', 756),
('CI', 'COTE D''IVOIRE', 'Cote D''Ivoire', 'CIV', 384),
('CK', 'COOK ISLANDS', 'Cook Islands', 'COK', 184),
('CL', 'CHILE', 'Chile', 'CHL', 152),
('CM', 'CAMEROON', 'Cameroon', 'CMR', 120),
('CN', 'CHINA', 'China', 'CHN', 156),
('CO', 'COLOMBIA', 'Colombia', 'COL', 170),
('CR', 'COSTA RICA', 'Costa Rica', 'CRI', 188),
('CS', 'SERBIA AND MONTENEGRO', 'Serbia and Montenegro', NULL, NULL),
('CU', 'CUBA', 'Cuba', 'CUB', 192),
('CV', 'CAPE VERDE', 'Cape Verde', 'CPV', 132),
('CX', 'CHRISTMAS ISLAND', 'Christmas Island', NULL, NULL),
('CY', 'CYPRUS', 'Cyprus', 'CYP', 196),
('CZ', 'CZECH REPUBLIC', 'Czech Republic', 'CZE', 203),
('DE', 'GERMANY', 'Germany', 'DEU', 276),
('DJ', 'DJIBOUTI', 'Djibouti', 'DJI', 262),
('DK', 'DENMARK', 'Denmark', 'DNK', 208),
('DM', 'DOMINICA', 'Dominica', 'DMA', 212),
('DO', 'DOMINICAN REPUBLIC', 'Dominican Republic', 'DOM', 214),
('DZ', 'ALGERIA', 'Algeria', 'DZA', 12),
('EC', 'ECUADOR', 'Ecuador', 'ECU', 218),
('EE', 'ESTONIA', 'Estonia', 'EST', 233),
('EG', 'EGYPT', 'Egypt', 'EGY', 818),
('EH', 'WESTERN SAHARA', 'Western Sahara', 'ESH', 732),
('ER', 'ERITREA', 'Eritrea', 'ERI', 232),
('ES', 'SPAIN', 'Spain', 'ESP', 724),
('ET', 'ETHIOPIA', 'Ethiopia', 'ETH', 231),
('FI', 'FINLAND', 'Finland', 'FIN', 246),
('FJ', 'FIJI', 'Fiji', 'FJI', 242),
('FK', 'FALKLAND ISLANDS (MALVINAS)', 'Falkland Islands (Malvinas)', 'FLK', 238),
('FM', 'MICRONESIA, FEDERATED STATES OF', 'Micronesia, Federated States of', 'FSM', 583),
('FO', 'FAROE ISLANDS', 'Faroe Islands', 'FRO', 234),
('FR', 'FRANCE', 'France', 'FRA', 250),
('GA', 'GABON', 'Gabon', 'GAB', 266),
('GB', 'UNITED KINGDOM', 'United Kingdom', 'GBR', 826),
('GD', 'GRENADA', 'Grenada', 'GRD', 308),
('GE', 'GEORGIA', 'Georgia', 'GEO', 268),
('GF', 'FRENCH GUIANA', 'French Guiana', 'GUF', 254),
('GH', 'GHANA', 'Ghana', 'GHA', 288),
('GI', 'GIBRALTAR', 'Gibraltar', 'GIB', 292),
('GL', 'GREENLAND', 'Greenland', 'GRL', 304),
('GM', 'GAMBIA', 'Gambia', 'GMB', 270),
('GN', 'GUINEA', 'Guinea', 'GIN', 324),
('GP', 'GUADELOUPE', 'Guadeloupe', 'GLP', 312),
('GQ', 'EQUATORIAL GUINEA', 'Equatorial Guinea', 'GNQ', 226),
('GR', 'GREECE', 'Greece', 'GRC', 300),
('GS', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'South Georgia and the South Sandwich Islands', NULL, NULL),
('GT', 'GUATEMALA', 'Guatemala', 'GTM', 320),
('GU', 'GUAM', 'Guam', 'GUM', 316),
('GW', 'GUINEA-BISSAU', 'Guinea-Bissau', 'GNB', 624),
('GY', 'GUYANA', 'Guyana', 'GUY', 328),
('HK', 'HONG KONG', 'Hong Kong', 'HKG', 344),
('HM', 'HEARD ISLAND AND MCDONALD ISLANDS', 'Heard Island and Mcdonald Islands', NULL, NULL),
('HN', 'HONDURAS', 'Honduras', 'HND', 340),
('HR', 'CROATIA', 'Croatia', 'HRV', 191),
('HT', 'HAITI', 'Haiti', 'HTI', 332),
('HU', 'HUNGARY', 'Hungary', 'HUN', 348),
('ID', 'INDONESIA', 'Indonesia', 'IDN', 360),
('IE', 'IRELAND', 'Ireland', 'IRL', 372),
('IL', 'ISRAEL', 'Israel', 'ISR', 376),
('IN', 'INDIA', 'India', 'IND', 356),
('IO', 'BRITISH INDIAN OCEAN TERRITORY', 'British Indian Ocean Territory', NULL, NULL),
('IQ', 'IRAQ', 'Iraq', 'IRQ', 368),
('IR', 'IRAN, ISLAMIC REPUBLIC OF', 'Iran, Islamic Republic of', 'IRN', 364),
('IS', 'ICELAND', 'Iceland', 'ISL', 352),
('IT', 'ITALY', 'Italy', 'ITA', 380),
('JM', 'JAMAICA', 'Jamaica', 'JAM', 388),
('JO', 'JORDAN', 'Jordan', 'JOR', 400),
('JP', 'JAPAN', 'Japan', 'JPN', 392),
('KE', 'KENYA', 'Kenya', 'KEN', 404),
('KG', 'KYRGYZSTAN', 'Kyrgyzstan', 'KGZ', 417),
('KH', 'CAMBODIA', 'Cambodia', 'KHM', 116),
('KI', 'KIRIBATI', 'Kiribati', 'KIR', 296),
('KM', 'COMOROS', 'Comoros', 'COM', 174),
('KN', 'SAINT KITTS AND NEVIS', 'Saint Kitts and Nevis', 'KNA', 659),
('KP', 'KOREA, DEMOCRATIC PEOPLE''S REPUBLIC OF', 'Korea, Democratic People''s Republic of', 'PRK', 408),
('KR', 'KOREA, REPUBLIC OF', 'Korea, Republic of', 'KOR', 410),
('KW', 'KUWAIT', 'Kuwait', 'KWT', 414),
('KY', 'CAYMAN ISLANDS', 'Cayman Islands', 'CYM', 136),
('KZ', 'KAZAKHSTAN', 'Kazakhstan', 'KAZ', 398),
('LA', 'LAO PEOPLE''S DEMOCRATIC REPUBLIC', 'Lao People''s Democratic Republic', 'LAO', 418),
('LB', 'LEBANON', 'Lebanon', 'LBN', 422),
('LC', 'SAINT LUCIA', 'Saint Lucia', 'LCA', 662),
('LI', 'LIECHTENSTEIN', 'Liechtenstein', 'LIE', 438),
('LK', 'SRI LANKA', 'Sri Lanka', 'LKA', 144),
('LR', 'LIBERIA', 'Liberia', 'LBR', 430),
('LS', 'LESOTHO', 'Lesotho', 'LSO', 426),
('LT', 'LITHUANIA', 'Lithuania', 'LTU', 440),
('LU', 'LUXEMBOURG', 'Luxembourg', 'LUX', 442),
('LV', 'LATVIA', 'Latvia', 'LVA', 428),
('LY', 'LIBYAN ARAB JAMAHIRIYA', 'Libyan Arab Jamahiriya', 'LBY', 434),
('MA', 'MOROCCO', 'Morocco', 'MAR', 504),
('MC', 'MONACO', 'Monaco', 'MCO', 492),
('MD', 'MOLDOVA, REPUBLIC OF', 'Moldova, Republic of', 'MDA', 498),
('MG', 'MADAGASCAR', 'Madagascar', 'MDG', 450),
('MH', 'MARSHALL ISLANDS', 'Marshall Islands', 'MHL', 584),
('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'Macedonia, the Former Yugoslav Republic of', 'MKD', 807),
('ML', 'MALI', 'Mali', 'MLI', 466),
('MM', 'MYANMAR', 'Myanmar', 'MMR', 104),
('MN', 'MONGOLIA', 'Mongolia', 'MNG', 496),
('MO', 'MACAO', 'Macao', 'MAC', 446),
('MP', 'NORTHERN MARIANA ISLANDS', 'Northern Mariana Islands', 'MNP', 580),
('MQ', 'MARTINIQUE', 'Martinique', 'MTQ', 474),
('MR', 'MAURITANIA', 'Mauritania', 'MRT', 478),
('MS', 'MONTSERRAT', 'Montserrat', 'MSR', 500),
('MT', 'MALTA', 'Malta', 'MLT', 470),
('MU', 'MAURITIUS', 'Mauritius', 'MUS', 480),
('MV', 'MALDIVES', 'Maldives', 'MDV', 462),
('MW', 'MALAWI', 'Malawi', 'MWI', 454),
('MX', 'MEXICO', 'Mexico', 'MEX', 484),
('MY', 'MALAYSIA', 'Malaysia', 'MYS', 458),
('MZ', 'MOZAMBIQUE', 'Mozambique', 'MOZ', 508),
('NA', 'NAMIBIA', 'Namibia', 'NAM', 516),
('NC', 'NEW CALEDONIA', 'New Caledonia', 'NCL', 540),
('NE', 'NIGER', 'Niger', 'NER', 562),
('NF', 'NORFOLK ISLAND', 'Norfolk Island', 'NFK', 574),
('NG', 'NIGERIA', 'Nigeria', 'NGA', 566),
('NI', 'NICARAGUA', 'Nicaragua', 'NIC', 558),
('NL', 'NETHERLANDS', 'Netherlands', 'NLD', 528),
('NO', 'NORWAY', 'Norway', 'NOR', 578),
('NP', 'NEPAL', 'Nepal', 'NPL', 524),
('NR', 'NAURU', 'Nauru', 'NRU', 520),
('NU', 'NIUE', 'Niue', 'NIU', 570),
('NZ', 'NEW ZEALAND', 'New Zealand', 'NZL', 554),
('OM', 'OMAN', 'Oman', 'OMN', 512),
('PA', 'PANAMA', 'Panama', 'PAN', 591),
('PE', 'PERU', 'Peru', 'PER', 604),
('PF', 'FRENCH POLYNESIA', 'French Polynesia', 'PYF', 258),
('PG', 'PAPUA NEW GUINEA', 'Papua New Guinea', 'PNG', 598),
('PH', 'PHILIPPINES', 'Philippines', 'PHL', 608),
('PK', 'PAKISTAN', 'Pakistan', 'PAK', 586),
('PL', 'POLAND', 'Poland', 'POL', 616),
('PM', 'SAINT PIERRE AND MIQUELON', 'Saint Pierre and Miquelon', 'SPM', 666),
('PN', 'PITCAIRN', 'Pitcairn', 'PCN', 612),
('PR', 'PUERTO RICO', 'Puerto Rico', 'PRI', 630),
('PS', 'PALESTINIAN TERRITORY, OCCUPIED', 'Palestinian Territory, Occupied', NULL, NULL),
('PT', 'PORTUGAL', 'Portugal', 'PRT', 620),
('PW', 'PALAU', 'Palau', 'PLW', 585),
('PY', 'PARAGUAY', 'Paraguay', 'PRY', 600),
('QA', 'QATAR', 'Qatar', 'QAT', 634),
('RE', 'REUNION', 'Reunion', 'REU', 638),
('RO', 'ROMANIA', 'Romania', 'ROM', 642),
('RU', 'RUSSIAN FEDERATION', 'Russian Federation', 'RUS', 643),
('RW', 'RWANDA', 'Rwanda', 'RWA', 646),
('SA', 'SAUDI ARABIA', 'Saudi Arabia', 'SAU', 682),
('SB', 'SOLOMON ISLANDS', 'Solomon Islands', 'SLB', 90),
('SC', 'SEYCHELLES', 'Seychelles', 'SYC', 690),
('SD', 'SUDAN', 'Sudan', 'SDN', 736),
('SE', 'SWEDEN', 'Sweden', 'SWE', 752),
('SG', 'SINGAPORE', 'Singapore', 'SGP', 702),
('SH', 'SAINT HELENA', 'Saint Helena', 'SHN', 654),
('SI', 'SLOVENIA', 'Slovenia', 'SVN', 705),
('SJ', 'SVALBARD AND JAN MAYEN', 'Svalbard and Jan Mayen', 'SJM', 744),
('SK', 'SLOVAKIA', 'Slovakia', 'SVK', 703),
('SL', 'SIERRA LEONE', 'Sierra Leone', 'SLE', 694),
('SM', 'SAN MARINO', 'San Marino', 'SMR', 674),
('SN', 'SENEGAL', 'Senegal', 'SEN', 686),
('SO', 'SOMALIA', 'Somalia', 'SOM', 706),
('SR', 'SURINAME', 'Suriname', 'SUR', 740),
('ST', 'SAO TOME AND PRINCIPE', 'Sao Tome and Principe', 'STP', 678),
('SV', 'EL SALVADOR', 'El Salvador', 'SLV', 222),
('SY', 'SYRIAN ARAB REPUBLIC', 'Syrian Arab Republic', 'SYR', 760),
('SZ', 'SWAZILAND', 'Swaziland', 'SWZ', 748),
('TC', 'TURKS AND CAICOS ISLANDS', 'Turks and Caicos Islands', 'TCA', 796),
('TD', 'CHAD', 'Chad', 'TCD', 148),
('TF', 'FRENCH SOUTHERN TERRITORIES', 'French Southern Territories', NULL, NULL),
('TG', 'TOGO', 'Togo', 'TGO', 768),
('TH', 'THAILAND', 'Thailand', 'THA', 764),
('TJ', 'TAJIKISTAN', 'Tajikistan', 'TJK', 762),
('TK', 'TOKELAU', 'Tokelau', 'TKL', 772),
('TL', 'TIMOR-LESTE', 'Timor-Leste', NULL, NULL),
('TM', 'TURKMENISTAN', 'Turkmenistan', 'TKM', 795),
('TN', 'TUNISIA', 'Tunisia', 'TUN', 788),
('TO', 'TONGA', 'Tonga', 'TON', 776),
('TR', 'TURKEY', 'Turkey', 'TUR', 792),
('TT', 'TRINIDAD AND TOBAGO', 'Trinidad and Tobago', 'TTO', 780),
('TV', 'TUVALU', 'Tuvalu', 'TUV', 798),
('TW', 'TAIWAN, PROVINCE OF CHINA', 'Taiwan, Province of China', 'TWN', 158),
('TZ', 'TANZANIA, UNITED REPUBLIC OF', 'Tanzania, United Republic of', 'TZA', 834),
('UA', 'UKRAINE', 'Ukraine', 'UKR', 804),
('UG', 'UGANDA', 'Uganda', 'UGA', 800),
('UM', 'UNITED STATES MINOR OUTLYING ISLANDS', 'United States Minor Outlying Islands', NULL, NULL),
('US', 'UNITED STATES', 'United States', 'USA', 840),
('UY', 'URUGUAY', 'Uruguay', 'URY', 858),
('UZ', 'UZBEKISTAN', 'Uzbekistan', 'UZB', 860),
('VA', 'HOLY SEE (VATICAN CITY STATE)', 'Holy See (Vatican City State)', 'VAT', 336),
('VC', 'SAINT VINCENT AND THE GRENADINES', 'Saint Vincent and the Grenadines', 'VCT', 670),
('VE', 'VENEZUELA', 'Venezuela', 'VEN', 862),
('VG', 'VIRGIN ISLANDS, BRITISH', 'Virgin Islands, British', 'VGB', 92),
('VI', 'VIRGIN ISLANDS, U.S.', 'Virgin Islands, U.s.', 'VIR', 850),
('VN', 'VIET NAM', 'Viet Nam', 'VNM', 704),
('VU', 'VANUATU', 'Vanuatu', 'VUT', 548),
('WF', 'WALLIS AND FUTUNA', 'Wallis and Futuna', 'WLF', 876),
('WS', 'SAMOA', 'Samoa', 'WSM', 882),
('YE', 'YEMEN', 'Yemen', 'YEM', 887),
('YT', 'MAYOTTE', 'Mayotte', NULL, NULL),
('ZA', 'SOUTH AFRICA', 'South Africa', 'ZAF', 710),
('ZM', 'ZAMBIA', 'Zambia', 'ZMB', 894),
('ZW', 'ZIMBABWE', 'Zimbabwe', 'ZWE', 716);

-- --------------------------------------------------------

--
-- Table structure for table `bf_customers`
--

DROP TABLE IF EXISTS `bf_customers`;
CREATE TABLE IF NOT EXISTS `bf_customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `contact_name` varchar(255) NOT NULL,
  `contact_phone` varchar(255) NOT NULL,
  `contact_email` varchar(255) NOT NULL,
  `address1` varchar(255) NOT NULL,
  `address2` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `country` varchar(2) NOT NULL,
  `work_phones` varchar(255) NOT NULL,
  `website_url` varchar(255) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `bf_customers`
--

INSERT INTO `bf_customers` (`id`, `name`, `contact_name`, `contact_phone`, `contact_email`, `address1`, `address2`, `city`, `country`, `work_phones`, `website_url`, `deleted`, `created_on`, `modified_on`) VALUES
(1, 'Rosun Natural Products', 'Sami ', '', '', '', '', 'California', 'US', '', '', 0, '2014-10-14 17:19:40', '2014-10-14 17:23:31');

-- --------------------------------------------------------

--
-- Table structure for table `bf_document_types`
--

DROP TABLE IF EXISTS `bf_document_types`;
CREATE TABLE IF NOT EXISTS `bf_document_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `bf_document_types`
--

INSERT INTO `bf_document_types` (`id`, `name`) VALUES
(1, 'Certificate of Origin'),
(2, 'Transaction Certificate'),
(3, 'Certificate of Analysis'),
(4, 'Bill of Lading');

-- --------------------------------------------------------

--
-- Table structure for table `bf_email_queue`
--

DROP TABLE IF EXISTS `bf_email_queue`;
CREATE TABLE IF NOT EXISTS `bf_email_queue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `to_email` varchar(128) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `alt_message` text,
  `max_attempts` int(11) NOT NULL DEFAULT '3',
  `attempts` int(11) NOT NULL DEFAULT '0',
  `success` tinyint(1) NOT NULL DEFAULT '0',
  `date_published` datetime DEFAULT NULL,
  `last_attempt` datetime DEFAULT NULL,
  `date_sent` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `bf_inquiries`
--

DROP TABLE IF EXISTS `bf_inquiries`;
CREATE TABLE IF NOT EXISTS `bf_inquiries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product` varchar(255) NOT NULL,
  `quantity` decimal(18,3) NOT NULL,
  `uom_id` int(11) NOT NULL,
  `required_by` date NOT NULL DEFAULT '0000-00-00',
  `prod_spec` varchar(1000) NOT NULL,
  `quality_spec` varchar(1000) NOT NULL,
  `packaging_spec` varchar(1000) NOT NULL,
  `priority` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `bf_login_attempts`
--

DROP TABLE IF EXISTS `bf_login_attempts`;
CREATE TABLE IF NOT EXISTS `bf_login_attempts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(40) NOT NULL,
  `login` varchar(50) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `bf_permissions`
--

DROP TABLE IF EXISTS `bf_permissions`;
CREATE TABLE IF NOT EXISTS `bf_permissions` (
  `permission_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(100) NOT NULL,
  `status` enum('active','inactive','deleted') NOT NULL DEFAULT 'active',
  PRIMARY KEY (`permission_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=373 ;

--
-- Dumping data for table `bf_permissions`
--

INSERT INTO `bf_permissions` (`permission_id`, `name`, `description`, `status`) VALUES
(2, 'Site.Content.View', 'Allow users to view the Content Context', 'active'),
(3, 'Site.Reports.View', 'Allow users to view the Reports Context', 'active'),
(4, 'Site.Settings.View', 'Allow users to view the Settings Context', 'active'),
(5, 'Site.Developer.View', 'Allow users to view the Developer Context', 'active'),
(6, 'Bonfire.Roles.Manage', 'Allow users to manage the user Roles', 'active'),
(7, 'Bonfire.Users.Manage', 'Allow users to manage the site Users', 'active'),
(8, 'Bonfire.Users.View', 'Allow users access to the User Settings', 'active'),
(9, 'Bonfire.Users.Add', 'Allow users to add new Users', 'active'),
(10, 'Bonfire.Database.Manage', 'Allow users to manage the Database settings', 'active'),
(11, 'Bonfire.Emailer.Manage', 'Allow users to manage the Emailer settings', 'active'),
(12, 'Bonfire.Logs.View', 'Allow users access to the Log details', 'active'),
(13, 'Bonfire.Logs.Manage', 'Allow users to manage the Log files', 'active'),
(14, 'Bonfire.Emailer.View', 'Allow users access to the Emailer settings', 'active'),
(15, 'Site.Signin.Offline', 'Allow users to login to the site when the site is offline', 'active'),
(16, 'Bonfire.Permissions.View', 'Allow access to view the Permissions menu unders Settings Context', 'active'),
(17, 'Bonfire.Permissions.Manage', 'Allow access to manage the Permissions in the system', 'active'),
(18, 'Bonfire.Roles.Delete', 'Allow users to delete user Roles', 'active'),
(19, 'Bonfire.Modules.Add', 'Allow creation of modules with the builder.', 'active'),
(20, 'Bonfire.Modules.Delete', 'Allow deletion of modules.', 'active'),
(21, 'Permissions.Administrator.Manage', 'To manage the access control permissions for the Administrator role.', 'active'),
(22, 'Permissions.Editor.Manage', 'To manage the access control permissions for the Editor role.', 'active'),
(24, 'Permissions.User.Manage', 'To manage the access control permissions for the User role.', 'active'),
(25, 'Permissions.Developer.Manage', 'To manage the access control permissions for the Developer role.', 'active'),
(27, 'Activities.Own.View', 'To view the users own activity logs', 'active'),
(28, 'Activities.Own.Delete', 'To delete the users own activity logs', 'active'),
(29, 'Activities.User.View', 'To view the user activity logs', 'active'),
(30, 'Activities.User.Delete', 'To delete the user activity logs, except own', 'active'),
(31, 'Activities.Module.View', 'To view the module activity logs', 'active'),
(32, 'Activities.Module.Delete', 'To delete the module activity logs', 'active'),
(33, 'Activities.Date.View', 'To view the users own activity logs', 'active'),
(34, 'Activities.Date.Delete', 'To delete the dated activity logs', 'active'),
(35, 'Bonfire.UI.Manage', 'Manage the Bonfire UI settings', 'active'),
(36, 'Bonfire.Settings.View', 'To view the site settings page.', 'active'),
(37, 'Bonfire.Settings.Manage', 'To manage the site settings.', 'active'),
(38, 'Bonfire.Activities.View', 'To view the Activities menu.', 'active'),
(39, 'Bonfire.Database.View', 'To view the Database menu.', 'active'),
(40, 'Bonfire.Migrations.View', 'To view the Migrations menu.', 'active'),
(41, 'Bonfire.Builder.View', 'To view the Modulebuilder menu.', 'active'),
(42, 'Bonfire.Roles.View', 'To view the Roles menu.', 'active'),
(43, 'Bonfire.Sysinfo.View', 'To view the System Information page.', 'active'),
(44, 'Bonfire.Translate.Manage', 'To manage the Language Translation.', 'active'),
(45, 'Bonfire.Translate.View', 'To view the Language Translate menu.', 'active'),
(46, 'Bonfire.UI.View', 'To view the UI/Keyboard Shortcut menu.', 'active'),
(49, 'Bonfire.Profiler.View', 'To view the Console Profiler Bar.', 'active'),
(50, 'Bonfire.Roles.Add', 'To add New Roles', 'active'),
(51, 'UOM.Content.View', '', 'active'),
(52, 'UOM.Content.Create', '', 'active'),
(53, 'UOM.Content.Edit', '', 'active'),
(54, 'UOM.Content.Delete', '', 'active'),
(55, 'UOM.Reports.View', '', 'active'),
(56, 'UOM.Reports.Create', '', 'active'),
(57, 'UOM.Reports.Edit', '', 'active'),
(58, 'UOM.Reports.Delete', '', 'active'),
(59, 'UOM.Settings.View', '', 'active'),
(60, 'UOM.Settings.Create', '', 'active'),
(61, 'UOM.Settings.Edit', '', 'active'),
(62, 'UOM.Settings.Delete', '', 'active'),
(63, 'UOM.Developer.View', '', 'active'),
(64, 'UOM.Developer.Create', '', 'active'),
(65, 'UOM.Developer.Edit', '', 'active'),
(66, 'UOM.Developer.Delete', '', 'active'),
(67, 'Product.Content.View', '', 'active'),
(68, 'Product.Content.Create', '', 'active'),
(69, 'Product.Content.Edit', '', 'active'),
(70, 'Product.Content.Delete', '', 'active'),
(71, 'Product.Reports.View', '', 'active'),
(72, 'Product.Reports.Create', '', 'active'),
(73, 'Product.Reports.Edit', '', 'active'),
(74, 'Product.Reports.Delete', '', 'active'),
(75, 'Product.Settings.View', '', 'active'),
(76, 'Product.Settings.Create', '', 'active'),
(77, 'Product.Settings.Edit', '', 'active'),
(78, 'Product.Settings.Delete', '', 'active'),
(79, 'Product.Developer.View', '', 'active'),
(80, 'Product.Developer.Create', '', 'active'),
(81, 'Product.Developer.Edit', '', 'active'),
(82, 'Product.Developer.Delete', '', 'active'),
(99, 'Document_Types.Content.View', '', 'active'),
(100, 'Document_Types.Content.Create', '', 'active'),
(101, 'Document_Types.Content.Edit', '', 'active'),
(102, 'Document_Types.Content.Delete', '', 'active'),
(103, 'Document_Types.Reports.View', '', 'active'),
(104, 'Document_Types.Reports.Create', '', 'active'),
(105, 'Document_Types.Reports.Edit', '', 'active'),
(106, 'Document_Types.Reports.Delete', '', 'active'),
(107, 'Document_Types.Settings.View', '', 'active'),
(108, 'Document_Types.Settings.Create', '', 'active'),
(109, 'Document_Types.Settings.Edit', '', 'active'),
(110, 'Document_Types.Settings.Delete', '', 'active'),
(111, 'Document_Types.Developer.View', '', 'active'),
(112, 'Document_Types.Developer.Create', '', 'active'),
(113, 'Document_Types.Developer.Edit', '', 'active'),
(114, 'Document_Types.Developer.Delete', '', 'active'),
(115, 'Permissions.Contributor.Manage', 'To manage the access control permissions for the Contributor role.', 'active'),
(164, 'PO_Transactions.Content.View', '', 'active'),
(165, 'PO_Transactions.Content.Create', '', 'active'),
(166, 'PO_Transactions.Content.Edit', '', 'active'),
(167, 'PO_Transactions.Content.Delete', '', 'active'),
(168, 'PO_Transactions.Reports.View', '', 'active'),
(169, 'PO_Transactions.Reports.Create', '', 'active'),
(170, 'PO_Transactions.Reports.Edit', '', 'active'),
(171, 'PO_Transactions.Reports.Delete', '', 'active'),
(172, 'PO_Transactions.Settings.View', '', 'active'),
(173, 'PO_Transactions.Settings.Create', '', 'active'),
(174, 'PO_Transactions.Settings.Edit', '', 'active'),
(175, 'PO_Transactions.Settings.Delete', '', 'active'),
(176, 'PO_Transactions.Developer.View', '', 'active'),
(177, 'PO_Transactions.Developer.Create', '', 'active'),
(178, 'PO_Transactions.Developer.Edit', '', 'active'),
(179, 'PO_Transactions.Developer.Delete', '', 'active'),
(196, 'Vendors.Content.View', '', 'active'),
(197, 'Vendors.Content.Create', '', 'active'),
(198, 'Vendors.Content.Edit', '', 'active'),
(199, 'Vendors.Content.Delete', '', 'active'),
(200, 'Vendors.Reports.View', '', 'active'),
(201, 'Vendors.Reports.Create', '', 'active'),
(202, 'Vendors.Reports.Edit', '', 'active'),
(203, 'Vendors.Reports.Delete', '', 'active'),
(204, 'Vendors.Settings.View', '', 'active'),
(205, 'Vendors.Settings.Create', '', 'active'),
(206, 'Vendors.Settings.Edit', '', 'active'),
(207, 'Vendors.Settings.Delete', '', 'active'),
(208, 'Vendors.Developer.View', '', 'active'),
(209, 'Vendors.Developer.Create', '', 'active'),
(210, 'Vendors.Developer.Edit', '', 'active'),
(211, 'Vendors.Developer.Delete', '', 'active'),
(212, 'Samples.Content.View', '', 'active'),
(213, 'Samples.Content.Create', '', 'active'),
(214, 'Samples.Content.Edit', '', 'active'),
(215, 'Samples.Content.Delete', '', 'active'),
(216, 'Samples.Reports.View', '', 'active'),
(217, 'Samples.Reports.Create', '', 'active'),
(218, 'Samples.Reports.Edit', '', 'active'),
(219, 'Samples.Reports.Delete', '', 'active'),
(220, 'Samples.Settings.View', '', 'active'),
(221, 'Samples.Settings.Create', '', 'active'),
(222, 'Samples.Settings.Edit', '', 'active'),
(223, 'Samples.Settings.Delete', '', 'active'),
(224, 'Samples.Developer.View', '', 'active'),
(225, 'Samples.Developer.Create', '', 'active'),
(226, 'Samples.Developer.Edit', '', 'active'),
(227, 'Samples.Developer.Delete', '', 'active'),
(228, 'Permissions.Viewer.Manage', 'To manage the access control permissions for the Viewer role.', 'active'),
(261, 'Inquiries.Content.View', '', 'active'),
(262, 'Inquiries.Content.Create', '', 'active'),
(263, 'Inquiries.Content.Edit', '', 'active'),
(264, 'Inquiries.Content.Delete', '', 'active'),
(265, 'Inquiries.Reports.View', '', 'active'),
(266, 'Inquiries.Reports.Create', '', 'active'),
(267, 'Inquiries.Reports.Edit', '', 'active'),
(268, 'Inquiries.Reports.Delete', '', 'active'),
(269, 'Inquiries.Settings.View', '', 'active'),
(270, 'Inquiries.Settings.Create', '', 'active'),
(271, 'Inquiries.Settings.Edit', '', 'active'),
(272, 'Inquiries.Settings.Delete', '', 'active'),
(273, 'Inquiries.Developer.View', '', 'active'),
(274, 'Inquiries.Developer.Create', '', 'active'),
(275, 'Inquiries.Developer.Edit', '', 'active'),
(276, 'Inquiries.Developer.Delete', '', 'active'),
(277, 'Purchase_Orders.Content.View', '', 'active'),
(278, 'Purchase_Orders.Content.Create', '', 'active'),
(279, 'Purchase_Orders.Content.Edit', '', 'active'),
(280, 'Purchase_Orders.Content.Delete', '', 'active'),
(281, 'Purchase_Orders.Reports.View', '', 'active'),
(282, 'Purchase_Orders.Reports.Create', '', 'active'),
(283, 'Purchase_Orders.Reports.Edit', '', 'active'),
(284, 'Purchase_Orders.Reports.Delete', '', 'active'),
(285, 'Purchase_Orders.Settings.View', '', 'active'),
(286, 'Purchase_Orders.Settings.Create', '', 'active'),
(287, 'Purchase_Orders.Settings.Edit', '', 'active'),
(288, 'Purchase_Orders.Settings.Delete', '', 'active'),
(289, 'Purchase_Orders.Developer.View', '', 'active'),
(290, 'Purchase_Orders.Developer.Create', '', 'active'),
(291, 'Purchase_Orders.Developer.Edit', '', 'active'),
(292, 'Purchase_Orders.Developer.Delete', '', 'active'),
(293, 'Customers.Content.View', '', 'active'),
(294, 'Customers.Content.Create', '', 'active'),
(295, 'Customers.Content.Edit', '', 'active'),
(296, 'Customers.Content.Delete', '', 'active'),
(297, 'Customers.Reports.View', '', 'active'),
(298, 'Customers.Reports.Create', '', 'active'),
(299, 'Customers.Reports.Edit', '', 'active'),
(300, 'Customers.Reports.Delete', '', 'active'),
(301, 'Customers.Settings.View', '', 'active'),
(302, 'Customers.Settings.Create', '', 'active'),
(303, 'Customers.Settings.Edit', '', 'active'),
(304, 'Customers.Settings.Delete', '', 'active'),
(305, 'Customers.Developer.View', '', 'active'),
(306, 'Customers.Developer.Create', '', 'active'),
(307, 'Customers.Developer.Edit', '', 'active'),
(308, 'Customers.Developer.Delete', '', 'active'),
(325, 'Containers.Content.View', '', 'active'),
(326, 'Containers.Content.Create', '', 'active'),
(327, 'Containers.Content.Edit', '', 'active'),
(328, 'Containers.Content.Delete', '', 'active'),
(329, 'Containers.Reports.View', '', 'active'),
(330, 'Containers.Reports.Create', '', 'active'),
(331, 'Containers.Reports.Edit', '', 'active'),
(332, 'Containers.Reports.Delete', '', 'active'),
(333, 'Containers.Settings.View', '', 'active'),
(334, 'Containers.Settings.Create', '', 'active'),
(335, 'Containers.Settings.Edit', '', 'active'),
(336, 'Containers.Settings.Delete', '', 'active'),
(337, 'Containers.Developer.View', '', 'active'),
(338, 'Containers.Developer.Create', '', 'active'),
(339, 'Containers.Developer.Edit', '', 'active'),
(340, 'Containers.Developer.Delete', '', 'active'),
(357, 'Purchase_Order_Documents.Content.View', '', 'active'),
(358, 'Purchase_Order_Documents.Content.Create', '', 'active'),
(359, 'Purchase_Order_Documents.Content.Edit', '', 'active'),
(360, 'Purchase_Order_Documents.Content.Delete', '', 'active'),
(361, 'Purchase_Order_Documents.Reports.View', '', 'active'),
(362, 'Purchase_Order_Documents.Reports.Create', '', 'active'),
(363, 'Purchase_Order_Documents.Reports.Edit', '', 'active'),
(364, 'Purchase_Order_Documents.Reports.Delete', '', 'active'),
(365, 'Purchase_Order_Documents.Settings.View', '', 'active'),
(366, 'Purchase_Order_Documents.Settings.Create', '', 'active'),
(367, 'Purchase_Order_Documents.Settings.Edit', '', 'active'),
(368, 'Purchase_Order_Documents.Settings.Delete', '', 'active'),
(369, 'Purchase_Order_Documents.Developer.View', '', 'active'),
(370, 'Purchase_Order_Documents.Developer.Create', '', 'active'),
(371, 'Purchase_Order_Documents.Developer.Edit', '', 'active'),
(372, 'Purchase_Order_Documents.Developer.Delete', '', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `bf_po_transactions`
--

DROP TABLE IF EXISTS `bf_po_transactions`;
CREATE TABLE IF NOT EXISTS `bf_po_transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `po_ref` varchar(255) NOT NULL,
  `trans_type` varchar(255) NOT NULL,
  `remit_date` date NOT NULL DEFAULT '0000-00-00',
  `rcvd_date` date NOT NULL DEFAULT '0000-00-00',
  `amount` decimal(18,3) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `bf_product`
--

DROP TABLE IF EXISTS `bf_product`;
CREATE TABLE IF NOT EXISTS `bf_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `bf_product`
--

INSERT INTO `bf_product` (`id`, `name`, `desc`, `deleted`, `created_on`, `modified_on`) VALUES
(1, 'OCF', 'Organic Coconut Flour', 0, '2014-10-14 11:55:14', '2014-10-15 11:08:07'),
(2, 'OVCO', 'Organic Virgin Coconut Oil', 0, '2014-10-14 11:55:27', '2014-10-15 11:08:21');

-- --------------------------------------------------------

--
-- Table structure for table `bf_purchase_orders`
--

DROP TABLE IF EXISTS `bf_purchase_orders`;
CREATE TABLE IF NOT EXISTS `bf_purchase_orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `po_num` varchar(255) NOT NULL,
  `po_date` date NOT NULL DEFAULT '0000-00-00',
  `po_ref` varchar(255) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` decimal(18,3) NOT NULL,
  `uom_id` int(11) NOT NULL,
  `reqd_by` date NOT NULL DEFAULT '0000-00-00',
  `status` varchar(25) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `bf_purchase_orders`
--

INSERT INTO `bf_purchase_orders` (`id`, `po_num`, `po_date`, `po_ref`, `product_id`, `quantity`, `uom_id`, `reqd_by`, `status`, `customer_id`, `deleted`, `created_on`, `modified_on`) VALUES
(1, 'RS-2014-12', '2014-09-01', 'RS-SB-OVCO-201409', 2, 56.000, 1, '2014-10-01', 'Active', 1, 0, '2014-10-14 17:31:45', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `bf_purchase_order_documents`
--

DROP TABLE IF EXISTS `bf_purchase_order_documents`;
CREATE TABLE IF NOT EXISTS `bf_purchase_order_documents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `doc_type` int(11) NOT NULL,
  `po_ref` varchar(255) NOT NULL,
  `container` varchar(255) NOT NULL,
  `attachments` varchar(4000) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `bf_purchase_order_documents`
--

INSERT INTO `bf_purchase_order_documents` (`id`, `doc_type`, `po_ref`, `container`, `attachments`, `deleted`, `created_on`, `modified_on`) VALUES
(2, 2, 'RS-SB-OVCO-201409', 'OOLU0448435', 'a:14:{s:9:"file_name";s:30:"TC_OOLU2180465_OOLU0448435.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:58:"/var/www/crm/public/uploads/TC_OOLU2180465_OOLU0448435.pdf";s:8:"raw_name";s:26:"TC_OOLU2180465_OOLU0448435";s:9:"orig_name";s:30:"TC_OOLU2180465_OOLU0448435.pdf";s:11:"client_name";s:30:"TC_OOLU2180465_OOLU0448435.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:63.259999999999998;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:55:10', '0000-00-00 00:00:00'),
(3, 2, 'RS-SB-OVCO-201409', 'OOLU2180465', 'a:14:{s:9:"file_name";s:31:"TC_OOLU2180465_OOLU04484351.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:59:"/var/www/crm/public/uploads/TC_OOLU2180465_OOLU04484351.pdf";s:8:"raw_name";s:27:"TC_OOLU2180465_OOLU04484351";s:9:"orig_name";s:30:"TC_OOLU2180465_OOLU0448435.pdf";s:11:"client_name";s:30:"TC_OOLU2180465_OOLU0448435.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:63.259999999999998;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:55:27', '0000-00-00 00:00:00'),
(4, 3, 'RS-SB-OVCO-201409', 'OOLU0448435', 'a:14:{s:9:"file_name";s:43:"CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:71:"/var/www/crm/public/uploads/CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:8:"raw_name";s:39:"CoA_OOLU2180465_OOLU0448435_KKTU7618462";s:9:"orig_name";s:43:"CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:11:"client_name";s:43:"CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1262.79;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:56:22', '0000-00-00 00:00:00'),
(5, 1, 'RS-SB-OVCO-201409', 'OOLU0448435', 'a:14:{s:9:"file_name";s:19:"CoO_OOLU0448435.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:47:"/var/www/crm/public/uploads/CoO_OOLU0448435.pdf";s:8:"raw_name";s:15:"CoO_OOLU0448435";s:9:"orig_name";s:19:"CoO_OOLU0448435.pdf";s:11:"client_name";s:19:"CoO_OOLU0448435.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:88.370000000000005;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:56:45', '0000-00-00 00:00:00'),
(6, 4, 'RS-SB-OVCO-201409', 'OOLU0448435', 'a:14:{s:9:"file_name";s:30:"BL_OOLU2180465_OOLU0448435.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:58:"/var/www/crm/public/uploads/BL_OOLU2180465_OOLU0448435.pdf";s:8:"raw_name";s:26:"BL_OOLU2180465_OOLU0448435";s:9:"orig_name";s:30:"BL_OOLU2180465_OOLU0448435.pdf";s:11:"client_name";s:30:"BL_OOLU2180465_OOLU0448435.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:319.92000000000002;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:57:14', '0000-00-00 00:00:00'),
(7, 3, 'RS-SB-OVCO-201409', 'OOLU2180465', 'a:14:{s:9:"file_name";s:44:"CoA_OOLU2180465_OOLU0448435_KKTU76184621.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:72:"/var/www/crm/public/uploads/CoA_OOLU2180465_OOLU0448435_KKTU76184621.pdf";s:8:"raw_name";s:40:"CoA_OOLU2180465_OOLU0448435_KKTU76184621";s:9:"orig_name";s:43:"CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:11:"client_name";s:43:"CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1262.79;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:57:54', '0000-00-00 00:00:00'),
(8, 1, 'RS-SB-OVCO-201409', 'OOLU2180465', 'a:14:{s:9:"file_name";s:19:"CoO_OOLU2180465.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:47:"/var/www/crm/public/uploads/CoO_OOLU2180465.pdf";s:8:"raw_name";s:15:"CoO_OOLU2180465";s:9:"orig_name";s:19:"CoO_OOLU2180465.pdf";s:11:"client_name";s:19:"CoO_OOLU2180465.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:87.819999999999993;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:58:18', '0000-00-00 00:00:00'),
(9, 4, 'RS-SB-OVCO-201409', 'OOLU2180465', 'a:14:{s:9:"file_name";s:31:"BL_OOLU2180465_OOLU04484351.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:59:"/var/www/crm/public/uploads/BL_OOLU2180465_OOLU04484351.pdf";s:8:"raw_name";s:27:"BL_OOLU2180465_OOLU04484351";s:9:"orig_name";s:30:"BL_OOLU2180465_OOLU0448435.pdf";s:11:"client_name";s:30:"BL_OOLU2180465_OOLU0448435.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:319.92000000000002;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:58:34', '0000-00-00 00:00:00'),
(10, 2, 'RS-SB-OVCO-201409', 'TCLU2993635', 'a:14:{s:9:"file_name";s:30:"TC_TCLU2993635_KKTU7618462.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:58:"/var/www/crm/public/uploads/TC_TCLU2993635_KKTU7618462.pdf";s:8:"raw_name";s:26:"TC_TCLU2993635_KKTU7618462";s:9:"orig_name";s:30:"TC_TCLU2993635_KKTU7618462.pdf";s:11:"client_name";s:30:"TC_TCLU2993635_KKTU7618462.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:63.710000000000001;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 10:59:19', '0000-00-00 00:00:00'),
(11, 3, 'RS-SB-OVCO-201409', 'TCLU2993635', 'a:14:{s:9:"file_name";s:19:"CoA_TCLU2993635.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:47:"/var/www/crm/public/uploads/CoA_TCLU2993635.pdf";s:8:"raw_name";s:15:"CoA_TCLU2993635";s:9:"orig_name";s:19:"CoA_TCLU2993635.pdf";s:11:"client_name";s:19:"CoA_TCLU2993635.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:117.69;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:00:28', '0000-00-00 00:00:00'),
(12, 1, 'RS-SB-OVCO-201409', 'TCLU2993635', 'a:14:{s:9:"file_name";s:19:"CoO_TCLU2993635.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:47:"/var/www/crm/public/uploads/CoO_TCLU2993635.pdf";s:8:"raw_name";s:15:"CoO_TCLU2993635";s:9:"orig_name";s:19:"CoO_TCLU2993635.pdf";s:11:"client_name";s:19:"CoO_TCLU2993635.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:89.290000000000006;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:00:59', '0000-00-00 00:00:00'),
(13, 2, 'RS-SB-OVCO-201409', 'KKTU7618462', 'a:14:{s:9:"file_name";s:31:"TC_TCLU2993635_KKTU76184621.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:59:"/var/www/crm/public/uploads/TC_TCLU2993635_KKTU76184621.pdf";s:8:"raw_name";s:27:"TC_TCLU2993635_KKTU76184621";s:9:"orig_name";s:30:"TC_TCLU2993635_KKTU7618462.pdf";s:11:"client_name";s:30:"TC_TCLU2993635_KKTU7618462.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:63.710000000000001;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:01:27', '0000-00-00 00:00:00'),
(14, 3, 'RS-SB-OVCO-201409', 'KKTU7618462', 'a:14:{s:9:"file_name";s:44:"CoA_OOLU2180465_OOLU0448435_KKTU76184622.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:72:"/var/www/crm/public/uploads/CoA_OOLU2180465_OOLU0448435_KKTU76184622.pdf";s:8:"raw_name";s:40:"CoA_OOLU2180465_OOLU0448435_KKTU76184622";s:9:"orig_name";s:43:"CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:11:"client_name";s:43:"CoA_OOLU2180465_OOLU0448435_KKTU7618462.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1262.79;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:01:52', '0000-00-00 00:00:00'),
(15, 2, 'RS-SB-OVCO-201409', 'EMCU146112-8', 'a:14:{s:9:"file_name";s:19:"TC_EMCU146112-8.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:47:"/var/www/crm/public/uploads/TC_EMCU146112-8.pdf";s:8:"raw_name";s:15:"TC_EMCU146112-8";s:9:"orig_name";s:19:"TC_EMCU146112-8.pdf";s:11:"client_name";s:19:"TC_EMCU146112-8.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:12.449999999999999;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:02:17', '0000-00-00 00:00:00'),
(16, 2, 'RS-SB-OVCO-201409', 'EMCU146112-8', 'a:14:{s:9:"file_name";s:20:"TC_EMCU146112-81.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:48:"/var/www/crm/public/uploads/TC_EMCU146112-81.pdf";s:8:"raw_name";s:16:"TC_EMCU146112-81";s:9:"orig_name";s:19:"TC_EMCU146112-8.pdf";s:11:"client_name";s:19:"TC_EMCU146112-8.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:12.449999999999999;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:02:18', '0000-00-00 00:00:00'),
(17, 3, 'RS-SB-OVCO-201409', 'EMCU146112-8', 'a:14:{s:9:"file_name";s:20:"CoA_EMCU_1461128.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:48:"/var/www/crm/public/uploads/CoA_EMCU_1461128.pdf";s:8:"raw_name";s:16:"CoA_EMCU_1461128";s:9:"orig_name";s:20:"CoA_EMCU_1461128.pdf";s:11:"client_name";s:20:"CoA_EMCU 1461128.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1409.5699999999999;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:02:44', '0000-00-00 00:00:00'),
(18, 1, 'RS-SB-OVCO-201409', 'EMCU146112-8', 'a:14:{s:9:"file_name";s:20:"CoO_EMCU146112-8.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:48:"/var/www/crm/public/uploads/CoO_EMCU146112-8.pdf";s:8:"raw_name";s:16:"CoO_EMCU146112-8";s:9:"orig_name";s:20:"CoO_EMCU146112-8.pdf";s:11:"client_name";s:20:"CoO_EMCU146112-8.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:821.10000000000002;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:03:00', '0000-00-00 00:00:00'),
(19, 2, 'RS-SB-OVCO-201409', 'TTHU5619064', 'a:14:{s:9:"file_name";s:30:"TC_TTHU5619064_APZU4887232.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:58:"/var/www/crm/public/uploads/TC_TTHU5619064_APZU4887232.pdf";s:8:"raw_name";s:26:"TC_TTHU5619064_APZU4887232";s:9:"orig_name";s:30:"TC_TTHU5619064_APZU4887232.pdf";s:11:"client_name";s:30:"TC_TTHU5619064_APZU4887232.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1112.79;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:03:22', '0000-00-00 00:00:00'),
(20, 3, 'RS-SB-OVCO-201409', 'TTHU5619064', 'a:14:{s:9:"file_name";s:31:"CoA_TTHU5619064_APZU4887232.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:59:"/var/www/crm/public/uploads/CoA_TTHU5619064_APZU4887232.pdf";s:8:"raw_name";s:27:"CoA_TTHU5619064_APZU4887232";s:9:"orig_name";s:31:"CoA_TTHU5619064_APZU4887232.pdf";s:11:"client_name";s:31:"CoA_TTHU5619064_APZU4887232.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1074.3;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:03:40', '0000-00-00 00:00:00'),
(21, 2, 'RS-SB-OVCO-201409', 'APZU4887232', 'a:14:{s:9:"file_name";s:31:"TC_TTHU5619064_APZU48872321.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:59:"/var/www/crm/public/uploads/TC_TTHU5619064_APZU48872321.pdf";s:8:"raw_name";s:27:"TC_TTHU5619064_APZU48872321";s:9:"orig_name";s:30:"TC_TTHU5619064_APZU4887232.pdf";s:11:"client_name";s:30:"TC_TTHU5619064_APZU4887232.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1112.79;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:04:06', '0000-00-00 00:00:00'),
(22, 3, 'RS-SB-OVCO-201409', 'APZU4887232', 'a:14:{s:9:"file_name";s:32:"CoA_TTHU5619064_APZU48872321.pdf";s:9:"file_type";s:15:"application/pdf";s:9:"file_path";s:28:"/var/www/crm/public/uploads/";s:9:"full_path";s:60:"/var/www/crm/public/uploads/CoA_TTHU5619064_APZU48872321.pdf";s:8:"raw_name";s:28:"CoA_TTHU5619064_APZU48872321";s:9:"orig_name";s:31:"CoA_TTHU5619064_APZU4887232.pdf";s:11:"client_name";s:31:"CoA_TTHU5619064_APZU4887232.pdf";s:8:"file_ext";s:4:".pdf";s:9:"file_size";d:1074.3;s:8:"is_image";b:0;s:11:"image_width";s:0:"";s:12:"image_height";s:0:"";s:10:"image_type";s:0:"";s:14:"image_size_str";s:0:"";}', 0, '2014-10-15 11:04:22', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `bf_roles`
--

DROP TABLE IF EXISTS `bf_roles`;
CREATE TABLE IF NOT EXISTS `bf_roles` (
  `role_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(60) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `default` tinyint(1) NOT NULL DEFAULT '0',
  `can_delete` tinyint(1) NOT NULL DEFAULT '1',
  `login_destination` varchar(255) NOT NULL DEFAULT '/',
  `deleted` int(1) NOT NULL DEFAULT '0',
  `default_context` varchar(255) NOT NULL DEFAULT 'content',
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `bf_roles`
--

INSERT INTO `bf_roles` (`role_id`, `role_name`, `description`, `default`, `can_delete`, `login_destination`, `deleted`, `default_context`) VALUES
(1, 'Administrator', 'Has full control over every aspect of the site.', 0, 0, '', 0, 'content'),
(2, 'Editor', 'Can handle day-to-day management, but does not have full power.', 0, 1, '/admin/content', 0, 'content'),
(4, 'User', 'This is the default user with access to login.', 0, 0, '', 0, 'content'),
(6, 'Developer', 'Developers typically are the only ones that can access the developer tools. Otherwise identical to Administrators, at least until the site is handed off.', 0, 1, '', 0, 'content'),
(7, 'Contributor', 'Contributor - One level above user, can create transactions', 1, 1, '/admin/content', 0, 'content'),
(8, 'Viewer', 'Has view access to selected sections', 0, 1, '/admin/content', 0, 'content');

-- --------------------------------------------------------

--
-- Table structure for table `bf_role_permissions`
--

DROP TABLE IF EXISTS `bf_role_permissions`;
CREATE TABLE IF NOT EXISTS `bf_role_permissions` (
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`role_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bf_role_permissions`
--

INSERT INTO `bf_role_permissions` (`role_id`, `permission_id`) VALUES
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(1, 18),
(1, 19),
(1, 20),
(1, 21),
(1, 22),
(1, 24),
(1, 25),
(1, 27),
(1, 28),
(1, 29),
(1, 30),
(1, 31),
(1, 32),
(1, 33),
(1, 34),
(1, 35),
(1, 36),
(1, 37),
(1, 38),
(1, 39),
(1, 40),
(1, 41),
(1, 42),
(1, 43),
(1, 44),
(1, 45),
(1, 46),
(1, 49),
(1, 50),
(1, 51),
(1, 52),
(1, 53),
(1, 54),
(1, 55),
(1, 56),
(1, 57),
(1, 58),
(1, 59),
(1, 60),
(1, 61),
(1, 62),
(1, 63),
(1, 64),
(1, 65),
(1, 66),
(1, 67),
(1, 68),
(1, 69),
(1, 70),
(1, 71),
(1, 72),
(1, 73),
(1, 74),
(1, 75),
(1, 76),
(1, 77),
(1, 78),
(1, 79),
(1, 80),
(1, 81),
(1, 82),
(1, 99),
(1, 100),
(1, 101),
(1, 102),
(1, 103),
(1, 104),
(1, 105),
(1, 106),
(1, 107),
(1, 108),
(1, 109),
(1, 110),
(1, 111),
(1, 112),
(1, 113),
(1, 114),
(1, 115),
(1, 164),
(1, 165),
(1, 166),
(1, 167),
(1, 168),
(1, 169),
(1, 170),
(1, 171),
(1, 172),
(1, 173),
(1, 174),
(1, 175),
(1, 176),
(1, 177),
(1, 178),
(1, 179),
(1, 196),
(1, 197),
(1, 198),
(1, 199),
(1, 200),
(1, 201),
(1, 202),
(1, 203),
(1, 204),
(1, 205),
(1, 206),
(1, 207),
(1, 208),
(1, 209),
(1, 210),
(1, 211),
(1, 212),
(1, 213),
(1, 214),
(1, 215),
(1, 216),
(1, 217),
(1, 218),
(1, 219),
(1, 220),
(1, 221),
(1, 222),
(1, 223),
(1, 224),
(1, 225),
(1, 226),
(1, 227),
(1, 228),
(1, 261),
(1, 262),
(1, 263),
(1, 264),
(1, 265),
(1, 266),
(1, 267),
(1, 268),
(1, 269),
(1, 270),
(1, 271),
(1, 272),
(1, 273),
(1, 274),
(1, 275),
(1, 276),
(1, 277),
(1, 278),
(1, 279),
(1, 280),
(1, 281),
(1, 282),
(1, 283),
(1, 284),
(1, 285),
(1, 286),
(1, 287),
(1, 288),
(1, 289),
(1, 290),
(1, 291),
(1, 292),
(1, 293),
(1, 294),
(1, 295),
(1, 296),
(1, 297),
(1, 298),
(1, 299),
(1, 300),
(1, 301),
(1, 302),
(1, 303),
(1, 304),
(1, 305),
(1, 306),
(1, 307),
(1, 308),
(1, 325),
(1, 326),
(1, 327),
(1, 328),
(1, 329),
(1, 330),
(1, 331),
(1, 332),
(1, 333),
(1, 334),
(1, 335),
(1, 336),
(1, 337),
(1, 338),
(1, 339),
(1, 340),
(1, 357),
(1, 358),
(1, 359),
(1, 360),
(1, 361),
(1, 362),
(1, 363),
(1, 364),
(1, 365),
(1, 366),
(1, 367),
(1, 368),
(1, 369),
(1, 370),
(1, 371),
(1, 372),
(2, 2),
(2, 51),
(2, 52),
(2, 53),
(2, 54),
(2, 67),
(2, 68),
(2, 69),
(2, 70),
(2, 99),
(2, 100),
(2, 101),
(2, 102),
(2, 115),
(2, 164),
(2, 165),
(2, 166),
(2, 167),
(2, 196),
(2, 197),
(2, 198),
(2, 199),
(6, 2),
(6, 3),
(6, 4),
(6, 5),
(6, 6),
(6, 7),
(6, 8),
(6, 9),
(6, 10),
(6, 11),
(6, 12),
(6, 13),
(6, 49),
(7, 2),
(7, 8),
(7, 67),
(7, 212),
(7, 213),
(7, 214),
(8, 2),
(8, 325),
(8, 357);

-- --------------------------------------------------------

--
-- Table structure for table `bf_samples`
--

DROP TABLE IF EXISTS `bf_samples`;
CREATE TABLE IF NOT EXISTS `bf_samples` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `quantity` decimal(18,3) NOT NULL,
  `uom_id` int(11) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  `date_received` date NOT NULL DEFAULT '0000-00-00',
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `bf_samples`
--

INSERT INTO `bf_samples` (`id`, `product_id`, `quantity`, `uom_id`, `vendor_id`, `date_received`, `deleted`, `created_on`, `modified_on`) VALUES
(2, 1, 2.000, 2, 1, '2014-10-02', 0, '2014-10-14 12:36:23', '2014-10-14 16:24:27');

-- --------------------------------------------------------

--
-- Table structure for table `bf_schema_version`
--

DROP TABLE IF EXISTS `bf_schema_version`;
CREATE TABLE IF NOT EXISTS `bf_schema_version` (
  `type` varchar(40) NOT NULL,
  `version` int(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bf_schema_version`
--

INSERT INTO `bf_schema_version` (`type`, `version`) VALUES
('containers_', 2),
('core', 37),
('customers_', 2),
('document_types_', 2),
('inquiries_', 2),
('po_transactions_', 2),
('product_', 2),
('purchase_orders_', 2),
('purchase_order_documents_', 2),
('samples_', 2),
('uom_', 2),
('vendors_', 2);

-- --------------------------------------------------------

--
-- Table structure for table `bf_sessions`
--

DROP TABLE IF EXISTS `bf_sessions`;
CREATE TABLE IF NOT EXISTS `bf_sessions` (
  `session_id` varchar(40) NOT NULL DEFAULT '0',
  `ip_address` varchar(45) NOT NULL DEFAULT '0',
  `user_agent` varchar(120) NOT NULL,
  `last_activity` int(10) unsigned NOT NULL DEFAULT '0',
  `user_data` text NOT NULL,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `bf_settings`
--

DROP TABLE IF EXISTS `bf_settings`;
CREATE TABLE IF NOT EXISTS `bf_settings` (
  `name` varchar(30) NOT NULL,
  `module` varchar(50) NOT NULL,
  `value` varchar(255) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bf_settings`
--

INSERT INTO `bf_settings` (`name`, `module`, `value`) VALUES
('auth.allow_name_change', 'core', '1'),
('auth.allow_register', 'core', '0'),
('auth.allow_remember', 'core', '1'),
('auth.do_login_redirect', 'core', '1'),
('auth.login_type', 'core', 'both'),
('auth.name_change_frequency', 'core', '1'),
('auth.name_change_limit', 'core', '1'),
('auth.password_force_mixed_case', 'core', '0'),
('auth.password_force_numbers', 'core', '0'),
('auth.password_force_symbols', 'core', '0'),
('auth.password_min_length', 'core', '8'),
('auth.password_show_labels', 'core', '0'),
('auth.remember_length', 'core', '1209600'),
('auth.user_activation_method', 'core', '0'),
('auth.use_extended_profile', 'core', '0'),
('auth.use_usernames', 'core', '1'),
('ext.country', 'core', 'US'),
('ext.state', 'core', 'CA'),
('ext.street_name', 'core', ''),
('ext.type', 'core', 'small'),
('mailpath', 'email', '/usr/sbin/sendmail'),
('mailtype', 'email', 'text'),
('password_iterations', 'users', '8'),
('protocol', 'email', 'mail'),
('sender_email', 'email', ''),
('site.languages', 'core', 'a:3:{i:0;s:10:"portuguese";i:1;s:7:"english";i:2;s:7:"persian";}'),
('site.list_limit', 'core', '25'),
('site.show_front_profiler', 'core', '1'),
('site.show_profiler', 'core', '1'),
('site.status', 'core', '1'),
('site.system_email', 'core', 'info@sristibiosciences.com'),
('site.title', 'core', 'Sristi Bio'),
('smtp_host', 'email', ''),
('smtp_pass', 'email', ''),
('smtp_port', 'email', ''),
('smtp_timeout', 'email', ''),
('smtp_user', 'email', ''),
('updates.bleeding_edge', 'core', '0'),
('updates.do_check', 'core', '0');

-- --------------------------------------------------------

--
-- Table structure for table `bf_states`
--

DROP TABLE IF EXISTS `bf_states`;
CREATE TABLE IF NOT EXISTS `bf_states` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(40) NOT NULL,
  `abbrev` char(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=64 ;

--
-- Dumping data for table `bf_states`
--

INSERT INTO `bf_states` (`id`, `name`, `abbrev`) VALUES
(1, 'Alaska', 'AK'),
(2, 'Alabama', 'AL'),
(3, 'American Samoa', 'AS'),
(4, 'Arizona', 'AZ'),
(5, 'Arkansas', 'AR'),
(6, 'California', 'CA'),
(7, 'Colorado', 'CO'),
(8, 'Connecticut', 'CT'),
(9, 'Delaware', 'DE'),
(10, 'District of Columbia', 'DC'),
(11, 'Florida', 'FL'),
(12, 'Georgia', 'GA'),
(13, 'Guam', 'GU'),
(14, 'Hawaii', 'HI'),
(15, 'Idaho', 'ID'),
(16, 'Illinois', 'IL'),
(17, 'Indiana', 'IN'),
(18, 'Iowa', 'IA'),
(19, 'Kansas', 'KS'),
(20, 'Kentucky', 'KY'),
(21, 'Louisiana', 'LA'),
(22, 'Maine', 'ME'),
(23, 'Marshall Islands', 'MH'),
(24, 'Maryland', 'MD'),
(25, 'Massachusetts', 'MA'),
(26, 'Michigan', 'MI'),
(27, 'Minnesota', 'MN'),
(28, 'Mississippi', 'MS'),
(29, 'Missouri', 'MO'),
(30, 'Montana', 'MT'),
(31, 'Nebraska', 'NE'),
(32, 'Nevada', 'NV'),
(33, 'New Hampshire', 'NH'),
(34, 'New Jersey', 'NJ'),
(35, 'New Mexico', 'NM'),
(36, 'New York', 'NY'),
(37, 'North Carolina', 'NC'),
(38, 'North Dakota', 'ND'),
(39, 'Northern Mariana Islands', 'MP'),
(40, 'Ohio', 'OH'),
(41, 'Oklahoma', 'OK'),
(42, 'Oregon', 'OR'),
(43, 'Palau', 'PW'),
(44, 'Pennsylvania', 'PA'),
(45, 'Puerto Rico', 'PR'),
(46, 'Rhode Island', 'RI'),
(47, 'South Carolina', 'SC'),
(48, 'South Dakota', 'SD'),
(49, 'Tennessee', 'TN'),
(50, 'Texas', 'TX'),
(51, 'Utah', 'UT'),
(52, 'Vermont', 'VT'),
(53, 'Virgin Islands', 'VI'),
(54, 'Virginia', 'VA'),
(55, 'Washington', 'WA'),
(56, 'West Virginia', 'WV'),
(57, 'Wisconsin', 'WI'),
(58, 'Wyoming', 'WY'),
(59, 'Armed Forces Africa', 'AE'),
(60, 'Armed Forces Canada', 'AE'),
(61, 'Armed Forces Europe', 'AE'),
(62, 'Armed Forces Middle East', 'AE'),
(63, 'Armed Forces Pacific', 'AP');

-- --------------------------------------------------------

--
-- Table structure for table `bf_uom`
--

DROP TABLE IF EXISTS `bf_uom`;
CREATE TABLE IF NOT EXISTS `bf_uom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `bf_uom`
--

INSERT INTO `bf_uom` (`id`, `name`, `deleted`, `created_on`, `modified_on`) VALUES
(1, 'Metric Tonnes', 0, '2014-10-14 09:59:39', '0000-00-00 00:00:00'),
(2, 'Kilograms', 0, '2014-10-14 09:59:49', '0000-00-00 00:00:00'),
(3, 'Litres', 0, '2014-10-14 09:59:56', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `bf_users`
--

DROP TABLE IF EXISTS `bf_users`;
CREATE TABLE IF NOT EXISTS `bf_users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL DEFAULT '4',
  `email` varchar(120) NOT NULL,
  `username` varchar(30) NOT NULL DEFAULT '',
  `password_hash` char(60) NOT NULL,
  `reset_hash` varchar(40) DEFAULT NULL,
  `last_login` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `last_ip` varchar(40) NOT NULL DEFAULT '',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `reset_by` int(10) DEFAULT NULL,
  `banned` tinyint(1) NOT NULL DEFAULT '0',
  `ban_message` varchar(255) DEFAULT NULL,
  `display_name` varchar(255) DEFAULT '',
  `display_name_changed` date DEFAULT NULL,
  `timezone` char(4) NOT NULL DEFAULT 'UM6',
  `language` varchar(20) NOT NULL DEFAULT 'english',
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `activate_hash` varchar(40) NOT NULL DEFAULT '',
  `password_iterations` int(4) NOT NULL,
  `force_password_reset` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `bf_users`
--

INSERT INTO `bf_users` (`id`, `role_id`, `email`, `username`, `password_hash`, `reset_hash`, `last_login`, `last_ip`, `created_on`, `deleted`, `reset_by`, `banned`, `ban_message`, `display_name`, `display_name_changed`, `timezone`, `language`, `active`, `activate_hash`, `password_iterations`, `force_password_reset`) VALUES
(1, 1, 'admin@procxl.com', 'admin', '$2a$08$7jP3hra4WC9u60BDu8dlQOd4pgYm03lAfb/M3ht3BZVvfDts2pwGe', NULL, '2014-10-15 11:40:39', '127.0.0.1', '2014-10-14 05:03:22', 0, NULL, 0, NULL, 'admin', NULL, 'UP55', 'english', 1, '', 0, 0),
(2, 2, 'ramakrishna@sristibiosciences.com', 'ramakrishna', '$2a$08$1XdzXDIBQ9Q2X0ww9kehzOoaVpP1R.Rc1cJSneq3LrFA9ubd8Ur6q', NULL, '2014-10-14 11:27:27', '127.0.0.1', '2014-10-14 05:50:45', 0, NULL, 0, NULL, 'Ramakrishna', NULL, 'UP55', 'english', 1, '', 8, 0),
(3, 7, 'karthik@sristibiosciences.com', 'karthik', '$2a$08$I6ELFHNUpOZg638Ky/K1feJ.2OnFwRCmdqCszEeNTk7wCbV8jS8si', NULL, '2014-10-15 10:04:25', '127.0.0.1', '2014-10-14 11:43:52', 0, NULL, 0, NULL, 'Karthik', NULL, 'UP55', 'english', 1, '', 8, 0),
(4, 8, 'alekhya@sristibiosciences.com', 'alekhya', '$2a$08$7srJdW7taabMucgzCRf7mOQ9dxUl3Zx1uJMKypFupjdX1FqnQvIMm', NULL, '2014-10-15 11:36:30', '127.0.0.1', '2014-10-14 12:42:59', 0, NULL, 0, NULL, 'Alekhya', NULL, 'UP55', 'english', 1, '', 8, 0);

-- --------------------------------------------------------

--
-- Table structure for table `bf_user_cookies`
--

DROP TABLE IF EXISTS `bf_user_cookies`;
CREATE TABLE IF NOT EXISTS `bf_user_cookies` (
  `user_id` bigint(20) NOT NULL,
  `token` varchar(128) NOT NULL,
  `created_on` datetime NOT NULL,
  KEY `token` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bf_user_cookies`
--

INSERT INTO `bf_user_cookies` (`user_id`, `token`, `created_on`) VALUES
(1, 'qpk3EU5BJArReKkt2IGTbexeR2fiQ6ESL4MXYYK9mK3WsWR3bUlBhLiinCnqJQ0UOi34fBIxPDg9eglosutpIvdMwDAZKtJKkehzhTg9WPWJIABR5FKRlEcZuDO2msjc', '2014-10-14 11:40:22'),
(1, 'HasiM0xc3DNeqHyUrptIFDyNETKW3bnRk82LeKWJoN79i61wiBguz7gsVbmgucspD6GACBwAw9jgHktCe7roq1isc5uwBafBvIRZaV5KYYz0PrsN9j5EYI1FG8lebiYV', '2014-10-15 06:13:37'),
(3, 'm1pqGhHP33F4jp202PpmD12EeuIxNbxR96vsZYsUaig0BYT8UVyzOyOEQYaKFwqBDynDa13z73751eAUbNx6UdlrjELEg5IwdmnKLZ1vY6ypMKiktOdA1XcyDDJeRMSS', '2014-10-15 06:17:40');

-- --------------------------------------------------------

--
-- Table structure for table `bf_user_meta`
--

DROP TABLE IF EXISTS `bf_user_meta`;
CREATE TABLE IF NOT EXISTS `bf_user_meta` (
  `meta_id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(20) unsigned NOT NULL DEFAULT '0',
  `meta_key` varchar(255) NOT NULL DEFAULT '',
  `meta_value` text,
  PRIMARY KEY (`meta_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `bf_user_meta`
--

INSERT INTO `bf_user_meta` (`meta_id`, `user_id`, `meta_key`, `meta_value`) VALUES
(1, 2, 'street_name', ''),
(2, 2, 'state', 'SC'),
(3, 2, 'country', 'IN'),
(4, 2, 'type', 'small'),
(5, 1, 'street_name', ''),
(6, 1, 'state', 'SC'),
(7, 1, 'country', 'US'),
(8, 1, 'type', 'small'),
(9, 3, 'street_name', ''),
(10, 3, 'state', 'SC'),
(11, 3, 'country', 'US'),
(12, 3, 'type', 'small'),
(13, 4, 'street_name', ''),
(14, 4, 'state', 'SC'),
(15, 4, 'country', 'US'),
(16, 4, 'type', 'small');

-- --------------------------------------------------------

--
-- Table structure for table `bf_vendors`
--

DROP TABLE IF EXISTS `bf_vendors`;
CREATE TABLE IF NOT EXISTS `bf_vendors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `contact_name` varchar(255) NOT NULL,
  `contact_phone` varchar(255) NOT NULL,
  `address1` varchar(255) NOT NULL,
  `address2` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `country` varchar(2) NOT NULL,
  `work_phones` varchar(255) NOT NULL,
  `contact_email` varchar(255) NOT NULL,
  `website_url` varchar(255) NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `bf_vendors`
--

INSERT INTO `bf_vendors` (`id`, `name`, `contact_name`, `contact_phone`, `address1`, `address2`, `city`, `country`, `work_phones`, `contact_email`, `website_url`, `deleted`, `created_on`, `modified_on`) VALUES
(1, 'Cocotona', 'Safolas', '+94-9866722247', '', '', 'Colombo', 'LK', '', '', '', 0, '2014-10-14 10:44:18', '2014-10-14 11:54:02'),
(2, 'Replay Country Corporation', 'Joseph Chen', '+63-34234324', '', '', '', 'PH', '', '', '', 0, '2014-10-14 16:51:58', '0000-00-00 00:00:00');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
