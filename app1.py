import streamlit as st
import pandas as pd
import os

# File name
file = "data.csv"

st.set_page_config(page_title="Job Dashboard", layout="wide")

# Custom CSS (UI Styling)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🚀 Job Seeker Details Dashboard")

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Add Candidate", "View Candidates", "Update Candidate", "Delete Candidate"])

# Load data function
def load_data():
    if os.path.exists(file):
        return pd.read_csv(file)
    else:
        return pd.DataFrame(columns=["Name", "Email", "Skills", "Experience"])

# Save data function
def save_data(data):
    data.to_csv(file, index=False)

# ===================== ADD =====================
if menu == "Add Candidate":
    st.subheader("📝 Add Candidate")

    name = st.text_input("Name")
    email = st.text_input("Email")
    skills = st.text_input("Skills")
    experience = st.number_input("Experience", 0, 50)

    if st.button("Add"):
        data = load_data()
        new_row = pd.DataFrame([[name, email, skills, experience]],
                               columns=data.columns)
        data = pd.concat([data, new_row], ignore_index=True)
        save_data(data)
        st.success("✅ Candidate Added!")

# ===================== VIEW =====================
elif menu == "View Candidates":
    st.subheader("📊 Candidates List")

    data = load_data()

    if not data.empty:
        st.dataframe(data)

        # Search
        st.subheader("🔍 Search")
        name_search = st.text_input("Search by Name")
        email_search = st.text_input("Search by Email")
        skill_search = st.text_input("Search by Skill")

        filtered = data.copy()

        if name_search:
            filtered = filtered[filtered["Name"].str.contains(name_search, case=False)]
        if email_search:
            filtered = filtered[filtered["Email"].str.contains(email_search, case=False)]
        if skill_search:
            filtered = filtered[filtered["Skills"].str.contains(skill_search, case=False)]

        st.dataframe(filtered)

        # Download button
        csv = filtered.to_csv(index=False).encode('utf-8')
        st.download_button("⬇ Download CSV", csv, "filtered_data.csv", "text/csv")

    else:
        st.warning("No data available")

# ===================== UPDATE =====================
elif menu == "Update Candidate":
    st.subheader("✏ Update Candidate")

    data = load_data()

    if not data.empty:
        selected_email = st.selectbox("Select Candidate (by Email)", data["Email"])

        candidate = data[data["Email"] == selected_email].iloc[0]

        name = st.text_input("Name", candidate["Name"])
        skills = st.text_input("Skills", candidate["Skills"])
        experience = st.number_input("Experience", 0, 50, int(candidate["Experience"]))

        if st.button("Update"):
            data.loc[data["Email"] == selected_email, ["Name", "Skills", "Experience"]] = [name, skills, experience]
            save_data(data)
            st.success("✅ Updated Successfully")
    else:
        st.warning("No data available")

# ===================== DELETE =====================
elif menu == "Delete Candidate":
    st.subheader("🗑 Delete Candidate")

    data = load_data()

    if not data.empty:
        selected_email = st.selectbox("Select Candidate (by Email)", data["Email"])

        if st.button("Delete"):
            data = data[data["Email"] != selected_email]
            save_data(data)
            st.success("✅ Deleted Successfully")
    else:
        st.warning("No data available")
