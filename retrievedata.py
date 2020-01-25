import psycopg2

def retrieve_data():
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "data")

        cursor = connection.cursor()

        empty=[]

        read_data = "SELECT * FROM data;"
        data = cursor.execute(read_data,(club,))
        for row in data:
            return row
        return empty

    except (Exception, psycopg2.Error) as error :
        print ("Error while retrieving data", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
