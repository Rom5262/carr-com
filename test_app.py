import streamlit as st

st.title("¡Hola Mundo con Streamlit!")
st.write("Esta es una aplicación de prueba muy simple.")
st.success("Si puedes ver esto, Streamlit está funcionando correctamente.")

# Opcional: Un botón para verificar interactividad
if st.button("Haz clic aquí"):
    st.write("¡Clic detectado!")
    