import streamlit as st

# Fungsi untuk menambahkan latar belakang dari URL
def tambah_background_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL gambar
image_url = "http://images.gofreedownload.net/3/set-of-dark-coffee-vector-background-106654.jpg"
tambah_background_from_url(image_url)

# Sidebar navigasi
menu = st.sidebar.radio("Navigasi", ["Home", "Kalkulator Kafein", "Tentang Kami"])

# Halaman Home
if menu == "Home":
    st.title("Selamat Datang di Kalkulator Kafein☕")
    st.write("Gunakan menu di sebelah kiri untuk mengakses fitur aplikasi.")

# Halaman Kalkulator Kafein
elif menu == "Kalkulator Kafein":
    st.title("Kalkulator Batas Kafein Harian☕")
    
    # Input dari pengguna
    berat_badan = st.number_input("Berat Badan (kg):", min_value=0.0, step=0.1)
    usia = st.number_input("Usia (tahun):", min_value=0, step=1)
    jenis_kelamin = st.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
    jenis_minuman = st.selectbox(
        "Sumber Kafein:",
        ["Minuman Soda", "Minuman Coklat", "Kopi", "Minuman Berenergi", "Matcha", "Espresso", "Teh Hijau", "Teh Hitam", "Cappuccino", "Americano"]
    )
    ml_dikonsumsi = st.number_input("Berapa ml yang diminum:", min_value=0, step=1)

    # Fungsi untuk menghitung batas aman konsumsi kafein
    def hitung_batas_aman_kafein(usia, jenis_kelamin):
        if usia < 18:
            return 100  # Anak-anak
        elif jenis_kelamin == "Laki-laki":
            return 400  # Dewasa laki-laki
        else:
            return 300  # Dewasa perempuan

    # Fungsi untuk menghitung konsumsi kafein berdasarkan jenis minuman
    def hitung
