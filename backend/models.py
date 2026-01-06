from pydantic import BaseModel, field_validator


class Article(BaseModel):
    id: int
    title: str
    body: str
    is_featured: bool = False

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, v: str) -> str:
        # Intention: avoid empty or whitespace-only titles
        if not v or not v.strip():
            raise ValueError("title must not be empty")
        return v