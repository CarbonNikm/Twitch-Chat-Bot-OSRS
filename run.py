# Author: Nicholas Misleh
# Twitch username: Carbon_Nikm
# Whisper me for help!
#

import string
from irc import sendMessage, sendPongToServer, getUser, getMessage
from initialize import openSocket, greetRoom
from settings import BOTOWNER, LOG_TO_FILE
from logger import getTime, logMessage
from commandlevel import getLevel
from commandlookup import lookup

server = openSocket() # Create a socket bound to the server
greetRoom(server) # Optional greeting when the bot is turned on. Comment this line to remove
tempBuffer = ""
while True: # Frees the bot from processing the greeting from the server
    tempBuffer = str(server.recv(4096))
    if "/NAMES" in str(tempBuffer): # Has potential to break in the future, if "/NAMES" gets split between 4096 byte chunks
        break

botIsRunning = True
while botIsRunning:
        ircReadBuffer = str(server.recv(2048))
        tempBuffer = ircReadBuffer.split("\\r\\n") # Remove return carriage text at the end of received messages
        tempBuffer.pop() # Remove the left over apostraphe from the split buffer array
        ircReadBuffer = tempBuffer # ircReadBuffer is ready for processing
        for line in ircReadBuffer: # This for loop allows "break" to be used for saving time checking for if statements
            
            if "PING :tmi.twitch.tv" in line: # PONGs on request of the server to prevent disconnecting
                sendPongToServer(server)
                break
                
            user = getUser(line)
            message = getMessage(line)
            wordList = message.split(" ") 
            print(str(getTime() + user + ": " + message)) # Prints messages from all users to console
            if LOG_TO_FILE:
                logMessage(str(getTime() + user + ": " + message))


########## Add custom functions below ##########
# Current configuration is modular. Just copy the design patterns as seen below

            if "!level" in wordList[0]:
                sendMessage(server, getLevel(user, message, wordList))
                break
                
            if "!lvl" in wordList[0]:
                sendMessage(server, getLevel(user, message, wordList))
                break
                
            if "!commands" in wordList[0]:
                sendMessage(server, "@"+ user + " !level [skill name] | !level [player name] [skill name]")
                break
                
            if BOTOWNER in user:
                if "!shutdown" in message:
                    sendMessage(server, "MrDestructoid SYSTEMS... FAILING... MrDestructoid")
                    botIsRunning = False