import streamlit as st

# Fungsi untuk menambahkan latar belakang dari file lokal
def tambah_background_from_local(image_file):
    with open(image_file, "rb") as f:
        image_data = f.read()
    b64_image = f"data:image/jpeg;base64,{image_data.decode('utf-8')}"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{b64_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Tambahkan background lokal
tambah_background_from_local("background.jpg")

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
    def hitung_kafein_terkonsumsi(jenis_minuman, ml):
        kandungan_kafein = {
            "Minuman Soda": 10,      # mg per 100 ml
            "Minuman Coklat": 5,    # mg per 100 ml
            "Kopi": 40,             # mg per 100 ml
            "Minuman Berenergi": 30, # mg per 100 ml
            "Matcha": 25,           # mg per 100 ml
            "Espresso": 212,        # mg per 100 ml
            "Teh Hijau": 12,        # mg per 100 ml
            "Teh Hitam": 47,        # mg per 100 ml
            "Cappuccino": 77,       # mg per 100 ml
            "Americano": 94         # mg per 100 ml
        }
        return (kandungan_kafein.get(jenis_minuman, 0) * ml) / 100*
