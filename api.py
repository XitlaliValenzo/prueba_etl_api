from flask import Flask, jsonify, render_template, request
import numeros

app = Flask(__name__)

@app.route('/extraer/', methods = ['POST'])
def extraer():
    try:
        n = numeros.Numeros()
        n.extract(int(request.form['numero']))
        num_extraido = n.calcular_numero_extraido()
        mensaje = f'¡Número extraído exitosamente!\nEl número que se extrajo fue el {num_extraido}'
        codigo = 200
    except ValueError as e:
         mensaje = str(e)
         codigo = 400
    return render_template('index.html', mensaje=mensaje), codigo

@app.route('/', methods = ['GET'])
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)