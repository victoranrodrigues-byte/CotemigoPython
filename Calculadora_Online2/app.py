from calculador import calcular
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('calculadora1.html', etapas='', resultados='')

@app.route('/calculando', methods=['GET','POST'])
def index():
    return calcular()

if __name__ == '__main__':
    app.run(debug=True)