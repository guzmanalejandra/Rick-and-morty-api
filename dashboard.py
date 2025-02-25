import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Function to fetch data from Rick and Morty API
def fetch_data(endpoint):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    all_data = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            all_data.extend(data['results'])
            url = data['info']['next']
        else:
            break

    return pd.json_normalize(all_data)

# Function to visualize character appearances
def plot_character_appearances(characters_df, selected_character):
    episodes = characters_df.loc[characters_df['name'] == selected_character, 'episode'].values
    if len(episodes) == 0:
        st.warning("No episode data found for this character.")
        return

    episode_numbers = [int(ep.split('/')[-1]) for ep in episodes[0]]
    fig = px.bar(
        x=episode_numbers,
        y=[1] * len(episode_numbers),
        labels={'x': 'Episode', 'y': 'Appearance'},
        title=f"{selected_character}'s Episode Appearances"
    )
    st.plotly_chart(fig)

# Streamlit app setup
st.title("🧬 Rick and Morty Interactive Character Dashboard")

# Sidebar for navigation
option = st.sidebar.selectbox("Choose an option", ["Search Characters", "Search Locations", "Search Episodes"])

# Search Characters Section
if option == "Search Characters":
    st.header("🔍 Search Characters")
    characters_df = fetch_data("character")

    if characters_df.empty:
        st.error("Failed to fetch character data.")
    else:
        species_options = characters_df['species'].dropna().unique().tolist()
        status_options = characters_df['status'].dropna().unique().tolist()
        gender_options = characters_df['gender'].dropna().unique().tolist()

        species_filter = st.multiselect("Filter by Species", species_options)
        status_filter = st.multiselect("Filter by Status", status_options)
        gender_filter = st.multiselect("Filter by Gender", gender_options)

        # Safely apply filters
        species_condition = characters_df['species'].isin(species_filter) if species_filter else pd.Series(True, index=characters_df.index)
        status_condition = characters_df['status'].isin(status_filter) if status_filter else pd.Series(True, index=characters_df.index)
        gender_condition = characters_df['gender'].isin(gender_filter) if gender_filter else pd.Series(True, index=characters_df.index)

        filtered_df = characters_df[species_condition & status_condition & gender_condition]

        st.dataframe(filtered_df[['name', 'species', 'status', 'gender']])

        selected_character = st.selectbox("Select a character to view episode appearances", filtered_df['name'].tolist())
        if selected_character:
            plot_character_appearances(filtered_df, selected_character)

# Search Locations Section
elif option == "Search Locations":
    st.header("🌎 Search Locations")
    locations_df = fetch_data("location")
    if locations_df.empty:
        st.error("Failed to fetch location data.")
    else:
        st.dataframe(locations_df[['name', 'type', 'dimension']])

# Search Episodes Section
elif option == "Search Episodes":
    st.header("📺 Search Episodes")
    episodes_df = fetch_data("episode")
    if episodes_df.empty:
        st.error("Failed to fetch episode data.")
    else:
        st.dataframe(episodes_df[['name', 'episode', 'air_date']])

st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ using Streamlit and Rick and Morty API")