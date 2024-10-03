import streamlit as st
import pydeck as pdk
from streamlit_navigation_bar import st_navbar


st.set_page_config(page_title="KAAN DANIŞMANLIK", initial_sidebar_state="collapsed")


html_string = """
  .stApp > header {
      background-color: transparent;
  }

  .stApp {
      margin: auto;
      font-family: "Gill Sans Extrabold", sans-serif;
      overflow: auto;

      background: black;
      animation: gradient 15s ease infinite;
      background-size: 400% 400%;
      background-attachment: fixed;
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

    "hover": {
        "background-color": " #AEEEEE",
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
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("denem2")
