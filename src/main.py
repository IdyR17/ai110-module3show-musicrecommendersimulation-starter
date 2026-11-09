"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Taste profile: a "late-night study" listener who wants calm, acoustic lofi
    user_prefs = {
        "favorite_genre": "lofi",   # +2.0 if the song's genre matches
        "favorite_mood": "chill",   # +1.0 if the song's mood matches
        "target_energy": 0.40,      # up to +1.5, more points the closer the song is to 0.40
        "likes_acoustic": True,     # +0.5 if the song's acousticness is 0.6 or higher
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
