import pytest
from httpx import AsyncClient
from fastapi import status

from app import app
from data import ARTICLES


@pytest.mark.asyncio
async def test_list_articles_returns_all():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/api/articles")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == len(ARTICLES)


@pytest.mark.asyncio
async def test_list_articles_filters_featured_true():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/api/articles?featured=true")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert all(item["is_featured"] is True for item in data)
    # Should return at least one item
    assert len(data) > 0


@pytest.mark.asyncio
async def test_list_articles_filters_featured_false():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/api/articles?featured=false")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert all(item["is_featured"] is False for item in data)
    assert len(data) > 0


@pytest.mark.asyncio
async def test_get_article_by_id():
    target = ARTICLES[0]
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get(f"/api/articles/{target.id}")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert data["id"] == target.id
    assert data["title"] == target.title


@pytest.mark.asyncio
async def test_create_article_requires_non_empty_title():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post(
            "/api/articles",
            json={"id": 99, "title": "   ", "body": "Empty title", "is_featured": False},
        )
    # Expect validation error
    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_create_article_generates_unique_id():
    # Expect that reusing an existing ID is considered an error or handled
    # so that we don't "silently overwrite" existing records.
    existing_id = ARTICLES[0].id
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post(
            "/api/articles",
            json={
                "id": existing_id,
                "title": "Duplicate id",
                "body": "Should not overwrite silently",
                "is_featured": False,
            },
        )

    assert resp.status_code in {status.HTTP_400_BAD_REQUEST, status.HTTP_409_CONFLICT}
