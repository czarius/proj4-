import regex as re
import urllib as urllib
import json
import requests

def script(usr):
    user = re.sub('[^a-zA-Z0-9\n\.]', ' ', usr)
    #ip="3.135.224.122"
    ip="54.90.53.130"
    inurl = 'http://'+ip+':8983/solr/P4/select?q='+urllib.parse.quote_plus("+".join(user.split()))+'&defType=dismax&qf=full_text&wt=json&indent=true&rows=500'
        #fl=id%2Cscore%2Cfull_text%2Ctext
    data=requests.get(inurl,verify=False)
    data.encoding = 'utf-8' 
    data = data.json()
    data=data['response']['docs']
    with open('./P4.json', 'w+') as f:
        json.dump(data, f, indent=4)