import streamlit as st
from login import cadastrar_usuario, autenticar, is_admin


def main():
    st.set_page_config(page_title="Safelog Enterprises", page_icon="🔐", layout="centered")

    st.title("Safelog Enterprises")
    st.markdown("Bem-vindo à **Safelog Enterprises**!")

    # Controle de sessão
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if "usuario" not in st.session_state:
        st.session_state.usuario = ""

    # Se estiver logado
    if st.session_state.logado:
        st.success(f"Login bem-sucedido! Bem-vindo, {st.session_state.usuario}!")

        st.subheader("Ferramentas do Usuário")
        st.markdown("*Aqui você pode acessar suas **ferramentas** e **recursos exclusivos** " \
        "como **colaborador(a)** da Safelog Enterprises*.")
        st.markdown("**EM DESENVOLVIMENTO...**")

        if st.button("Sair"):
            st.session_state.logado = False
            st.session_state.usuario = ""
            st.rerun()

        return

    # Se não estiver logado
    aba = st.radio("Escolha uma opção:", ("Login", "Cadastrar"))

    if aba == "Cadastrar":
        st.subheader("Cadastro de Usuário")
        usuario = st.text_input("Nome de usuário", key="cad_usuario")
        senha = st.text_input("Senha", type="password", key="cad_senha")

        if st.button("Cadastrar"):
            if cadastrar_usuario(usuario, senha):
                st.success("Usuário cadastrado com sucesso!")
            else:
                st.error("Não foi possível cadastrar. Verifique se o usuário já existe ou se os campos estão vazios.")

    else:
        st.subheader("Login")
        usuario = st.text_input("Nome de usuário", key="login_usuario")
        senha = st.text_input("Senha", type="password", key="login_senha")

        if st.button("Login"):
            if autenticar(usuario, senha):
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.rerun()
            else:
                st.error("Nome de usuário ou senha incorretos. Tente novamente.")


if __name__ == "__main__":
    main()