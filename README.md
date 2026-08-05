# 🎵 Applied AI Music Recommender

## Project Summary

This project recommends songs based on a user's preferred genre, mood, and energy level. Each song is scored, ranked, and returned with an explanation and confidence score. The project also validates user input and includes automated evaluation tests to improve reliability.

---

## Original Base Project

Project 3: Music Recommender Simulation

The original project focused on building a rule-based music recommender that compared a user's preferences with song attributes and ranked songs based on similarity. Its goal was to demonstrate how recommendation systems work before adding AI-inspired features such as confidence scoring, explanations, testing, and input validation.

## Architecture Overview

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

Real recommendation systems work similarly but on a much larger scale. Instead of comparing only song attributes, services such as Spotify and YouTube also analyze user behavior including likes, skips, listening history, playlists, watch time, and interactions from millions of users. They often combine content-based filtering with collaborative filtering and machine learning models to provide more personalized recommendations. The accompanying Mermaid diagram illustrates how user input flows through validation, scoring, confidence calculation, recommendation generation, and testing.

## Project Structure

```
applied-ai-music-recommender/
│
├── src/
│   ├── main.py
│   └── recommender.py
│
├── tests/
│   ├── test_recommender.py
│   └── evaluate_system.py
│
├── data/
│   └── songs.csv
│
├── diagrams/
│   └── architecture.mmd
│
├── README.md
├── model_card.md
└── requirements.txt
```

## New AI and Reliability Features

- Confidence scoring (High, Medium, Low)
- Recommendation explanations
- Input validation
- Automated evaluation script
- Error handling


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

## Setup Instructions

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```
## How to Run the Application

3. Run the app:

```bash
py src/main.py
```

## How to Run Tests

Run the unit tests:

```bash
pytest
```

Run the evaluation script:

```bash
py -m tests.evaluate_system
```

--- 

## Sample Interactions
```

Loaded songs: 20

=== High-Energy Pop ===

=== Top Recommendations ===

1. Sunrise City
Score: 3.92
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.92) | Confidence: 98% (High)

2. Gym Hero
Score: 2.97
Because: genre match (+2.0), energy similarity (+0.97) | Confidence: 74% (Medium)

3. Tokyo Lights
Score: 1.92
Because: mood match (+1.0), energy similarity (+0.92) | Confidence: 48% (Low)

4. Rooftop Lights
Score: 1.86
Because: mood match (+1.0), energy similarity (+0.86) | Confidence: 46% (Low)

5. Storm Runner
Score: 0.99
Because: energy similarity (+0.99) | Confidence: 25% (Low)

=== Chill Lofi ===

=== Top Recommendations ===

1. Library Rain
Score: 3.95
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.95) | Confidence: 99% (High)

2. Midnight Coding
Score: 3.88
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.88) | Confidence: 97% (High)

3. Focus Flow
Score: 2.90
Because: genre match (+2.0), energy similarity (+0.90) | Confidence: 72% (Medium)

4. Spacewalk Thoughts
Score: 1.98
Because: mood match (+1.0), energy similarity (+0.98) | Confidence: 50% (Medium)

5. Deep Waters
Score: 0.99
Because: energy similarity (+0.99) | Confidence: 25% (Low)

=== Deep Intense Rock ===

=== Top Recommendations ===

1. Storm Runner
Score: 3.99
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.99) | Confidence: 100% (High)

2. Broken Promises
Score: 2.84
Because: genre match (+2.0), energy similarity (+0.84) | Confidence: 71% (Medium)

3. Gym Hero
Score: 1.97
Because: mood match (+1.0), energy similarity (+0.97) | Confidence: 49% (Low)

4. Fire Within
Score: 1.91
Because: mood match (+1.0), energy similarity (+0.91) | Confidence: 48% (Low)

5. Electric Pulse
Score: 0.94
Because: energy similarity (+0.94) | Confidence: 24% (Low)
```

## Guardrail Examples
```
Blank Genre

**Input**

```
{
    "genre": "",
    "mood": "happy",
    "energy": 0.8
}
```

**Output**

```Loaded songs: 20

=== Blank Genre ===

Unable to generate recommendations.
- Genre cannot be blank.

```

---


```
Invalid Energy

**Input**

```
{
    "genre": "pop",
    "mood": "happy",
    "energy": 1.7
}
```


**Output**

---
```
Loaded songs: 20

=== Invalid Energy ===

Unable to generate recommendations.
- Energy must be between 0.0 and 1.0.


```
Unknown Genre_Mood

**Input**

```
{
    "genre": "opera",
    "mood": "dramatic",
    "energy": 0.7
}
```


**Output**

```Loaded songs: 20

=== Unknown Genre_Mood ===

Unable to generate recommendations.
- Unknown genre 'opera'. Available genres: ambient, country, edm, folk, indie, indie pop, j-pop, jazz, lofi, metal, pop, reggae, rock, synthwave
- Unknown mood 'dramatic'. Available moods: chill, dreamy, energetic, focused, happy, hopeful, intense, melancholy, moody, nostalgic, peaceful, relaxed, smooth

```


---

## Testing Summary

The recommender was tested using three predefined user profiles representing different music preferences: High-Energy Pop, Chill Lofi, and Deep Intense Rock. For each profile, the evaluation script verified that the top recommendation matched the expected genre and reported the recommendation's confidence score.

All three test cases passed successfully. The recommender correctly identified the expected genre for the highest-ranked song in every case, producing confidence scores between 98% and 100%. This confirmed that the scoring algorithm, confidence calculation, and ranking logic were working as intended.

Additional guardrail tests were also performed using invalid inputs, including a blank genre, an energy value outside the valid range, and unknown genre and mood values. In each case, the application displayed clear validation errors instead of crashing, demonstrating that invalid user input is handled safely.

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
### Reliability Evaluation Summary

The recommender was evaluated using three valid user profiles and three invalid input cases. All recommendation tests produced the expected top genre, and the evaluation script reported 3 out of 3 successful recommendation tests. Invalid inputs were correctly rejected with descriptive error messages instead of causing the application to fail. Confidence scores were also generated for every recommendation, providing an estimate of how strongly the system matched each user's preferences.

| Test Input                         | Evaluation Criteria                | Result |
| ---------------------------------- | ---------------------------------- | ------ |
| High-Energy Pop profile            | Top recommendation should be Pop   | ✅ Pass |
| Chill Lofi profile                 | Top recommendation should be Lofi  | ✅ Pass |
| Deep Intense Rock profile          | Top recommendation should be Rock  | ✅ Pass |
| Blank genre                        | Input validation displays an error | ✅ Pass |
| Energy = 1.7                       | Reject invalid energy value        | ✅ Pass |
| Genre = "opera", Mood = "dramatic" | Unknown values reported to user    | ✅ Pass |


## Design Decisions

During testing, I increased the weight of the energy feature and reduced the weight of the genre feature. After rerunning the recommender, songs with energy levels closer to the user's preference ranked higher, even if they were from a different genre. This demonstrated that changing feature weights has a noticeable impact on the final recommendations and confirmed that the scoring system responds as expected. Genre was weighted highest because it usually has the strongest impact on user preference, while energy similarity provides finer ranking among songs with similar characteristics.

---

## Limitations

This recommender only uses a small catalog of 20 songs, so its recommendations are limited. It also relies on only a few song features and does not consider listening history, lyrics, popularity, or recommendations from similar users. Because genre has a relatively high weight, songs from the preferred genre may be ranked above songs that are otherwise very similar.

---

## Future Improvements

- Expand the song catalog
- Learn user preferences automatically
- Use machine learning for ranking
- Add Spotify integration
- Support larger music datasets
- Use collaborative filtering

## Reflection

Building this project helped me understand how recommendation systems convert user preferences into numerical scores and use those scores to rank results. I learned that even a simple scoring algorithm can produce recommendations that feel useful when the chosen features and weights make sense.

I also learned that recommendation systems can introduce bias depending on how features are weighted and what data is available. Testing different user profiles and adjusting the scoring weights showed how small changes in the algorithm can produce different recommendations, highlighting the importance of evaluating and improving AI systems over time.






