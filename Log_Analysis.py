#!/usr/bin/env python3

import psycopg2
database_name = "news"


def three_popular_articles(query_1):
    """What are the most popular three articles of all time?"""
query_1 = """
    WITH  rpt as (select articles.title from articles
    inner join log on log.path like concat('%', articles.slug, '%')
    where log.status like '%200%' )
    select title,count(*) total  from rpt group by
    title order by total desc limit 3;
"""

db = psycopg2.connect('dbname=' + database_name)
c = db.cursor()
c.execute(query_1)
results = c.fetchall()
""" Print the Results"""
print('\n The Results are:')
print("\n1. What are the most popular three articles of all time?")
print(' TOP THREE ARTICLES BY PAGE VIEWS :')
count = 1
for i in results:
    number = '(' + str(count) + ') "'
    title = i[0]
    views = '" ==>' + str(i[1]) + " views"
    print(number + title + views)
    count += 1
    db.close()


def most_popular_authors(query_2):
    """ Who are the most popular article authors of all time?"""
query_2 = """
        WITH rpt as (select name from authors a inner join
        articles b on (a.id=b.author) inner join log c on
        (c.path like concat('%', b.slug, '%') and a.id=b.author)
        where c.status like '%200%')
        select name, count(*)
        total from
        rpt group by
        name order by total desc limit 3;
    """

"""Connect to the Database and Executing the query"""
db = psycopg2.connect('dbname=' + database_name)
c = db.cursor()
c.execute(query_2)
results = c.fetchall()
""" Print the Results"""
print("\n 2. Who are the most popular article authors of all time?")
print("TOP THREE AUTHORS BY VIEWS :")
count = 1
for i in results:
    number = '(' + str(count) + ') "'
    title = str(i[0])
    views = '" ==>' + str(i[1]) + " views"
    print(number + title + views)
    count += 1
    db.close()


def get_error_percentage(query_3):
    """ On which days did more than 1% of requests lead to errors"""
query_3 = """
        WITH rpt as (SELECT total.day as date,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS Percent
        FROM (
          SELECT time::date "day", count(*) AS Error_Requests
          FROM log
          WHERE status LIKE '%NOT%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT time::date "day", count(*) AS Requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.Error_Requests*1.0)
        / total.Requests), 3) > 0.01))
        select date::date,percent from rpt
        ORDER BY Percent DESC;
    """
"""Connect to the Database and Executing the query"""
db = psycopg2.connect('dbname=' + database_name)
c = db.cursor()
c.execute(query_3)
results = c.fetchall()
""" Print the Results"""
print("\n 3. On which days did more than 1% of requests lead to errors")
print(' DAYS WITH MORE THAN 1% ERRORS:')
count = 1
for i in results:
    date = i[0].strftime('%B, %d, %Y')
    per = str(round(i[1]*100, 1))
    print(date + " ==> " + per + "%" + " errors")
    count += 1
    db.close()

if __name__ == '__main__':
    three_popular_articles = three_popular_articles(query_1)
    most_popular_authors = most_popular_authors(query_2)
    get_error_percentage = get_error_percentage(query_3)
