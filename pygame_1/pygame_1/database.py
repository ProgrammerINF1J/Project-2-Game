import psycopg2
import psycopg2.extras
import sys

try:
    conn = psycopg2.connect("dbname='pygame' user='postgres' password='root'")
except:
    print ("no connection")

cc = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cc.execute("""SELECT id, name, score FROM player""")
except:
    print("I can't select")

# fetch all of the rows from the query
data = cc.fetchall ()

# get rows
for row in data:
    if row[0] == 1:
        player1_name = row[1]
        player1_score = row[2]
    '''elif row[0] == 2:
        player2_name = row[1]
        player2_score = row[2]'''

# updatescore
def update_score(name, score):
    print(name, score)
    try:
        cc.execute("""UPDATE player SET score=%s WHERE name=%s""", (score, name))
    except Exception as error:
        print(error)
    conn.commit()

#reset score
def reset():
    try:
        cc.execute("""UPDATE player SET score=%s WHERE name=%s""", (0, 'player1'))
    except Exception as error:
        print(error)
    conn.commit()
#reset()