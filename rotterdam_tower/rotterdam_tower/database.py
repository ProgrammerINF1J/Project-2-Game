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
def insert_highscore(id, name, score):
    try:
        ccp.execute("insert into highscore (h_id, h_name, h_score) values(%s, %s, %s)""", (id, name, score))
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

# select highscore for highscore screen
def select_screen_highscore():
    try:
        cch.execute("select h_id, h_name, h_score from highscore order by h_score desc limit 5")
    except Exception as error:
        return(error)
    conn.commit()
    result = cch.fetchall()
    return result

# update player_score
def update_score(score, id):
    try:
        ccp.execute("""UPDATE player SET p_score=%s WHERE p_id=%s""", (score, id))
    except Exception as error:
        return(error)
    conn.commit()

# update high_score
def update_highscore(score, id):
    try:
        cch.execute("""UPDATE highscore SET h_score=%s WHERE h_id=%s""", (score, id))
    except Exception as error:
        return(error)
    conn.commit()

# reset score
def reset_db():
    try:
        cc.execute("""drop table if exists player, highscore; 
            create table if not exists player ( 
	            p_id SERIAL primary key, 
                p_name varchar(14), 
	            p_score int
            ); 
            create table if not exists highscore ( 
	            h_id SERIAL primary key, 
                h_name varchar(14), 
                h_score int 
            ); 
            insert into player (p_name, p_score) values ('a', 0), ('b', 0), ('c', 0), ('d', 0); 
            insert into highscore (h_name, h_score) values ('a', 0), ('b', 0), ('c', 0), ('d', 0); """)
    except Exception as error:
        return(error)
    conn.commit()