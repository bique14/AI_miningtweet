import facebook
import os
import json
import requests

if __name__ == '__main__':
    page_id = ["thammasat.uni","ScienceThammasat","ThammasatUniversity","100009775518215","tumailameung","1622143711350441"]
    token = 'EAACEdEose0cBAEcBtYugfZC6cyZCWSaZCNcPZBBpvZBzPj11BPQGmLfZAjZAS2Uh26DDK5sCHj3ZCzksfvvlB6gStKFDFGrCFi5Qv6ax1wr4qkKrZBoC1ZBIlnVh7VEroA6MqbKLCXOvZCROFfaur9Q9REXGUYTK0IAcWoKofeKwK7wS5m9yf91beHLuVK60ccZCHZCUZD'
    graph = facebook.GraphAPI(token)
    while 'true':
        try:
            with open ('my_post.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(posts, ensure_ascii=False)+"\n")
                posts = requests.get(posts['paging']['next'])
        except KeyError:
            break
    print("end!")