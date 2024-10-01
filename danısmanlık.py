import streamlit as st
import pydeck as pdk
from streamlit_navigation_bar import st_navbar

# Sayfa yapılandırmasını ayarlayın
st.set_page_config(page_title="KAAN DANIŞMANLIK", initial_sidebar_state="collapsed")
st.markdown("""
<style>
    .css-1kyxreq {  # Bu sınıfı uygulamanıza göre özelleştirin
        max-width: 600px;  /* Örnek genişlik ayarı */
        margin: auto;  /* Merkeze yerleştirme */
    }
</style>
""", unsafe_allow_html=True)
</style>""", unsafe_allow_html=True)
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
options = {"show_sidebar": False}
page = st_navbar(
    pages,
    styles=styles,
    options=options,
)

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

    # Hoş geldiniz mesajı
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

# Hizmetlerimiz sayfası
elif page == "Hizmetlerimiz":
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
    st.title("Hizmetlerimiz")
    st.subheader("""Kaan Danışmanlık olarak sunduğumuz hizmetler:""")
    services = [
        ("Çalışma İzni", "picture/WhatsApp Image 2024-10-01 at 13.56.24 (2).jpeg"),
        ("Oturum İzni", "picture/WhatsApp Image 2024-10-01 at 13.56.24 (3).jpeg"),
        ("Deport İşlemleri", "picture/deport.jpeg"),
        ("Yabancı Hukuk İşlemleri", "picture/WhatsApp Image 2024-10-01 at 13.56.24.jpeg"),
        ("Evlilik İşlemleri", "picture/WhatsApp Image 2024-10-01 at 13.56.24 (4).jpeg"),
        ("Öğrenci İşlemleri", "picture/ogrenci.jpeg"),
        ("Yabancı Sağlık Sigortası", "picture/WhatsApp Image 2024-10-01 at 13.56.24 (1).jpeg"),
        ("Randevu İşlemleri", "picture/son.jpeg"),
    ]

    for service, image in services:
        st.markdown(f"<h3 style='font-size: 24px; font-weight: bold; color: white;'>{service}</h3>", unsafe_allow_html=True)
        st.image(image, width=700)

# İletişim sayfası
elif page == "İletişim":
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
    st.title("İletişim")
    st.write("""
    Bize ulaşmak için aşağıdaki bilgileri kullanabilirsiniz:
    """)

    # Adres
    st.subheader("Adres")
    st.subheader(
        "[Cumhuriyet Mahallesi Tuna Caddesi No: 11/18 Çanakçı İşhanı Çankaya/Ankara](https://www.google.com/maps/search/?api=1&query=Cumhuriyet+Mahallesi+Tuna+Caddesi+No:+11/18+Çanakçı+İşhanı+Çankaya/Ankara)")
    st.write("#")
    st.write("Diğer şubemiz:")
    st.write(
        "[Osmanağa Mah. Halitağa Cad. No:31 Daire:6 Kadıköy İstanbul](https://www.google.com/maps/search/?api=1&query=Osmanağa+Mah.+Halitağa+Cad.+No:31+Daire:6+Kadıköy+İstanbul)")

    # Telefon numarası
    st.subheader("Telefon: *0553 794 6771*")

    # Logo için alan
    st.image("picture/logo.jpeg", width=500)




    latitude = 39.923952513749335
    longitude = 32.85656321135337
    view_state = pdk.ViewState(
        latitude=latitude,
        longitude=longitude,
        zoom=11,  # Yakınlaştırma seviyesi
        pitch=50  # Haritanın eğim açısı
    )

    # Kırmızı işaretçi için ScatterplotLayer kullanıyoruz
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=[{'lat': latitude, 'lon': longitude}],
        get_position='[lon, lat]',
        get_radius=500,  # İşaretçinin büyüklüğü
        get_color=[255, 0, 0],  # Kırmızı renk
        pickable=True
    )

    # Renkli harita stili ekleyelim (Mapbox stilleri kullanılıyor)
    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/streets-v11"  # Google Haritalar benzeri bir stil
    )

    # Harita bileşenini ekleyelim
    st.pydeck_chart(deck)
