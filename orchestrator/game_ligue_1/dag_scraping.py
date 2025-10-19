from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.game_ligue_1.scraping import scraping
from etl.game_ligue_1.transformation import transformation
from etl.game_ligue_1.export import export


with DAG(
    dag_id="test_dag",
    start_date=datetime(2025, 10, 15),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_scraping = PythonOperator(
        task_id="scraping",
        python_callable=scraping
    )

    run_transformation = PythonOperator(
        task_id="transformation",
        python_callable=transformation
    )

    run_export = PythonOperator(
        task_id="export",
        python_callable=export
    )

run_scraping >> run_transformation >> run_export