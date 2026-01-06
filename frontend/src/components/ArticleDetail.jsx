import React from "react";

export function ArticleDetail({ article }) {
  if (!article) {
    return <div>Select an article to view details.</div>;
  }

  return (
    <article>
      <h2>{article.title}</h2>
      <p>{article.body}</p>
      {article.is_featured && <span>⭐ Featured</span>}
    </article>
  );
}
