from flask import Blueprint,jsonify,request,render_template,flash,url_for
from models.RegistroModel import RegistroModel
from models.entities.Registro import Registro
import datetime

registros = Blueprint('Registros_blueprint',__name__,template_folder='../plantillas')

@registros.route('listar')
def get_registros():
    try:
        registros = RegistroModel.get_registros() 
        return render_template('registros/listar.html', registros = registros)
    except Exception as ex:
        flash(jsonify({'message':str(ex)}))
        return render_template('registros/listar.html')
        #return jsonify({'message':str(ex)}),500 

@registros.route('agregar',methods=['GET','POST'])
def add_registro():
    try:
        if request.method == 'POST':
            regi = request.form
            
            registro = Registro(regi['id_integrante'],regi['valor'])
            
            affected_rows = RegistroModel.add_registro(registro)

            if affected_rows == 1:
                flash("Agregado con exito!!!")
                return render_template('registros/agregar.html')
                #jsonify(registro,"Num ",affected_rows)
            else:
                flash("No se puedo encontro el ID")
                return render_template('registros/agregar.html')
                #return jsonify(registro)
        else:
            return render_template('registros/agregar.html')    
    except Exception as ex:
        flash(Exception(ex))
        return render_template('integrantes/agregar.html')
        
        #return jsonify({'message':str(ex)}),500
