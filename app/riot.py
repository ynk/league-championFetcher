import json
import sys
from collections import Counter
import requests
from time import gmtime, strftime
import time
from datetime import datetime

valid_servers = ['euw1', 'na1', 'eun1', 'br1',
                 'la1', 'la2', 'tr1', 'jp1', 'kr', 'ru', 'oc1']


class Riot:
    def __init__(self, acc_name, server, api_key):
        self.account_name = acc_name
        self.server = server
        self.api_key = api_key
        self.root_url = "https://{}.api.riotgames.com/lol/summoner/v4".format(
            server)
        self.match_data_url = "https://{}.api.riotgames.com/lol/match/v4/matchlists/by-account".format(
            server)
        self.champion_names = {
            1: 'Annie',
            2: 'Olaf',
            3: 'Galio',
            4: 'Twisted Fate',
            5: 'Xin Zhao',
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
            20: 'Nunu & Willump',
            21: 'Miss Fortune',
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
            235: 'Senna',
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

    def master_controller(self):

        """
        This is a master controller function inside Riot class.
        I wrote this function so that you can directly call this function in order to execute the script as it is.
        It will take some time, but will return a the summoners information or some HTTP Errors
        :return: dict
        """
        if self.account_name is None or len(self.account_name) == 0:
            return {
                "message": "Account name cannot be None. It's required!",
                "status": 404,
            }
        if self.server is None or len(self.server) == 0:
            return {
                "message": "server cannot be None. It's required!",
                "status": 404,
            }
        if self.api_key is None or len(self.api_key) == 0:
            return {
                "message": "API Key cannot be None. It's required!",
                "status": 404,
            }

        account_data = self.get_account_data()
        if account_data.status_code == 404:

            return {
                "message": "Are you this summoner \"{}\" exist in the nine realm?".format(self.account_name),
                "status": 404
            }
        elif account_data.status_code == 403:
            return {
                "message": "You see, I was getting account data for summoner \"{}\". But I just don't have the permission!"
                    .format(self.account_name),
                "status": 404
            }
        elif account_data.status_code != 200:
            return {
                "message": "All you need to know I recieved a not-so-good HTTP error ({}) for summoner \"{}\" when I was fetching his/her account information"
                    .format(account_data.status_code,
                            self.account_name),
                "status": 404
            }

        account_id = json.loads(account_data.text)["accountId"]
        account_level = json.loads(account_data.text)["summonerLevel"]
        matchlist_data = self.get_matchlist_data(account_id)

        if matchlist_data.status_code == 403:
            return {
                "message": "Bro! I was stopped while requesting total number of matches for summoner \"{}\". Aparently I didn't have enough permission!"
                    .format(self.account_name),
                "status": 404
            }
        elif matchlist_data.status_code != 200:
            return {
                "message": "I received a not-so-good HTTP code: {} when requesting total number of matches"
                           " for summoner \"{}\". Bad day!".format(
                    matchlist_data.status_code, self.account_name),
                "status": 404
            }

        total_games = json.loads(matchlist_data.text)["totalGames"]
        champions = self.game_calculation(total_games, account_id)
        counterOutput = Counter(champions)
        self.modify_total_lookups()
        get_lookup_number = self.get_totalLookups()



        return {
            "message": "success",
            "total_games": total_games,
            "account_name": self.account_name,
            "level": account_level,
            "server": self.server,
            "total_champions": len(counterOutput),
            "champions": counterOutput.most_common(),
            "totalLookups": get_lookup_number,
            "status": 200
        }

    def get_account_data(self):
        """
        get account information for this particular user
        even though the name of the function is pretty much self explanatory!
        :return:
        """

        account_data = requests.get("{}/summoners/by-name/{}?api_key={}"
                                    .format(self.root_url,
                                            self.account_name,
                                            self.api_key))
        return account_data

    def get_matchlist_data(self, account_id):
        """
        the function name says what it does. Self explanatory!
        If you don't understand, then may be you lack basic!
        """
        matchlist_data = requests.get("{}/{}?beginIndex=99999999&api_key={}"
                                      .format(self.match_data_url, account_id, self.api_key))
        # little trick to get that.
        return matchlist_data

    # def get_mastery_data(self, f):
    def game_calculation(self, total_games, account_id):
        """
        this function will calculate how many games a player had with a champion.
        :param total_games: number of games you played
        :param account_id: your account_id duh!
        :return: :list
        """
        champions = []
        # always wanna do more then actually needed to prevent that matches are missing
        limit = int(total_games / 100) + 1
        index_end = 100
        index_start = 0

        for _ in range(limit):
            matches_data = requests.get("{}/{}?endIndex={}&beginIndex={}&api_key={}"
                                        .format(self.match_data_url, account_id, index_end,
                                                index_start, self.api_key))
            if matches_data.status_code == 200:
                matches = json.loads(matches_data.text)['matches']
                for match in matches:
                    champions.append(self.champion_names[match['champion']])
            else:

                print(matches_data)
                sys.exit(-1)

            index_start = index_end
            index_end += 100
        return champions

    def get_totalLookups(self) -> int:
        f = open("totalLookups.log", "r")
        if f.mode == 'r':
            contents = f.read()
        return contents

    def modify_total_lookups(self):
        newTotalLookups = int(str(self.get_totalLookups())) + 1
        f = open("totalLookups.log", "w+")
        f.write(str(newTotalLookups))
        f.close()
        return (newTotalLookups)

