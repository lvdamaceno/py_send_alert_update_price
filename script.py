import pymssql
import variables as v


def connect():
    conn = pymssql.connect(v.SERVER_NAME, v.USER, v.PSSWD, v.DATABASE)
    return conn


def execute_query(query):
    conn = connect()
    conn.cursor(as_dict=True)
    cursor = conn.cursor()
    cursor.execute(query)
    for row in cursor:
        print("Produto atualizado: %s" % row[0])
    # conn.close()


execute_query(v.QUERY)
