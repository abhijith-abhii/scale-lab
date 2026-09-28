FROM python:3.12-slim
WORKDIR /app
COPY worker.py .
USER 10001
EXPOSE 8080
CMD ["python", "worker.py"]
