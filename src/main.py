"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs, MAX_SCORE


# Three main taste profiles
PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.85,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.40,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.90,
        "likes_acoustic": False,
    },
}

# Edge-case profiles that try to trick the scoring
EDGE_CASE_PROFILES = {
    "Conflicting: high energy + sad mood": {
        "favorite_genre": "blues",
        "favorite_mood": "sad",
        "target_energy": 0.90,
        "likes_acoustic": False,
    },
    "Capitalized input (Pop / Happy)": {
        "favorite_genre": "Pop",
        "favorite_mood": "Happy",
        "target_energy": 0.85,
        "likes_acoustic": False,
    },
    "Genre fights everything else (calm, acoustic metal fan)": {
        "favorite_genre": "metal",
        "favorite_mood": "peaceful",
        "target_energy": 0.20,
        "likes_acoustic": True,
    },
    "Energy out of range (1.5)": {
        "favorite_genre": "edm",
        "favorite_mood": "euphoric",
        "target_energy": 1.50,
        "likes_acoustic": False,
    },
}


def print_recommendations(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print the top k recommendations for one profile with scores and reasons."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    acoustic = "likes acoustic" if user_prefs["likes_acoustic"] else "prefers non-acoustic"
    print()
    print("=" * 60)
    print(f"  {name}: top {len(recommendations)} recommendations")
    print(f"  Profile: {user_prefs['favorite_genre']} | {user_prefs['favorite_mood']} | "
          f"energy {user_prefs['target_energy']:.2f} | {acoustic}")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print()
        print(f"  {rank}. {song['title']} - {song['artist']}")
        print(f"     Score: {score:.2f} / {MAX_SCORE:.2f}")
        for reason in explanation.split(", "):
            print(f"       * {reason}")

    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    for name, user_prefs in {**PROFILES, **EDGE_CASE_PROFILES}.items():
        print_recommendations(name, user_prefs, songs)


if __name__ == "__main__":
    main()
