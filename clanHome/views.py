from django.shortcuts import render
import requests

# Create your views here.

def getClanData(request):
    headers = {
        'Accept': 'application/json',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM0ODQ2YTNjLTExM2YtNGY1OS1iNGViLWU3ODU1ZjZjYWFiNSIsImlhdCI6MTY3Mjc5Mzg4OSwic3ViIjoiZGV2ZWxvcGVyLzcxZjc3OTIwLTg4ODctNTc2ZS05Y2E0LWMyNmU1Y2ExMDEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE5MC41My4yNDkuMTcyIl0sInR5cGUiOiJjbGllbnQifV19.pzDQTszO7_sGandgUAjHEzkuQM5yNIl09BRcjBiIf-u4juNZKq1jHUAw_1bIyKHAE4OG5Tj58xEEL49jKKgMjQ'
    }
    
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329q92yl9y', headers = headers)
    clan_json = response.json()
    print(clan_json)

    return render(request, 'index.html',{
        'title' : 'Clan Page',
        'data': clan_json
    })
