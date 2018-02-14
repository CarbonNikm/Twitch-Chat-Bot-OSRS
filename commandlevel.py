# Author: Nicholas Misleh
# 
# To properly install this class, add the following line to the top of run.py
### from commandlevel import getLevel
# 
# To use this command, add the following lines of code to the "Add functions below" in run.py
### if "!level" in wordList[0]:
###     sendMessage(server, getLevel(user, message, wordList))
###     break
#
# This command is specifically for the streamer, rather than looking up any other player
#

########## Imports ##########

import string, requests

########## Settings ##########

OSRSNAME = "Nikm" # Change this to set the account to be looked up

########## Functions ##########

def getLevel(user, message, wordList):
    
    if len(wordList) != 2:
        return ("@" + user + " Usage: !level [skill name]")

    hiscoreResponse = requests.get("http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + OSRSNAME)
    hiscoreResponse = hiscoreResponse.text.replace("\n",",")
    hiscoreResponse = hiscoreResponse.split(",")
    skillName = wordList[1].lower()
    
    # Total exp required per level, placed in an array for fast calculation of exp required until next level
    osrsExpRequirementsArray = [0, 0, 83, 174, 276, 388, 512, 650, 801, 969, 1154, 
        1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470, 5018, 5624, 
        6291, 7028, 7842, 8740, 9730, 10824, 12031, 13363, 14833, 16456, 
        18247, 20224, 22406, 24815, 27473, 30408, 33648, 37224, 41171, 
        45529, 50339, 55649, 61512, 67983, 75127, 83014, 91721, 101333, 
        111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886,
        273742, 302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032,
        668051, 737627, 814445, 899257, 992895, 1096278, 1210421, 1336443,
        1475581, 1629200, 1798808, 1986068, 2192818, 2421087, 2673114, 2951373, 
        3258594, 3597792, 3972294, 4385776, 4842295, 5346332, 5902831, 6517253, 
        7195629, 7944614, 8771558, 9684577, 10692629, 11805606, 13034431]
    
    if "total" in skillName:
        hiscoreIndex =  1
        skillName = "Total"
    elif "overall" in skillName:
        hiscoreIndex =  1
        skillName = "Overall"
    elif "attack" in skillName:
        hiscoreIndex =  4
        skillName = "Attack"
    elif "att" in skillName:
        hiscoreIndex =  4
        skillName = "Attack"
    elif "defence" in skillName:
        hiscoreIndex =  7
        skillName = "Defence"
    elif "defense" in skillName:
        hiscoreIndex =  7
        skillName = "Defence"
    elif "def" in skillName:
        hiscoreIndex = 7
        skillName = "Defence"
    elif "strength" in skillName:
        hiscoreIndex =  10
        skillName = "Strength"
    elif "str" in skillName:
        hiscoreIndex =  10
        skillName = "Strength"
    elif "hitpoints" in skillName:
        hiscoreIndex =  13
        skillName = "Hitpoints"
    elif "hp" in skillName:
        hiscoreIndex =  13
        skillName = "Hitpoints"
    elif "ranged" in skillName:
        hiscoreIndex =  16
        skillName = "Ranged"
    elif "range" in skillName:
        hiscoreIndex =  16
        skillName = "Ranged"
    elif "prayer" in skillName:
        hiscoreIndex =  19
        skillName = "Prayer"
    elif "pray" in skillName:
        hiscoreIndex =  19
        skillName = "Prayer"
    elif "magic" in skillName:
        hiscoreIndex =  22
        skillName = "Magic"
    elif "mage" in skillName:
        hiscoreIndex =  22
        skillName = "Magic"
    elif "cooking" in skillName:
        hiscoreIndex =  25
        skillName = "Cooking"
    elif "cook" in skillName:
        hiscoreIndex =  25
        skillName = "Cooking"
    elif "woodcutting" in skillName:
        hiscoreIndex =  28
        skillName = "Woodcutting"
    elif "woodcut" in skillName:
        hiscoreIndex =  28
        skillName = "Woodcutting"
    elif "wc" in skillName:
        hiscoreIndex =  28
        skillName = "Woodcutting"
    elif "fletching" in skillName:
        hiscoreIndex =  31
        skillName = "Fletching"
    elif "fletch" in skillName:
        hiscoreIndex =  31
        skillName = "Fletching"
    elif "fishing" in skillName:
        hiscoreIndex =  34
        skillName = "Fishing"
    elif "fish" in skillName:
        hiscoreIndex =  34
        skillName = "Fishing"
    elif "firemaking" in skillName:
        hiscoreIndex =  37
        skillName = "Firemaking"
    elif "fm" in skillName:
        hiscoreIndex =  37
        skillName = "Firemaking"
    elif "runecrafting" in skillName: # Moved above crafting to prevent "runecrafting" from triggering "crafting"
        hiscoreIndex =  64            # The index looks number out of order, but does not matter
        skillName = "Runecrafting"
    elif "crafting" in skillName:
        hiscoreIndex =  40
        skillName = "Crafting"
    elif "smithing" in skillName:
        hiscoreIndex =  43
        skillName = "Smithing"
    elif "smith" in skillName:
        hiscoreIndex =  43
        skillName = "Smithing"
    elif "mining" in skillName:
        hiscoreIndex =  46
        skillName = "Mining"
    elif "herblore" in skillName:
        hiscoreIndex =  49
        skillName = "Herblore"
    elif "herb" in skillName:
        hiscoreIndex =  49
        skillName = "Herblore"
    elif "agility" in skillName:
        hiscoreIndex =  52
        skillName = "Agility"
    elif "thieving" in skillName:
        hiscoreIndex =  55
        skillName = "Thieving"
    elif "theiving" in skillName:
        hiscoreIndex =  55
        skillName = "Thieving"
    elif "thief" in skillName:
        hiscoreIndex =  55
        skillName = "Thieving"
    elif "theif" in skillName:
        hiscoreIndex =  55
        skillName = "Thieving"
    elif "slayer" in skillName:
        hiscoreIndex =  58
        skillName = "Slayer"
    elif "slay" in skillName:
        hiscoreIndex =  58
        skillName = "Slayer"
    elif "farming" in skillName:
        hiscoreIndex =  61
        skillName = "Farming"
    elif "farm" in skillName:
        hiscoreIndex =  61
        skillName = "Farming"
    elif "runecraft" in skillName:
        hiscoreIndex =  64
        skillName = "Runecrafting"
    elif "rc" in skillName:
        hiscoreIndex =  64
        skillName = "Runecrafting"
    elif "hunter" in skillName:
        hiscoreIndex =  67
        skillName = "Hunter"
    elif "hunt" in skillName:
        hiscoreIndex =  67
        skillName = "Hunter"
    elif "construction" in skillName:
        hiscoreIndex =  70
        skillName = "Construction"
    else:
        return ("@" + user + " Error in skill name")
        
    currentLevel = int(hiscoreResponse[hiscoreIndex])
    if currentLevel == 99:
        return("@" + user + " ("+ OSRSNAME + ") " + skillName + " level: 99. Exp: " + str(hiscoreResponse[hiscoreIndex + 1] + ". Rank: " + str(hiscoreResponse[hiscoreIndex-1])))
    elif currentLevel > 100: # Assume 
        return("@" + user + " ("+ OSRSNAME + ") " + " Total Level: " + str(hiscoreResponse[hiscoreIndex] + ". Rank: " + str(hiscoreResponse[hiscoreIndex-1])))
    else:
        return("@" + user + " ("+ OSRSNAME + ") " + skillName + " level: " + str(currentLevel) + ". Exp until next level: " + str(int(osrsExpRequirementsArray[currentLevel+1])-int(hiscoreResponse[hiscoreIndex+1])))
        