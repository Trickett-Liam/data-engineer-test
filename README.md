# Apache Beam Batch Job

This repository contains a simple Apache Beam batch processing pipeline that reads transaction data from a CSV file, processes it, and writes the results to a Gzipped JSONL file.

The pipeline can be executed in two ways:

- **Using Docker** (recommended) Ensures a reproducible environment by running the pipeline inside a container.
- **Running locally** If you prefer to execute the pipeline directly on your host machine using a Python virtual environment.

Both methods are detailed below.

## Prerequisites

- **Docker** (and Docker Compose) – for containerized execution  
- **Git** – to clone the repository  
- *(Optional)* **Python 3.10** – if you prefer to run the pipeline or tests locally using a virtual environment

## Setup

### Clone the Repository

Clone this repository to your local machine:

    git clone https://github.com/Trickett-Liam/data-engineer-test.git

Navigate to the project directory:

    cd data-engineer-test

### Authenticate with Google Cloud

Since this pipeline reads data from a Google Cloud Storage (GCS) bucket, you must authenticate using the Google Cloud SDK.

Ensure you are logged into Google Cloud:

    gcloud auth application-default login

Check that you have access to the required bucket:

    gsutil ls gs://cloud-samples-data/bigquery/sample-transactions/

If access is denied, ensure you have the correct IAM permissions.

### Build the Docker Image

Use Docker Compose to build the image (ensuring a clean build):

    docker-compose build --no-cache

## Running the Pipeline

### Using Docker Compose

To run the Apache Beam pipeline inside the Docker container, run:

    docker-compose run --rm app /venv/bin/python main.py

This command starts the container and executes `main.py` using the Python executable from the container's virtual environment.

### Running Locally

If you prefer to run the pipeline on your host machine:

1. **Create a virtual environment:**

       python3 -m venv venv

2. **Activate the virtual environment:**

   - On macOS/Linux:

         source venv/bin/activate

   - On Windows:

         venv\Scripts\activate

3. **Ensure VS Code is Using the Correct Interpreter:**

Open the Command Palette (Cmd + Shift + P on Mac or Ctrl + Shift + P on Windows)

4. **Install the dependencies:**

       pip install -r requirements.txt

5. **Run the pipeline:**

       python main.py

## Running Tests

### Using Docker Compose

To run unit tests inside the Docker container, run:

    docker-compose run --rm app /venv/bin/python -m unittest discover tests

This command uses the container’s Python interpreter (with Apache Beam installed) to run all tests in the `tests` directory.

### Running Locally

If you want to run tests locally:

1. **Ensure your virtual environment is activated** (see above).

2. **Run the tests:**

       python -m unittest discover tests

*Note:* If tests are not discovered, ensure your test files are named using the `test_*.py` pattern and that an empty `__init__.py` file exists in the `tests` directory.

## Notes

- The output files in the `output/` directory are git-ignored.
- The pipeline uses the DirectRunner, so no Cloud Dataflow configuration is required.
