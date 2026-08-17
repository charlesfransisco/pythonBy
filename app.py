import streamlit as st
import datetime
from supabase import create_client
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

st.set_page_config(  ## Untuk mengatur tulisan dan icon kecil pada tab browser
    page_title="Expense Tracker",
    page_icon="💰"
)

st.title("Expenses Tracker")

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)


def load_data():
    try:
        response = supabase.table("expenses").select("*").order("id").execute()
        logger.info("Loaded %d expenses from Supabase.", len(response.data))
        return response.data
    except Exception:
        logger.exception("Error loading data")
        st.error(f"Error loading data. Please try again ...")
        return []


def tambah_data(tanggal, deskripsi, jumlah, kategori):
    try:
        supabase.table("expenses").insert({
            "date": tanggal,
            "description": deskripsi,
            "amount": jumlah,
            "category": kategori
        }).execute()
        logger.info("Data added successfully.")
        return True
    except Exception:
        logger.exception("Error adding data")
        st.error(f"Error adding data. Please try again ...")
        return False


# session_state dipakai supaya data tidak hilang setiap Streamlit rerun script
if "expenses" not in st.session_state:
    st.session_state.expenses = load_data()

option = st.selectbox(
    "Berikan kategori untuk jenis expenses? ",
    ("Food&beverages", "daily necessities", "Leisure / Entertainment")
)

st.write("You selected:", option)

# st.form supaya input hanya diproses saat tombol submit ditekan,
# bukan setiap kali satu widget berubah
with st.form("form_tambah", clear_on_submit=True):
    expense_date = st.date_input(
        "Tanggal pengeluaran",
        value=datetime.date.today()
    )

    description = st.text_input("Deskripsi pengeluaran")

    amount = st.number_input(
        "Jumlah pengeluaran",
        min_value=0.0,
        value=None,
        placeholder="Type a number..."
    )

    submitted = st.form_submit_button("Tambah Data")

if submitted:
    if not description or amount is None:
        st.warning("Deskripsi dan jumlah wajib diisi.")
    else:
        tambah_data(expense_date.isoformat(), description, amount, option)
        st.session_state.expenses = load_data()
        st.success("Data pengeluaran berhasil ditambahkan!")


st.subheader("Data Pengeluaran")

if not st.session_state.expenses:
    st.write("Belum ada data pengeluaran.")
else:
    for nomor, expense in enumerate(st.session_state.expenses, start=1):
        tanggal = expense.get("date", "-")
        kategori = expense.get("category", "-")
        st.write(
            f"{nomor}. {tanggal} — {expense['description']} ({kategori}) - Rp {expense['amount']:,.0f}"
        )
