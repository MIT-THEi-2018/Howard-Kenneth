from jikanpy import Jikan
from pprint import pprint

jikan = Jikan()

# json of all anime info specified by Jikan docs
mushishi = jikan.anime(457)
# pprint.pprint(mushishi)

# same as above, but with extra info
# (see Jikan docs for information about which endpoints have which extensions)
mushishi_with_eps = jikan.anime(457, extension='episodes')
mushishi_with_eps_2 = jikan.anime(457, extension='episodes', page=2)
mushishi_with_characters_and_staff = jikan.anime(457, extension='characters_staff')

# pprint.pprint(mushishi_with_characters_and_staff)

overlord = jikan.anime(37675)
# pprint.pprint(overlord)
pic_test = jikan.character(extension = 'pictures', id = 11)
pprint(pic_test['image'])
# pprint.pprint(pic_test)

season_sum_2018 = jikan.season(year = 2018, season = 'summer')
# pprint.pprint(season_sum_2018)
# you can also query characters
# ginko = jikan.character(425)

# # and manga
# mushishi_manga = jikan.manga(418)

# # search
# search_result = jikan.search('anime', 'Mushishi')
# # add a page number to the search request
# search_result = jikan.search('anime', 'Mushishi', page=2)
# # add a filter to the search (see Jikan docs about what filters are legal)
# search_result = jikan.search('anime', 'Mushishi', key='type', value='tv')
# search_result = jikan.search('anime', 'Mushishi', key='genre', value=37)
# # use it all!
# search_result = jikan.search('anime', 'Mushishi', page=3, key='type', value='tv')

# # seasonal anime
# winter_2018 = jikan.season(year=2018, season='winter')
# spring_2016 = jikan.season(year=2016, season='spring')

# # scheduled anime
# scheduled = jikan.schedule()
# # add a day of the week if you only want the day's schedule
# monday = jikan.schedule(day='monday')

# # top anime
# top_anime = jikan.top(type='anime')
# # add a page and subtype if you want
# top_anime = jikan.top(type='anime', page=2, subtype='upcoming')

# # meta info about the Jikan REST API
# # meta info about what requests have been done
# requests = jikan.meta(request='requests', type='anime', period='today')
# # meta info about API's status
# status = jikan.meta(request='status', type='anime', period='today')