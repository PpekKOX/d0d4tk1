# Pobranie obrazu Python
FROM python:3.9

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików do kontenera
COPY . /app

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Ustawienie zmiennej PORT (Render go nadpisze)
ENV PORT=5000

# Uruchomienie aplikacji
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app:app", "--bind", "0.0.0.0:5000"]
