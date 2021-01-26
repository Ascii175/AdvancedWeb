import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                    password="BBSooe46676",
                                    host="node8557-advweb-05.app.ruk-com.cloud",
                                    port="11104",
                                    database="CloudDB")
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(),"\n")


    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to -", record,"\n")

except(Exception,psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")