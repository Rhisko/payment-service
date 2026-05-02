FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

ENV AWS_ACCESS_KEY_ID=AKIAEXAMPLEKEY123456
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

EXPOSE 8000

# INTENTIONAL: running as root
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
