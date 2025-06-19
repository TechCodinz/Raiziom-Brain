
# Raiziom Brain — Flask Backend

This is the real working backend of Raiziom with active Paiddail logic.

## Features

- ✅ Task logging and divine command recording
- ✅ Paiddail mission handler (add, list)
- ✅ Poster content logic
- ✅ Memory stored in JSON

## Endpoints

- `/` → Status check
- `/command` → POST: {"command": "any text"}
- `/paiddail/mission` → POST: {"mission": "earn 100 coins"}
- `/paiddail/missions` → GET: list all missions
- `/poster` → GET: one daily divine caption

## Deploy Steps

1. Push to GitHub
2. Connect repo to [https://render.com](https://render.com)
3. Deploy as web service (Flask)
4. Set start command: `python app.py`
