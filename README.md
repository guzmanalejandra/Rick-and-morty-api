# 📄 README for Rick and Morty Projects

## 🚀 Features

### 🖥️ `dashboard.py`
🔎 **Character Search:** Filter characters by species, status, and gender.  
📊 **Episode Appearances:** Visualize how often characters appear in episodes.  
🌎 **Location Browser:** View location details like type and dimension.  
📺 **Episode Browser:** Explore episode names, codes, and air dates.  
🎨 **Interactive Charts:** Built with Plotly for rich visualizations.  

---

### 🗺️ `multiverse.py`
🗺️ **Interactive Map:** Displays locations with fictional coordinates.  
📍 **Marker Clusters:** Grouped markers improve map clarity.  
🧑‍🚀 **Character Popups:** Click markers to see resident characters.  
🌐 **HTML Export:** Generates an easily shareable HTML map.  

---

### 📊 `sentiment.py`
📝 **Sentiment Analysis:** Analyze simulated episode transcripts using TextBlob and VADER.  
📈 **Sentiment Visualization:** View sentiment trends across episodes with interactive charts.  
👥 **Character Presence Trends:** Discover how many characters appear per season.  
🔮 **Episode Rating Prediction:** Predict episode ratings based on character involvement using linear regression.  
📊 **Rich Visualizations:** Explore clear charts showing sentiment scores, character trends, and predicted ratings.  

---

## 🛠️ Technologies Used
- **Streamlit:** For interactive web dashboards.  
- **Folium:** Interactive maps with marker clusters.  
- **Requests:** Fetch data from the Rick and Morty API.  
- **Pandas:** Data manipulation and analysis.  
- **Plotly & Matplotlib:** Interactive and static visualizations.  
- **TextBlob & VADER:** Sentiment analysis tools.  
- **Scikit-Learn:** Machine learning for rating prediction.  

---

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd rick-and-morty-projects
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Projects

### 🖥️ **Interactive Character Dashboard**
```bash
streamlit run dashboard.py
```

### 🗺️ **Multiverse Location Map**
```bash
python multiverse.py
```
Generated map: `multiverse_map.html`  

### 📊 **Episode Analytics & Sentiment Analysis**
```bash
python sentiment.py
```

---

## 📄 Project Structure
```
rick-and-morty-projects/
├── dashboard.py                    # Interactive character dashboard
├── multiverse.py                   # Interactive location map
├── sentiment.py  # Episode analytics and sentiment analysis
└── README.md                       # Project documentation
```

---

## ❤️ Credits
Made with ❤️ using Streamlit, Folium, Plotly, and the Rick and Morty API.

---

🔗 **Happy Exploring the Multiverse!** 🌌✨
