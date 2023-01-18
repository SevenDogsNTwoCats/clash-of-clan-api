from django.shortcuts import render
import requests

# Create your views here.

def getClanData(request):
    headers = {
        'Accept': 'application/json',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImU5NzRhOTViLWNjZGItNGZlZC1hN2Y5LWI0YTljNGNlM2JiNCIsImlhdCI6MTY3NDA4NTc4NCwic3ViIjoiZGV2ZWxvcGVyLzcxZjc3OTIwLTg4ODctNTc2ZS05Y2E0LWMyNmU1Y2ExMDEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjE2MC4xMjAuMTI2IiwiNDQuMjMzLjE1MS4yNyIsIjE5MC41My4yNDkuMTcyIiwiMzQuMjExLjIwMC44NSIsIjAuMC4wLjAiXSwidHlwZSI6ImNsaWVudCJ9XX0.4XFfDKnsGDMNDtb_ogkw6jmDrpMV-Et3ZTv8kGiqUXqfFNw4I_ksopmV5RlCt8OPqplj6RZFEXftcDMIJWAhSw'
    }
    
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329q92yl9y', headers = headers)
    clan_json = response.json()
    print(clan_json)

    return render(request, 'index.html',{
        'title' : 'Clan Page',
        'data': clan_json
    })
