🧬 Rick and Morty Multiverse Explorer
An interactive set of tools to explore characters, locations, and episodes from the Rick and Morty universe. This repository contains:

Interactive Dashboard: Built with Streamlit to visualize character appearances, search locations, and episodes.
Multiverse Map: A dynamic Folium map showcasing locations in the multiverse with character details.
📂 Project Structure
bash
Copy
Edit
├── dashboard.py          # Streamlit dashboard for interactive exploration
├── multiverse.py         # Folium map of Rick and Morty locations with fictional coordinates
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
🚀 Getting Started
Prerequisites
Ensure you have Python 3.8+ installed. You can install the required libraries using:

bash
Copy
Edit
pip install -r requirements.txt
Requirements include:

streamlit
requests
pandas
plotly
folium
geopandas
📊 Running the Dashboard
The dashboard provides interactive searches for characters, locations, and episodes.

Features:
Search Characters: Filter by species, status, and gender. Visualize character appearances across episodes.
Search Locations: View detailed location information.
Search Episodes: Explore episode details and air dates.
Run the app:
bash
Copy
Edit
streamlit run dashboard.py
Open the provided local URL in your browser to explore the dashboard.

🗺️ Generating the Multiverse Map
The multiverse.py script fetches location data from the Rick and Morty API and assigns fictional coordinates for visualization.

Features:
Interactive map with clustered location markers.
Popup information including location name, type, dimension, and residents.
Run the script:
bash
Copy
Edit
python multiverse.py
✅ The map will be saved as multiverse_map.html. Open it in your browser to explore.

🖼️ Sample Screenshots
📊 Dashboard Interface

🗺️ Multiverse Map

🛠️ API Reference
Both applications utilize the Rick and Morty API to fetch real-time data.

🤝 Contributing
Contributions are welcome! Fork the repo, make changes, and submit a pull request.

📜 License
This project is licensed under the MIT License.

❤️ Acknowledgements
Rick and Morty API for providing the data.
Streamlit and Folium for the amazing visualization libraries.
