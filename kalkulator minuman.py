import streamlit as st
import time
import random

# Game sederhana sebelum kalkulator
st.title("Selamat Datang di Caffeine Tracker!")

if "game_completed" not in st.session_state:
    st.session_state["game_completed"] = False

if not st.session_state["game_completed"]:
    st.subheader("Game Sederhana: Hitung Mundur!")
    st.write("Tekan tombol mulai dan tunggu 5 detik untuk membuka kalkulator.")

    if "game_start_time" not in st.session_state:
        st.session_state["game_start_time"] = None

    if "fireworks_shown" not in st.session_state:
        st.session_state["fireworks_shown"] = False

    if st.session_state["game_start_time"] is None:
        if st.button("Mulai Game"):
            st.session_state["game_start_time"] = time.time()
    else:
        elapsed_time = time.time() - st.session_state["game_start_time"]
        if elapsed_time >= 5:
            if not st.session_state["fireworks_shown"]:
                st.balloons()
                st.session_state["fireworks_shown"] = True
            st.success("Game selesai! Anda dapat mengakses kalkulator.")
            st.session_state["game_completed"] = True
        else:
            st.write(f"Tunggu selama {5 - int(elapsed_time)} detik lagi...")
            st.progress(min(int((elapsed_time / 5) * 100), 100))

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
