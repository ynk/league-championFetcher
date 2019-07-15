#! /usr/bin/env python3

try:
    import requests
except ImportError:
    print("\"requests\" module is not installed. \nPlease look at the Github instructions. -> "
          "https://github.com/YannickDC/league-championFetcher")
    quit(1)

import json
from collections import Counter
import sys

api_key = ""  # Enter your own API key in here.
if not api_key:
    if len(sys.argv) == 2:
        api_key = sys.argv[1]
    else:
        print("You forgot to change the api key.\nPlease look at the Github instructions. -> "
              "https://github.com/YannickDC/league-championFetcher")
        quit(1)

valid_servers = ['euw1', 'na1', 'eun1', 'br1', 'la1', 'la2', 'tr1', 'jp1', 'kr', 'ru', 'oc1']

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
account_data = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name"
                            "/{}?api_key={}".format(server, account_name, api_key))
if account_data.status_code == 404:
    print("Summoner \"{}\" does not exist!".format(account_name))
    quit(1)
elif account_data.status_code == 403:
    print("Permission denied when requesting account data for summoner \"{}\"".format(account_name))
    quit(1)
elif account_data.status_code != 200:
    print("Recieved error HTTP {} when requesting data for summoner \"{}\"".format(account_data.status_code,
                                                                                   account_name))
    quit(1)

account_id = json.loads(account_data.text)["accountId"]
print("Summoner has been found. Fetching match data. This might take a while...")

matchlist_data = requests.get("https://{}.api.riotgames.com/lol/match/v4/matchlists"
                              "/by-account/{}?beginIndex=9999999&api_key={}".format(server, account_id,
                                                                                    api_key))  # little trick to get that.
if matchlist_data.status_code == 403:
    print("Permission denied when requesting total number of matches for summoner \"{}\"".format(account_name))
    quit(1)
elif matchlist_data.status_code != 200:
    print("Received error HTTP {} when requesting total number of matches"
          " for summoner \"{}\"".format(matchlist_data.status_code, account_name))
    quit(1)

total_games = json.loads(matchlist_data.text)["totalGames"]

champion_names = {
    1: 'Annie',
    2: 'Olaf',
    3: 'Galio',
    4: 'TwistedFate',
    5: 'XinZhao',
    6: 'Urgot',
    7: 'LeBlanc',
    8: 'Vladimir',
    9: 'Fiddlesticks',
    10: 'Kayle',
    11: 'Master Yi',
    12: 'Alistar',
    13: 'Ryze',
    14: 'Sion',
    15: 'Sivir',
    16: 'Soraka',
    17: 'Teemo',
    18: 'Tristana',
    19: 'Warwick',
    20: 'Nunu',
    21: 'MissFortune',
    22: 'Ashe',
    23: 'Tryndamere',
    24: 'Jax',
    25: 'Morgana',
    26: 'Zilean',
    27: 'Singed',
    28: 'Evelynn',
    29: 'Twitch',
    30: 'Karthus',
    31: "Cho'Gath",
    32: 'Amumu',
    33: 'Rammus',
    34: 'Anivia',
    35: 'Shaco',
    36: 'Dr.Mundo',
    37: 'Sona',
    38: 'Kassadin',
    39: 'Irelia',
    40: 'Janna',
    41: 'Gangplank',
    42: 'Corki',
    43: 'Karma',
    44: 'Taric',
    45: 'Veigar',
    48: 'Trundle',
    50: 'Swain',
    51: 'Caitlyn',
    53: 'Blitzcrank',
    54: 'Malphite',
    55: 'Katarina',
    56: 'Nocturne',
    57: 'Maokai',
    58: 'Renekton',
    59: 'JarvanIV',
    60: 'Elise',
    61: 'Orianna',
    62: 'Wukong',
    63: 'Brand',
    64: 'LeeSin',
    67: 'Vayne',
    68: 'Rumble',
    69: 'Cassiopeia',
    72: 'Skarner',
    74: 'Heimerdinger',
    75: 'Nasus',
    76: 'Nidalee',
    77: 'Udyr',
    78: 'Poppy',
    79: 'Gragas',
    80: 'Pantheon',
    81: 'Ezreal',
    82: 'Mordekaiser',
    83: 'Yorick',
    84: 'Akali',
    85: 'Kennen',
    86: 'Garen',
    89: 'Leona',
    90: 'Malzahar',
    91: 'Talon',
    92: 'Riven',
    96: "Kog'Maw",
    98: 'Shen',
    99: 'Lux',
    101: 'Xerath',
    102: 'Shyvana',
    103: 'Ahri',
    104: 'Graves',
    105: 'Fizz',
    106: 'Volibear',
    107: 'Rengar',
    110: 'Varus',
    111: 'Nautilus',
    112: 'Viktor',
    113: 'Sejuani',
    114: 'Fiora',
    115: 'Ziggs',
    117: 'Lulu',
    119: 'Draven',
    120: 'Hecarim',
    121: "Kha'Zix",
    122: 'Darius',
    126: 'Jayce',
    127: 'Lissandra',
    131: 'Diana',
    133: 'Quinn',
    134: 'Syndra',
    136: 'AurelionSol',
    141: 'Kayn',
    142: 'Zoe',
    143: 'Zyra',
    145: "Kai'sa",
    150: 'Gnar',
    154: 'Zac',
    157: 'Yasuo',
    161: "Vel'Koz",
    163: 'Taliyah',
    164: 'Camille',
    201: 'Braum',
    202: 'Jhin',
    203: 'Kindred',
    222: 'Jinx',
    223: 'TahmKench',
    236: 'Lucian',
    238: 'Zed',
    240: 'Kled',
    245: 'Ekko',
    246: 'Qiyana',
    254: 'Vi',
    266: 'Aatrox',
    267: 'Nami',
    268: 'Azir',
    350: 'Yuumi',
    412: 'Thresh',
    420: 'Illaoi',
    421: "Rek'Sai",
    427: 'Ivern',
    429: 'Kalista',
    432: 'Bard',
    497: 'Rakan',
    498: 'Xayah',
    516: 'Ornn',
    517: 'Sylas',
    518: 'Neeko',
    555: 'Pyke',
}

champions = []

# always wanna do more then actually needed to prevent that matches are missing
limit = int(total_games / 100) + 1
index_end = 100
index_start = 0

for a in range(limit):
    matches_data = requests.get("https://{}.api.riotgames.com/lol/match/v4/matchlists"
                                "/by-account/{}?endIndex={}&beginIndex={}&api_key={}"
                                .format(server, account_id, index_end, index_start, api_key))
    if matches_data.status_code == 200:
        matches = json.loads(matches_data.text)['matches']
        for match in matches:
            champions.append(champion_names[match['champion']])
    else:
        print("Received error HTTP {} when requesting match info for "
              "summoner \"{}\"".format(matches_data.status_code, account_name))
        print(matches_data)
        quit(1)

    index_start = index_end
    index_end += 100

counterOutput = Counter(champions)
print("[ Results for {} ] ".format(account_name))
print("Total games on this account: ", total_games)
print("Total champions in this result set: {}".format(len(counterOutput)))
print("[  Champion Results  ]")
print("")

for key, value in counterOutput.most_common():
    print(key, value)
