import streamlit as st

motivos_imagenes = {
    "Para perder peso": "c:/Users/casa/Downloads/quemag.jpg",
    "Para perder grasa y tonificar": "c:/Users/casa/Downloads/tonificar.jpg",
    "Para aumentar el volumen de mi cuerpo": "c:/Users/casa/Downloads/volumen.jpg",
    "Quisiera en un futuro participar en competiciones de fisicoculturismo": "c:/Users/casa/Downloads/hiper.jpg",
    "Por cuestiones de salud": "c:/Users/casa/Downloads/salud.jpg",
}

def mostrar_imagen(motivo):
    if motivo in motivos_imagenes:
        st.image(motivos_imagenes[motivo], caption=f"Motivo: {motivo}", use_column_width=True)
    else:
        st.warning("Motivo no encontrado. Por favor, selecciona uno válido.")

st.markdown(
    "<div style='text-align: center;'><h1>Welcome</h1></div>",
    unsafe_allow_html=True,
)


st.image("c:/Users/casa/Downloads/gym1.jpg",width=700)

with st.form("formulario"):
    col1, col2 = st.columns(2)
    nombre = col1.text_input("**Nombre(s)**")
    apellidos = col2.text_input("**Apellidos(s)**")

    edad = st.number_input("**Selecciona tu edad**", 0, 150)

    sexo = st.radio("**Sexo**", ["Femenino", "Masculino"])
    municipio = st.selectbox("**Municipio de procedencia**", ["Habana Vieja", "Centro Habana", "Cerro", "Diez de Octubre", "Plaza", "Arroyo Naranjo", "Boyeros", "Cotorro", "San Miguel del Padrón", "Playa", "Marianao", "La Lisa", "Habana del Este", "Guanabacoa", "Regla"])

    razones = st.radio("**¿Por qué quieres comenzar a ir al gimnasio?**", list(motivos_imagenes.keys()))

    a = st.form_submit_button(label="Enviar", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)


if a and edad >= 15:
    st.write("**Datos del usuario:**")
    st.write(f"Nombre: {nombre} {apellidos}")
    st.write(f"Edad: {edad}")
    st.write(f"Sexo: {sexo}")
    st.write(f"Municipio de procedencia: {municipio}")
    st.write(f"Motivo para ir al gimnasio: {razones}")
    mostrar_imagen(razones)
elif edad < 15 and edad != 0:
    st.error(f"Tu edad es: {edad} años. Lo sentimos, no puedes acceder a nuestro gimnasio. Debes ser mayor de 15 años.")


