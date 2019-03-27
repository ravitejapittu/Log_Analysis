# Log Analysis Project

### By Ravi Teja Pittu

This is the project from udacity NanoDegree : [Fullstack Web Developer](https://classroom.udacity.com/nanodegrees/nd004/dashboard/overview)

Aim of this project is to print report based on data in database by using python3 
and postgresql

### Here is your Tasks to Answer:-
1. **What are the most popular three articles of all time?** Which
  articles have been accessed the most? Present this information as a
  sorted list with the most popular article at the top.
2. **Who are the most popular article authors of all time?** That is,
   when you sum up all of the articles each author has written, which
   authors get the most page views? Present this as a sorted list with
   the most popular author at the top.
3. **On which days did more than 1% of requests lead to errors?** The
   log table includes a column status that indicates the HTTP status
   code that the news site sent to the user's browser. (Refer to this
   lesson for more information about the idea of HTTP status codes.) 
   
### Tools to Install for Project Setup:   

1. **Vagrant** - [Vagrant 2.2.3](https://releases.hashicorp.com/vagrant/2.2.3/vagrant_2.2.3_x86_64.msi)
2. **VirtualBox** - [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3. Download vagrant setup files from **[Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)**
This files contains all configuration (Python3, Postgresql,PIP8 etc) setup for our project
4. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
5. After downloading goto downloads folder and extract the zip file name contains **Log_Analysis**
6. Keep it there (or) you can move to your own project path
7. Download this project: [Log_Analysis project](https://github.com/ravitejapittu/Log_Analysis)

### Process of executing the project:
1. Goto Vagrant folder<br>
2. Open command prompt (or) Git Bash <br>
3. Run **vagrant up** - to start the commandline virtual machine for the first it may take very long time depending on your internet connection<br>
4. Run **vagrant ssh** command to enter into the virtual machine<br>
5. use command 'psql -d news -f newsdata.sql' to load database<br>
    -use '\c' to connect to database="news"<br>
    -use '\dt' to see the tables in database<br>
    -use '\dv' to see the views in database<br>
    -use '\q' to quit the database<br>
6. use command 'python Log_analysis.py' to run the program<br>

### Expected Output

vagrant@vagrant:~$ cd /vagrant/<br>
vagrant@vagrant:/vagrant$ cd Log_Analysis/<br>
vagrant@vagrant:/vagrant/Log_Analysis$ python Log_Analysis.py<br>

 The Results are:<br>

1. What are the most popular three articles of all time?<br>
 TOP THREE ARTICLES BY PAGE VIEWS :<br>
(1) "Candidate is jerk, alleges rival" ==>338647 views<br>
(2) "Bears love berries, alleges bear" ==>253801 views<br>
(3) "Bad things gone, say good people" ==>170098 views<br>

 2. Who are the most popular article authors of all time?<br>
 TOP THREE AUTHORS BY VIEWS :<br>
(1) "Ursula La Multa" ==>507594 views<br>
(2) "Rudolf von Treppenwitz" ==>423457 views<br>
(3) "Anonymous Contributor" ==>170098 views<br>

 3. On which days did more than 1% of requests lead to errors<br>
 DAYS WITH MORE THAN 1% ERRORS:<br>
July, 17, 2016 ==> 2.3% errors<br>

vagrant@vagrant:/vagrant/Log_Analysis$<br>

### Miscellaneous

This README document is based on a template suggested by PhilipCoach in this
Udacity forum [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524).
