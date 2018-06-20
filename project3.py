from __future__ import print_function
import psycopg2

# create views. easy to debug.
# valid_articles specify the view select the valid article
# which name is valid and
valid_articles = """CREATE VIEW valid_articles
    AS SELECT REPLACE(path, '/article/', '') as path,
    count(*) as cnt FROM log, articles
    WHERE path LIKE '/article/%'
    AND REPLACE(path, '/article/', '') = articles.slug
    GROUP BY path ORDER BY cnt DESC"""

# create view select valid author
valid_authors = """CREATE VIEW valid_authors
    AS SELECT author, sum(cnt) AS acnt
    FROM valid_articles, articles
    WHERE valid_articles.path = articles.slug
    GROUP BY author
    ORDER BY acnt DESC"""

# create view group by data but not datetime
all_status = """CREATE VIEW all_status
    AS SELECT CAST(time AS DATE) AS day, count(*) AS cnt
    FROM log
    GROUP BY day"""

error_status = """CREATE VIEW error_status
    AS SELECT CAST(time AS DATE) AS day, count(*) AS cnt
    FROM log
    WHERE CAST(SUBSTRING(status, 1, 3) AS INTEGER) != 200
    GROUP BY day"""


# connect to the news database return the db object
db = psycopg2.connect("dbname=news")
# create a cursor object from database object
cursor = db.cursor()

# init view
cursor.execute(valid_articles)
cursor.execute(valid_authors)
cursor.execute(all_status)
cursor.execute(error_status)

# the most popular three aritcles of all time
cursor.execute(
    """SELECT title, cnt
    FROM valid_articles, articles
    WHERE valid_articles.path = articles.slug LIMIT 3""")

# print the result
paths = cursor.fetchall()
print("Most popular three articles of all time")
for p in paths:
    print(p[0], '--', p[1], 'views', sep=' ')

# the most popular authors
cursor.execute(
    """SELECT authors.name, acnt
    FROM valid_authors, authors
    WHERE valid_authors.author = authors.id
    ORDER BY acnt DESC""")

paths = cursor.fetchall()
print()
print("Most popular article authors of all time? ")
for p in paths:
    print(p[0], '--', p[1], 'views', sep=' ')

# caculate errors with all_status view and
# error_view with subquery
cursor.execute("""SELECT day, percentage FROM
    (SELECT alls.day as day,
    CAST(
    CAST(errors.cnt AS DECIMAL(10,4))
    /CAST(alls.cnt AS DECIMAL(10,4))
    AS DECIMAL(10,4))
    AS percentage
    FROM all_status AS alls,
    error_status AS errors
    WHERE alls.day = errors.day)
    AS ptable
    WHERE percentage > 0.01""")

paths = cursor.fetchall()
print()
print("On which days lead to more errors? ")
for p in paths:
    print(p[0], '{:.1%}'.format(p[1]), 'errors', sep=' ')
