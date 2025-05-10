 import streamlit as st

# Game sederhana sebelum kalkulator
st.title("Selamat Datang di Caffeine Tracker!")

if "game_completed" not in st.session_state:
    st.session_state["game_completed"] = False

if not st.session_state["game_completed"]:
    st.subheader("Tebak Angka!")
    st.write("Tebak angka antara 1 hingga 10. Jika benar, Anda dapat mengakses kalkulator.")

    import random
    if "target_number" not in st.session_state:
        st.session_state["target_number"] = random.randint(1, 10)

    guess = st.number_input("Masukkan tebakan Anda:", min_value=1, max_value=10, step=1)
    if st.button("Tebak"):
        if guess == st.session_state["target_number"]:
            st.success("Tebakan Anda benar! Anda dapat mengakses kalkulator.")
            st.session_state["game_completed"] = True
        else:
            st.error("Tebakan salah, coba lagi!")

# Kalkulator kafein jika game selesai
if st.session_state["game_completed"]:
    st.title("Kalkulator Asupan Kafein")

    # Input dari pengguna
    berat_badan = st.number_input("Berat badan Anda (kg):", min_value=10, max_value=200, step=1)
    usia = st.number_input("Usia Anda:", min_value=1, max_value=120, step=1)
    jenis_kelamin = st.selectbox("Jenis Kelamin:", ["Laki-laki", "Wanita"])

    sumber_kafein = st.selectbox(
        "Sumber Kafein:",
        ["Minuman Soda", "Minuman Coklat", "Teh", "Kopi", "Minuman Berenergi"]
    )

    jumlah_ml = st.number_input("Berapa ml minuman yang Anda konsumsi:", min_value=0, step=1)

    if st.button("Hitung Asupan Kafein"):
        # Kandungan kafein per 100ml (rata-rata)
        kafein_per_100ml = {
            "Minuman Soda": 10,
            "Minuman Coklat": 5,
            "Teh": 20,
            "Kopi": 40,
            "Minuman Berenergi": 80
        }

        kandungan_kafein = (kafein_per_100ml[sumber_kafein] / 100) * jumlah_ml
        batas_harian = berat_badan * 2.5  # Anggap 2.5 mg kafein per kg berat badan sebagai batas aman
        sisa_konsumsi = max(0, batas_harian - kandungan_kafein)

        st.write(f"Anda telah mengonsumsi sekitar **{kandungan_kafein:.2f} mg** kafein.")
        st.write(f"Batas kafein harian Anda adalah **{batas_harian:.2f} mg**.")

        if sisa_konsumsi > 0:
            st.success(f"Anda masih bisa mengonsumsi sekitar **{sisa_konsumsi:.2f} mg** kafein hari ini.")
        else:
            st.warning("Anda telah mencapai atau melebihi batas kafein harian Anda. Hindari konsumsi lebih lanjut!")
