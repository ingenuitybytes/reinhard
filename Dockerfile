# Verwenden Sie ein Basis-Image mit Python 3.11
FROM python:3.11-slim-bullseye

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /bot_data

# Kopieren Sie die aktuellen Inhalte des Verzeichnisses in den Container
COPY . .

# Installieren Sie notwendige Pakete
RUN apt-get update && apt-get install -y git && \
    pip install --no-cache-dir -r requirements.txt

# CMD gibt den Standardbefehl zum Ausführen des Containers an.
CMD ["python3", "-m", "main"]
