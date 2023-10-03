# Verwenden Sie ein Basis-Image mit Python 3
FROM python:3.8-slim-buster

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /bot_data

# Kopieren Sie die aktuellen Inhalte des Verzeichnisses in den Container
COPY . .

# Installieren Sie notwendige Pakete
RUN apt-get update && apt-get install -y git && \
    python -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt

# CMD gibt den Standardbefehl zum Ausführen des Containers an. 
CMD ["./venv/bin/python", "-m", "main"]
