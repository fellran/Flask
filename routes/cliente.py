from flask import Blueprint, render_template, request
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

"""
    rotas de clientes

    - /clientes/ (GET) - listar os clientes
    - /clientes/ (POST) - inserir o cliente no servidor
    - /clientes/new (GET) - renderizar  o formularios para criar um clientes
    - /clientes/<id> (GET) - obter os dados de um cliente
    - /clientes/<id>/edit (GET) - renderizar um formulario para editar um cliente
    - /clientes/<id>/update (PUT) - atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - deletar o registro do cliente

"""

@cliente_route.route('/')
def lista_clientes():
    #listar os clientes
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    # inserir cliente 
    print(request.json)
    return {"ok": "ok"}

@cliente_route.route('/new')
def form_cliente(): 
    # formulario para cadastrar cliente
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id): 
    # exibir detalhes do cliente
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id): 
    # formulario para editar um cliente
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id): 
    # atualizar os dados de um cliente
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['PUT'])
def deletar_cliente(cliente_id): 
    # deletar informações do cliente
    pass