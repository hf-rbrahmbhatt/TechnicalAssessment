# News Articles Viewer --- Take-Home Assessment

Thank you for taking the time to complete this short exercise.

This is a small **full-stack app** consisting of:

-   A Python backend (FastAPI)
-   A React frontend (Vite + React Testing Library)

The app displays a list of news articles and allows the user to:

-   view all articles
-   optionally filter to "featured" articles
-   click an article to view its details

There are **intentional bugs** in both the frontend and backend.

Your goal is to use the tests, your debugging skills, and reasoning to
identify and fix them.

After you have fixed the bugs, please provide written responses to the following questions:

1. The 'Show only featured' checkbox wasn't triggering a refetch. Describe how you diagnosed this issue and what you changed. Are there any trade-offs or alternative approaches you considered?
 
2. Describe how you would modify both the backend API and frontend code to support fetching reduced payloads for the list view, and detailed payloads for a full article view. What are the advantages in performing this refactor?
 
3. The project includes both passing and failing tests. Walk us through how you used the test suite to guide your debugging process. Did you write any additional tests? If so, why?
 
4. Looking at the overall architecture, what potential issues do you see with this approach at scale? How would you refactor the codebase if this needed to handle 10,000+ articles?

> ⏱ Expected time: about **60 minutes**.\
> It's okay if you don't finish everything --- we want to see how you
> think.

------------------------------------------------------------------------

## 🧭 What we are looking for

We are evaluating:

-   your ability to read unfamiliar code
-   your ability to debug backend + frontend issues
-   how you reason about failing tests
-   clean and minimal fixes (rather than rewriting everything)
-   small, thoughtful improvements if time allows

Please add short comments if something feels ambiguous or if you made a
conscious trade-off.

------------------------------------------------------------------------

## 🚀 Running the project

You can run backend and frontend independently.

### 1️⃣ Backend (FastAPI)

From the `backend/` folder:

#### Install dependencies

``` bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

#### Run the API

``` bash
uvicorn app:app --reload
```

The API should now be available at:

-   http://127.0.0.1:8000/api/articles
-   http://127.0.0.1:8000/docs (Swagger)

#### Run backend tests

``` bash
pytest
```

------------------------------------------------------------------------

### 2️⃣ Frontend (React)

From the `frontend/` folder:

#### Install dependencies

``` bash
npm install
```

#### Start the dev server

``` bash
npm run dev
```

Open the printed URL (usually):

> http://localhost:5173

#### Run frontend tests

``` bash
npm test
```

------------------------------------------------------------------------

## 🧩 Your tasks

Please focus on:

### 🔎 1. Investigate failing tests

Use the failing tests as clues.

-   Fix backend behaviour so the API behaves as expected.
-   Fix frontend behaviour so the UI behaves correctly and tests pass.

Try to avoid large rewrites --- aim for targeted, intentional fixes.

------------------------------------------------------------------------

### ✨ 2. (Optional, if time allows)

If you still have time:

-   leave TODO comments where things could improve
-   suggest edge cases that might break the app
-   add a small refactor if it improves clarity

Totally optional --- do not feel you must complete this.

------------------------------------------------------------------------

## 📝 Submitting your work

Feel free to:

-   commit incrementally (we like seeing how you worked)
-   add short notes explaining important fixes

Thank you
