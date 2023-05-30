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

    js = {
        'query': query,
        'variables': {'id': name},
    }

    print(f"正在向Anilist请求{name}的数据")

    # 3次重试机会，避免网络原因导致请求失败
    retry = 0
    while retry < 3:
        response = requests.post('https://graphql.anilist.co', json=js, headers=headers)

        if response.status_code == 200:
            result = json.loads(response.text.encode().decode('unicode_escape'))
            return result

        # 若请求失败，等待0.5秒重试
        else:
            print("Anilist请求失败，重试" + str(retry + 1))
            time.sleep(0.5)
            retry += 1

    print(f"在Anilist中请求{name}数据失败")







# name = "atashi ni Tenshi ga Maiorita! Precious Friends"
# result = anilist(name)
# print(result)