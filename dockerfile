FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/venv/bin/python", "main.py"]
