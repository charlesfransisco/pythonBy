import streamlit as st
import datetime


st.set_page_config( ## Untuk mengatur tulisan dan icon kecil pada tab browser
    page_title="Expense Tracker",
    page_icon="💰"
)

expense_date = st.date_input(
    "Tanggal pengeluaran",
    value=datetime.date.today()
)

st.title("Expenses Tracker")

description = st.text_input("Deskripsi pengeluaran")

amount = st.number_input(
    "Jumlah pengeluaran",
    value=None,
    placeholder="Type a number..."
)

st.write(f"Deskripsi: {description}")
st.write(f"Jumlah: Rp {amount}")



