import os
import requests
import streamlit as st

# =============================
# CONFIG
# =============================

API_BASE =  "https://movie-recommendation-system-2fek.onrender.com" or "http://127.0.0.1:8000"

TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# =============================
# SESSION STATE
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"

if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None


# =============================
# API HELPER
# =============================
@st.cache_data(ttl=30)
def api_get_json(path, params=None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=60)
        if r.status_code >= 400:
            return None, r.json()
        return r.json(), None
    except Exception as e:
        return None, str(e)


# =============================
# NAVIGATION
# =============================
def goto_home():
    st.session_state.view = "home"
    st.session_state.selected_tmdb_id = None


def goto_details(tmdb_id):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = tmdb_id


# =============================
# POSTER GRID
# =============================
def poster_grid(cards, cols=6):
    cols = int(cols)  # 🔥 ensure always integer

    if not cards:
        st.info("No movies found.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0

    for _ in range(rows):
        columns = st.columns(cols)
        for col in columns:
            if idx >= len(cards):
                break

            movie = cards[idx]
            idx += 1

            with col:
                if movie.get("poster_url"):
                    st.image(movie["poster_url"], use_column_width=True)
                else:
                    st.write("🖼️ No poster")

                if movie.get("tmdb_id"):
                    if st.button("Open", key=f"{movie['tmdb_id']}_{idx}"):
                        goto_details(movie["tmdb_id"])

                st.markdown(
                    f"<div style='font-size:0.9rem;height:2.2rem;overflow:hidden'>{movie.get('title')}</div>",
                    unsafe_allow_html=True
                )


# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.title("🎬 Menu")

    if st.button("🏠 Home"):
        goto_home()

    st.markdown("---")

    category = st.selectbox(
        "Home Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"]
    )

    grid_cols = int(st.slider("Grid Columns", 4, 8, 6))  # 🔥 force int


# =============================
# MAIN HEADER
# =============================
st.title("🎬 Movie Recommender")
st.divider()


# ==========================================================
# HOME VIEW
# ==========================================================
if st.session_state.view == "home":

    st.markdown("### 🔎 Search Movies")

    search_query = st.text_input(
        "Search by movie title",
        placeholder="Type: Avengers, Batman, Interstellar..."
    )

    if search_query.strip():

        data, err = api_get_json(
            "/tmdb/search",
            {"query": search_query.strip(), "page": 1}
        )

        if err or not data:
            st.error(f"Search failed: {err}")
        else:
            results = data.get("results", [])

            cards = []
            for m in results[:24]:
                cards.append({
                    "tmdb_id": m.get("id"),
                    "title": m.get("title"),
                    "poster_url": (
                        f"{TMDB_IMG}{m.get('poster_path')}"
                        if m.get("poster_path")
                        else None
                    )
                })

            poster_grid(cards, cols=grid_cols)

        st.stop()

    # -------------------------------
    # HOME FEED
    # -------------------------------
    st.markdown(f"### {category.title().replace('_',' ')} Movies")

    data, err = api_get_json("/home", {"category": category, "limit": 24})

    if err or not data:
        st.error(f"Failed to load movies: {err}")
    else:
        poster_grid(data, cols=grid_cols)


# ==========================================================
# DETAILS VIEW
# ==========================================================
elif st.session_state.view == "details":

    tmdb_id = st.session_state.selected_tmdb_id

    if not tmdb_id:
        st.warning("No movie selected.")
        st.stop()

    details, err = api_get_json(f"/movie/id/{tmdb_id}")

    if err or not details:
        st.error(f"Failed to load movie details: {err}")
        st.stop()

    bundle, err = api_get_json(
        "/movie/search",
        {
            "query": details.get("title"),
            "tfidf_top_n": 12,
            "genre_limit": 12,
        }
    )

    if err or not bundle:
        st.error(f"Failed to load recommendations: {err}")
        st.stop()

    if st.button("← Back to Home"):
        goto_home()
        st.stop()

    left, right = st.columns([1, 2.5])

    with left:
        if details.get("poster_url"):
            st.image(details["poster_url"], use_column_width=True)
        else:
            st.write("🖼️ No poster")

    with right:
        st.markdown(f"## {details.get('title')}")
        st.write(details.get("overview", "No overview available."))

    if details.get("backdrop_url"):
        st.markdown("### Backdrop")
        st.image(details["backdrop_url"], use_column_width=True)

    st.divider()

    # TF-IDF
    st.markdown("### 🔎 Similar Movies (TF-IDF)")

    tfidf_items = bundle.get("tfidf_recommendations", [])
    tfidf_cards = []

    for item in tfidf_items:
        tmdb = item.get("tmdb")
        if tmdb:
            tfidf_cards.append({
                "tmdb_id": tmdb.get("tmdb_id"),
                "title": tmdb.get("title"),
                "poster_url": tmdb.get("poster_url"),
            })

    poster_grid(tfidf_cards, cols=grid_cols)

    # Genre
    st.markdown("### 🎭 More Like This (Genre)")
    genre_cards = bundle.get("genre_recommendations", [])
    poster_grid(genre_cards, cols=grid_cols)