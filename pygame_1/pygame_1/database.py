import psycopg2
import psycopg2.extras
import sys

try:
    conn = psycopg2.connect("dbname='pygame' user='postgres' password='root'")
except:
    print ("no connection")

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cur.execute("""SELECT id, name, score FROM player""")
except:
    print("I can't select")

# fetch all of the rows from the query
data = cur.fetchall ()

# print the rows
for row in data:
    if row[0] == 1:
        player1_name = row[1]
        player1_score = row[2]
    '''elif row[0] == 2:
        player2_name = row[1]
        player2_score = row[2]'''

print(player1_name, player1_score)

# close the cursor object
cur.close ()

# close the connection
conn.close ()