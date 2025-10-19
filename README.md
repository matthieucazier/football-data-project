# Football Data Project

## Objective

This project collects and displays football match statistics for leagues such as Ligue 1 and Premier League.  
The main goals are:

- **Scraping & ETL pipelines:** Using Apache Airflow, we scrape, transform, and export match data automatically.
- **Data visualization:** A lightweight web app (FanStats) displays the collected stats in real time.
- **Extensible design:** Easily add new leagues, DAGs, or additional stats.

---

## Project Structure
architecture/
├─ dev/ # Development environment
│ ├─ airflow-db/ # Airflow database and logs (ignored in Git)
│ ├─ dags/ # Airflow DAGs
│ ├─ etl/ # ETL scripts for each league
│ ├─ orchestrator/ # Airflow DAG orchestrator scripts
│ ├─ plugins/ # Airflow plugins
│ ├─ logs/ # Airflow runtime logs (ignored in Git)
│ ├─ .env.dev # Development environment variables
│ └─ docker-compose.dev.yml
site/
├─ FanStats/ # Web app to display stats
│ ├─ Dockerfile
│ ├─ index.html
│ ├─ run_server.py
│ └─ data/ # Shared JSON data for the web app


---

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
