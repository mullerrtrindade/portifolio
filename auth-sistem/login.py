import os
import csv

ARQUIVO = "usuarios.csv"
def criar_arquivo_se_nao_existir():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(['usuario', 'senha'])
def cadastrar_usuario(usuario, senha):
    with open(ARQUIVO, 'a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow([usuario, senha])
def autenticar(usuario, senha):
    with open(ARQUIVO, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)  # Pular o cabeçalho
        for linha in leitor_csv:
            if linha[0] == usuario and linha[1] == senha:
                return True
    return False
def main():
    criar_arquivo_se_nao_existir()
    print("Deseja criar um novo usuário? (s/n)")
    resposta = input().lower()
    if resposta == 's':
        print("Digite um nome de usuário:")
        usuario = input()
        print("Digite uma senha:")
        senha = input()
        cadastrar_usuario(usuario, senha)
        print("Usuário criado com sucesso!")
    else:
        print("Digite seu nome de usuário:")
        usuario = input()
        print("Digite sua senha:")
        senha = input()
        if autenticar(usuario, senha):
            print("Login bem-sucedido!")
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")

def autenticar(usuario, senha):
    criar_arquivo_se_nao_existir()

    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            if linha["usuario"] == usuario and linha["senha"] == senha:
                return True

    return False