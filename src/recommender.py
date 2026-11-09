import csv
import math
from typing import List, Dict, Tuple, Optional
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
    Required by src/main.py
    """
    float_fields = ["energy", "tempo_bpm", "valence", "danceability", "acousticness"]

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)

    print(f"Loaded {len(songs)} songs from {csv_path}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Genre match: +2.0
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append(f"genre matches ({song['genre']}) +2.0")

    # Mood match: +1.0
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append(f"mood matches ({song['mood']}) +1.0")

    # Energy closeness: up to +1.5 (the closer to the target, the more points)
    distance = song["energy"] - user_prefs["target_energy"]
    energy_points = 1.5 * math.exp(-(distance ** 2) / (2 * 0.15 ** 2))
    score += energy_points
    reasons.append(f"energy {song['energy']:.2f} vs target {user_prefs['target_energy']:.2f} +{energy_points:.2f}")

    # Acoustic fit: +0.5
    if user_prefs["likes_acoustic"] and song["acousticness"] >= 0.6:
        score += 0.5
        reasons.append("acoustic sound +0.5")
    elif not user_prefs["likes_acoustic"] and song["acousticness"] < 0.4:
        score += 0.5
        reasons.append("non-acoustic sound +0.5")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
