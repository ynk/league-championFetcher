#! /usr/bin/env python3
from app.riot import Riot

try:
    import requests
except ImportError:
    print("\"requests\" module is not installed. \nPlease look at the Github instructions. -> "
          "https://github.com/ynkx/league-championFetcher")
    quit(1)

import json
from collections import Counter
import sys

api_key = ""  # Enter your own API key in here.
while True:
    api_key = input("Please provide your api_key: ")
    if len(api_key) == 0:
        print("You forgot to change the api key.\nPlease look at the Github instructions. -> "
              "https://github.com/ynkx/league-championFetcher")
        sys.exit(-1)
    break

valid_servers = ['euw1', 'na1', 'eun1', 'br1',
                 'la1', 'la2', 'tr1', 'jp1', 'kr', 'ru', 'oc1']

account_name = None
server = None
while not account_name:
    try:
        account_name = input("What name would you like to lookup: ")
    except ValueError:
        print("Invalid input.")
while not server in valid_servers:
    try:
        server = input(
            "Enter a valid server from this list {}: ".format(valid_servers))
    except ValueError:
        print("Invalid input.")

"""
This is a class which simplified the import for the webview.
It has been implemented fully from the previous version of the file.
check app > riot_py
"""
riot = Riot(account_name, server, api_key)
print('Trying to find summoner...')
account_data = riot.get_account_data()
if account_data.status_code == 404:
    print("Summoner \"{}\" does not exist!".format(account_name))
    sys.exit(-1)
elif account_data.status_code == 403:
    print("Permission denied when requesting account data for summoner \"{}\"".format(
        account_name))
    sys.exit(-1)
elif account_data.status_code != 200:
    print("Received error HTTP {} when requesting data for summoner \"{}\""
          .format(account_data.status_code,
                  account_name))
    sys.exit(-1)

account_id = json.loads(account_data.text)["accountId"]
print("Summoner has been found. Fetching match data. This might take a while...")

matchlist_data = riot.get_matchlist_data(account_id)
if matchlist_data.status_code == 403:
    print("Permission denied when requesting total number of matches for summoner \"{}\"".format(
        account_name))
    sys.exit(-1)
elif matchlist_data.status_code != 200:
    print("Received error HTTP {} when requesting total number of matches"
          " for summoner \"{}\"".format(matchlist_data.status_code, account_name))
    sys.exit(-1)

total_games = json.loads(matchlist_data.text)["totalGames"]
champions = riot.game_calculation(total_games, account_id)
counterOutput = Counter(champions)
print("[ Results for {} ] ".format(account_name))
print("Total games on this account: ", total_games)
print("Total champions in this result set: {}".format(len(counterOutput)))
print("[  Champion Results  ]")
print("")

for key, value in counterOutput.most_common():
    print(key, value)
