import sqlite3

# from time import sleep
from tabulate import tabulate

# from collections import Counter
# import sys

conn = sqlite3.connect('contacorente.db')


def database():
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    c.execute('''create table if not exists cliente  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                      nome TEXT, 
                                                      cidade TEXT, 
                                                      telefone TEXT)''')
    c.execute('''create table if not exists conta    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                      cod_cliente INTEGER,                                                      
                                                      saida REAL,
                                                      entrada REAL,
                                                      saldo REAL,
                                                      tr INTEGER,
                                                      comprovante INTEGER,
                                                      FOREIGN KEY (cod_cliente) REFERENCES cliente (id)
                                                      )''')
    c.execute('''create table if not exists transacao (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                      id_conta INTEGER,                                                      
                                                      deposito REAL,
                                                      saque REAL,
                                                      saldo REAL,
                                                      FOREIGN KEY (id_conta) REFERENCES conta (id)
                                                      )''')
    conn.commit()
    conn.close()


def novo_cliente():
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    print('------- 1 - CADASTRO CLIENTE / C.C ---------------\n')
    nome = input('NOME DO CLIENTE: ')
    cidade = input('CIDADE: ')
    telefone = input('TELEFONE: ')

    c.execute('''INSERT INTO cliente (nome, cidade, telefone)
                VALUES(?, ?, ?)''', (nome, cidade, telefone))
    conn.commit()
    print('{} Cadastrado com Sucesso'.format(nome))
    conn.close()


def clientes():
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    sql = '''SELECT * FROM cliente'''
    c.execute(sql)
    for l in c.fetchall():
        print(l)
    print('')
    print('Quantidade de Clientes: {}'.format(len(c.execute(sql).fetchall())))
    conn.close()
    monta_menu(menu_cadastro)


def consulta_cliente_id():
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    sql = "SELECT * FROM cliente WHERE id=?"
    id = input('Qual o numero do ID_Cliente?: ')
    print('')
    c.execute(sql, [(id)])
    print(c.fetchall())
    monta_menu(menu_cadastro)


def consulta_cliente_nome():
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    sql = "SELECT * FROM cliente WHERE nome LIKE '%'||?||'%'"
    nome = input('Qual o nome do cliente?: ')
    c.execute(sql, ([nome]))
    print(c.fetchall())
    monta_menu(menu_cadastro)


def consulta_cliente_cidade():
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    sql = "SELECT * FROM cliente WHERE cidade LIKE '%'||?||'%'"
    cidade = input('Qual a Cidade do Cliente: ')
    c.execute(sql, ([cidade]))
    print(c.fetchall())
    monta_menu(menu_cadastro)


def consulta_cliente():
    print('Contalta de Clientes, escolha as opções abaixo: ')
    selecao = '''
    1 - ID
    2 - Nome
    3 - Cidade
    4 - Todos
    '''
    print(selecao)
    menu = input('Digite uma das Opções: ')

    if menu == '1':
        print('')
        print('+++++ Consulta por ID_Cliente +++++')
        consulta_cliente_id()


    if menu == '2':
        print('')
        print('+++++ Consulta por NOME_Cliente +++++')
        consulta_cliente_nome()

    if menu == '3':
        print('')
        print('+++++ Consulta por CIDADE_Cliente +++++')
        consulta_cliente_nome()

    if menu == '4':
        print('')
        print('+++++ Consulta TODOS_Clientes +++++')
        clientes()


menu_cadastro = {
    '1': ('- Cadastro', novo_cliente),
    #'2': ('- Lista', clientes),
    #'3': ('- Consulta por ID', consulta_cliente_id),
    '2': ('- Consulta Geral', consulta_cliente),
    #'9': ('- Deslogar', sair),
}
# menu_trans = {
#    '1': ('- Depósito', transDeposito),
#    '2': ('- Saque', transSaque),
#    '3': ('- Transferência', transFerencia),
#    '4': ('- Pagamentos', pagamentos),
#    '5': ('- Extrato', extrato),
#    '9': ('- Voltar', menu_cadastro),
# }
menu_principal = {
    '1': ('- Clientes', menu_cadastro),
    #    '2': ('- Transações', menu_trans),
    #    '9': ('- Deslogar', sair),
}


def monta_menu(menu) -> object:
    print()
    print('******* Sistema VBANK *******:')
    print('')
    for k, v in menu.items():
        texto, _ = v
        print(k, texto)
    print('')
    opcao = input('Digite a Opçao Desejada:    ')
    print('')
    try:
        escolhido = menu[opcao]
        _, funcao = escolhido
        if isinstance(funcao, dict):
            monta_menu(funcao)
        else:
            funcao()
    except KeyError:
        print()
        monta_menu(menu_principal)


if __name__ == '__main__':
    monta_menu(menu_principal)
