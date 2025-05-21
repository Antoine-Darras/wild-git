import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Chargement des utilisateurs depuis le CSV
df_users = pd.read_csv("users.csv")

# Conversion des données en format attendu par streamlit-authenticator
credentials = {
    "usernames": {
        row["username"]: {
            "name": row["name"],
            "password": row["password"],
            "email": row["email"],
            "role": row["role"],
            "failed_login_attempts": 0,
            "logged_in": False,
        }
        for _, row in df_users.iterrows()
    }
}

# Création de l'authenticator
authenticator = Authenticate(
    credentials,
    "cookie_name",  # Peut être n'importe quel nom
    "cookie_key",  # Peut être n'importe quelle clé
    30,  # Expiration du cookie en jours
)

# Formulaire de connexion
authenticator.login()

# Vérification de l'état de connexion
if st.session_state["authentication_status"]:
    # Bouton de déconnexion
    authenticator.logout("Déconnexion", "sidebar")

    # Menu latéral
    with st.sidebar:
        selection_menu = option_menu(
            menu_title=None,
            options=["Accueil", "Gif de Michael Scott"],
            icons=["house", "camera-video"],
            orientation="vertical",
        )

    # Contenu principal
    st.success(f"Bienvenue {st.session_state['name']} 👋")

    if selection_menu == "Accueil":
        st.title("Bienvenue sur ma page !")
        st.image(
            "https://media.tenor.com/M1a8cbcCmEgAAAAM/the-office-welcome.gif", width=500
        )

    elif selection_menu == "Gif de Michael Scott":
        st.title("Très bon choix, enjoy 😎")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://media.tenor.com/BW79x4OUJnAAAAAM/whoopdidy-scoop.gif")
            st.image(
                "https://media.tenor.com/mUR6IIN2CnEAAAAM/wow-surprised.gif", width=500
            )
        with col2:
            st.image(
                "https://media.tenor.com/gH8YEHtt0akAAAAM/michael-scott-the-office.gif"
            )
            st.image("https://media1.tenor.com/m/WxzYDPsP_DoAAAAd/the-office-hit.gif")
        with col3:
            st.image(
                "https://media.tenor.com/5y7fAjBCM7UAAAAM/embarrassed-michaelscott.gif"
            )
            st.image(
                "https://media1.tenor.com/m/tCT5wHxxyzIAAAAC/the-office-michael-scott.gif"
            )

elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez entrer vos identifiants")
