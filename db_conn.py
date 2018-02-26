import pymysql


the_database_connection = False

def get_conn():
    db = pymysql.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="maggie",  # your password
                         db="ipl_live")        # name of the data base
    return db

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