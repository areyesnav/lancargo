from datetime import date, datetime, timedelta
import mysql.connector

comm_id = raw_input("\nCod Commodity : ")
comm_nom = raw_input("Nom Commodity : ")
comm_price = raw_input("Precio : ")
comm_fecha = raw_input("Fecha : ")
comm_fuente = raw_input("Fuente : ")
comm_detalle = raw_input("Observaciones : ")

add_price_values = (comm_id, comm_nom, float(comm_price), comm_fecha, comm_fuente, comm_detalle)

cnx = mysql.connector.connect(user='arn', password='valeria?4', database='inter')
cursor = cnx.cursor()

add_price = ("INSERT INTO prices "
			"(comm_id, comm_nom, comm_price, comm_fecha, comm_fuente, comm_detalle) "
			"VALUES (%s, %s, %s, %s, %s, %s) ")


cursor.execute(add_price, add_price_values)

cnx.commit()

cursor.close()

cnx.close()
