import pymysql.cursors

# Open database connection
db = pymysql.connect('localhost', 'root', 'secret', 'testdb')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method
cursor.execute("SELECT VERSION()")

#Fetch a single row using fetchone() method
data = cursor.fetchone()

print ("Database version : %s " % data)

#Disconnect from server
db.close()