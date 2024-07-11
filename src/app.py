from flask import Flask
from config import config

#rutas 

from routes import Integrantes,Registros,Ahorros

app = Flask(__name__,template_folder='./plantillas')

def page_not_found(error):
    return '<h1>Pagina no encontrada</h1>',404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    #Blurprints
    app.register_blueprint(Integrantes.integrantes,url_prefix='/api/integrantes')
    app.register_blueprint(Registros.registros,url_prefix = '/api/registros' )
    app.register_blueprint(Ahorros.ahorros,url_prefix = '/api/ahorros')
    
    
    #Error handlers
    app.register_error_handler(404,page_not_found)
    app.run()