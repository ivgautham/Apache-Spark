# Apache Airflow with Python Spark Jobs

## Table of Contents

- [Description](#description)
- [Code-Flow](#code-flow)
- [Module-Explanation](#module-explanation)
- [Usage](#usage)
- [Future-Development](#future-development)
  
## Description
This project orchestrates Spark jobs written in Python using Apache Airflow, all within a Dockerized environment. The DAG sparking_flow is designed to submit Spark jobs written in Python ensuring that data processing is handled efficiently and reliably on a daily schedule.

## Code-Flow
The DAG sparking_flow includes the following tasks:

start: A PythonOperator that prints "Jobs started".
python_job: A SparkSubmitOperator that submits a Python Spark job.
end: A PythonOperator that prints "Jobs completed successfully".

These tasks are executed in a sequence where the start task triggers the Spark jobs in parallel, and upon their completion, the end task is executed.

## Module-Explanation
- `spark_airflow.py`: The main Spark script which holds the SparkSubmitOperator that submits a Python Spark job.

## Usage
After the Docker environment is set up, the sparking_flow DAG will be available in the Airflow web UI localhost:8080, where it can be triggered manually or run on its daily schedule.

The DAG will execute the following steps:
Print "Jobs started" in the Airflow logs.
Submit the Python Spark job to the Spark cluster.
Print "Jobs completed successfully" in the Airflow logs after all jobs have finished.

## Future-Development
1) Increase the Dataset - To improve the efficiency of processing the data in Apache airflow.
