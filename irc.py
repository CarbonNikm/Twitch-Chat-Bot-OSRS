# Author: Nicholas Misleh
#
# Includes functions related to IRC protocol when already connected to a server, including
# responding to a PING, reading messages sent to the channel, and sending a message to a channel
#

########## Imports ##########

import socket
from settings import CHANNEL, NICK, LOG_TO_FILE
from logger import getTime, logMessage

########## Functions ##########

def sendMessage(server, message):
    messageToSend = "PRIVMSG #" + CHANNEL + " :" + message
    server.send((messageToSend + "\r\n").encode())
    print(getTime() + NICK +": " + message)
    if LOG_TO_FILE:
        logMessage(str(getTime() + NICK +": " + message))
    
def sendPongToServer(server): # Twitch servers will ping the bot every 5 minutes. Failure to pong will close the connection
    server.send("PONG\r\n".encode())
    print(getTime() + "PONG sent to server")
    if LOG_TO_FILE:
        logMessage(str(getTime() + "PONG sent to server"))

def getUser(line):
    splitLine = line.split(":", 2)
    user = splitLine[1].split("!", 1)[0]
    return user
    
def getMessage(line):
    splitLine = line.split(":", 2)
    message = splitLine[2]
    return message