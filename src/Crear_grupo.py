import mysql.connector

def create_user_group(group_name):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Grupos (id INT AUTO_INCREMENT PRIMARY KEY, group_name VARCHAR(255))")

    sql = "INSERT INTO Grupos (group_name) VALUES (%s)"
    val = (group_name,)
    cursor.execute(sql, val)

    conn.commit()

    cursor.close()
    conn.close()



