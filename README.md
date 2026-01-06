# News Articles Viewer – Take-Home Task

Welcome!

This is a small full-stack app: a Python backend (FastAPI) and a React frontend.
The app displays a list of news articles, lets you click to view details, and
optionally filter to "featured" articles.

There are a few bugs in the existing code. Your task is to:

1. Set up and run the backend and frontend.
2. Run the test suites (backend + frontend).
3. Fix issues so that:
   - The basic user flows work as expected.
   - The tests pass.
4. If you have time, make any small improvements you feel are reasonable
   (comments, small refactors, etc.) – but this is optional.

> **Timebox:** Please spend around **40 minutes** on this. Don't worry if you
> cannot fix everything: we’re more interested in how you reason and structure
> your changes.

---

## 1. Backend (Python / FastAPI)

### 1.1. Setup

From the `backend/` directory:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt