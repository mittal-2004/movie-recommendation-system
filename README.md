# 🎬 Movie Recommendation System
<img width="1916" height="937" alt="image" src="https://github.com/user-attachments/assets/bddf39dd-d771-4295-971f-05ba9491cb08" />



A full-stack movie recommendation system built using **TF-IDF and Cosine Similarity**.  
It recommends similar movies based on their content (overview + genres) and fetches real-time posters and details using the **TMDB API**.

## 🌐 Live Demo

Frontend:  
https://movie-recommendation-system-ks9mzpbewrdqqtay45flhj.streamlit.app/

Backend API:  
https://movie-recommendation-system-2fek.onrender.com  
API Docs:  
https://movie-recommendation-system-2fek.onrender.com/docs

## 🚀 Features

- Search any movie  
- Get similar movie recommendations  
- View posters and movie details  
- Genre-based suggestions  
- FastAPI backend + Streamlit frontend  
- Fully deployed  

## 🛠 Tech Stack

- FastAPI  
- Streamlit  
- Scikit-learn (TF-IDF)  
- Pandas & NumPy  
- TMDB API  
- Render & Streamlit Cloud  

## ▶️ Run Locally

```bash
git clone https://github.com/mittal-2004/movie-recommendation-system.git
cd movie-recommendation-system
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt


---

## 📌 What I Learned

- How content-based recommendation systems work  
- Why cosine similarity works well with TF-IDF vectors  
- How to design and deploy a FastAPI backend  
- How to integrate third-party APIs  
- How to connect frontend and backend in a real project  
- Deployment workflow for full-stack ML applications  

---

## ⚠ Limitations

- No user-based personalization
- Only content-based filtering
- Cold-start problem
- Depends on quality of metadata

---

## 📈 Future Improvements

- Add collaborative filtering
- Add user login & watch history
- Improve ranking strategy
- Add caching for faster responses
- Dockerize the backend

---

## 👨‍💻 Author

Manav Mittal  
B.Tech CSE Student  
Interested in Machine Learning & Backend Development  

---

⭐ If you liked this project, feel free to give it a star!
