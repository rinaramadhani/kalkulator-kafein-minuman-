import streamlit as st
import time

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
                st.session_state["fireworks_shown"]_]()_

