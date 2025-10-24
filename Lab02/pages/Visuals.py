# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

csv_file = 'Lab02/data.csv'
if os.path.exists(csv_file):
    df_csv = pd.read_csv(csv_file)
else:
    st.error("CSV file not found.")
json_file = 'data.json'
if os.path.exists(json_file):
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    df_json = pd.DataFrame(json_data['data_points'])
else:
    st.error("JSON file not found.")
st.info("TODO: Add your data loading logic here.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Hours you spent on Each School Subject")
st.write("The bar chart shows how many hours you spent studying each subject based on CSV data.")
st.bar_chart(df_csv.set_index("Category"))
st.warning("Placeholder for your first graph.")


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Select a Day")
st.write("The graph shows how many hours you studied on different days based on JSON data.")
selected_day = st.selectbox("Choose a day to use:", df_json["label"])
if "selected_day" not in st.session_state:
    st.session_state["selected_day"] = selected_day  
st.session_state["selected_day"] = selected_day  
st.line_chart(df_json.set_index("label"))
st.write(f"You selected: **{st.session_state['selected_day']}**")
st.warning("Placeholder for your second graph.")


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Filtered Study Data (Dynamic)")
st.write("Use the slider to filter study sessions by hours (JSON data again).")
min_hours = st.slider("Minimum study hours", min_value=0, max_value=5, value=1)
filtered = df_json[df_json["value"] >= min_hours]
if "min_hours" not in st.session_state:
    st.session_state["min_hours"] = min_hours
st.session_state["min_hours"] = min_hours  
st.bar_chart(filtered.set_index("label"))
st.write(f"Showing days with **≥ {st.session_state['min_hours']} hours** of study.")
st.warning("Placeholder for your third graph.")
