FROM python:3.11-slim AS builder
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY app/app.py .
EXPOSE 5000
CMD ["python3", "app.py"]