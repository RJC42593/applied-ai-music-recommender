# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works



The recommender system uses information from both the song catalog and the user's taste profile to generate personalized recommendations.

Each `Song` stores several features including:
- Genre
- Mood
- Energy
- Tempo (BPM)
- Valence
- Danceability
- Acousticness

The `UserProfile` stores the user's preferred values for these same features.

To calculate a recommendation score, the recommender compares each song's attributes to the user's preferences. Genre and mood use exact matching, while numerical features such as energy, tempo, valence, danceability, and acousticness are scored based on how close they are to the user's preferred values. Each feature is multiplied by a weight, with genre and mood receiving the highest weights because they have the greatest influence on musical preference.

After every song receives a score, the songs are sorted from highest to lowest score. The highest-scoring songs become the recommended songs shown to the user.

Real recommendation systems work similarly but on a much larger scale. Instead of comparing only song attributes, services such as Spotify and YouTube also analyze user behavior including likes, skips, listening history, playlists, watch time, and interactions from millions of users. They often combine content-based filtering with collaborative filtering and machine learning models to provide more personalized recommendations.


### Algorithm Recipe

The recommender scores each song by comparing its features to the user's preferences.

- Genre match: +2.0 points
- Mood match: +1.0 point
- Energy: Up to +1.0 point based on similarity
- Tempo: Up to +0.5 point based on similarity
- Valence: Up to +0.5 point based on similarity
- Danceability: Up to +0.5 point based on similarity
- Acousticness: Up to +0.5 point based on similarity

For numerical features, the recommender rewards songs whose values are closest to the user's preferred values instead of simply rewarding larger or smaller numbers. After every song receives a score, the songs are sorted from highest to lowest, and the highest-scoring songs are recommended.


### Potential Biases

This recommender has several limitations. Because genre receives the highest weight, it may over-prioritize songs from the user's favorite genre while overlooking songs from other genres that have similar moods or musical characteristics. The system also assumes the user has only one set of preferences, even though people often enjoy different types of music depending on their activity or mood. In addition, the recommender only uses song attributes and does not consider listening history, lyrics, popularity, or recommendations based on other users, so its suggestions may be less personalized than those of real streaming platforms.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output
```

Loaded songs: 20

Top recommendations:

Sunrise City - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy similarity (+0.87)

Tokyo Lights - Score: 1.98
Because: mood match (+1.0), energy similarity (+0.98)

Rooftop Lights - Score: 1.96
Because: mood match (+1.0), energy similarity (+0.96)

Night Drive Loop - Score: 0.95
Because: energy similarity (+0.95)
```

## Sample Recommendation Output Phase 4 Step 1
```
Loaded songs: 20

=== High-Energy Pop ===

Sunrise City - Score: 3.92
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.92)

Gym Hero - Score: 2.97
Because: genre match (+2.0), energy similarity (+0.97)

Tokyo Lights - Score: 1.92
Because: mood match (+1.0), energy similarity (+0.92)

Rooftop Lights - Score: 1.86
Because: mood match (+1.0), energy similarity (+0.86)

Storm Runner - Score: 0.99
Because: energy similarity (+0.99)


=== Chill Lofi ===

Library Rain - Score: 2.95
Because: genre match (+2.0), energy similarity (+0.95)

Focus Flow - Score: 2.90
Because: genre match (+2.0), energy similarity (+0.90)

Midnight Coding - Score: 2.88
Because: genre match (+2.0), energy similarity (+0.88)

Deep Waters - Score: 0.99
Because: energy similarity (+0.99)

Spacewalk Thoughts - Score: 0.98
Because: energy similarity (+0.98)


=== Deep Intense Rock ===

Storm Runner - Score: 3.99
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.99)

Broken Promises - Score: 2.84
Because: genre match (+2.0), energy similarity (+0.84)

Gym Hero - Score: 1.97
Because: mood match (+1.0), energy similarity (+0.97)

Fire Within - Score: 1.91
Because: mood match (+1.0), energy similarity (+0.91)

Electric Pulse - Score: 0.94
Because: energy similarity (+0.94)



---

## Evaluation Results

```
Loaded songs: 20
PASS: High-Energy Pop
Expected genre: pop
Top recommendation genre: pop
Confidence: 98.0%

PASS: Chill Lofi
Expected genre: lofi
Top recommendation genre: lofi
Confidence: 99.0%

PASS: Deep Intense Rock
Expected genre: rock
Top recommendation genre: rock
Confidence: 100.0%

Evaluation summary: 3/3 passed
```

## Experiments You Tried

During testing, I increased the weight of the energy feature and reduced the weight of the genre feature. After rerunning the recommender, songs with energy levels closer to the user's preference ranked higher, even if they were from a different genre. This demonstrated that changing feature weights has a noticeable impact on the final recommendations and confirmed that the scoring system responds as expected.

---

## Limitations and Risks

This recommender only uses a small catalog of 20 songs, so its recommendations are limited. It also relies on only a few song features and does not consider listening history, lyrics, popularity, or recommendations from similar users. Because genre has a relatively high weight, songs from the preferred genre may be ranked above songs that are otherwise very similar.

---

## Reflection

Building this project helped me understand how recommendation systems convert user preferences into numerical scores and use those scores to rank results. I learned that even a simple scoring algorithm can produce recommendations that feel useful when the chosen features and weights make sense.

I also learned that recommendation systems can introduce bias depending on how features are weighted and what data is available. Testing different user profiles and adjusting the scoring weights showed how small changes in the algorithm can produce different recommendations, highlighting the importance of evaluating and improving AI systems over time.



