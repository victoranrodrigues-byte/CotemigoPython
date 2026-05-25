import requests
from flask import Flask, render_template

def calculando():
    num1 = float(requests.form['num1'])
    num2 = float(requests.form['num2'])
    operacao = requests.form['operacao']
    
    if operacao == '+':
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
        return etapas
    elif operacao == '-':
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
        
    elif operacao == '*':
        resultado = num1 * num2
        etapas = f"{num1} * {num2} = {resultado}"
    
    elif operacao == '/':
        if num1 or num2 != 0:
            resultado = num1 / num2
            etapas = f"{num1} / {num2} = {resultado}"
            
        else:
            resultado = "Ocorreu um erro"
            etapas = f"{resultado}, você tentou dividir algum número por 0"
            
    return render_template('calculadora.html', etapas=etapas, resultados=resultado)