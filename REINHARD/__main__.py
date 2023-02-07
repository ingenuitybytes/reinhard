#!/usr/bin/env python3
'''This is the main file of the bot.
It starts the bot and the webserver.
'''

# Import modules and files
from flask import Flask, render_template, jsonify
from flask.logging import default_handler
import sqlite3

import threading

from REINHARD.bot import *
from resources import Token
import utils


# Flask
app = Flask(__name__)
default_handler.setFormatter(utils.formatter)
utils.log.addHandler(default_handler)
# logFlask = logging.getLogger() # 'werkzeug'
# logFlask.removeHandler(default_handler)
# logFlask.addHandler(default_handler)

@app.route("/")
def index():
    # Log-Informationen aus der Datenbank abrufen
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    return render_template("index.html")
@app.route("/api/start", methods=["POST"])
def start():
    # Starte den Bot in einem neuen Thread
    thread = threading.Thread(target=bot_start)
    thread.start()
    # Beispiel-Log hinzufügen
    cursor.execute("INSERT INTO logs (time, message) VALUES (?, ?)", (utils.currentTime, "Started bot"))
    conn.commit()
    return "Bot started"
def bot_start():
    bot.run(Token.TOKEN, log_formatter=utils.formatter, log_handler=utils.stream)
@app.route("/api/stop", methods=["POST"])
async def stop():
    # Hier könnten Sie den discord.py-Client stopen
    await bot.close()
    # Beispiel-Log hinzufügen
    cursor.execute("INSERT INTO logs (time, message) VALUES (?, ?)", (utils.currentTime, "Stopped bot"))
    conn.commit()
    return "Bot stopped" 
@app.route("/api/logs")
def logs():
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    logs_as_dict = [{"time": log[0], "message": log[1]} for log in logs]
    return jsonify(logs_as_dict)
@app.route("/api/status")
def get_status():
    status = "offline"
    status = "online" if bot.is_ready() else "offline"
    return status

if __name__ == "__main__":
    # Connect SQLite database
    db_file = 'resources/database.sqlite'
    conn = sqlite3.connect(db_file, check_same_thread=False)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS logs (time text, message text)""")
    conn.commit()
    
    # Start the webserver
    app.run(debug=False, port=8080)