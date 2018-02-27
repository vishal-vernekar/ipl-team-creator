import pymysql


_connection = None

def get_conn():
    global _connection
    if not _connection:
        _connection = pymysql.connect(
            host="localhost",   # your host, usually localhost
            user="root",        # your username
            passwd="maggie",    # your password
            db="ipl_final"       # name of the data base
        )
    return _connection

# cur = db.cursor()
#
# # Use all the SQL you like
# cur.execute("SELECT * FROM test_table")
#
# # print all the first cell of all t
# # he rows
# for row in cur.fetchall():
#     print(row)
#
# db.close()