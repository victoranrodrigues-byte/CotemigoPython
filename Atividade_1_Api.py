from flask import Flask

decora = Flask(__name__)

@decora.route('/')
def explicando_decorator():
    return 'O que é um decorator em Python? \n É uma função que modifica qou estende o comportamento de outra função, método ou classe sem alterar seu código-fonte original.'

@decora.route('/funcao')
def funcao_decorator():
    return 'Para que serve um decorator? \n Serve para modificar e estender o comportamento de funções, métodos ou classes sem alterar seu código original.'

@decora.route('/exemplo')
def exemplo_decorator():
    return 'Um exemplo de decorator: * \n from flask import Flask \n app = Flask(__name__) \n @app.route *'

if __name__ == '__main__':
    decora.run(debug=True)