from flask import Blueprint, render_template, request 
from database.models.cliente import Cliente
from cryptografy import bcrypt

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
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    # inserir cliente 

    data = request.json

    senha_sem_hash = data['senha']

    senha_hash = bcrypt.generate_password_hash(senha_sem_hash).decode('utf-8')

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
        senha = senha_hash,
    )

    return render_template('item_cliente.html', cliente=novo_usuario )

@cliente_route.route('/new')
def form_cliente(): 
    # formulario para cadastrar cliente
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id): 
    # exibir detalhes do cliente

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('detalhe_cliente.html', cliente=cliente) 

    # formulario para editar um cliente

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_cliente.html', cliente=cliente)


    # atualizar os dados de um cliente

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id): 

    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.senha = data['senha'],
    cliente_editado.save()

    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id): 
    # deletar informações do cliente

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()

    return {"delete": "ok"}