import requests
import json
import pandas as pd
s_id=[10,11,20,25,8]
t_id=[31,28,30,29]
for j in s_id:
    for i in t_id:
        url = "https://feeds.prokabaddi.com/SI/{}".format(j)+"/Squad/{}.json".format(i)
        print(url)
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data=response.text
        file1 = open("myfile.json", "w")
        file1.write(data)
        file1.close()

        with open('myfile.json') as f:
            jd=json.load(f)
        player_id=[]
        f=jd['squads']['squad']['players']

        for i in range(0,len(f)):
            ps=jd['squads']['squad']['players'][i]['player_id']

            player_id.append(ps)

        f2= open("player_id.txt","a")
        f2.write(str(player_id))
        f2.close()