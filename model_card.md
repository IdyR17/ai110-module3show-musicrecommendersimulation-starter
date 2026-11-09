# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**TuneJudge 1.0**: it judges every song and gives it points.

---

## 2. Intended Use  

**Goal:** TuneJudge suggests 5 songs a person will probably like. It uses what they tell it: favorite genre, favorite mood, how much energy they want, and if they like acoustic music.

**What it's for:**

- Learning how music apps like Spotify turn data into suggestions
- Classroom practice and experiments with a small, made-up song list
- Showing *why* a song was picked, with a list of reasons

**What it's NOT for:**

- Real users or a real music app. It only knows 20 songs.
- Learning someone's taste over time. It doesn't use likes, skips, or listening history.
- Judging if a song or artist is "good". A low score just means it doesn't match one person's settings.

**It assumes** the user knows their favorite genre and mood, and that one of each is enough to describe their taste.

---

## 3. How the Model Works  

My recommender works like a judge giving points. The user tells it what they like: a favorite genre, a favorite mood, how much energy they want (from calm to intense), and whether they like acoustic music.

Then it looks at every song, one at a time, and gives it points:

- **Same genre as the user likes:** 2 points. This counts the most because genre is usually the biggest part of someone's taste.
- **Same mood:** 1 point.
- **Energy close to what the user wants:** up to 1.5 points. A song with exactly the right energy gets all 1.5. The further away it is, the fewer points it gets, and a song that is way off gets almost nothing. So it doesn't reward songs just for being loud or quiet, only for being *close* to what the user asked for.
- **Acoustic sound matches:** 0.5 points.

The best possible score is 5. After every song has a score, it sorts them from highest to lowest and shows the top 5. Each song also comes with a list of reasons, so you can see exactly why it was picked.

**Changes from the starter:** the starter just returned the first few songs in the file. I added the point system, the "closer is better" rule for energy, the reasons list, and 10 more songs with new genres and moods. It also ignores capital letters, so "Pop" and "pop" count as the same. I left out tempo and danceability because in this data they go up and down with energy, so they would just count the same thing twice.

---

## 4. Data  

**Size:** 20 songs in `data/songs.csv`. The starter had 10, and I added 10 more.

**What each song has:** title, artist, genre, mood, and 5 numbers: energy, tempo, valence (how happy it sounds), danceability, and acousticness. My scoring only uses genre, mood, energy, and acousticness.

**Variety:** 17 genres and 16 moods. The songs I added brought in genres like hip-hop, country, classical, metal, and latin, and moods like sad, angry, and romantic.

**Limits:**

- 13 of the 17 genres have only 1 song. Lofi has the most, with 3.
- Half the songs are high energy (0.7 or more).
- Only 3 songs sound sad.
- No song is both calm and electronic.
- The songs and their numbers are made up, not from a real music service.

---

## 5. Strengths  

- **Clear tastes work great.** High-Energy Pop, Chill Lofi, and Deep Intense Rock all got the song I expected at #1.
- **Opposite users get opposite lists.** Pop and Lofi had zero songs in common, which is right.
- **"Closer is better" works for energy.** A calm listener doesn't get loud songs just because they score high on a number.
- **It explains itself.** Every song comes with reasons and points, so it's easy to see why it was picked.
- **It doesn't break on unknown genres.** If nothing matches the genre, mood and energy still give a sensible list.

---

## 6. Limitations and Bias 

My system has a "loud song" bubble. Gym Hero, Fiesta de Noche, and Storm Runner showed up in the top 5 for 5 out of my 7 test profiles. This happens because most genres only have one song, so once the genre match runs out, energy decides the rest, and half of my songs are high energy. It also doesn't use valence, so it can't tell a happy loud song from an angry one, which is how a dark rock song ended up in a happy pop fan's list.

---

## 7. Evaluation  

**How I tested:** I made 7 user profiles: 3 normal ones and 4 tricky ones. I ran `python -m src.main` to get the top 5 for each, checked if the results felt right, and compared profiles side by side. I also ran one experiment where I changed the weights (see "Experiments You Tried" in the README).

**Profiles I tested:**

| Profile | Genre | Mood | Energy | Acoustic? | What it tests |
|---|---|---|---|---|---|
| High-Energy Pop | pop | happy | 0.85 | no | A normal, upbeat listener |
| Chill Lofi | lofi | chill | 0.40 | yes | A normal, calm listener |
| Deep Intense Rock | rock | intense | 0.90 | no | A normal, loud listener with only 1 matching song |
| Sad + high energy | blues | sad | 0.90 | no | Preferences that fight each other |
| Capitalized (Pop / Happy) | Pop | Happy | 0.85 | no | Does typing style matter? |
| Calm acoustic metal fan | metal | peaceful | 0.20 | yes | Genre vs. everything else |
| Energy out of range | edm | euphoric | 1.50 | no | A number that's too big |

The output below is from my original weights (genre 2.0, mood 1.0, energy 1.5, acoustic 0.5).

### Main profiles

**High-Energy Pop:** Works as expected. Sunrise City (pop, happy, right energy) wins. Gym Hero is 2nd because it's pop, even though its mood is "intense".

```
============================================================
  High-Energy Pop: top 5 recommendations
  Profile: pop | happy | energy 0.85 | prefers non-acoustic
============================================================

  1. Sunrise City - Neon Echo
     Score: 4.97 / 5.00
       * genre matches (pop) +2.0
       * mood matches (happy) +1.0
       * energy 0.82 vs target 0.85 +1.47
       * non-acoustic sound +0.5

  2. Gym Hero - Max Pulse
     Score: 3.80 / 5.00
       * genre matches (pop) +2.0
       * energy 0.93 vs target 0.85 +1.30
       * non-acoustic sound +0.5

  3. Rooftop Lights - Indigo Parade
     Score: 2.75 / 5.00
       * mood matches (happy) +1.0
       * energy 0.76 vs target 0.85 +1.25
       * non-acoustic sound +0.5

  4. Fiesta de Noche - Los Brillantes
     Score: 2.00 / 5.00
       * energy 0.84 vs target 0.85 +1.50
       * non-acoustic sound +0.5

  5. Storm Runner - Voltline
     Score: 1.88 / 5.00
       * energy 0.91 vs target 0.85 +1.38
       * non-acoustic sound +0.5
```

**Chill Lofi:** Works as expected. All 3 lofi songs are on top, followed by other calm, acoustic songs.

```
============================================================
  Chill Lofi: top 5 recommendations
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
```

**Deep Intense Rock:** Storm Runner gets a perfect 5.00. But it's the only rock song, so spots 3 to 5 are just "whatever is loud", including a happy latin song.

```
============================================================
  Deep Intense Rock: top 5 recommendations
  Profile: rock | intense | energy 0.90 | prefers non-acoustic
============================================================

  1. Storm Runner - Voltline
     Score: 5.00 / 5.00
       * genre matches (rock) +2.0
       * mood matches (intense) +1.0
       * energy 0.91 vs target 0.90 +1.50
       * non-acoustic sound +0.5

  2. Gym Hero - Max Pulse
     Score: 2.97 / 5.00
       * mood matches (intense) +1.0
       * energy 0.93 vs target 0.90 +1.47
       * non-acoustic sound +0.5

  3. Afterglow Rush - Pulsewave
     Score: 1.92 / 5.00
       * energy 0.95 vs target 0.90 +1.42
       * non-acoustic sound +0.5

  4. Fiesta de Noche - Los Brillantes
     Score: 1.88 / 5.00
       * energy 0.84 vs target 0.90 +1.38
       * non-acoustic sound +0.5

  5. Iron Requiem - Grave Signal
     Score: 1.85 / 5.00
       * energy 0.97 vs target 0.90 +1.35
       * non-acoustic sound +0.5
```

### Edge-case profiles

**Conflicting: high energy + sad mood:** The only sad song wins with 0 energy points, then the list jumps to loud, happy songs. No song is both sad and intense, so it can't satisfy both.

```
============================================================
  Conflicting: high energy + sad mood: top 5 recommendations
  Profile: blues | sad | energy 0.90 | prefers non-acoustic
============================================================

  1. Empty Platform - The Grey Hours
     Score: 3.00 / 5.00
       * genre matches (blues) +2.0
       * mood matches (sad) +1.0
       * energy 0.30 vs target 0.90 +0.00

  2. Storm Runner - Voltline
     Score: 2.00 / 5.00
       * energy 0.91 vs target 0.90 +1.50
       * non-acoustic sound +0.5

  3. Gym Hero - Max Pulse
     Score: 1.97 / 5.00
       * energy 0.93 vs target 0.90 +1.47
       * non-acoustic sound +0.5

  4. Afterglow Rush - Pulsewave
     Score: 1.92 / 5.00
       * energy 0.95 vs target 0.90 +1.42
       * non-acoustic sound +0.5

  5. Fiesta de Noche - Los Brillantes
     Score: 1.88 / 5.00
       * energy 0.84 vs target 0.90 +1.38
       * non-acoustic sound +0.5
```

**Capitalized input (Pop / Happy):** A bug! It's the same as High-Energy Pop, just with capital letters. "Pop" doesn't equal "pop", so genre and mood never match. Sunrise City drops from #1 (4.97) to #2 (1.97), behind a latin song. **Fixed:** the code now ignores capital letters, and this profile now gives the exact same list as High-Energy Pop. The output below is from before the fix.

```
============================================================
  Capitalized input (Pop / Happy): top 5 recommendations
  Profile: Pop | Happy | energy 0.85 | prefers non-acoustic
============================================================

  1. Fiesta de Noche - Los Brillantes
     Score: 2.00 / 5.00
       * energy 0.84 vs target 0.85 +1.50
       * non-acoustic sound +0.5

  2. Sunrise City - Neon Echo
     Score: 1.97 / 5.00
       * energy 0.82 vs target 0.85 +1.47
       * non-acoustic sound +0.5

  3. Storm Runner - Voltline
     Score: 1.88 / 5.00
       * energy 0.91 vs target 0.85 +1.38
       * non-acoustic sound +0.5

  4. Concrete Crown - Rhyme Theory
     Score: 1.85 / 5.00
       * energy 0.78 vs target 0.85 +1.35
       * non-acoustic sound +0.5

  5. Gym Hero - Max Pulse
     Score: 1.80 / 5.00
       * energy 0.93 vs target 0.85 +1.30
       * non-acoustic sound +0.5
```

**Genre fights everything else (calm, acoustic metal fan):** Mood + energy + acoustic (3.0) beat genre (2.0), so a calm classical song wins over the only metal song. I think that's right, because the metal song matches nothing else the user asked for.

```
============================================================
  Genre fights everything else (calm, acoustic metal fan): top 5 recommendations
  Profile: metal | peaceful | energy 0.20 | likes acoustic
============================================================

  1. Glass Garden - Arden Quartet
     Score: 2.99 / 5.00
       * mood matches (peaceful) +1.0
       * energy 0.18 vs target 0.20 +1.49
       * acoustic sound +0.5

  2. Iron Requiem - Grave Signal
     Score: 2.00 / 5.00
       * genre matches (metal) +2.0
       * energy 0.97 vs target 0.20 +0.00

  3. Spacewalk Thoughts - Orbit Bloom
     Score: 1.80 / 5.00
       * energy 0.28 vs target 0.20 +1.30
       * acoustic sound +0.5

  4. Empty Platform - The Grey Hours
     Score: 1.70 / 5.00
       * energy 0.30 vs target 0.20 +1.20
       * acoustic sound +0.5

  5. Library Rain - Paper Lanterns
     Score: 1.41 / 5.00
       * energy 0.35 vs target 0.20 +0.91
       * acoustic sound +0.5
```

**Energy out of range (1.5):** Energy only goes up to 1.0, but the code doesn't check. Every song is too far away, so energy gives 0 points to everyone and spots 2 to 5 are all tied at 0.50.

```
============================================================
  Energy out of range (1.5): top 5 recommendations
  Profile: edm | euphoric | energy 1.50 | prefers non-acoustic
============================================================

  1. Afterglow Rush - Pulsewave
     Score: 3.50 / 5.00
       * genre matches (edm) +2.0
       * mood matches (euphoric) +1.0
       * energy 0.95 vs target 1.50 +0.00
       * non-acoustic sound +0.5

  2. Iron Requiem - Grave Signal
     Score: 0.50 / 5.00
       * energy 0.97 vs target 1.50 +0.00
       * non-acoustic sound +0.5

  3. Gym Hero - Max Pulse
     Score: 0.50 / 5.00
       * energy 0.93 vs target 1.50 +0.00
       * non-acoustic sound +0.5

  4. Storm Runner - Voltline
     Score: 0.50 / 5.00
       * energy 0.91 vs target 1.50 +0.00
       * non-acoustic sound +0.5

  5. Fiesta de Noche - Los Brillantes
     Score: 0.50 / 5.00
       * energy 0.84 vs target 1.50 +0.00
       * non-acoustic sound +0.5
```

### Comparing profiles

- **High-Energy Pop vs. Chill Lofi:** Their top 5 lists have zero songs in common. Pop gets loud, electric songs, and Lofi gets quiet, acoustic ones. That makes sense, because every preference is the opposite.
- **High-Energy Pop vs. Deep Intense Rock:** They share 3 songs (Gym Hero, Fiesta de Noche, Storm Runner), just in a different order. Storm Runner is #1 for rock but #5 for pop. Both users want loud, non-acoustic music, so the same songs fit. Only the genre and mood labels decide who's on top.
- **Chill Lofi vs. Deep Intense Rock:** No songs in common. One wants calm and acoustic, the other wants loud and electric, so this is the result I wanted.
- **Deep Intense Rock vs. Sad + high energy:** After #1, the lists are almost the same (Storm Runner, Gym Hero, Afterglow Rush, Fiesta de Noche). Both asked for energy 0.9, and there's only one sad song, so the sad listener ends up with the rock fan's playlist. The system can't make "sad and loud" because no song is like that.
- **Chill Lofi vs. Calm acoustic metal fan:** The metal fan's list looks like a chill playlist (classical, ambient, lofi), and 2 songs are the same as Lofi's. Both want low energy and acoustic, and those 2 rules add up to more than the 1 metal song's genre points. I think that's right.
- **High-Energy Pop vs. Capitalized Pop:** These should be identical. Before the fix, a capital "P" made the top song drop to #2. After the fix, they match exactly.
- **Deep Intense Rock vs. Energy out of range:** Both want loud songs and get many of the same ones. But with energy at 1.5, every song is "too far", so spots 2 to 5 all tie at 0.50. The energy rule just stops working.

### Why does "Gym Hero" keep showing up for people who want happy pop?

Gym Hero is a loud workout song. Its mood is "intense", not "happy". But it's still #2 for the happy pop fan, because:

1. **It's labeled "pop".** That's worth 2 points, the biggest prize, just for the label.
2. **It's loud.** The happy pop fan asked for energy 0.85, and Gym Hero is 0.93, which is close enough to get most of the energy points.
3. **The wrong mood only costs 1 point.** Being "intense" instead of "happy" doesn't hurt much, because mood is worth less than genre.

So a pop song that isn't happy beats Rooftop Lights, a happy song labeled "indie pop". It's like a store that sorts by the sign on the shelf instead of what's in the box.

Gym Hero also shows up for the rock fan and the sad + high energy profile. It's one of the loudest songs in the catalog, so anyone who asks for high energy gets it. It ended up in 5 of my 7 top 5 lists.

### What surprised me

- **Capital letters broke it.** "Pop" instead of "pop" pushed the best song down to #2. I fixed it by making the text lowercase before comparing.
- **Out-of-range energy is silently ignored.** The code should limit the target to between 0 and 1.
- **The same loud songs fill every list.** Once genre and mood run out, energy decides everything, so Gym Hero, Fiesta de Noche, and Storm Runner keep coming back. It can't tell "loud and happy" from "loud and angry" because it doesn't use valence.
- **Genre doesn't always win.** For the calm metal fan, a song that fits 3 things beat a song that only fits the genre. That's what I wanted.
- **Changing the weights made things different, not better.** When I doubled energy and halved genre, the sad listener lost the only sad song from their list completely.

---

## 8. Future Work  

1. **Add valence (how happy a song sounds).** This would stop dark rock songs from showing up for happy pop fans. It's already in the data, I just don't score it yet.
2. **Give partial credit for close matches.** "Indie pop" should count a little for a pop fan, and "relaxed" should count a little for a chill fan.
3. **Add more variety to the top 5.** For example, only one song per artist, and more songs per genre so the same loud songs stop filling every list.

I'd also keep the energy target between 0 and 1, so a typo like 1.5 doesn't break the energy score.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
