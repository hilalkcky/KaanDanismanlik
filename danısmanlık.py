import streamlit as st
import pydeck as pdk

st.set_page_config(page_title="KAAN DANIŞMANLIK", initial_sidebar_state="collapsed")
st.markdown("""
<style>
    .css-1kyxreq {  # Bu sınıfı uygulamanıza göre özelleştirin
        max-width: 600px;  /* Örnek genişlik ayarı */
        margin: auto;  /* Merkeze yerleştirme */
    }
    .radio-container {
        display: flex;
        justify-content: center;  /* Ortalamak için */
        margin-top: 20px;  /* Üstten boşluk */
    }
</style>
""", unsafe_allow_html=True)

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
st.markdown(f'<style>{html_string}</style>', unsafe_allow_html=True)

# Sayfa seçim
page = st.radio("", ["Ana Sayfa", "Hizmetlerimiz", "İletişim"], horizontal=True, key="menu_radio", help="Sayfa seçin")

st.write("#")
# Ana Sayfa
st.markdown(
    """
    <h2 style="background-color: #AEEEEE; font-weight: bold; padding: 10px; border-radius: 5px; color: black;">
        TÜRKİYE'YE GELDİNİZ VE NE YAPACAĞINIZI BİLEMİYOR MUSUNUZ? YENİ HAYATINIZA KAAN DANIŞMANLIĞI ZİYARET EDEREK BAŞLAYABİLİRSİNİZ.
    </h2>
    """,
    unsafe_allow_html=True
)
st.write("#")
st.image("ilkresim.jpeg", width=700)

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
    st.image("peter.jpeg", width=500)  # Yorum sahibinin fotoğrafı
    st.write("Phillip Mayer, 35")
    st.write("""
    "Kaan Danışmanlık ile göçmenlik süreci hakkında endişelenmenize gerek yok. Kendimi hoş ve emin ellerde hissettim."
    """)

    # Yorum 2
    st.image("noni.jpeg", width=500) 

