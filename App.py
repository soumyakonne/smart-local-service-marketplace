import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Smart Local Service Marketplace", layout="wide")

# --- Custom Background CSS ---
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.bing.com/images/search?view=detailV2&ccid=0oA5G%2brZ&id=CF99EEFA7AC866ABAC3676488C22F2BDBE534AFB&thid=OIP.0oA5G-rZUyvqvQLpiF9MQAAAAA&mediaurl=https%3a%2f%2fmir-s3-cdn-cf.behance.net%2fprojects%2f404%2f4099f038827113.Y3JvcCw5MDcsNzA4LDAsMA.png&exph=316&expw=404&q=smart+local+service+marketplace+background+photos+in+black+color&FORM=IRPRST&ck=71F5D816E1676C7216B574E0EF931C2B&selectedIndex=0&itb=0");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.8);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Sample Data ---
data = {
    "Service": ["Plumber", "Electrician", "Tutor", "Cleaner", "Mechanic"],
    "Provider": ["Ravi Kumar", "Anita Sharma", "John Doe", "Meena Devi", "Arjun Singh"],
    "Location": ["Hyderabad", "kompally", "Secunderabad", "maisammaguda", "Secunderabad"],
    "Price": [500, 600, 400, 300, 700],
    "Rating": [4.5, 4.2, 4.8, 4.0, 4.6]
}
df = pd.DataFrame(data)

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Services")
service_filter = st.sidebar.selectbox("Choose Service", ["All"] + df["Service"].unique().tolist())
location_filter = st.sidebar.selectbox("Choose Location", ["All"] + df["Location"].unique().tolist())

# --- Apply Filters ---
filtered_df = df.copy()
if service_filter != "All":
    filtered_df = filtered_df[filtered_df["Service"] == service_filter]
if location_filter != "All":
    filtered_df = filtered_df[filtered_df["Location"] == location_filter]

# --- Display Marketplace ---
st.title("🛠️ Smart Local Service Marketplace")
st.write("Find and book trusted local service providers instantly.")

st.dataframe(filtered_df, use_container_width=True)

# --- Booking Section ---
st.subheader("📅 Book a Service")
selected_provider = st.selectbox("Select Provider", filtered_df["Provider"].tolist())
booking_date = st.date_input("Choose Date")
booking_time = st.time_input("Choose Time")

if st.button("Confirm Booking"):
    st.success(f"✅ Booking confirmed with {selected_provider} on {booking_date} at {booking_time}!")

