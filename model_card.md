# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **TuneMatch 2.0**  

---

## 2. Intended Use  

This recommender suggests songs based on a user's preferred genre, mood, and energy level. It is designed as a classroom project to demonstrate how a simple recommendation system works, not for real-world music streaming. 

---

## 3. How the Model Works  

The system compares each song to the user's preferences. It gives points for matching the preferred genre and mood, then adds extra points based on how close the song's energy level is to the user's target. The songs with the highest scores are recommended first.
---

## 4. Data  

The dataset contains 20 songs with features including genre, mood, energy, tempo, valence, danceability, and acousticness. I expanded the starter dataset by adding 10 additional songs. The catalog is still small and does not represent every musical style. 

---

## 5. Strengths  

The recommender works well when users have clear genre and mood preferences. The recommendations generally matched my expectations during testing, and changing the scoring weights produced noticeable changes in the rankings.  

---

## 6. Limitations and Bias 

This recommender may create a filter bubble because genre receives the largest weight, so songs outside the user's preferred genre can be overlooked even when their mood and energy are similar. The system also uses a small catalog of only 20 songs, and some genres have more examples than others, which can make recommendations less balanced. Its scoring logic only considers genre, mood, and energy, even though the dataset also includes tempo, valence, danceability, and acousticness. As a result, users with more complex or changing musical tastes may receive overly narrow recommendations.
---

## 7. Evaluation  

I tested the recommender using three different user profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. For each profile, I checked whether the top recommendations matched the user's preferred genre, mood, and energy level.

The results generally matched my expectations. The High-Energy Pop profile returned upbeat pop songs, the Chill Lofi profile recommended calmer low-energy tracks, and the Deep Intense Rock profile ranked rock songs with high energy at the top. I also tested changing the scoring weights by increasing the importance of energy and reducing the importance of genre. This caused songs with similar energy levels to move higher in the rankings, showing that the recommender responds appropriately when the scoring logic changes.

One interesting observation was that songs like "Gym Hero" appeared in multiple recommendation lists because their energy level closely matched several user profiles, even when the genre was not a perfect match.

Comparing High-Energy Pop and Chill Lofi, the recommendations changed from upbeat, energetic pop songs to calmer, low-energy tracks. This makes sense because the preferred genre, mood, and target energy were very different.

Comparing High-Energy Pop and Deep Intense Rock, both profiles received high-energy songs, but the rock profile prioritized rock songs while the pop profile prioritized pop songs because genre has the highest weight in the scoring system.

Comparing Chill Lofi and Deep Intense Rock, the recommendations were almost completely different. The Chill Lofi profile favored relaxing, low-energy songs, while the Deep Intense Rock profile favored intense, high-energy rock tracks, showing that the recommender responds appropriately to different user preferences.
---

## 8. Future Work  

- Add more songs to increase variety.
- Use additional features such as tempo and danceability in the scoring.
- Support users who enjoy multiple genres instead of only one favorite.

---


## 9. Personal Reflection

### Limitations and Bias

This recommender relies on a small dataset of only 20 songs and uses fixed scoring weights. Because genre has the highest weight, the system may favor songs from a user's preferred genre even when songs from other genres have similar moods or energy levels. The recommender also ignores other available features such as tempo, danceability, valence, and acousticness, which limits how personalized the recommendations can be.

### Potential Misuse

This system could be misused if users assume the recommendations are objective or universally "best." In reality, the results depend entirely on the scoring weights and available data. To reduce misuse, the application explains why each song was recommended, displays a confidence score, and validates user input before generating recommendations.

### Reliability Reflection

One thing that surprised me during testing was how much changing the scoring weights affected the rankings. Even small adjustments caused different songs to appear near the top, showing how important it is to carefully choose and evaluate scoring rules.

### Collaboration with AI

I used AI as a programming assistant throughout this project. It was especially helpful when suggesting how to add confidence scoring and clear explanations for each recommendation, which made the output easier to understand.

One AI suggestion was incorrect because it recommended code changes that introduced indentation and formatting problems. I reviewed the code myself, tested the application, and corrected those issues before continuing. This reinforced that AI is a useful assistant, but its suggestions should always be verified through testing and debugging.
