# create table ahorros(
# 	numero_id varchar(10),
# 	numero_de_aportes int,
# 	ahorros_totales numeric(15,2),
# 	foreign key(numero_id) references integrantes(numero_id)
# )

class Ahorro():
    
    def __init__(self,id_integrante,nombre_integrante, apellidos_integrante,numero_aportes,ahorros_totales):
        self.id_integrante = id_integrante
        self.nombre_integrante = nombre_integrante
        self.apellidos_integrante = apellidos_integrante
        self.numero_aportes = numero_aportes
        self.ahorros_totales = ahorros_totales

    def to_JSON(self):
        return {
            'id_integrante':self.id_integrante,
            'nombre_integrante':self.nombre_integrante,
            'apellidos_integrantes': self.apellidos_integrante,
            'numero_aportes': self.numero_aportes,
            'ahorros_totales': self.ahorros_totales
        } 
        