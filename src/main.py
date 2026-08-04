"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import (
    load_songs,
    recommend_songs,
    validate_user_preferences,
)


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        {
            "name": "High-Energy Pop",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9
        },
        {
            "name": "Chill Lofi",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3
        },
        {
            "name": "Deep Intense Rock",
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9
        }
    ]

    for user_prefs in profiles:
        print(f"\n=== {user_prefs['name']} ===\n")

        is_valid, errors = validate_user_preferences(
            user_prefs,
            songs
        )

        if not is_valid:
            print("Unable to generate recommendations.")
            for error in errors:
                print(f"- {error}")
            continue

        recommendations = recommend_songs(
            user_prefs,
            songs,
            k=5
        )

        print("=== Top Recommendations ===")

        for index, (song, score, explanation) in enumerate(
            recommendations,
            start=1
        ):
            print(f"\n{index}. {song['title']}")
            print(f"Score: {score:.2f}")
            print(f"Because: {explanation}")


if __name__ == "__main__":
    main()            
    