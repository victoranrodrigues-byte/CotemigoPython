from flask import Flask, request, render_template_string

apps = Flask(__name__)

@apps.route('/')
def formula_login():
    return render_template_string("""

        <img src="https://media.tenor.com/tfH0x4odLH0AAAAM/niko-oneshot.gif" style="width: 300px;">
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def logando():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')


    if usuario == 'Victor' and senha == '777':
        return f"<h1>Bem-vindo, {usuario}!</h1> <img src='hhttps://media.tenor.com/WbLQYcVDNrwAAAAM/yay-oneshot.gif'>"
    else:
        return "<h1>Login inválido</h1> <img src='https://art.pixilart.com/sr23d4a3e8b23aws3.gif'>"

@apps.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return logando()
    else:
        return formula_login()


if __name__ == "__main__":
    apps.run(debug=True)


# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping

