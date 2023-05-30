import requests
import json
import time


# 向Anilist请求数据
def anilist(name):
    headers = {
        'accept': 'application/json',
        'User-Agent': 'akko/bgm-renamer'
    }

    query = '''
    query ($id: String) {
        Media (search: $id, type: ANIME) {
            title {
                native
            }
            format
        }
    }'''

    anilist_json = {
        'query': query,
        'variables': {'id': name},
    }

    anilistresponse = requests.post('https://graphql.anilist.co', json=anilist_json, headers=headers)
    anilistresult = json.loads(anilistresponse.text.encode().decode('unicode_escape'))


    # 如果成功，返回请求的字典内容
    # 如果失败，返回 False
    return anilistresult



name = "atashi ni Tenshi ga Maiorita! Precious Friends"
result = anilist(name)
print(result)