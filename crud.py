# Importing MySQL Python connector
import mysql.connector

# Connecting the code to the database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='crud',
)

cursor = connection.cursor()

######## CREATE #########

#name = "Brazil"
#continent = "South America"
#population = 216280343

#command = f'INSERT INTO countries (name, continent, population) VALUES ("{name}", "{continent}", {population})'
#cursor.execute(command)
#connection.commit()

######## READ ########

#command = f'SELECT * FROM countries'
#cursor.execute(command)
#result = cursor.fetchall()
#print(result)

######## UPDATE POPULATION ########

#name = "Brazil"
#population = 216280343

#command = f'UPDATE countries SET population = {population} WHERE name = "{name}"'
#cursor.execute(command)
#connection.commit()

######## DELETE ########

#name = "Brazil"

#command = f'DELETE FROM countries WHERE name = "{name}"'
#cursor.execute(command)
#connection.commit()

# Closing the connection
cursor.close()
connection.close()
