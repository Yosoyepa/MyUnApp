import Levenshtein
import mysql.connector

def obtener_nombres_grupo_especifico(nombre_grupo):
    resultados = []

    try:
        # Establecer conexión a la base de datos
        con = mysql.connector.connect(
            host="34.68.234.58",
            user="root",
            password='cm<\PbV#1PN"#k4T', #type: ignore
            database="myunbd"
        )
        cursor = con.cursor()

        # Obtener todos los nombres de grupo desde la base de datos
        query = "SELECT NOMBRE_GRUPO FROM GRUPO"
        cursor.execute(query)
        nombres_grupo = cursor.fetchall()

        # Calcular la similitud utilizando Levenshtein Distance y ordenar los resultados
        for nombre in nombres_grupo:
            similitud = Levenshtein.distance(str(nombre_grupo), str(nombre[0]))
            resultados.append((nombre[0], similitud))

        resultados.sort(key=lambda x: x[1])
        resultados = resultados[:3]
        print("Resultados: ", resultados)

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")

    finally:
        if cursor: #type: ignore
            cursor.close()
        if con and con.is_connected(): #type: ignore
            con.close()

    return resultados
    


if __name__ == "__main__":
    grupo_buscar = input("Ingrese el nombre del grupo a buscar: ")
    resultados = obtener_nombres_grupo_especifico(grupo_buscar)

    print("Resultados:")
    for resultado in resultados:
        print(f"Nombre: {resultado[0]}, Similitud: {resultado[1]}")