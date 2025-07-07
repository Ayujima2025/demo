import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQLite DB (creates file if not exists)
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table if not exists
c.execute('''
CREATE TABLE IF NOT EXISTS grants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    grant_status TEXT NOT NULL,
    amount REAL,
    start_date TEXT,
    end_date TEXT
)
''')
conn.commit()

# Function to add a grant/project
def add_grant(project_name, grant_status, amount, start_date, end_date):
    c.execute('INSERT INTO grants (project_name, grant_status, amount, start_date, end_date) VALUES (?, ?, ?, ?, ?)',
              (project_name, grant_status, amount, start_date, end_date))
    conn.commit()

# Function to get all grants/projects
def get_all_grants():
    c.execute('SELECT * FROM grants')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Project Name', 'Grant Status', 'Amount', 'Start Date', 'End Date'])
    return df

# Streamlit UI
st.title("📊 Grants / Projects Status Dashboard")

# Add new grant form
with st.form(key='add_grant_form'):
    st.subheader("Add New Project/Grant")
    project_name = st.text_input("Project/Grant Name")
    grant_status = st.selectbox("Status", ["Draft", "Submitted", "Approved", "Rejected", "Completed"])
    amount = st.number_input("Amount (USD)", min_value=0.0, step=100.0)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    submit_button = st.form_submit_button("Add Project/Grant")
    
    if submit_button:
        add_grant(project_name, grant_status, amount, str(start_date), str(end_date))
        st.success(f"Added project '{project_name}' successfully!")

# Display all grants/projects
st.subheader("All Projects / Grants")
df = get_all_grants()
st.dataframe(df)
