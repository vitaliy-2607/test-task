from telethon.sync import TelegramClient
import json
import pandas as pd

random_names = pd.read_csv('names.csv')



api_id = 17186452
api_hash = 'b9c1d1314730faa0d325fb3e4415e6e5'


with TelegramClient('anon', api_id, api_hash) as client:
    participants_dict = {}
    for participant in client.iter_participants('pyflood'):
        participants_dict[participant.username] = {
            "Name": participant.first_name,
            "Last_name": participant.last_name
        }



    with open('members_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(participants_dict, json_file, ensure_ascii=False, indent=2)

men = set(random_names[random_names['Gender'] == 'male']['GivenName'])
women = set(random_names[random_names['Gender'] == 'female']['GivenName'])

list_men = []
list_women = []
list_other = []

for nick, name in participants_dict.items():
    if name["Name"] in men:
        list_men.append(nick)
    if name["Name"] in women:
        list_women.append(nick)
    else:
        list_other.append(nick)

with open('men.txt', 'w') as f:
    for username in list_men:
        f.write(str(username) + '\n')

with open('women.txt', 'w') as f:
    for username in list_women:
        f.write(str(username) + '\n')

with open('other.txt', 'w') as f:
    for username in list_other:
        f.write(str(username) + '\n')