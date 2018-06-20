#! /usr/bin/env python2
from __future__ import print_function
import psycopg2


class Database_query():
    """a class provide funtion to connect to a given database.
    Enable to perform query to the given query.

    Attributes:
        self.db_name(str): database name is here. will connect
        to this database.
        self.result(list): after perform query. the results
        are stored here. Will be print by print function.
    """

    def __init__(self, dbname):
        """Database_query constructor.

        Arguments:
            self(Databse_query): class instance.
            dbname(str): is self.db_name.
        No return values
        """
        self.db_name = dbname

    def connect(self):
        """connect database. Catch exception if not success.
        Arguments:
            self(Database_query): class instance.
        Return:
            No return.
        """
        try:
            db = psycopg2.connect("dbname={}".format(self.db_name))
            cursor = db.cursor()
            return db, cursor
        except psycopg2.DatabaseError, e:
            """if not sucess print a error message"""
            print("<error message>")

    def run_query(self, querystr):
        """use connect function to get db and cursor object.
        run query.
        Arguments:
            self(Database_query): class instance.
            querystr(srt): query string.
        Return:
            No return.
        """
        db, cursor = self.connect()

        """the most popular three aritcles of all time"""
        cursor.execute(querystr)

        """print the result"""
        self.result = cursor.fetchall()

        """close database"""
        db.close()

    def print_result(self, qtype):
        """a fucntion to print last query result
        Arguments:
            qtype(int): specify print type.
            cuz print format may differ.
        Return:
            No return but will see in console line.
        """
        if qtype == 1:
            print("Most popular three articles of all time")
            for p in self.result:
                print(p[0], '--', p[1], 'views', sep=' ')
        elif qtype == 2:
            print()
            print("Most popular article authors of all time? ")
            for p in self.result:
                print(p[0], '--', p[1], 'views', sep=' ')
        elif qtype == 3:
            print()
            print("On which days lead to more errors? ")
            for p in self.result:
                print(p[0], '{:.1%}'.format(p[1]), 'errors', sep=' ')
