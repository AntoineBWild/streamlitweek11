import streamlit as st
from streamlit_option_menu import option_menu

#Données des utilisateurs en dur dans le code
users_data = {
    "root": {
        "password": "rootMDP",
        "email": "root@gmail.com",
        "failed_login_attempts": 0,
        "logged_in": False,
        "role": "administrateur"
    },
    "utilisateur": {
        "password": "userMDP",
        "email": "user@gmail.com",
        "failed_login_attempts": 0,
        "logged_in": False,
        "role": "utilisateur"
    }
}

#Fonction d'authentification
def authenticate(username, password):
    if username in users_data:
        user = users_data[username]
        if user["password"] == password:
            users_data[username]["logged_in"] = True
            return True
        else:
            users_data[username]["failed_login_attempts"] += 1
            return False
    return False

#Afficher la page d'authentification
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            if authenticate(username, password):
                st.session_state["username"] = username
                st.session_state["logged_in"] = True
                st.success("Connexion réussie !")
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect")
        else:
            st.warning("Les champs username et mot de passe doivent être remplis")
