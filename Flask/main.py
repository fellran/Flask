from flask import Flask
from configuration import configure_all
from cryptografy import bcrypt


# inicializção do flask
app = Flask(__name__)

bcrypt.init_app(app)

# configurando a coneção com o banco
configure_all(app)


# exeecução
app.run(debug=True)


