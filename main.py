from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# inicializção do flask
app = Flask(__name__)


app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

# exeecução
app.run(debug=True)

