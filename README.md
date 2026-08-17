# Expense Tracker

A simple expense tracking app, built as a learning project for Python & Streamlit. It ships in two independent versions:

| Version | File | Data storage |
|---|---|---|
| Terminal (CLI) | [`main.py`](main.py) | Local, `expenses.json` |
| Web (Streamlit) | [`app.py`](app.py) | Cloud, [Supabase](https://supabase.com) |

## Features

- Add an expense (date, description, amount, category)
- List all expenses
- Terminal version: compute total & total per category, save to a JSON file
- Web version: input form, data persisted in a Supabase database

## Installation

```bash
git clone <this-repo-url>
cd pythonBy
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Running

**Terminal version** (no extra setup needed):

```bash
python main.py
```

**Web version** — requires a [Supabase](https://supabase.com) project with an `expenses` table (columns: `date`, `description`, `amount`, `category`). Create a `.streamlit/secrets.toml` file with:

```toml
SUPABASE_URL = "https://xxxx.supabase.co"
SUPABASE_KEY = "xxxx"
```

Then run:

```bash
streamlit run app.py
```

## Project structure

```
main.py                  # terminal version, reads/writes expenses.json
app.py                   # web version (Streamlit), reads/writes Supabase
expenses.json            # local data used by main.py
migrate_to_supabase.py   # one-off script: move old data from expenses.json to Supabase
test_supabase.py         # small script to check the Supabase connection
```

## Notes

This project was built to practice core logic (functions, data persistence, form handling) before moving on to database integration and web deployment.
