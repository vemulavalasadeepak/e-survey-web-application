import mysql.connector
db_config={
    'host': 'deepak',
    'user':'manjith',
    'password':'123',
    'database': 'deepaku',
}
connection =mysql.connector.connect(**db_config)
cursor = connection.cursor()
cursor.close()
connection.close()