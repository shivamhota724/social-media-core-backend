FROM python:3.10-slim

WORKDIR /app

# Prevent Python from buffering outputs or writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip to the latest fast version
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .

# Force binary wheels for faster installation without freezing
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
