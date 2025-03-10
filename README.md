# 📌 Apache Beam Batch Job

This repository contains a simple **Apache Beam batch processing pipeline** that:

✅ Reads transaction data from a CSV file  
✅ Processes the data  
✅ Writes the results to a **Gzipped JSONL file**

---

## **⚡ Prerequisites**
Before setting up, ensure you have the following:

-  **Git** – to clone the repository  
-  **Python 3.10** – required for local execution  
-  **Pyenv** – to ensure the correct Python version  
-  **Docker (and Docker Compose)** – for containerized execution  
-  **Colima** – (Mac/Linux users) required before using Docker  
-  **Google Cloud SDK** – for authentication (if accessing GCS)

---

## **🐳 Setting Up & Running with Docker (Recommended)**
### **1️⃣ Clone the Repository**
    git clone https://github.com/Trickett-Liam/data-engineer-test.git
    
    cd data-engineer-test

### **2️⃣ Authenticate with Google Cloud**
If the pipeline **reads data from Google Cloud Storage**, log in:
    
    gcloud auth application-default login

Check access to the required GCS bucket:
    
    gsutil ls gs://cloud-samples-data/bigquery/sample-transactions/

If access is **denied**, check your IAM permissions.

### **3️⃣ Start Colima (Mac/Linux Users)**
Before using Docker:

    colima start

### **4️⃣ Build the Docker Image**
Run:

    make build

### **5️⃣ Run the Pipeline with Docker**

    make run

This starts the container and executes `main.py` using the container’s **virtual environment**.

---

## **🧪 Running Tests with Docker**
To run tests inside the **Docker container**, execute:

    make test

This uses the container’s **Apache Beam environment**.

---

## **🏠 Setting Up & Running Locally**
### **1️⃣ Check Python Version**
Ensure you’re using **Python 3.10. - 3.12**:

    python3 --version

✅ If it prints `Python 3.10.0 - Python 3.12.0`, you're good!  
❌ If not, install it using **Pyenv**:

    pyenv install 3.10.0
    pyenv local 3.10.0

Now, Python **3.10.0 will be used** whenever you enter this project.

### **2️⃣ Create and Activate a Virtual Environment**
    python3 -m venv venv

- **On macOS/Linux:**
  
      source venv/bin/activate

- **On Windows:**
  
      venv\Scripts\activate

### **3️⃣ Ensure VS Code Uses the Correct Interpreter**
1. Open **Command Palette** (`Cmd + Shift + P` on Mac / `Ctrl + Shift + P` on Windows)
2. Search for **"Python: Select Interpreter"** and choose your **Python 3.10.0 virtual environment**.
3. Run the following

       which python
   
4. Paste into the interpetor path.

### **4️⃣ Install Dependencies**
    pip install -r requirements.txt

### **5️⃣ Run the Pipeline Locally**
    python main.py

---

## **🧪 Running Tests Locally**
Ensure the virtual environment is **activated**, then run:

    python -m unittest discover tests

✅ If tests are not discovered, ensure:
- Test files are named using the `test_*.py` pattern
- The `tests/` directory contains an empty `__init__.py` file

---

## **📌 Notes**
- 🚀 The output files in the `output/` directory are **git-ignored**.
- 🏗 The pipeline uses **DirectRunner**, so **no Cloud Dataflow setup** is required.

---

✅ **This version ensures Docker users see their setup first, while local setup is still available below!** 🚀  
Let me know if you need further refinements! 🔥
