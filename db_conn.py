import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="vishal",         # your username
                     passwd="maggie",  # your password
                     db="ipl")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM test")

# print all the first cell of all t
# he rows
for row in cur.fetchall():
    print row[0]

db.close()