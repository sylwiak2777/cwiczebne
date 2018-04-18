import psycopg2
try:
    connect_str = "dbname='www' user='postgres' host='localhost' password='12345'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # run a SELECT statement - no data in there, but we can try it
    cursor.execute("""SELECT * from iso;""")
    for record in cursor:
        print(record[1])
except Exception as error:
    print("Error")
    print(error)
