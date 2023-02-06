#!/usr/bin/env python3
'''This is the main file of the bot.
It starts the bot and the webserver.
'''

# Import modules and files
from flask import Flask, render_template, jsonify
import sqlite3

import threading

from REINHARD.bot import *


# Bot
bot = MyBot()

# Flask
app = Flask(__name__)
status = "offline"

@app.route("/")
def index():
    # Log-Informationen aus der Datenbank abrufen
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    return render_template("index.html", status=status)
@app.route("/api/start", methods=["POST"])
def start():
    # Starte den Bot in einem neuen Thread
    thread = threading.Thread(target=bot_start)
    thread.start()
    # Beispiel-Log hinzufügen
    cursor.execute("INSERT INTO logs (time, message) VALUES (?, ?)", ((now.strftime("%d/%m/%Y %H:%M:%S")), "Started bot"))
    conn.commit()
    return "Bot started"
def bot_start():
    bot.run(TOKEN)
@app.route("/api/stop", methods=["POST"])
async def stop():
    # Hier könnten Sie den discord.py-Client stopen
    await bot.close()
    # Beispiel-Log hinzufügen
    cursor.execute("INSERT INTO logs (time, message) VALUES (?, ?)", ((now.strftime("%d/%m/%Y %H:%M:%S")), "Stopped bot"))
    conn.commit()
    return "Bot stopped" 
@app.route("/api/status")
def get_status():
    global status
    return status
@app.route("/api/logs")
def logs():
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    logs_as_dict = [{"time": log[0], "message": log[1]} for log in logs]
    return jsonify(logs_as_dict)

if __name__ == "__main__":
    # Verbindung mit der SQLite-Datenbank herstellen
    conn = sqlite3.connect("logs.db", check_same_thread=False)
    cursor = conn.cursor()
    # Tabelle erstellen, falls sie noch nicht existiert
    cursor.execute("""CREATE TABLE IF NOT EXISTS logs (time text, message text)""")
    conn.commit()
    app.run(debug=True, port=8080)