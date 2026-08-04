from src.recommender import (
    load_songs,
    recommend_songs,
    calculate_confidence,
)

songs = load_songs("data/songs.csv")

test_cases = [
    {
        "name": "High-Energy Pop",
        "profile": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9
        },
        "expected_top_genre": "pop"
    },
    {
        "name": "Chill Lofi",
        "profile": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3
        },
        "expected_top_genre": "lofi"
    },
    {
        "name": "Deep Intense Rock",
        "profile": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9
        },
        "expected_top_genre": "rock"
    }
]

passed = 0

for test in test_cases:

    recommendations = recommend_songs(
        test["profile"],
        songs,
        k=1
    )

    top_song, score, explanation = recommendations[0]

    confidence, _ = calculate_confidence(score)

    if top_song["genre"].lower() == test["expected_top_genre"]:
        print(f"PASS: {test['name']}")
        passed += 1
    else:
        print(f"FAIL: {test['name']}")

    print(f"Expected genre: {test['expected_top_genre']}")
    print(f"Top recommendation genre: {top_song['genre']}")
    print(f"Confidence: {confidence:.1f}%")
    print()

print(f"Evaluation summary: {passed}/{len(test_cases)} passed")