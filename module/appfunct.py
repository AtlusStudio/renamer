import os
import re

from module import gui


def drop_print(event):
    paths = event.data

    # 使用正则表达式提取大括号内的内容
    cleaned_paths = re.findall(r'{(.*?)}', paths)
    for path in cleaned_paths:
        # 判断是否为文件夹 若为文件夹则不插入treeview
        if os.path.isdir(path):
            cleaned_name = os.path.basename(os.path.normpath(path))
            gui.win.table_files.insert("", "end", values=(cleaned_name,))