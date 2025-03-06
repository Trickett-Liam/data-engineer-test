# Apache Beam Batch Job

This repository contains a simple Apache Beam batch processing pipeline that reads transaction data from a CSV file, processes it, and writes the results to a Gzipped JSONL file. The solution fulfills the requirements of the Data Engineer Tech Test.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.10+**
- **Apache Beam** (with the Direct Runner)
- **pip** (for managing Python dependencies)

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:

git clone <repository_url>
cd <repository_name>

### 2. Create and Activate a Virtual Environment
If you don’t have `venv` installed, you can create a new virtual environment with the following command:

python3 -m venv venv

Then, activate the virtual environment:

For **macOS/Linux**:

source venv/bin/activate

For **Windows**:

venv\Scripts\activate

Once the virtual environment is activated, install all the required Python libraries listed in the `requirements.txt` file:

pip install -r requirements.txt

## Running the Pipeline

Once you've set up the environment, you can run the pipeline with the following command:

python <path_to_pipeline_script>.py

## Running Tests

To run unit tests, use the following command:

pytest tests/unit_test.py