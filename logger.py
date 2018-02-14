# Author: Nicholas Misleh
# 
# Includes logging functions such as recording when a message was sent/read
# as well as logging every message to a separate file
#

########## Imports ##########

import datetime
import logging

########## Functions ##########

def getTime(): # formatting the date and time for the logs
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S | ")

def createLogFile(): # create a log file in the same location the bot resides
    global basicLogger
    basicLogger = logging.getLogger("")
    basicLogger.setLevel(logging.DEBUG)
    logFile = logging.FileHandler(str(datetime.datetime.now().strftime("%Y %m %d %H %M %S.txt")))
    formatStyle = logging.Formatter("%(message)s")
    logFile.setFormatter(formatStyle)
    basicLogger.addHandler(logFile)
    
def logMessage(messageToLog):
    basicLogger.info(messageToLog)  
