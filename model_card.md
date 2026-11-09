# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

My recommender works like a judge giving points. The user tells it what they like: a favorite genre, a favorite mood, how much energy they want (from calm to intense), and whether they like acoustic music.

Then it looks at every song, one at a time, and gives it points:

- **Same genre as the user likes:** 2 points. This counts the most because genre is usually the biggest part of someone's taste.
- **Same mood:** 1 point.
- **Energy close to what the user wants:** up to 1.5 points. A song with exactly the right energy gets all 1.5. The further away it is, the fewer points it gets, and a song that is way off gets almost nothing. So it doesn't reward songs just for being loud or quiet, only for being *close* to what the user asked for.
- **Acoustic sound matches:** 0.5 points.

The best possible score is 5. After every song has a score, it sorts them from highest to lowest and shows the top 5. Each song also comes with a list of reasons, so you can see exactly why it was picked.

**Changes from the starter:** the starter just returned the first few songs in the file. I added the point system, the "closer is better" rule for energy, the reasons list, and 10 more songs with new genres and moods. I left out tempo and danceability because in this data they go up and down with energy, so they would just count the same thing twice.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
