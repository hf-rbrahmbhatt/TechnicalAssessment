const BASE_URL = "http://127.0.0.1:8000";

export async function fetchArticles({ featured } = {}) {
  const params = new URLSearchParams();
  if (featured !== undefined && featured !== null) {
    params.set("featured", String(featured));
  }
  const url =
    params.toString().length > 0
      ? `${BASE_URL}/api/articles?${params.toString()}`
      : `${BASE_URL}/api/articles`;

  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to load articles: ${res.status}`);
  }
  return res.json();
}

export async function fetchArticleById(id) {
  const res = await fetch(`${BASE_URL}/api/articles/${id}`);
  if (!res.ok) {
    throw new Error(`Failed to load article: ${res.status}`);
  }
  return res.json();
}
