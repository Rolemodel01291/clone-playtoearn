from rest_framework import serializers
from .models import Game, GameHistory, GameContract, SiteInfo
 
class AutoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ( 'id', 'name', 'profile_pic' )

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ( 'id', 'name', 'profile_pic', 'short_desc', 'genres', 'block_chains', 'devices',\
                'status', 'nft', 'f2p', 'p2e', 'p2e_score', 'social_24h', 'social_7d', 'is_new' )

class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameHistory
        fields = '__all__'

class GameContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameContract
        fields = '__all__'

class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = '__all__'