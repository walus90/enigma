import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return conn
  
def insert_photo(conn, photo):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = ''' INSERT INTO photos(name, photo) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, photo)
    return cur.lastrowid
        
