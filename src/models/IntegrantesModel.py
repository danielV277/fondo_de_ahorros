from database.db import get_connection
from .entities.Integrante import Integrante

class IntegrantesModel():
    @classmethod
    def get_integrantes(self):
        try:
            connection = get_connection()
            integrantes = []
            
            with connection.cursor() as cursor:
                cursor.execute("select * from integrantes order by nombres")
                resultset = cursor.fetchall()

                for row in resultset:
                    integrante=Integrante(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    integrantes.append(integrante.to_JSON())
            connection.close()
            return integrantes
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_integrante(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select * from integrantes where numero_id = %s",(id,))
                row = cursor.fetchone()
                integrante = None
                if row != None:
                    integrante=Integrante(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    integrante = integrante.to_JSON()
            
            connection.close()
            return integrante
        except Exception as ex:
            raise Exception(ex)    

    @classmethod
    def add_integrante(self,inte):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                
                cursor.execute("""INSERT INTO integrantes (numero_id, tipo_id, nombres, apellidos, telefono, correo, direccion, barrio, fecha_nacimiento) VALUES
                               (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(inte.nu_id,inte.t_id,inte.nom,inte.ape,inte.tel,inte.cor,inte.bar,inte.dir,inte.f_na))
            
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)  
    
    @classmethod
    def update_integrante(self,id,key,new_value):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                
                cursor.execute(f"UPDATE integrantes SET {key} = (%s) where numero_id = %s",(new_value,id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)  
    
    
    
    
    
    