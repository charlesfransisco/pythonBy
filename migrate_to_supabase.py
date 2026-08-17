import json
import streamlit as st
from supabase import create_client

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

with open("expenses.json", "r") as file:
    expenses_lama = json.load(file)

rows = []
for expense in expenses_lama:
    rows.append({
        "date": expense.get("date", "2026-08-17"),
        "description": expense["description"],
        "amount": expense["amount"],
        "category": expense.get("category") or expense.get("categoriy")
    })

response = supabase.table("expenses").insert(rows).execute()
print(f"Berhasil migrasi {len(response.data)} data ke Supabase.")
