How this works
==============

Launch command prompt go to c:\freecycle_org\App

Run the following commands 

1. python freecycle.py URLS 
2. python freecycle.py POSTS

1. This is to fetch all the group urls from the 12 regions in UK, a file named freecycle_groups.csv is created once this command runs successfullly

2. This is to fetch all the posts from each group url retrieved by step 1. 
	- On every run, picks a group url from freecycle_groups.csv
	- Append details into freecycle.csv 
	- Saves the image into images folder with the unique post_id value as image name
	- Writes the group url into urls_done file

The advantages of this process is that
	- For any reason if the job fails (internet down or we cancel the job etc), it would resume from the last group where it left
	- If we want to run this only for a specific group, simply remove the group url from urls_done file and run the 2nd command
	- Images are always over written 

Posted By
---------

To get posted by, you should be part of the group. Few groups allow you to join automatically, while the rest have admin approval. Wherever the admin approval is required, we will have to run the job again once we receive the confirmation email

How to re-run
-------------

Most of the occassions the list of groups doesn't change, 
	- we simply need to delete urls_done 
	- backup or delete freecycle.csv 
	- run the second command "python freecycle.py POSTS"

If we find any new groups on freecycle, we will run the first command "python freecycle.py posts", this will overwrite the existing file freecycle_groups.csv and include any new / changed groups


Pre-requisites
==============

* requests
* beautifulSoup 4

Other built in packages used
* re
* time
* datetime
* sys
* os
* collections
* csv
* urllib

Tested on windows 7 64bit Python 3.5