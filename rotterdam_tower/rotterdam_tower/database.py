import psycopg2
import psycopg2.extras
import sys

try:
    conn = psycopg2.connect("dbname='pygame' user='postgres' password='root'")
except:
    print ("no connection")

cc = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cc.execute("""SELECT id, name, score, highscore FROM player""")
except:
    print("I can't select")

# fetch all of the rows from the query
data = cc.fetchall ()