import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser lo primero que se ejecuta en tu script
st.set_page_config(
    page_title="FocusFlow Pro",
    page_icon="✅",
    layout="wide",  # Usa el ancho completo de la página
    initial_sidebar_state="expanded"
)

# --- LEER EL ARCHIVO HTML ---
# Asegúrate de que tu archivo HTML se llame 'index.html' y esté en la misma carpeta
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html_code = f.read()
except FileNotFoundError:
    st.error("No se encontró el archivo 'index.html'. Asegúrate de que esté en la misma carpeta que 'app.py'.")
    st.stop()


# --- MOSTRAR EL COMPONENTE HTML ---
st.components.v1.html(html_code, height=1000, scrolling=True)
