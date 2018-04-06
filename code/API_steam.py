from urllib import request
import json

import webbrowser

"""
steam WEB API references:
https://developer.valvesoftware.com/wiki/Steam_Web_API#GetGlobalAchievementPercentagesForApp_.28v0001.29

"""

# straight into python, json version
def getInventory_json(steamid):
    data = request.urlopen('http://steamcommunity.com/profiles/'+steamid+'/inventory/json/730/2')
    json_data = json.loads(data.read())
    print(json_data)
    descriptions = json_data['rgDescriptions']
    print([descriptions[v]['name'] for v in descriptions])
    print('Done!')
    return

#getInventory(steamid);

# panzerstadt
steamid = '76561198029188984'
# this is my steamid in various formats: https://steamid.io/lookup/STEAM_0:0:34461628


# testing
def get_stuff_from_steam_id(steamID64):
    # whole thing is a GET request
    # https://partner.steamgames.com/doc/webapi/IPlayerService#GetOwnedGames
    # bool has to be 1 and not 'true' dammit

    # how to get your API key:
    # 1. go to this: https://steamcommunity.com/dev/apikey
    # 2. fill in your website (just a reference for your work, not used in any way at all for subsequent API calls
    apikey = 'YOUR_OWN_API_KEY_HERE'


    steamid = steamID64
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    url += "?key={0}&steamid={1}&include_appinfo={2}&include_played_free_games={3}".format(
        apikey, steamid, 1, 1
    )

    # will give you apps names in the form of appid

    # if you wanna see the thing as it comes back from steam's server
    #webbrowser.open(url=url, new=2)

    # if you wanna get it back into python to do stuff with it
    result = request.urlopen(url=url)
    json_data = json.loads(result.read())
    print(json_data)  # will give you apps names in the form of appid

    # if the stuff (json) coming from steam servers has something called a 'response' in their json...
    if 'response' in json_data:
        num_of_games = json_data['response']['game_count']
        list_of_games = json_data['response']['games']

        # see stuff
        print('number of games in account {0}: {1}'.format(steamid, num_of_games))
        for game in list_of_games:
            game_appid = game['appid']
            game_name = game['name']
            minutes_played = game['playtime_forever']
            print('hours played: {1}, game: {0}, game app_id : {2}'.format(game_name, game_appid, minutes_played))



get_stuff_from_steam_id(steamID64=steamid)







# IMAGES
# https://github.com/SteamLUG/steamlug.org/issues/169

# images (tested, works)
def get_images(app_id='320', img_url='6dd9f66771300f2252d411e50739a1ceae9e5b30'):
    app_id = app_id
    icon_url = img_url
    url_image = 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/{0}/{1}.jpg'.format(
        app_id, icon_url
    )
    #webbrowser.open(url_image)  # see the image you downloaded
    #image = request.urlretrieve(url_image)  # download the image you downloaded

