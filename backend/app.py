from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from models import Article
from data import ARTICLES

app = FastAPI()

# Allow local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/articles", response_model=List[Article])
def list_articles(featured: Optional[str] = Query(None)):
    articles = ARTICLES

    if featured:
        # Intended: return only featured when featured == "true",
        # and only non-featured when featured == "false".
        if featured.lower() == "true":
            articles = [a for a in articles if a.is_featured]
        elif featured.lower() == "false":
            articles = [a for a in articles if not a.is_featured]
        else:
            # unexpected value, just return all
            pass

    return articles


@app.get("/api/articles/{article_id}", response_model=Article)
def get_article(article_id: int):
    try:
        return ARTICLES[article_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Article not found")


@app.post("/api/articles", response_model=Article, status_code=201)
def create_article(article: Article):
    for idx, existing in enumerate(ARTICLES):
        if existing.id == article.id:
            ARTICLES[idx] = article
            return article

    ARTICLES.append(article)
    return article
