import requests
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.linear_model import LinearRegression
import numpy as np

# Function to fetch episodes from the API
def fetch_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    episodes = []

    while url:
        response = requests.get(url)
        data = response.json()
        episodes.extend(data['results'])
        url = data['info']['next']

    return pd.json_normalize(episodes)

# Function to fetch characters and their involvement in episodes
def fetch_characters():
    url = "https://rickandmortyapi.com/api/character"
    characters = []

    while url:
        response = requests.get(url)
        data = response.json()
        characters.extend(data['results'])
        url = data['info']['next']

    return pd.json_normalize(characters)

# Function to simulate transcript sentiment analysis (since transcripts aren't available via API)
def simulate_transcript_sentiment(episodes_df):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []

    for episode in episodes_df['name']:
        # Simulate transcript text (replace with real transcripts if available)
        transcript = f"This is a transcript simulation for the episode {episode}." 
        blob = TextBlob(transcript)
        vader_score = analyzer.polarity_scores(transcript)['compound']
        sentiments.append({'episode': episode, 'textblob_sentiment': blob.sentiment.polarity, 'vader_sentiment': vader_score})

    return pd.DataFrame(sentiments)

# Function to analyze character presence trends
def character_presence_trends(characters_df, episodes_df):
    presence_data = []

    for _, episode in episodes_df.iterrows():
        episode_id = episode['id']
        episode_code = episode['episode']
        character_count = len(episode['characters'])
        season = int(episode_code.split('E')[0].replace('S', ''))
        presence_data.append({'episode_id': episode_id, 'season': season, 'character_count': character_count})

    presence_df = pd.DataFrame(presence_data)
    presence_df.groupby('season')['character_count'].mean().plot(kind='bar', title='Average Character Presence per Season')
    plt.xlabel('Season')
    plt.ylabel('Average Number of Characters')
    plt.show()

# Function to predict episode ratings based on character involvement (simulated ratings)
def predict_episode_ratings(presence_df):
    presence_df['simulated_rating'] = presence_df['character_count'].apply(lambda x: 5 + (x * 0.1))
    
    X = presence_df[['character_count']]
    y = presence_df['simulated_rating']

    model = LinearRegression()
    model.fit(X, y)

    plt.scatter(presence_df['character_count'], presence_df['simulated_rating'], color='blue')
    plt.plot(presence_df['character_count'], model.predict(X), color='red')
    plt.title('Predicted Episode Ratings Based on Character Involvement')
    plt.xlabel('Character Count')
    plt.ylabel('Simulated Rating')
    plt.show()

# Main execution
if __name__ == "__main__":
    print("Fetching episode data...")
    episodes_df = fetch_episodes()

    print("Fetching character data...")
    characters_df = fetch_characters()

    print("Analyzing transcript sentiment...")
    sentiment_df = simulate_transcript_sentiment(episodes_df)
    print(sentiment_df)

    print("Analyzing character presence trends...")
    character_presence_trends(characters_df, episodes_df)

    print("Predicting episode ratings based on character involvement...")
    presence_data = [{'episode_id': ep['id'], 'character_count': len(ep['characters'])} for ep in episodes_df.to_dict('records')]
    presence_df = pd.DataFrame(presence_data)
    predict_episode_ratings(presence_df)
