import streamlit as st
from streamlit_option_menu import option_menu

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

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

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

def main_menu():
    with st.sidebar:
        st.write(f"Bienvenue, {st.session_state['username']}!")
        selection = option_menu(
            menu_title="Navigation",
            options=["Accueil", "Photos"],
            icons=["house", "camera"],
            menu_icon="cast",
            default_index=0
        )
        if st.button("Déconnexion"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()

    if selection == "Accueil":
        st.title("Page d'accueil")
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.title("Photos de Gizmo")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Gizmo qui regarde un film d'horreur")
            st.image("https://miro.medium.com/v2/resize:fit:720/format:webp/0*yxzaBxdjxYrc0-Ie")
        with col2:
            st.write("Gizmo qui pilote une voiture")
            st.image("https://64.media.tumblr.com/9553ccc7ae6519a2223fcf2a811fc6e2/tumblr_n9k65qnmdG1rvpu8lo2_r1_500.png")
        with col3:
            st.write("GIZMO RAMBO !!")
            st.image("https://pbs.twimg.com/media/F_PXn_VXEAALx_u?format=jpg&name=small")

# Logique principale de l'application
if st.session_state["logged_in"]:
    main_menu()
else:
    login_page()
