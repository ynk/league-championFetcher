#! /usr/bin/env python3

import requests
import json
from collections import Counter
from champion_names import champion_names
import sys

api_key = "" # Enter your own API key in here.
if not api_key:
    if len(sys.argv) == 2:
        api_key = sys.argv[1]
    else:
        print("You forgot to change the api key.\nPlease look at the Github instructions. -> https://github.com/YannickDC/league-championFetcher")
        quit(1)

valid_servers = ['euw1', 'na1', 'eun1', 'br1', 'la1', 'la2', 'tr1', 'jp1', 'kr','ru','oc1']

account_name = None
server = None
while not account_name:
    try:
        account_name = input("What name would you like to lookup? >  ")
    except ValueError:
        print("Invalid input.")
while not server in valid_servers:
    try:
        server = input("Enter a valid server: {} > ".format(valid_servers))
    except ValueError:
        print("Invalid input.")

print('Trying to find summoner...')
account_data = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(server, account_name, api_key))
if account_data.status_code == 404:
    print("Summoner \"{}\" does not exist!".format(account_name))
    quit(1)
elif account_data.status_code == 403:
    print("Permission denied when requesting account data for summoner \"{}\"".format(account_name))
    quit(1)
elif account_data.status_code != 200:
    print("Recieved error HTTP {} when requesting data for summoner \"{}\"".format(account_data.status_code, account_name))
    quit(1)

account_id = json.loads(account_data.text)["accountId"]
print("Summoner has been found. Fetching match data. This might take a while...")

matchlist_data = requests.get("https://{}.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?beginIndex=9999999&api_key={}".format(server, account_id, api_key)) # little trick to get that.
if matchlist_data.status_code == 403:
    print("Permission denied when requesting total number of matches for summoner \"{}\"".format(account_name))
    quit(1)
elif matchlist_data.status_code != 200:
    print("Recieved error HTTP {} when requesting total number of matches for summoner \"{}\"".format(matchlist_data.status_code, account_name))
    quit(1)

total_games = json.loads(matchlist_data.text)["totalGames"]

champions = []


limit = int(total_games / 100 ) + 1 #always wanna do more then actually needed to prevent that matches are missing
index_end = 100
index_start = 0

for a in range(limit):
    matches_data = requests.get("https://{}.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?endIndex={}&beginIndex={}&api_key={}".format(server, account_id, index_end, index_start, api_key))
    if matches_data.status_code == 200:
        matches = json.loads(matches_data.text)['matches']
        for match in matches:
            champions.append(champion_names[match['champion']])
    else:
        print("Recieved error HTTP {} when requesting match info for summoner \"{}\"".format(matches_data.status_code, account_name))
        print(matches_data)
        quit(1)


    index_start = index_end
    index_end +=100

counterOutput = Counter(champions)
print("[ Results for {} ] ".format(account_name))
print("Total games on this account: ", total_games)
print("Total champions in this result set: {}".format(len(counterOutput)))
print("[  Champion Results  ]")
print("")
for key,value in counterOutput.most_common():
    print(key, value)

