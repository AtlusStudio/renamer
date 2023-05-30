import re



# 将输入的动画文件夹 file_name 格式化为动画名 romaji_name
def get_romaji_name(name, ignored):

    # 将指定字符加入忽略列表
    pattern_ignored = '|'.join(ignored)

    # 更新 file_name 为忽略后的名字
    file_name = re.sub(pattern_ignored, '', name)

    # 匹配第一个 ] 开始，到第一个 [ 或 (，若无上述内容，则匹配至末尾
    pattern_romaji = r"\](.*?)(?:\[|\(|$)"

    # 使用正则表达式匹配并提取内容
    result = re.search(pattern_romaji, file_name)

    # 输出提取的内容
    # 如果没匹配到内容就返回 False
    if result:
        # 使用 strip() 去除首尾空格
        romaji_name = result.group(1).strip()
    else:
        romaji_name = False
        print(f"非标准的动画格式: {name}")

    return romaji_name



file_name = "[Moozzi2] Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S2 BD-BOX[ x265-10Bit Ver. ] - TV + SP"
ignored_strings = ["BD-BOX", "BD"]

romaji_name = get_romaji_name(file_name, ignored_strings)
print(romaji_name)
