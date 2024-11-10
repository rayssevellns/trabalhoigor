from flask import Blueprint, render_template, request, redirect, url_for, session, flash, json,make_response
from model import Filme, addFilme, getFilmes, autenticar, listFilmesAlugar


filme_controllers = Blueprint("filme", __name__)

@filme_controllers.before_request
def before_request():
    print(f"Método da Requisição: {request.method} | Caminho da Requisição: {request.path}")

@filme_controllers.after_request
def after_request(response):
    response.set_cookie('visited', 'true')
    return response

@filme_controllers.route("/")
def index():
    filmes = getFilmes()
    username = session.get('username')
    visited = request.cookies.get('visited')
    cookie = json.loads(request.cookies.get('carrinho', '[]'))
    return render_template('index.html', filmes=filmes, username=username, visited=visited)

@filme_controllers.route("/home")
def homePage():
    id = request.args.get('id', default=0, type=int)
    cookie = json.loads(request.cookies.get('carrinho', '[]'))

    if id != 0:
        if id in cookie:
            cookie.remove(id)
        else:
            cookie.append(id)

    # Renderizando com lista de filmes e carrinho
    resp = make_response(render_template("homepage.html", 
                                         listaFilmesAlugar=listFilmesAlugar, 
                                         carrinho=cookie))
    resp.set_cookie('carrinho', json.dumps(cookie), max_age=60*60*24)
    return resp

@filme_controllers.route("/add", methods=["POST"])
def add():
    descricao = request.form["descricao"]
    addFilme(descricao)
    return redirect(url_for('filme.index'))

@filme_controllers.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']
        
        autenticado = autenticar(user, senha)
        if autenticado:
            session['username'] = user
            flash(f'Bem-vindo, {autenticado}!', 'success')
            return redirect(url_for('filme.welcome'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')  
    return render_template('login.html')

@filme_controllers.route("/welcome")
def welcome():
    username = session.get('username')
    if username == "admin":
        message = "Bem-vindo, ADMIN!"
    else:
        message = "Bem-vindo, USER!"
    return render_template('welcome.html', username=username, message=message)

@filme_controllers.route("/logout")
def logout():
    session.pop('username', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('filme.login'))

@filme_controllers.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

@filme_controllers.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

@filme_controllers.errorhandler(401)
def unauthorized(e):
    return render_template("401.html"), 401

@filme_controllers.errorhandler(500)
def serverError(e):
    return render_template("500.html"), 500
