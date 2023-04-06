#!/usr/bin/env python3
'''This is the main file.
It starts the bot and the webserver.
'''

# Import modules and files
from REINHARD.bot import *
from REINHARD.flask import *
from resources import Token
import utils


if __name__ == "__main__": 
    # Start the webserver
    # app.run(debug=False, port=8080)
    # Start the bot
    bot.run(Token.TOKEN, log_formatter=utils.formatter, log_handler=utils.stream)