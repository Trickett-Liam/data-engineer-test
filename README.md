# Apache Beam Batch Job

This repository contains a simple Apache Beam batch processing pipeline that reads transaction data from a CSV file, processes it, and writes the results to a Gzipped JSONL file.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.10** (via pyenv recommended)
- **Apache Beam** (with the Direct Runner)
- **Docker** (for containerized execution)
- **pip** (for managing Python dependencies)

## Setup

### Clone the Repository

Clone this repository to your local machine:

**git clone https://github.com/Trickett-Liam/data-engineer-test.git**

Navigate to the project directory:

**cd data-engineer-test**

### Using Docker Compose

If you prefer using Docker Compose, you can define a `docker-compose.yml` file and run the following:

**docker-compose up --build**

Running the Pipeline

To execute the pipeline inside the container:

## Running the Pipeline

To run the pipeline, use one of the following whitelisted commands:

**python <path_to_pipeline_script>.py**

For example, if your main script is named **main.py**, run:

**python main.py**

## Running Tests

To run unit tests, use one of the following whitelisted commands:

**python -m pytest <path_to_test_file>**

For example, if your unit test script is named **unit_test.py**, run:

**python -m pytest tests/unit_test.py**
