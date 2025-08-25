import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(
                rgba(255, 255, 255, 0.7),   /* capa de transparencia arriba */
                rgba(255, 255, 255, 0.7)    /* capa de transparencia abajo */
            ),
            url(https://images.unsplash.com/photo-1525373612132-b3e820b87cea?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZGVzcGVkaWRhJTIwZGUlMjBzb2x0ZXJhfGVufDB8fDB8fHww);

            background-size: cover; /*Ajusta sin deformar*/
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: scroll; /* Para que se mueva con el scroll */
        }
    </style>
""", unsafe_allow_html=True)

# Configuración de la página
st.set_page_config(
    page_title="Misión Despedida",
    page_icon= "https://template.canva.com/EAGA_yEY_pk/2/0/622w-MK3RO2C4ttQ.jpg",
    layout="centered",
    initial_sidebar_state="collapsed"
)
# CSS personalizado
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');

    .custom-title {
        font-family: 'Comic sans', sans-serif; /* Cambia la fuente */
        font-size: 40px;
        color: rgba(255, 255, 255, 1.0); /* Blanco */
        text-shadow: 5px 5px 4px rgba(0,0,0,0.8); /* Sombra del texto */
        text-align: center;
    }

.logo {
    display: inline-block;
    width: 150px;
    cursor: pointer;
    transition: transform 0.3s;
    position: fixed;
    bottom: 50px; /* Pegado al borde inferior */
}

.logo1 {
 display: inline-block;
    width: 215px;
    cursor: pointer;
    transition: transform 0.3s;
    position: fixed;
    bottom: 200px; /* Pegado al borde inferior */
}

.logo {
    left: 15%; /* Ajusta según quieras */
}

.logo1 {
    left: 5%; /* Junto al otro logo */
}

.logo:hover, .logo1:hover {
    transform: scale(1.1);
}

</style>
""", unsafe_allow_html=True)

# HTML para el logo y título
st.markdown(f"""
    <a href="https://www.google.com/?hl=es" target="_blank">
      <img class="logo" src="https://cdn-icons-png.flaticon.com/512/7824/7824658.png">
""", unsafe_allow_html=True)
st.markdown(f"""
 <a href="https://www.google.com/?hl=es" target="_blank">
    <img class="logo1" src="https://png.pngtree.com/png-clipart/20230813/original/pngtree-princess-party-bridal-shower-card-design-picture-image_7907151.png">
""", unsafe_allow_html=True)


# Estilos CSS para mejorar la visualización en móviles
st.markdown("""
    <style>
        /* Ajustar tamaño de texto y márgenes para móviles */
        body {
            font-size: 16px;
        }
        .css-1d391kg {  /* Cambia el padding del contenido */
            padding: 1rem 0.5rem;
        }
        /* Ajustar ancho de los inputs y botones */
        .stTextInput>div>div>input,
        .stButton>button {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)