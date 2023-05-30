import requests

def get_chinese_name(anime_name):
    url = f"https://myanimelist.net/search/all?q={anime_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    start_index = response.text.find('<a class="hoverinfo_trigger fw-b" href="') + len('<a class="hoverinfo_trigger fw-b" href="')
    end_index = response.text.find('">', start_index)
    anime_url = response.text[start_index:end_index]

    response = requests.get(anime_url, headers=headers)
    response.raise_for_status()

    start_index = response.text.find('<span itemprop="name">') + len('<span itemprop="name">')
    end_index = response.text.find('</span>', start_index)
    chinese_name = response.text[start_index:end_index]

    return chinese_name

anime_name = input("请输入动画的英文名：")
chinese_name = get_chinese_name(anime_name)
print(f"动画的中文名是：{chinese_name}")
