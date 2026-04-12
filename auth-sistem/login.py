import csv
import os

ARQUIVO_USUARIOS = "usuarios.csv"


def inicializar_arquivo():
    
    if not os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, mode="w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["usuario", "senha"])


def cadastrar_usuario(usuario, senha):
   
    inicializar_arquivo()

    usuario = usuario.strip()
    senha = senha.strip()

    if not usuario or not senha:
        return False

    # Verifica se o usuário já existe
    with open(ARQUIVO_USUARIOS, mode="r", newline="", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        for linha in reader:
            if linha["usuario"] == usuario:
                return False


    with open(ARQUIVO_USUARIOS, mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([usuario, senha])

    return True


def autenticar(usuario, senha):
    
    inicializar_arquivo()

    usuario = usuario.strip()
    senha = senha.strip()

    with open(ARQUIVO_USUARIOS, mode="r", newline="", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        for linha in reader:
            if linha["usuario"] == usuario and linha["senha"] == senha:
                return True

    return False

def is_admin(senha):
    return senha == "admin123"