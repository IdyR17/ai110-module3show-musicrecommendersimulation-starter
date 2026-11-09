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

Apps like Spotify and TikTok mix two ideas. One looks at what people with similar taste listen to (collaborative filtering). The other looks at what a song actually sounds like (content-based filtering). They learn from things like likes, skips, replays, and playlists, then rank the best options for you. My version is much simpler. It only uses content-based filtering. It compares each song to what the user says they like and gives it a score. It cares most about genre, then mood, then how close the song's energy is to what the user wants.

**Song features I use:**

- `genre`: the type of music (pop, lofi, rock...)
- `mood`: how it feels (happy, chill, intense...)
- `energy`: how calm or intense it is, from 0 to 1
- `acousticness`: how acoustic it is, from 0 to 1

I skip `tempo_bpm` and `danceability` because in this dataset they basically go up and down with energy, so they would just repeat it.

**UserProfile features I use:**

- `favorite_genre`
- `favorite_mood`
- `target_energy`: the energy level they want, from 0 to 1
- `likes_acoustic`: true or false

**Algorithm Recipe:**

```
INPUT     User prefs + 20 songs from songs.csv
   ↓
PROCESS   Score every song:
            Genre matches?     +2.0
            Mood matches?      +1.0
            Energy close?      up to +1.5 (the closer, the more points)
            Acoustic fits?     +0.5
   ↓
OUTPUT    Sort by score → show the top 5
```

**Biases I expect:**

- **Genre wins too much.** A great song with the right mood and energy can lose to an average song that just has the right genre.
- **Exact matches only.** "Chill" and "relaxed" count as different moods, so close songs get no credit.
- **Small genres lose out.** Most genres have only one song, so fans of those genres get fewer good matches.
- **It only knows what the user tells it.** It doesn't learn from likes or skips, so it never finds anything surprising.

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

Output from `python -m src.main`:

```
Loaded 20 songs from data/songs.csv

============================================================
  Top 5 recommendations
  Profile: lofi | chill | energy 0.40 | likes acoustic
============================================================

  1. Midnight Coding - LoRoom
     Score: 4.99 / 5.00
       * genre matches (lofi) +2.0
       * mood matches (chill) +1.0
       * energy 0.42 vs target 0.40 +1.49
       * acoustic sound +0.5

  2. Library Rain - Paper Lanterns
     Score: 4.92 / 5.00
       * genre matches (lofi) +2.0
       * mood matches (chill) +1.0
       * energy 0.35 vs target 0.40 +1.42
       * acoustic sound +0.5

  3. Focus Flow - LoRoom
     Score: 4.00 / 5.00
       * genre matches (lofi) +2.0
       * energy 0.40 vs target 0.40 +1.50
       * acoustic sound +0.5

  4. Spacewalk Thoughts - Orbit Bloom
     Score: 2.59 / 5.00
       * mood matches (chill) +1.0
       * energy 0.28 vs target 0.40 +1.09
       * acoustic sound +0.5

  5. Coffee Shop Stories - Slow Stereo
     Score: 1.97 / 5.00
       * energy 0.37 vs target 0.40 +1.47
       * acoustic sound +0.5

============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

### Weight shift: half the genre, double the energy

**What I changed:** Genre went from 2.0 to 1.0 points, and energy went from 1.5 to 3.0 points. The max score went from 5.0 to 5.5.

**Did the math still work?** Yes. Every score stayed between 0 and 5.5, and the reasons for each song still added up to its score.

**What happened:** 5 of my 7 profiles kept the same top 5. Only 2 changed:

| Profile | Before | After |
|---|---|---|
| Sad + high energy | #1 was Empty Platform, the only blues/sad song | Empty Platform dropped out of the top 5. All 5 songs were just loud songs |
| Calm acoustic metal fan | #2 was Iron Requiem, a loud metal song | Iron Requiem dropped out. All 5 were calm, acoustic songs |

For High-Energy Pop, Rooftop Lights (happy "indie pop") got much closer to Gym Hero, from 1.05 points behind to only 0.09 behind.

**More accurate or just different?** Just different. The metal fan's list got better, but the sad listener lost the only sad song. With energy worth so much, the system mostly ranks by loudness. It still put a dark rock song in the happy pop fan's top 5. So I went back to genre 2.0 and energy 1.5.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



