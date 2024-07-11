Instrucciones de uso

        
    1. crear una base  de datos en posgresSQL local o en la nuve
    en el archivo "sql_data_base/base_de_datos_fondo.sql" se encuentra el script
    para la creacion de la base de datos

    2. espefica las variables de entorno (SECRET_KEY, PGSQL_HOST, PGSQL_USER etc.)en el archivo ".env"

    3. inicializa un entorno virtual preferiblemente si lo vas a lanzar de manera local

    4. importa los archivos que se especifican en "requirements.txt" (pip install -r requirements.txt)
    
    5. lanza el servidor que usa flask  python ./src/app.py si estas de manera local
    
    6. enlaces validos ejemplo si el servidor esta de manera local
        para Integrantes
        (http://localhost:5000/api/integrantes/listar) 
        (http://localhost:5000/api/integrantes/agregar)
        (http://localhost:5000/api/integrantes/actualizar)
        
        para Registros de ahorro
        (http://localhost:5000/api/registros/listar)
        (http://localhost:5000/api/registros/agregar)
        
        para Ahorro Generales
        (http://localhost:5000/api/ahorros/listar)

        
        modifica el puerto y el host 

    7. y ya puedes hacer uso de un gestor de integrantes y ahorros