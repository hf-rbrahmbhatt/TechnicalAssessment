import React from "react";
import { describe, expect, it, vi, beforeEach } from "vitest";
import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import App from "../App.jsx";
import * as api from "../api.js";

describe("App", () => {
  beforeEach(() => {
    vi.restoreAllMocks();
  });

  it("loads and displays articles", async () => {
    vi.spyOn(api, "fetchArticles").mockResolvedValue([
      { id: 1, title: "Article 1", body: "Body 1", is_featured: false },
    ]);

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText("Article 1")).toBeInTheDocument();
    });
  });

  it("loads article details when item is clicked", async () => {
    vi.spyOn(api, "fetchArticles").mockResolvedValue([
      { id: 1, title: "Article 1", body: "Body 1", is_featured: false },
    ]);
    const fetchArticleByIdSpy = vi
      .spyOn(api, "fetchArticleById")
      .mockResolvedValue({
        id: 1,
        title: "Article 1",
        body: "Body 1",
        is_featured: false,
      });

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText("Article 1")).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText("Article 1"));

    await waitFor(() => {
      expect(fetchArticleByIdSpy).toHaveBeenCalledWith(1);
      expect(screen.getByText("Body 1")).toBeInTheDocument();
    });
  });

  it("refetches when 'show featured' is toggled", async () => {
    const fetchArticlesSpy = vi
      .spyOn(api, "fetchArticles")
      .mockResolvedValue([]);

    render(<App />);

    await waitFor(() => {
      expect(fetchArticlesSpy).toHaveBeenCalledTimes(1);
    });

    const checkbox = screen.getByLabelText("Show only featured");
    fireEvent.click(checkbox);

    await waitFor(() => {
      // Expect another fetch when the checkbox changes
      expect(fetchArticlesSpy).toHaveBeenCalledTimes(2);
      expect(fetchArticlesSpy).toHaveBeenLastCalledWith({ featured: true });
    });
  });
});
