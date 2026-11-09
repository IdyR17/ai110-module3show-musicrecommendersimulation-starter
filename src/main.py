"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


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

    acoustic = "likes acoustic" if user_prefs["likes_acoustic"] else "prefers non-acoustic"
    print()
    print("=" * 60)
    print(f"  Top {len(recommendations)} recommendations")
    print(f"  Profile: {user_prefs['favorite_genre']} | {user_prefs['favorite_mood']} | "
          f"energy {user_prefs['target_energy']:.2f} | {acoustic}")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print()
        print(f"  {rank}. {song['title']} - {song['artist']}")
        print(f"     Score: {score:.2f} / 5.00")
        for reason in explanation.split(", "):
            print(f"       * {reason}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
