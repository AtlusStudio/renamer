# import ctypes
import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD

# ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

class RenamerGUI(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        # 高分屏缩放
        # self.tk.call('tk', 'scaling', ScaleFactor/75)

        # 窗口标题
        self.title("renamer")

        # 窗口居中
        width = 1000
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        # self.resizable(width=False, height=False)

        # 创建表格
        # 设置项目的左右间距
        ttk.Style().configure("pd.Treeview", padding=(5, 0))

        table_columns = {"文件名":280,"中文名":280,"重命名":380}
        self.table_files = ttk.Treeview(self, show="headings", columns=list(table_columns), selectmode="browse", style="pd.Treeview")
        self.table_files.pack(fill="x", padx="25", pady="25")


        for text, width in table_columns.items():
            self.table_files.heading(text, text=text, anchor='center')
            self.table_files.column(text, width=width, anchor='w', stretch=False)

        

        # vbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.table_files.yview)
        # self.table_files.configure(yscrollcommand=vbar.set)
        # #tree.grid(row=0, column=0, sticky=NSEW)
        # vbar.pack(fill="x", padx="25", pady="25")




win = RenamerGUI()