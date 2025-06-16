# 🎬 Movie Recommender System

A content-based movie recommendation system built using **Python**, **Jupyter Notebook**, and **The Movie Database (TMDB) API**. It analyzes movie metadata from the **TMDB 5000 Movies dataset** to suggest similar movies using **cosine similarity**.

## 🚀 Features

- 🔍 Input any movie title from the dataset
- 🤝 Get top 5 similar movies based on metadata
- 🖼️ Dynamic movie posters using the TMDB API
- ⚡ Fast performance using precomputed similarity matrix
- 📓 Developed entirely in Jupyter Notebook for easy understanding

## 🧠 How It Works

This project uses **Natural Language Processing (NLP)** and **cosine similarity** to find and recommend similar movies.

Steps:
1. Loaded the TMDB 5000 Movies & Credits datasets
2. Preprocessed metadata (genres, cast, crew, keywords, overview)
3. Combined relevant features into a single text column
4. Converted text to vectors using **CountVectorizer**
5. Computed pairwise **cosine similarity** between movies
6. Stored the results for quick access in a `.pkl` file

⚠️ No machine learning models were used — this is a **purely content-based filtering system**.

## 🛠️ Tech Stack

- 🐍 Python
- 📓 Jupyter Notebook
- 📦 Pandas, Numpy, Scikit-learn, Requests
- 🌐 TMDB API (for fetching posters)

## 🗂️ Project Structure

```
📦 Movie Recommender System
│
├── Movie_Recommendation.ipynb   # Main Jupyter Notebook
├── tmdb_5000_movies.csv         # Raw movie metadata
├── tmdb_5000_credits.csv        # Raw credits data
├── movies.pkl                   # Processed movie dataframe
├── similarity.pkl               # Cosine similarity matrix (excluded from GitHub)
├── .env                         # Contains TMDB API key (excluded from GitHub)
├── .gitignore
└── README.md
```

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/7parth/Movie-recommender-system.git
   cd Movie-recommender-system
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy scikit-learn requests python-dotenv
   ```

3. **Create a `.env` file** and add your TMDB API key:
   ```
   TMDB_API_KEY=your_tmdb_api_key_here
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   Open and run `Movie_Recommendation.ipynb`

> ⚠️ `similarity.pkl` is not included in the repo due to size limits. You'll need to generate or download it locally.


## 🙋‍♂️ Author

Made with ❤️ by [Parth Waradkar](https://github.com/7parth)