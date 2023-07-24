import unicodedata

def is_katakana(text):
    for char in text:
        if 'KATAKANA' not in unicodedata.name(char):
            return False
    return True

# 测试
text1 = "イノセンス" # 全部是片假名

print(is_katakana(text1))  # 输出 True