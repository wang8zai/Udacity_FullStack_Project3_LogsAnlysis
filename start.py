#! /usr/bin/env python2
import project3

# get class instance.
dq = project3.Database_query("news")

# querys here.
query1 = """SELECT title, cnt
    FROM valid_articles, articles
    WHERE valid_articles.path = articles.slug
    LIMIT 3"""
query2 = """SELECT authors.name, acnt
    FROM valid_authors, authors
    WHERE valid_authors.author = authors.id
    ORDER BY acnt DESC"""
query3 = """SELECT day, percentage FROM
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
    WHERE percentage > 0.01"""

# run query respectively. and show results.
dq.run_query(query1)
dq.print_result(1)

dq.run_query(query2)
dq.print_result(2)

dq.run_query(query3)
dq.print_result(3)
