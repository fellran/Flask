from flask import Flask
from configuration import configure_all


# inicializção do flask
app = Flask(__name__)

# configurando a coneção com o banco
configure_all(app)


# exeecução
app.run(debug=True)


