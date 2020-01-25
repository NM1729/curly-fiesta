import psycopg2

def get_Data():
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "events")

        cursor = connection.cursor()

        read_data = "SELECT password,priority FROM login_credentials WHERE username = %s AND club =%c;"
        pwd = cursor.execute(read_data,(username,))
        for row in pwd:
            log_pwd = row.password
            if log_pwd == password:
                return True,row.priority

        return False,-1

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
