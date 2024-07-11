import datetime

class Integrante():
    def __init__(self,nu_id,t_id,nom,ape,tel,cor,bar,dir,f_na,f_reg):
        self.nu_id  = nu_id    
        self.t_id  = t_id    
        self.nom  = nom   
        self.ape  = ape    
        self.tel  = tel    
        self.cor  = cor    
        self.bar  = bar    
        self.dir  = dir   
        self.f_na  = datetime.datetime.strftime(f_na,'%Y-%m-%d')  
        self.f_reg  = datetime.datetime.strftime(f_reg,'%Y-%m-%d') if f_reg != None else ""
        
    def to_JSON(self):
        return {
                'identificacion':self.nu_id,    
                'tipo_identificacion':self.t_id,   
                'nombres':self.nom, 
                'apellidos':self.ape,  
                'telefono':self.tel,  
                'correo':self.cor,  
                'barrio':self.bar,  
                'direccion':self.dir, 
                'fecha_nacimiento':self.f_na,   
                'fecha_registro':self.f_reg
        } 
    
    
# create table integrantes(
# 	numero_id varchar(10) primary key,
# 	tipo_id char (2),
# 	nombres varchar(50),
# 	apellidos varchar(50),
# 	telefono char(10),
# 	correo varchar(50),
# 	direccion varchar(80),
#     barrio varchar(60),
# 	fecha_nacimiento date,
# 	fecha_registro date default CURRENT_TIMESTAMP
# )

# {
#     "nu_id": "1100000000",    
#     "t_id":  "CC",   
#     "nom" :  "Juan",
#     "ape" :  "Lorenz perez", 
#     "tel" :  "3227679999", 
#     "cor" :  "dan@ejemplo.com", 
#     "bar" :  "Lorenzo", 
#     "dir" :  "A 4 #5",
#     "f_na": "2000-02-01"
# }