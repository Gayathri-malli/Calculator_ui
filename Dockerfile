From python:3.10-slim
WORKDIR /app
COPY reqyuirements.txt
RUn pip install -r requirements.txt
COPy ...
EXPOSE 5000
CMD ["python", "app.py"]
