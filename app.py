import sqlite3
from tabulate import tabulate
import sys
from time import sleep


def sair():
    print('Encerrando o sistema. \nAguarde...\nGravando Dados no Bando de Dados...')
    contagem()
    print('Sistema Encerrado')
    sys.exit()


def contagem():
    for cont in range(3, -1, -1):
        print(cont, '... ', end='')
        sleep(1)


def criar_conta_corrente():
    print('')
    print('++++++++++ CRIAR CONTA-CORRENTE ++++++++++')
    print('')
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    sql = c.execute('''SELECT * FROM cliente''')
    consulta = sql.fetchall()
    head = [col[0] for col in sql.description]
    print(tabulate(consulta, headers=head, tablefmt="grid"))
    input('INFORME O ID DO CLIENTE: ')
    # INSERT NA TABELA DE CONTA COM O ID DO CLIENTE


def novo_cliente():
    print('')
    print('+++++ Cadastro de Clientes +++++')
    print('')
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    nome = input('NOME DO CLIENTE: ')
    cidade = input('CIDADE: ')
    telefone = input('TELEFONE: ')
    c.execute('''INSERT INTO cliente (nome, cidade, telefone)
                VALUES(?, ?, ?)''', (nome, cidade, telefone))
    conn.commit()
    print('{} Cadastrado com Sucesso'.format(nome))
    conn.close()
    return print('{} Cadastrado com Sucesso'.format(nome))


def consulta_todos_clientes():
    print('')
    print('+++++ Consulta TODOS Clientes +++++')
    print('')
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    sql = c.execute('''SELECT * FROM cliente''')
    consulta = sql.fetchall()
    if consulta:
        head = [col[0] for col in sql.description]
        print(tabulate(consulta, headers=head, tablefmt="grid"))
        print('Quantidade de Clientes: {}'.format(len(consulta)))
        print('')
        conn.close()
        input("Prescione ENTER para sair.")
    else:
        print('Nenhum cliente encontrado')
        conn.close()


def consulta_cliente_id():
    print('')
    print('+++++ Consulta Cliente por ID +++++')
    print('')
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    id = int(input('Informe o numero do ID_Cliente: '))
    print('')
    sql = c.execute('''SELECT id, nome, cidade, telefone FROM cliente WHERE id=?''', (id,))
    consulta = sql.fetchall()
    if consulta:
        head = [col[0] for col in sql.description]
        print(tabulate(consulta, headers=head, tablefmt="grid"))
        input("Prescione ENTER para sair.")
    else:
        print(f'ID numero {id} não localizado.')
        print('')
        consulta_cliente_id()
        print('')

    conn.close()


def consulta_cliente_nome():
    print('')
    print('+++++ Consulta Cliente NOME +++++')
    print('')
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    nome = input('Informe o nome do cliente: ')
    sql = c.execute("SELECT * FROM cliente WHERE nome LIKE '%'||?||'%'", (nome,))
    print('')
    consulta = sql.fetchall()
    if consulta:
        head = [col[0] for col in sql.description]
        print(tabulate(consulta, headers=head, tablefmt="grid"))
        input("Prescione ENTER para sair.")
    else:
        print(f'Cliente {nome} não localizado(a).')
        print('')
        consulta_cliente_nome()
        print('')

    conn.close()


def consulta_cliente_cidade():
    print('')
    print('+++++ Consulta Cliente por Cidade +++++')
    print('')
    conn = sqlite3.connect('contacorente.db')
    c = conn.cursor()
    cidade = input('Informe a Cidade do Cliente: ')
    sql = c.execute("SELECT * FROM cliente WHERE cidade LIKE '%'||?||'%'", (cidade,))
    consulta = sql.fetchall()
    if cidade:
        head = [col[0] for col in sql.description]
        print(tabulate(consulta, headers=head, tablefmt="grid"))
        conn.close()
        input("Prescione ENTER para sair.")
    else:
        print(f' Cidade {cidade} não foi localizado.')
        print('')
        conn.close()


def transDeposito():
    print('')
    print('+++++ DEPÓSITO +++++')
    print('')
    input('Sua Identificação: Informe o seu ID: ')
    input('Selecione o cliente para realizar o depósito: ')
    print('')
    print('CAIXA EM MANUTENÇÃO')


def transSaque():
    pass


def transFerencia():
    pass


def pagamentos():
    pass


def extrato():
    pass


menu_cadastro = {
    '1': ('- Cadastro de Cliente', novo_cliente),
    '2': ('- Consulta por ID', consulta_cliente_id),
    '3': ('- Consulta por Cidade', consulta_cliente_cidade),
    '4': ('- Consulta Todos Clientes', consulta_todos_clientes),
    '9': ('- Deslogar', sair),
}
menu_trans = {
    '1': ('- Depósito', transDeposito),
    '2': ('- Saque', transSaque),
    '3': ('- Transferência', transFerencia),
    '4': ('- Pagamentos', pagamentos),
    '5': ('- Extrato', extrato),
    '9': ('- Voltar', menu_cadastro),
}
menu_principal = {
    '1': ('- Cadastros', menu_cadastro),
    '2': ('- Transações - Em desenvolvimento', menu_trans),
    '9': ('- Deslogar - Em desenvolvimento', sair),
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
    criar_conta_corrente()
    # monta_menu(menu_principal)
