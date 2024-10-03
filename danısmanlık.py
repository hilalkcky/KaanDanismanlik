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

# Sidebar menüsü
st.sidebar.title("Menü")
pages = ["Ana Sayfa", "Hizmetlerimiz", "İletişim"]

page = st_navbar(
    pages,
    styles=styles,

)

st.write("#")
# Ana Sayfa

st.write("#")
st.image("picture/ilkresim.jpeg", width=700)

if page == "Ana Sayfa":
    st.markdown(
        """
        <style>
        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Başlık
    st.title("Kaan Danışmanlık")

    st.subheader("Merhabalar ülkemizin değerli misafirleri,")
    st.write("""
    Öncelikle hepinizi sevgi ile kucaklıyor, ülkenizden ayrılmanın verdiği hüznü sizlerle paylaşmak istiyoruz.
    Kaan Danışmanlık olarak uzman kadromuzla birlikte 8 yıldır sizden önceki misafirlerimize kaliteli hizmet sunduk ve bu kalitemizi sizlere de hizmet vererek devam ettirmek istiyoruz.
    Peki biz 8 yıldır neler mi yapıyoruz?
    """)

    # Kullanıcı Yorumları
    st.subheader("Müşteri Yorumları")

    # Yorum 1
    st.image("picture/peter.jpeg", width=500)  # Yorum sahibinin fotoğrafı
    st.write("Phillip Mayer, 35")
    st.write("""
    "Kaan Danışmanlık ile göçmenlik süreci hakkında endişelenmenize gerek yok. Kendimi hoş ve emin ellerde hissettim."
    """)

    # Yorum 2
    st.image("picture/noni.jpeg", width=500)  # Yorum sahibinin fotoğrafı
    st.write("Noni Faraji, 25")
    st.write("""
    "Türkiye'ye tek başıma okumak için gelmek çok stresli olabilirdi. Neyse ki, Kaan Danışmanlık benim evden uzaktaki ailemdi ve her şeyi halletmeme yardım etti."
    """)

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
