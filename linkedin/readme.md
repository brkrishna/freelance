Overview
========

This Python script reads the linkedin credentials from settings.ini and searches for all companies listed in companies file. For each company it parses
the members and creates a csv with member details

Features
========

Runs in a batch mode and can resume from the last run company, for each company processed it would be written into companies done, so that it can
resume from the last run

System Requirements
===================

Tested on Win7 64 bit with python 3.5, along with the following python plugins
selenium - for interactive browsing
lxml - for parsing html content
os, time, random, re, configparser - built in python packages

Files in package
================

linkedin.py - contains the main routine to read settings, get companies and write members into csv
settings.ini - configuration file from which linkedin credentials, min and max wait time are read. A random number between min and max is used to wait
                during certain calls to enable page load and avoid getting blocked
companies - listed names of target companies from which we need members
companies_done - lists all companies that have been processed
dst_worldwide_services.csv - File with sample data, csv files are created with the name of the company in lowercase and underscore for spaces
                            ex: DST Worldwide Services was the name of the company and the output csv file is dst_worldwide_services.csv

How to use this package
=====================

from command prompt navigate to folder.
Add names of companies to be parsed into companies file
At the command prompt type : python linkedin.py

