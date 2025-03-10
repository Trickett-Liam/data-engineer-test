.PHONY: all build run test auth clean

# Default target: Build and run the pipeline
all: build run

# Authenticate with Google Cloud
auth:
	gcloud auth application-default login

# Build the Docker image
build:
	docker-compose build --no-cache

# Run the Apache Beam pipeline
run:
	docker-compose run --rm app /venv/bin/python main.py

# Run tests inside the Docker container
test:
	docker-compose run --rm app /venv/bin/python -m unittest discover tests

# Clean up Docker containers and images
clean:
	docker-compose down --rmi all --volumes --remove-orphans
