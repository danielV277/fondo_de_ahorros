from database.db import get_connection
from .entities.Registro import Registro
from datetime import datetime

class RegistroModel():
    
    @classmethod
    def get_registros(self):
        try:
            connection = get_connection()
            registros = []
            
            with connection.cursor() as cursor:
                cursor.execute("select * from registro_aportes")
                resultset = cursor.fetchall()

                for row in resultset:
                    registro=Registro(row[1],row[3],row[0],row[2],row[4])
                    registros.append(registro.to_JSON())
            connection.close()
            return registros
        except Exception as ex:
            return Exception(ex)
            # raise Exception(ex)
    
    @classmethod
    def add_registro(self,regi):
        try:
            connection = get_connection()
            now = datetime.now()
            id_registro = now.strftime('%Y%m%d%H%M')
            with connection.cursor() as cursor:
                
                cursor.execute("""INSERT INTO registro_aportes(id_registro, id_integrante, tipo, valor) VALUES
                               (%s,%s,%s,%s)""",(id_registro,regi.id_integrante,regi.tipo,regi.valor))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            return Exception(ex)
            # raise Exception(ex)  