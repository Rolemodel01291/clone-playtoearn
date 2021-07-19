from django.shortcuts import render
from django.db.models import Q
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from games.models import Game as GameModel, GameHistory as GameHistoryModel, GameContract as GameContractModel, SiteInfo as SiteInfoModel
from games.serializers import AutoCompleteSerializer, GameSerializer, GameDetailSerializer, GameHistorySerializer, GameContractSerializer, SiteInfoSerializer
from rest_framework.decorators import api_view

from games.utilities import __sort, __with_total_count

@api_view(['GET'])
def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def filter(request):
    if request.method=='GET':
        try:
            page = int(request.GET.get('page', 1))

            sort = request.GET.get('sort', 'total_rank')
            sort = 'total_score' if sort=='p2e_score' else sort
            
            direction = request.GET.get('direction', 'asc')

            blockchain = request.GET.get('blockchain', 'All-Blockchain')
            genre = request.GET.get('genre', 'All-Genre')
            device = request.GET.get('device', 'All-Device')
            status = request.GET.get('status', 'All-Status')
            nft = request.GET.get('nft', 'All-NFT')
            f2p = request.GET.get('f2p', 'All-FreeToPlay')
            p2e = request.GET.get('p2e', 'All-PlayToEarn')
            
            keyword = request.GET.get('keyword', '')
            
            is_new = request.GET.get('is_new', '')

            return JsonResponse(__with_total_count(__sort(sort, direction).filter(
                    Q(block_chains__icontains=('' if blockchain=='All-Blockchain' else blockchain)) & 
                    Q(genres__icontains=('' if genre=='All-Genre' else genre)) & 
                    Q(devices__icontains=('' if device=='All-Device' else device)) & 
                    Q(status__icontains=('' if status=='All-Status' else status)) & 
                    Q(nft__icontains=('' if nft=='All-NFT' else nft)) & 
                    Q(f2p__icontains=('' if f2p=='All-FreeToPlay' else f2p)) & 
                    Q(p2e__icontains=('' if p2e=='All-PlayToEarn' else p2e)) &
                    (Q(name__icontains=keyword)|Q(short_desc__icontains=keyword)|Q(genres__icontains=keyword)) &
                    Q(is_new__icontains=is_new)
                ), page, 50), safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail(request, id):
    if request.method=='GET':
        try: 
            game = GameModel.objects.filter(id=id)
            game_detail_serializer = GameDetailSerializer(game, many=True)
            return JsonResponse(game_detail_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def history(request, id):
    if request.method=='GET':
        try: 
            game = GameHistoryModel.objects.filter(game_id=id)
            game_history_serializer = GameHistorySerializer(game, many=True)
            return JsonResponse(game_history_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def contracts(request, id):
    if request.method=='GET':
        try: 
            contracts = GameContractModel.objects.filter(game_id=id)
            game_contract_serializer = GameContractSerializer(contracts, many=True)
            return JsonResponse(game_contract_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def auto_complete(request, keyword):
    if request.method=='GET':
        try: 
            games = GameModel.objects.only('id', 'name', 'detail_link', 'profile_pic') \
                    .filter(Q(name__contains=keyword)|Q(short_desc__contains=keyword))
            autocomplete_serializer = AutoCompleteSerializer(games, many=True)
            return JsonResponse(autocomplete_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def site_info(request):
    if request.method=='GET':
        try: 
            info = SiteInfoModel.objects.first()
            info_serializer = SiteInfoSerializer(info)
            return JsonResponse(info_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)