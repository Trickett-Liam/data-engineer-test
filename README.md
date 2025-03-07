# Apache Beam Batch Job

This repository contains a simple Apache Beam batch processing pipeline that reads transaction data from a CSV file, processes it, and writes the results to a Gzipped JSONL file.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.10** (via pyenv recommended)
- **Apache Beam** (with the Direct Runner)
- **pip** (for managing Python dependencies)

## Setup

### Clone the Repository

Clone this repository to your local machine:

**git clone <repository_url>**

Navigate to the project directory:

**cd <repository_name>**

### Install Python Version Using pyenv 

To ensure you're using the correct version of Python (3.10.0), we recommend using pyenv. This tool allows you to easily manage multiple versions of Python and automatically set the version for your project.

Install pyenv (if it's not already installed):

**brew install pyenv**

Install Python 3.10.0 using pyenv

Inside the project directory, run:

**pyenv local 3.10.0**

Verify Python version:

You can verify that the correct version of Python is being used by running:

**pyenv version**

This should output 3.10.0.

### Create and Activate a Virtual Environment

Make sure to use the exact Python interpreter inside your virtual environment. For example, if your working path is:

**/Users/liam.trickett/Test/data-engineer-test/venv/bin/python**

Create the virtual environment using:

**python3 -m venv venv**

Activate the virtual environment on macOS/Linux:

**source venv/bin/activate**

Once activated, verify you're using the correct interpreter by running:

**which python**

You should see an output similar to:

**/Users/liam.trickett/Test/data-engineer-test/venv/bin/python**

Then, install the required Python libraries:

**pip install -r requirements.txt**

## Running the Pipeline

To run the pipeline, use one of the following whitelisted commands:

**python <path_to_pipeline_script>.py**

For example, if your main script is named **main.py**, run:

**python main.py**

## Running Tests

To run unit tests, use the following whitelisted command:

**pytest tests/unit_test.py**
