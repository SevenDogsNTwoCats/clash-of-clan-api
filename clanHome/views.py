from django.shortcuts import render
import requests

# Create your views here.

def getClanData(request):
    headers = {
        'Accept': 'application/json',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE4ODgxODBiLWZiZTUtNDU2NS04NDU0LWEzZWI5Zjg4ODc0NSIsImlhdCI6MTY3NDA3MTE2NSwic3ViIjoiZGV2ZWxvcGVyLzcxZjc3OTIwLTg4ODctNTc2ZS05Y2E0LWMyNmU1Y2ExMDEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM0LjIxMS4yMDAuODUiXSwidHlwZSI6ImNsaWVudCJ9XX0.Dzn3PKjnuTG80iW44altpwwUVIYVou9ER0eMqIQUXoxd_vMy4nXjgEPtJbcU6u8IIRXyl8VT457JDxACz9I_9A'
    }
    
    response = requests.get('https://api.clashofclans.com/v1/clans/%2329q92yl9y', headers = headers)
    clan_json = response.json()
    print(clan_json)

    return render(request, 'index.html',{
        'title' : 'Clan Page',
        'data': clan_json
    })
