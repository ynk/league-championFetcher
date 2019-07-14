import requests
import json
from collections import Counter
from getChampionNameByID import get_champions_name

api_key = "" # Enter your own API key in here.

#Ask for input
playerName = input("What name would you like to lookup? >  " )
server =  input("What server? > ") # "na1, euw1"


championIDs = []
roles = []
lanesS = []
gameIDlist = []
#First things first, get sumID to pull data

print('trying to find player...')
getPlayerAccount = requests.get("https://"+server+".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + playerName + "?api_key=" + api_key)
if getPlayerAccount.status_code == 200:
    print("player has been found...")

    playerAccountJSON = json.loads(getPlayerAccount.text)
    # accountID has been found
    accountId = playerAccountJSON["accountId"]
    accountName = playerAccountJSON["name"]
    # Now we need to get the total games Value

    getTotalGames = requests.get("https://"+server+".api.riotgames.com/lol/match/v4/matchlists/by-account/"+accountId +"?beginIndex=9999999&api_key=" + api_key) # little trick to get that.
    if getTotalGames.status_code == 200:
        totalGamesJSON = json.loads(getTotalGames.text)
        totalGames = totalGamesJSON["totalGames"]
        print("total games: ", totalGames)
        bestTimesToLoop = int(totalGames / 100 ) + 1 #always wanna do more then actually needed to prevent that matches are missing
        endIndex = int(100)
        beginindex = int (0)


        a = int(0)
        for a in range(bestTimesToLoop):

           # print("Progress {}/{}".format(endIndex, totalGames))  #

            getMe100Games = requests.get("https://"+server+".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId+ "?endIndex=" + format(endIndex)+"&beginIndex="+format(beginindex)+"&api_key="+api_key)
            if getMe100Games.status_code == 200:
                lastMatches = json.loads(getMe100Games.text)
                matches = int(len(lastMatches["matches"]))
                matchesdata = lastMatches['matches']

                for matches in matchesdata:
                    gameID = matches['gameId']
                    champion = matches['gameId']
                    try:

                        currentChampion = matches['champion']
                        role = matches['role']
                        lane = matches['lane']
                        currentGameID = gameIDlist.append(matches['gameId'])
                        roleName = roles.append(role)
                        laneName = lanesS.append(lane)
                        championName = get_champions_name(currentChampion)
                        championIDs.append(championName)
                    except:
                        print('Error')

            endIndex +=100
            beginindex = int(endIndex - 100)
            a+=1

        counterRoles = Counter(roles)
        counterLanes = Counter(lanesS)
        counterOutput = Counter(championIDs)
        print("[ Results for {} ] ".format(playerName))
        print("totalGames: {}".format(totalGames))
        print("\n")
        print("[  Champion Results  ]")
        print("")
        for key,value in counterOutput.most_common():
            print(key, value)



    elif getTotalGames.status_code == 403:
     print("Forbidden! (getTotalGames)")
elif getPlayerAccount.status_code == 404:
    print("Player account does not exist!")
elif getPlayerAccount.status_code == 403:
    print("Forbidden!(getPlayerAccount)")


