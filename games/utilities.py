from games.models import Game as GameModel, GameHistory as GameHistoryModel, GameContract as GameContractModel
from games.serializers import GameSerializer
from itertools import chain

def __with_sponsored(query_set):
    return chain(__data_list().filter(is_new=2), query_set)

def __sort(sort, direction):
    direction = '-' if direction=='desc' else ''
    if sort!='':
        return __data_list().order_by(direction+sort)
    else:
        return __data_list()

def __with_total_count(query_set, page, page_count):
    total_count = query_set.count()
    games = __with_sponsored(query_set[(page-1)*page_count: page*page_count])
    games_serializer = GameSerializer(games, many=True) 
    response = {
        'total_count': total_count,
        'rows': games_serializer.data
    }
    return response


def __data_list():
    return GameModel.objects.only(
                'id', 'name', 'detail_link', 'profile_pic', 'short_desc', 'genres', 'block_chains', 'devices',\
                'status', 'nft', 'f2p', 'p2e', 'p2e_score', 'social_24h', 'social_7d', 'is_new' )