from flask import Blueprint,jsonify,request,render_template,flash,url_for
from models.AhorrosModel import AhorrosModel
from models.entities.Ahorro import Ahorro

ahorros = Blueprint('Ahorros_blueprint',__name__,template_folder='../plantillas')

@ahorros.route('listar')
def get_ahorros():
    try:
        ahorros = AhorrosModel.get_ahorros() 
        return render_template('ahorros/listar.html', ahorros = ahorros)
    except Exception as ex:
        flash(jsonify({'message':str(ex)}))
        return render_template('ahorros/listar.html')
        #return jsonify({'message':str(ex)}),500 
