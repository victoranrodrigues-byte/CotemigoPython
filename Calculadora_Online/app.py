import requests
from calculadorax import calculando
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('calculadora.html', etapas='', resultados='')

@app.route('/calcular', methods=['POST'])
def calc():
    return calculando()

if __name__ == '__main__':
    app.run(debug=True)