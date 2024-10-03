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
page = st.radio("", ["Ana Sayfa", "Hizmetlerimiz", "İletişim"], horizontal=True)

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
    st.image("noni.jpeg", width=500)  # Yorum sahibinin fotoğrafı
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
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Çalışma İzni</h3>", unsafe_allow_html=True)
        st.image("WhatsApp Image 2024-10-01 at 13.56.24 (2).jpeg", width=300, use_column_width=True)

    with col2:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Oturum İzni</h3>", unsafe_allow_html=True)
        st.image("WhatsApp Image 2024-10-01 at 13.56.24 (3).jpeg", width=300, use_column_width=True)

    # 2. Hizmet
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Deport İşlemleri</h3>", unsafe_allow_html=True)
        st.image("deport.jpeg", width=300, use_column_width=True)

    with col2:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Yabancı Hukuk İşlemleri</h3>", unsafe_allow_html=True)
        st.image("WhatsApp Image 2024-10-01 at 13.56.24.jpeg", width=300, use_column_width=True)

    # 3. Hizmet
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Evlilik İşlemleri</h3>", unsafe_allow_html=True)
        st.image("WhatsApp Image 2024-10-01 at 13.56.24 (4).jpeg", width=300, use_column_width=True)

    with col2:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Öğrenci İşlemleri</h3>", unsafe_allow_html=True)
        st.image("ogrenci.jpeg", width=300, use_column_width=True)

    # 4. Hizmet
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Yabancı Sağlık Sigortası</h3>", unsafe_allow_html=True)
        st.image("WhatsApp Image 2024-10-01 at 13.56.24 (1).jpeg", width=300, use_column_width=True)

    with col2:
        st.markdown("<h3 style='font-size: 24px; font-weight: bold; color: white;'>Randevu İşlemleri</h3>", unsafe_allow_html=True)
        st.image("son.jpeg", width=300, use_column_width=True)
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
    st.write("""Bize ulaşmak için aşağıdaki bilgileri kullanabilirsiniz:""")

    # Adres
    st.subheader("Adres")
    st.subheader(
        "[Cumhuriyet Mahallesi Tuna Caddesi No: 11/18 Çanakçı İşhanı Çankaya/Ankara](https://www.google.com/search?q=KAAN+DANI%C5%9EMANLIK&rlz=1C1CHZN_trTR1017TR1017&oq=kaan+dan%C4%B1%C5%9Fmanl%C4%B1k&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIICAEQRRgnGDsyBggCEEUYQDIICAMQABgWGB4yCggEEAAYgAQYogQyCggFEAAYgAQYogQyBggGEEUYPDIGCAcQRRg80gEJNDEzMmowajE1qAIIsAIB&sourceid=chrome&ie=UTF-8)")
    st.write("#")
    st.write("Diğer şubemiz:")
    st.write(
        "[Osmanağa Mah. Halitağa Cad. No:31 Daire:6 Kadıköy İstanbul](https://www.google.com/maps/search/?api=1&query=Osmanağa+Mah.+Halitağa+Cad.+No:31+Daire:6+Kadıköy+İstanbul)")

    # Telefon numarası
    st.subheader("Telefon: *0553 794 6771*")

    # Logo için alan
    st.image("logo.jpeg", width=500)

    latitude = 39.923952513749335
    longitude = 32.85656321135337
    view_state = pdk.ViewState(
        latitude=latitude,
        longitude=longitude,
        zoom=11,  # Yakınlaştırma seviyesi
        pitch=50  # Haritanın eğim açısı
    )

    layer = pdk.Layer(
        'ScatterplotLayer',
        data=[{'lat': latitude, 'lon': longitude}],
        get_position='[lon, lat]',
        get_radius=30,  # İşaretçinin büyüklüğü
        get_color=[255, 0, 0],  # Kırmızı renk
        pickable=True
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/streets-v11"  # Google Haritalar benzeri bir stil
    )

    st.pydeck_chart(deck)


