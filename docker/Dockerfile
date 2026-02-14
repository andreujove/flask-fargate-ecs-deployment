FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements/requirements.txt .
RUN pip3 install -r requirements.txt

COPY main.py .
COPY src/ /app/src/

RUN useradd -m myuser
USER myuser

EXPOSE 5000
CMD ["python3", "main.py"]