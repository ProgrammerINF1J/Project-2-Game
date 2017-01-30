import psycopg2, psycopg2.extras, sys

try:
    conn = psycopg2.connect("dbname='pygame' user='postgres' password='root'")
except:
    print ("no connection")

ccp = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccp.execute("""SELECT p_id, p_name, p_score FROM player""")
except:
    print("I can't select players")

cch = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cch.execute("""SELECT h_id, h_name, h_score FROM highscore""")
except:
    print("I can't select highscore")

# check name
def check_name(name):
    try:
        ccp.execute("SELECT count(p_id) FROM player WHERE p_name = '"+name+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()    for row in result:
        return row[0]

# insert player
def insert_player(name, score):
    try:
        ccp.execute("""insert into player(p_name, p_score) values (%s, %s)""", (name, score))
    except Exception as error:
        return(error)
    conn.commit()

# select player id
def select_player_id(name):
    try:
        ccp.execute("SELECT p_id FROM player WHERE p_name = '"+name+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()    for row in result:
        return row[0]

# insert highscore
def insert_highscore(name, score, id):
    try:
        ccp.execute("insert into highscre(h_name, h_score) values ('"+name+"', '"+score+"') where id = '"+id+"'")
    except Exception as error:
        return(error)
    conn.commit()

# select highscore
def select_highscore(name):
    try:
        cch.execute("SELECT h_score FROM highscore where h_name = '"+name+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = cch.fetchall()    for row in result:
        return row[0]

# update score
def update_score(name, score):
    try:
        ccp.execute("""UPDATE player SET p_score=%s WHERE p_name=%s""", (score, name))
    except Exception as error:
        return(error)
    conn.commit()

#reset score
def reset():
    try:
        cc.execute("""UPDATE player SET score=%s WHERE name=%s""", (0, 'player1'))
    except Exception as error:
        return(error)
    conn.commit()
#reset()