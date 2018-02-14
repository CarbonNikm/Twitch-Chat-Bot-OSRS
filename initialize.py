# Author: Nicholas Misleh
# 
# Includes functions for connecting to a server
#

########## Imports ##########

import string, socket, datetime
from settings import HOST, PORT, PASS, NICK, CHANNEL, GREETING, LOG_TO_FILE
from irc import sendMessage
from logger import getTime, createLogFile

########## Functions ##########

def openSocket():
    server = socket.socket()
    server.connect((HOST, PORT))
    server.send(("PASS " + PASS + "\r\n").encode()) # IRC protocol stuff
    server.send(("NICK " + NICK + "\r\n").encode()) # IRC protocol stuff
    server.send(("JOIN #" + CHANNEL + "\r\n").encode()) # IRC protocol stuff
    if LOG_TO_FILE: # Check settings to see if logging to a file is enabled
        createLogFile() # Imported from logger
    return server
    
def greetRoom(server):
    print(getTime() + "Bot initiated")
    sendMessage(server, GREETING) # If the greeting empty is left blank, as "", no greeting will be sent