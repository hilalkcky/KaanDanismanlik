import streamlit as st
import pydeck as pdk
from streamlit_navigation_bar import st_navbar

st.set_page_config(page_title="KAAN DANIŞMANLIK", initial_sidebar_state="collapsed")
st.markdown("""
<style>
    .css-1kyxreq {  # Bu sınıfı uygulamanıza göre özelleştirin
        max-width: 600px;  /* Örnek genişlik ayarı */
        margin: auto;  /* Merkeze yerleştirme */
    }
</style>
""", unsafe_allow_html=True)

html_string = """
  .stApp {
      background: black;

  }
  """
styles = {
    "nav": {
        "background-color": "black",
    },

    "span": {

        "color": "white",

        "margin": "auto",
        "font-family": "'Gill Sans Extrabold', sans-serif",
        "overflow": "auto"
    },

}
st.markdown(f'<style>{html_string}</style>', unsafe_allow_html=True)



st.write("denem")
    
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")

st.write("#")
st.write("#")
st.write("denem2")

