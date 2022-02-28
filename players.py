import requests
import pandas as pd
# import sqlite3
from nba_api.stats.static import players



# endponts: https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints

header_dict = {
    'User-Agent': 'Mozilla/5.0',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.nba.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Host': 'stats.nba.com'
}

LIST_OF_DICT_PLAYERS = players.get_players()

def get_allPlayers():
    players_list = []
    for i in range(len(LIST_OF_DICT_PLAYERS)):
        players_list.append(LIST_OF_DICT_PLAYERS[i]['full_name'])
    return players_list

def get_firstName():
    first_names = []
    for i in range(len(LIST_OF_DICT_PLAYERS)):
        first_names.append(LIST_OF_DICT_PLAYERS[i]['first_name'])
    return first_names

def get_lastName():
    last_names = []
    for i in range(len(LIST_OF_DICT_PLAYERS)):
        last_names.append(LIST_OF_DICT_PLAYERS[i]['last_name'])
    return last_names



def get_playerID(name):
    for i in range(len(LIST_OF_DICT_PLAYERS)):
        if LIST_OF_DICT_PLAYERS[i]['full_name'].upper() == name.upper():
            return LIST_OF_DICT_PLAYERS[i]['id']
    return None

def get_playerName(name):
    for i in range(len(LIST_OF_DICT_PLAYERS)):
        if LIST_OF_DICT_PLAYERS[i]['full_name'].upper() == name.upper():
            return LIST_OF_DICT_PLAYERS[i]['full_name']
    return None

def convert_to_percentage(num):
    return round(100 * num, 2)

def convert_to_per_game(values):
    return round(values / df['GP'], 1)

def get_playerImageURL(playerID):
    image_url = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{playerID}.png"
    return image_url

def creating_dataframe(playerID):
    '''
      Call get_playerID() first and pass in the player name, then call this function which'll create all our data
    '''

    # Main url to source data from
    url = f"https://stats.nba.com/stats/playercareerstats?LeagueID=&PerMode=Totals&PlayerID={playerID}"

    response = requests.request("GET", url, headers=header_dict)
    json_set = response.json()

    headers = json_set['resultSets'][0]['headers']
    data_set = json_set['resultSets'][0]['rowSet']

    # Create dataframe with each player and their corresponding attributes
    global df
    df = pd.DataFrame(data_set, columns=headers)

    # Add PPG column
    df['PPG'] = convert_to_per_game(df['PTS'])

    # Convert totals to per game
    df['MIN'] = convert_to_per_game(df['MIN'])
    df['BLK'] = convert_to_per_game(df['BLK'])
    df['AST'] = convert_to_per_game(df['AST'])
    df['STL'] = convert_to_per_game(df['STL'])
    df['REB'] = convert_to_per_game(df['REB'])

    # Drop unnecessary columns
    df = df.drop(columns=["PLAYER_ID", "LEAGUE_ID", "TEAM_ID", "PLAYER_AGE", "FTM", "FTA",
                          "FGM", "FGA", "FG3M", "FG3A", "OREB", "DREB", "TOV", "PF", "GS"])

    # Rename columns
    df.rename({'SEASON_ID': 'SEASON', 'TEAM_ABBREVIATION': 'TEAM', 'FG_PCT': 'FG%', 'FG3_PCT': '3FG%',
               'FT_PCT': 'FT%'}, axis=1, inplace=True)

    # Convert decimals to %
    df[["FG%", "3FG%", "FT%"]] = df[["FG%", "3FG%", "FT%"]].apply(convert_to_percentage)

    # Use 'TEAM_ID' to get player's profile picture
    image_url = get_playerImageURL(playerID)

    # Reorder columns
    df = df[["SEASON", "TEAM", "PPG", "REB", "AST", "STL", "BLK", "FG%", "3FG%", "FT%", "GP", "MIN", "PTS"]]
    df.rename_axis("YEAR", axis="columns", inplace=True)
    df.index = range(1, len(df) + 1)

    return df, image_url


# establish SQLite connection
# database = "player_database.db"
# conn = sqlite3.connect(database)

# # save df data to SQlite database
# df.to_sql(name=player_name, con=conn, if_exists="replace")
# conn.close()

