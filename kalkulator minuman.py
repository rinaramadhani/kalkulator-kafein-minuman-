import streamlit as st

# Fungsi untuk menambahkan CSS background
def tambah_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{image_path}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Fungsi untuk membaca gambar sebagai base64
import base64
def baca_gambar_untuk_css(path):
    with open(path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

# Tambahkan background
image_path = "/mnt/data/WhatsApp Image 2025-05-17 at 10.15.59_4adf024d.jpg"
background_image = baca_gambar_untuk_css(image_path)
tambah_background(background_image)

# Sidebar navigasi
menu = st.sidebar.radio("Navigasi", ["Home", "Kalkulator Kafein", "Tentang Kami"])

# Halaman Home
if menu == "Home":
    st.title("Selamat Datang di Kalkulator Kafein☕")
    st.write("""
    **Kalkulator Kafein Harian** membantu Anda mengetahui batas aman konsumsi kafein berdasarkan usia, jenis kelamin, 
    dan jenis minuman. Gunakan fitur ini untuk menjaga kesehatan Anda dan keluarga! 
    Pilih menu **Kalkulator Kafein** untuk memulai perhitungan. 😊
    """)

# Halaman Kalkulator Kafein
elif menu == "Kalkulator Kafein":
    st.title("Kalkulator Batas Kafein Harian☕")

    berat_badan = st.number_input("Berat Badan (kg):", min_value=0.0, step=0.1)
    usia = st.number_input("Usia (tahun):", min_value=0, step=1)
    jenis_kelamin = st.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
    jenis_minuman = st.selectbox(
        "Sumber Kafein:",
        ["Minuman Soda", "Minuman Coklat", "Kopi", "Minuman Berenergi", "Matcha", "Espresso", "Teh Hijau", "Teh Hitam", "Cappuccino", "Americano"]
    )
    ml_dikonsumsi = st.number_input("Berapa ml yang diminum:", min_value=0, step=1)

    if st.button("Hitung"):
        batas_aman = hitung_batas_aman_kafein(usia, jenis_kelamin)
        kafein_terkonsumsi = hitung_kafein_terkonsumsi(jenis_minuman, ml_dikonsumsi)
        sisa_kafein = max(batas_aman - kafein_terkonsumsi, 0)

        st.subheader("Hasil Perhitungan:")
        st.write(f"**Batas Harian:** {batas_aman} mg")
        st.write(f"**Konsumsi Kafein:** {kafein_terkonsumsi:.2f} mg")
        st.write(f"**Sisa Batas Aman:** {sisa_kafein:.2f} mg")

        if sisa_kafein > 0:
            st.write(f"**Status:** Aman✅, Anda masih dalam batas konsumsi kafein yang aman😊.")
        else:
            st.warning("**Status:** Tidak Aman❗, Anda telah melewati batas konsumsi kafein harian yang aman!😔")

# Halaman Tentang Kami
elif menu == "Tentang Kami":
    st.title("Tentang Kami")
    st.write("""
    **Kalkulator Batas Kafein Harian** adalah aplikasi sederhana yang dirancang untuk membantu Anda mengelola konsumsi kafein dengan mudah.
    
    **Pengembang:**
    - Aplikasi ini dibuat oleh **Kelompok 9** sebagai bagian dari proyek pembelajaran.
    - Tujuannya adalah memberikan alat yang praktis untuk menjaga kesehatan dengan membatasi konsumsi kafein berlebih.

    **Fitur Utama:**
    - Perhitungan batas kafein berdasarkan usia dan jenis kelamin.
    - Kalkulasi konsumsi kafein dari berbagai jenis minuman.
    - Informasi yang interaktif dan mudah digunakan.

    **Terima kasih telah menggunakan aplikasi kami! 😊**
    """)


