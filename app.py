import streamlit as st

st.set_page_config(page_title="Hola PyDay!", page_icon="🐍")

st.title("🐍 ¡Hola PyDay Chile 2025!")
st.subheader("Esta es una app simple hecha con Streamlit")

nombre = st.text_input("¿Cómo te llamas?")
opcion = st.selectbox("¿Qué te interesa de Python?", ["Data Science", "Web", "Automatización", "Machine Learning", "Todo 😍"])

if st.button("Mostrar mensaje"):
    if nombre:
        st.balloons()
        st.success(f"¡Hola {nombre}! Te encanta Python para {opcion} 🧠✨")
    else:
        st.warning("Por favor escribe tu nombre.")

st.markdown("---")
st.caption("Creado con ❤️ para la comunidad de Python Chile.")
