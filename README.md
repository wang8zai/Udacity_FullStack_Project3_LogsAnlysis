# Udacity FullStack Project3 LogsAnlysis

## Dependency 
    ### python 3.6.5
        python pakage psycopg2
    ### Virtual Machine
        vagrant install here https://www.vagrantup.com/ Follow instructions there.

## Installtion
    ### Load the data
        Unzip newsdata.zip to newsdata.sql. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
    ### make it work
        run project3.py

## Description
    The user-facing newspaper site frontend itself, and the database behind it, are already built and running. Build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity. The program in this project run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.
        
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
