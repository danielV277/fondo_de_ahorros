from database.db import get_connection
from .entities.Ahorro import Ahorro

class AhorrosModel():
    
    @classmethod
    def get_ahorros(self):
        try:
            connection = get_connection()
            ahorros = []
            
            with connection.cursor() as cursor:
                cursor.execute("""select ahorros.numero_id,nombres,apellidos,numero_de_aportes,ahorros_totales from 
                                ahorros join integrantes on integrantes.numero_id = ahorros.numero_id""")
                resultset = cursor.fetchall()

                for row in resultset:
                    ahorro=Ahorro(row[0],row[1],row[2],row[3],row[4])
                    ahorros.append(ahorro.to_JSON())
            connection.close()
            return ahorros
        except Exception as ex:
            return Exception(ex)
            # raise Exception(ex)
    