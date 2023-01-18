from django.shortcuts import render
import requests

# Create your views here.

def getClanData(request):
    headers = {
        'Accept': 'application/json',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM5MTU0NjRlLWZlNjEtNDA0YS05NTVmLWU5Y2IwYWIzMWYwMSIsImlhdCI6MTY3NDA4NjA3OSwic3ViIjoiZGV2ZWxvcGVyLzcxZjc3OTIwLTg4ODctNTc2ZS05Y2E0LWMyNmU1Y2ExMDEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE5MC41My4yNDkuMTcyIiwiMjE2LjI0LjU3LjMiLCIzNS4xNjAuMTIwLjEyNiIsIjM0LjIxMS4yMDAuODUiLCI0NC4yMzMuMTUxLjI3Il0sInR5cGUiOiJjbGllbnQifV19.ygquu4tdXZS3oOPEe2mMk2dmTkKAi533_cCUw31LnKVuW5ORgedGxUYnIimRwyHbCKWt_b5YzKhowkIUWuoCwA'
    }
    
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329q92yl9y', headers = headers)
    clan_json = response.json()
    print(clan_json)

    return render(request, 'index.html',{
        'title' : 'Clan Page',
        'data': clan_json
    })
