# 🎬 Movie Recommendation System

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
Create a .env file:
TMDB_API_KEY=your_api_key_here
Run backend:
python -m uvicorn main:app --reload
👨‍💻 Author

Manav Mittal
B.Tech CSE Student
