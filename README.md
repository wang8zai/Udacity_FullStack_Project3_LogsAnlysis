# Udacity FullStack Project3 LogsAnlysis

## Dependency 
### python 2.7
    install python here https://www.python.org/downloads/
    python pakage psycopg2 here http://initd.org/psycopg/docs/install.html
### Linux-based Virtual Machine
    vagrant download here https://www.vagrantup.com/downloads.html.
    Under the downloaded directionary. Bring the virtual machine back online (with vagrant up).
    Then log into it with vagrant ssh.

## Installtion

### Prerequisite
    1. Make sure you have installed vagrant. 
    2. You need to unzip vagrant and use cd to enter the unzip foller location.
    3. Bring the virtual machine back online. Using command line: vagrant up
    4. Log into virtual machine: vagrant ssh
    
### Load the data
    1. Unzip newsdata.zip to the vagrant directory, which is shared with your virtual machine.
    2. Get into vagrant directary: cd /vagrant
    3. load the data: psql -d news -f newsdata.sql
    
### Create view
    Before get into the program you need to create view.
    1. Connect to database called news: psql -d news
    2. You are now connected to the database. See addition below you will find four CREATE VIEWs.
    Copy them into the command line and press enter to create views.
    
### make it work
    Finally you made it ! run python project3.py in command line to see results.

## Description

    The user-facing newspaper site frontend itself, and the database behind it, are already built and running. 
    Build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. 
    The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. 
    Using that information, your code will answer questions about the site's user activity. The program in this project run from the command line. It won't take any input from the user. 
    Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.
        
## Results

    Most popular three articles of all time
    Candidate is jerk, alleges rival -- 338647 views
    Bears love berries, alleges bear -- 253801 views
    Bad things gone, say good people -- 170098 views

    Most popular article authors of all time?
    Ursula La Multa -- 507594 views
    Rudolf von Treppenwitz -- 423457 views
    Anonymous Contributor -- 170098 views
    Markoff Chaney -- 84557 views

    On which days lead to more errors?
    2016-07-17 2.3% errors

## Addition

### Create View

    Create views are embbed in the program. So once you run it it will create it automatically.
    But to make it clear:
    
    CREATE VIEW valid_articles
    AS SELECT REPLACE(log.path, '/article/', '') as path,
    count(*) as cnt FROM log, articles
    WHERE log.path = CONCAT('/article/', articles.slug)
    GROUP BY path ORDER BY cnt DESC;

    CREATE VIEW valid_authors
    AS SELECT author, sum(cnt) AS acnt
    FROM valid_articles, articles
    WHERE valid_articles.path = articles.slug
    GROUP BY author
    ORDER BY acnt DESC;

    CREATE VIEW all_status
    AS SELECT CAST(time AS DATE) AS day, count(*) AS cnt
    FROM log
    GROUP BY day;

    CREATE VIEW error_status
    AS SELECT CAST(time AS DATE) AS day, count(*) AS cnt
    FROM log
    WHERE CAST(SUBSTRING(status, 1, 3) AS INTEGER) != 200
    GROUP BY day;

