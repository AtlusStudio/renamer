import re

# 假设name变量包含待匹配的字符串
name = "[提取这个内容]这是一些其他的文本[不提取这个内容]"
print(name)

# 使用修正后的正则表达式提取第一个]到第二个[或(之间的内容
result = re.search(r'\](.*?)\[[\(\)]', name)
if result:
    extracted_content = result.group(1)
    print(extracted_content)
