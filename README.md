# Football Data Project

## Objective

This project collects and displays football match statistics for leagues such as Ligue 1 and Premier League.  
The main goals are:

- **Scraping & ETL pipelines:** Using Apache Airflow, we scrape, transform, and export match data automatically.
- **Data visualization:** A lightweight web app (FanStats) displays the collected stats in real time.
- **Extensible design:** Easily add new leagues, DAGs, or additional stats.


## Project Structure
<pre>
C:.
| docker.txt
| REDME.md
| requirements.txt
|
+---.github
+---architecture
| +---dev
| | | .env.dev
| | | docker-compose.dev.yml
| | ...
---site
---FanStats
| dockerfile
| index.html
| run_server.py
---data
stats.json
</pre>


## How to Run

### 1. Prerequisites
- Docker & Docker Compose installed
- Python 3.8+ (for local scripts)

### 2. Start the stack
From `architecture/dev`:

```bash
docker-compose -f docker-compose.dev.yml up --build -d


Airflow webserver: http://localhost:8080

FanStats web app: http://localhost:8000


3. Stop the stack
docker-compose -f docker-compose.dev.yml down

Notes

Data flow: ETL scripts write JSON to site/FanStats/data/stats.json. FanStats reads this file in real time.

Git best practices: Ignore logs, DB files, and runtime JSON data if not needed.

Future development: DAGs will be extended to include more leagues, stats, and automatic updates.

Commit Message Guidelines

feat: - new features (e.g., add new DAG or site module)

fix: - bug fixes

docs: - documentation updates

chore: - maintenance or setup changes (Docker, config files)
