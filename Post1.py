import psycopg2
try:
    #Tworzyny string (text) zawierająca paramatry bazy danych
    connectionString = "dbname='dvd' user='postgres' host='localhost' password='12345'"
    #Połaczenie z bazą
    connection = psycopg2.connect(connectionString)
    #Tworzymy wskaźnik
    cursor = connection.cursor()
    # Działanie na wskaźniku
    cursor.execute("""SELECT * FROM film;""")
    #wylistowanie rekordów z bazy
    for record in cursor:
        print(record[1])
    



    
except Exception as error:
    print('Błąd:')
    print(error)
    
