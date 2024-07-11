from flask import Blueprint,jsonify,request,render_template,flash,url_for
from models.IntegrantesModel import IntegrantesModel
from models.entities.Integrante import Integrante
import datetime
integrantes = Blueprint('Integrantes_blueprint',__name__,template_folder='../plantillas')

@integrantes.route('listar')
def get_integrantes():
    try:
        integrantes = IntegrantesModel.get_integrantes() 
        return render_template('integrantes/listar.html', integrantes = integrantes)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500 
        

@integrantes.route('buscar/<id>')
def get_integrante(id):
    try:
        integrante = IntegrantesModel.get_integrante(id) 
        if integrante != None:
            return jsonify(integrante)
        else:
            return jsonify({}),404
        
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
    
@integrantes.route('agregar',methods=['GET','POST'])
def add_integrante():
    try:
        if request.method == 'POST':
            inte = request.form
            f_na = datetime.datetime.strptime(inte["fecha_nacimiento"], "%Y-%m-%d").date()
            
            integrante = Integrante(inte['identificacion'],inte['tipo_identificacion'],inte['nombres'],inte['apellidos'],inte['telefono'],inte['correo'],inte['barrio'],inte['direccion'],f_na,None)
            
            affected_rows = IntegrantesModel.add_integrante(integrante)

            if affected_rows == 1:
                #return jsonify({'numero_id':integrante.nu_id})
                flash("Agregado con exito!!!")
                return render_template('integrantes/agregar.html')
            else:
                flash("No se puedo agregar el integrantes")
                return render_template('integrantes/agregar.html')
            
        else:
            return render_template('integrantes/agregar.html')    
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@integrantes.route('actualizar',methods=['POST','GET'])
def update_integrante():
    try:
        if request.method == 'POST':
            numero_id = request.form['id']
            key = request.form['key']
            new_value = request.form['new_value']
            
            affected_rows = IntegrantesModel.update_integrante(numero_id,key,new_value)

            if affected_rows == 1:
                flash("Agregado con exito!!!")
                print("actualizado")
                return render_template('integrantes/actualizar.html')
            else:
                flash("No se puedo actualizar el registro!!!")
                print("no actualizado")
                return jsonify({'message':"Error on update"}),500
        else:
            print("no put enotnces: ",request.method)
            return render_template('integrantes/actualizar.html')   
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    