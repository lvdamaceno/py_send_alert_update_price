import pymssql
import variables as v

conn = pymssql.connect(v.SERVER_NAME, v.USER, v.PSSWD, v.DATABASE)
cursor = conn.cursor(as_dict=True)

# cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# for row in cursor:
#    print("ID=%d, Name=%s" % (row['id'], row['name']))

cursor = conn.cursor()
cursor.execute('SELECT TOP 1 CODPROD FROM TGFPRO')
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()

conn.close()
