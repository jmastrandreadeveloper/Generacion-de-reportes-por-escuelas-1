import pyodbc

import platform
print(platform.architecture())

import mysql.connector
from mysql.connector import Error

# def conectarseAlaBD():
#     try:
#         conn = mysql.connector.connect(
#             host="gemdbrep1.mendoza.gob.ar",
#             database="gem",
#             user="jmastrandrea",
#             password="C*1cuZRvsr"
#         )

#         if conn.is_connected():
#             print("Conexión exitosa a la base de datos")
#             return conn
#         else:
#             print("No se pudo conectar a la base de datos")
#             return None

#     except Error as e:
#         print("Error de conexión:", e)
#         return None

def conectarseAlaBD():   

    # db_connection_str = (
    #     "DRIVER={MySQL ODBC 8.0 Unicode Driver};"
    #     "SERVER=gemproxysqlprd.mendoza.gov.ar;"
    #     "DATABASE=gem;"
    #     "UID=jmastrandrea;"
    #     "PWD=u*MC=9U)e91%;"
    # )#C*1cuZRvsr
    # try:
    #     db_connection = pyodbc.connect(db_connection_str)
    #     print("Conexión exitosa")
    # except Exception as e:
    #     print("Error de conexión:", e)
    #     #db_connection = pyodbc.connect(db_connection_str) # "Driver={SQL Server};Server=TU_SERVIDOR;Database=TU_BD;UID=USUARIO;PWD=CONTRASEÑA;"
    
    
    # return db_connection
    
    
    from sqlalchemy import create_engine

    # host="gemproxysqlprd.mendoza.gov.ar",
    # user="jmastrandrea",
    # password="u*MC=9U)e91%",
    # database="gem"
    
    db_connection_str = 'mysql+pymysql://jmastrandrea:u*MC=9U)e91%@gemproxysqlprd.mendoza.gov.ar:6033/gem'
    db_connection = create_engine(db_connection_str)
    return db_connection
    
    # driver = 'MySQL ODBC 8.0 Unicode Driver'
    # server = 'gemdbrep1.mendoza.gob.ar'
    # database = 'gem'
    # uid = 'jmastrandrea'
    # pwd = 'C*1cuZRvsr'
    # db_connection_str = f"{driver}://{uid}:{pwd}@{server}/{database}"

    # # drivers = ['mysql+pymysql', 'mysql+mysqlconnector', 'mysql+mysqldb', 'mysql+cymysql']
    # # server = 'gemdbrep1.mendoza.gob.ar'
    # # database = 'gem'
    # # uid = 'jmastrandrea'
    # # pwd = 'C*1cuZRvsr'

    # # for driver in drivers:
    # #     try:
    # #         print(f"Probando driver: {driver}")
    # #         connection_string = f"{driver}://{uid}:{pwd}@{server}/{database}"
    # #         engine = create_engine(connection_string)
    # #         # Intenta conectar para verificar si funciona
    # #         with engine.connect() as conn:
    # #             print(f"¡Conexión exitosa con {driver}!")
    # #         break
    # #     except Exception as e:
    # #         print(f"Error con {driver}: {e}")
    