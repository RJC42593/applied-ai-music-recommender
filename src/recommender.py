import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
     

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"
    

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    """
    songs = []

    with open(csv_path, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    print(f"Loaded songs: {len(songs)}")
    return songs


def validate_user_preferences(
    user_prefs: Dict,
    songs: List[Dict]
) -> Tuple[bool, List[str]]:
    """Validate user preferences before generating recommendations."""
    errors = []

    required_fields = ["genre", "mood", "energy"]

    for field in required_fields:
        if field not in user_prefs:
            errors.append(f"Missing required preference: {field}")

    if errors:
        return False, errors

    genre = str(user_prefs["genre"]).strip().lower()
    mood = str(user_prefs["mood"]).strip().lower()

    if not genre:
        errors.append("Genre cannot be blank.")

    if not mood:
        errors.append("Mood cannot be blank.")

    try:
        energy = float(user_prefs["energy"])
    except (TypeError, ValueError):
        errors.append("Energy must be a number between 0.0 and 1.0.")
        return False, errors

    if not 0.0 <= energy <= 1.0:
        errors.append("Energy must be between 0.0 and 1.0.")

    available_genres = {
        str(song["genre"]).strip().lower()
        for song in songs
    }
    available_moods = {
        str(song["mood"]).strip().lower()
        for song in songs
    }

    if genre and genre not in available_genres:
        errors.append(
            f"Unknown genre '{user_prefs['genre']}'. "
            f"Available genres: {', '.join(sorted(available_genres))}"
        )

    if mood and mood not in available_moods:
        errors.append(
            f"Unknown mood '{user_prefs['mood']}'. "
            f"Available moods: {', '.join(sorted(available_moods))}"
        )

    return len(errors) == 0, errors


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Calculate a recommendation score and explain the result.
    """
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_difference = abs(song["energy"] - user_prefs["energy"])
    energy_similarity = max(0.0, 1.0 - energy_difference)

    score += energy_similarity
    reasons.append(f"energy similarity (+{energy_similarity:.2f})")

    return score, reasons


def calculate_confidence(score: float,
                         max_score: float = 4.0) -> Tuple[float, str]:
    """Convert a recommendation score into a confidence percentage."""

    percentage = round(
        max(0.0, min(score / max_score, 1.0)) * 100
    )

    if percentage >= 80:
        label = "High"
    elif percentage >= 50:
        label = "Medium"
    else:
        label = "Low"

    return percentage, label


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Return the top k ranked song recommendations.
    """
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        confidence, label = calculate_confidence(score)

        explanation = (
            f"{', '.join(reasons)} | "
            f"Confidence: {confidence:.0f}% ({label})"
        )

        recommendations.append((song, score, explanation))

    recommendations.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return recommendations[:k]