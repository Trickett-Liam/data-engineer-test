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

## **🐳 Setting Up & Running with Docker**
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

## **📌 Notes**
- 🚀 The output files in the `output/` directory are **git-ignored**.
- 🏗 The pipeline uses **DirectRunner**, so **no Cloud Dataflow setup** is required.

---

✅ **This version ensures Docker users see their setup first, while local setup is still available below!** 🚀  
Let me know if you need further refinements! 🔥
