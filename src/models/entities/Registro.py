from datetime import datetime 
# insert into registro_aportes(id_registro,id_integrante,tipo,valor) 
# values ('100000000001','1000000001','AH',25000);

class Registro():
    
    def __init__(self,id_integrante,valor,id_registro = "",tipo = "AH",fecha = ""):
        self.id_registro = id_registro
        self.id_integrante = id_integrante
        self.tipo = tipo
        self.valor = valor
        self.fecha = datetime.strftime(fecha, '%Y-%m-%d') if fecha != "" else ""

    def to_JSON(self):
        return {
            'id_registro':self.id_registro,
            'id_integrante':self.id_integrante,
            'tipo': self.tipo,
            'valor': self.valor,
            'fecha_registro': self.fecha
        } 
        