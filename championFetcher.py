#! /usr/bin/env python3

import requests
import json
from collections import Counter
from getChampionNameByID import get_champions_name
import sys

api_key = ""  # Enter your own API key in here.
existingServers = ['euw1', "na1", "eun1", "br1", "la1", "la2", "tr1", "jp1", "kr", "ru"]

if not api_key:
    print("You forgot to change the api key.\nPlease look at the Github instructions. -> https://github.com/YannickDC/league-championFetcher")
    sys.exit(0)

# ask for input


while True:
    try:
        playerName = input("What name would you like to lookup? >  ")
        if playerName is None or len(playerName) == 0:
            print("Summoners name cannot be empty!")
        else:
            break
    except ValueError:
        print("Invalid input.")
while True:
    try:
        server = input("What server? (euw1, na1, eun1, br1, la1, la2, tr1, jp1, kr, ru)  > ")
        if server in existingServers:
            break
        else:
            print("Server does not exist.")
    except ValueError:
        print("Invalid input.")

championIDs = []
# First things first, get sumID to pull data

print('trying to find player...')
getPlayerAccount = requests.get(
    "https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + playerName + "?api_key=" + api_key)
if getPlayerAccount.status_code == 200:
    print("player has been found...")

    playerAccountJSON = json.loads(getPlayerAccount.text)
    # accountID has been found
    accountId = playerAccountJSON["accountId"]
    accountName = playerAccountJSON["name"]
    # Now we need to get the total games Value

    getTotalGames = requests.get(
        "https://" + server + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?beginIndex=9999999&api_key=" + api_key)  # little trick to get that.
    if getTotalGames.status_code == 200:
        totalGamesJSON = json.loads(getTotalGames.text)
        totalGames = totalGamesJSON["totalGames"]
        print("total games: ", totalGames)
        bestTimesToLoop = int(
            totalGames / 100) + 1  # always wanna do more then actually needed to prevent that matches are missing
        endIndex = int(100)
        beginindex = int(0)

        a = int(0)
        print("calculating...")
        for a in range(bestTimesToLoop):
            getMe100Games = requests.get(
                "https://" + server + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?endIndex=" + format(
                    endIndex) + "&beginIndex=" + format(beginindex) + "&api_key=" + api_key)
            if getMe100Games.status_code == 200:
                lastMatches = json.loads(getMe100Games.text)
                matches = int(len(lastMatches["matches"]))
                matchesdata = lastMatches['matches']

                for matches in matchesdata:
                    try:
                        currentChampion = matches['champion']
                        championName = get_champions_name(currentChampion)
                        championIDs.append(championName)
                    except:
                        pass

            endIndex += 100
            beginindex = int(endIndex - 100)
            a += 1
        counterOutput = Counter(championIDs)
        print("[ Results for {} ] ".format(playerName))
        print("totalGames: {}".format(totalGames))
        print("Champions in this result: {}".format(len(counterOutput)))
        print("[  Champion Results  ]")
        for key, value in counterOutput.most_common():
            print(key, value)



    elif getTotalGames.status_code == 403:
        print("Forbidden! (getTotalGames)")
elif getPlayerAccount.status_code == 404:
    print("Player account does not exist!")
elif getPlayerAccount.status_code == 403:
    print("Forbidden!(getPlayerAccount)")


