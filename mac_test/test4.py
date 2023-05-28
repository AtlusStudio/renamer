"""
本代码由[Tkinter布局助手]生成
当前版本:3.4.2
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *
from typing import Dict

class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_table_li432jpn"] = self.__tk_table_li432jpn(self)
        self.widget_dic["tk_label_frame_li434100"] = self.__tk_label_frame_li434100(self)
        self.widget_dic["tk_label_li43598d"] = self.__tk_label_li43598d(self)
        self.widget_dic["tk_button_li4362dq"] = self.__tk_button_li4362dq(self)
        self.widget_dic["tk_button_li438t26"] = self.__tk_button_li438t26(self)
        self.widget_dic["tk_progressbar_li43fe50"] = self.__tk_progressbar_li43fe50(self)
        self.widget_dic["tk_input_li43gwo7"] = self.__tk_input_li43gwo7(self)
        self.widget_dic["tk_button_li4cctpt"] = self.__tk_button_li4cctpt(self)

    def __win(self):
        self.title("renamer")
        # 设置窗口大小、居中
        width = 1000
        height = 620
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)

    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
        
    def __tk_table_li432jpn(self,parent):
        # 表头字段 表头宽度
        columns = {"ID":189,"字段#1":284,"字段#2":474}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=25, y=70, width=950, height=250)
        
        return tk_table

    def __tk_label_li43598d(self,parent):
        label = Label(parent,text="命名格式",anchor="center", )
        label.place(x=30, y=20, width=66, height=30)
        return label

    def __tk_button_li4362dq(self,parent):
        btn = Button(parent, text="开始识别", takefocus=False,)
        btn.place(x=780, y=570, width=90, height=30)
        return btn

    def __tk_button_li438t26(self,parent):
        btn = Button(parent, text="重命名全部", takefocus=False,)
        btn.place(x=890, y=570, width=90, height=30)
        return btn

    def __tk_progressbar_li43fe50(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL, )
        progressbar.place(x=20, y=570, width=733, height=18)
        return progressbar

    def __tk_input_li43gwo7(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=110, y=20, width=751, height=30)
        return ipt

    def __tk_button_li4cctpt(self,parent):
        btn = Button(parent, text="应用", takefocus=False,)
        btn.place(x=880, y=20, width=92, height=30)
        return btn

    def __tk_label_frame_li434100(self,parent):
        frame = LabelFrame(parent,)
    
        frame.configure(text="修改关联条目")
        frame.place(x=20, y=360, width=942, height=182)

        self.widget_dic["tk_button_li49z10i"] = self.__tk_button_li49z10i(frame)
        self.widget_dic["tk_label_li4a0d4j"] = self.__tk_label_li4a0d4j(frame)
        self.widget_dic["tk_input_li4a0p6p"] = self.__tk_input_li4a0p6p(frame)
        self.widget_dic["tk_frame_li4cmiox"] = self.__tk_frame_li4cmiox(frame)
        self.widget_dic["tk_button_li4cs66a"] = self.__tk_button_li4cs66a(frame)
        self.widget_dic["tk_frame_li4dzyr3"] = self.__tk_frame_li4dzyr3(frame)
        return frame
    def __tk_button_li49z10i(self,parent):
        btn = Button(parent, text="查看网页", takefocus=False,)
        btn.place(x=350, y=120, width=90, height=30)
        return btn

    def __tk_label_li4a0d4j(self,parent):
        label = Label(parent,text="更改ID",anchor="center", )
        label.place(x=140, y=120, width=43, height=30)
        return label

    def __tk_input_li4a0p6p(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=190, y=120, width=150, height=30)
        return ipt

    def __tk_button_li4cs66a(self,parent):
        btn = Button(parent, text="更改ID", takefocus=False,)
        btn.place(x=450, y=120, width=90, height=30)
        return btn

    def __tk_frame_li4cmiox(self,parent):
        frame = Frame(parent,)
        frame.place(x=20, y=10, width=104, height=136)

        return frame

    def __tk_frame_li4dzyr3(self,parent):
        frame = Frame(parent,)
        frame.place(x=140, y=10, width=778, height=92)

        self.widget_dic["tk_label_li4e061i"] = self.__tk_label_li4e061i(frame)
        self.widget_dic["tk_label_li4e0kun"] = self.__tk_label_li4e0kun(frame)
        self.widget_dic["tk_label_li4e108n"] = self.__tk_label_li4e108n(frame)
        self.widget_dic["tk_label_li4e128f"] = self.__tk_label_li4e128f(frame)
        self.widget_dic["tk_label_li4e1frr"] = self.__tk_label_li4e1frr(frame)
        self.widget_dic["tk_label_li4e1lrq"] = self.__tk_label_li4e1lrq(frame)
        return frame

    def __tk_label_li4e061i(self,parent):
        label = Label(parent,text="当前选择",anchor="center", )
        label.place(x=0, y=0, width=80, height=30)
        return label

    def __tk_label_li4e0kun(self,parent):
        label = Label(parent,text="[VCB-Studio] Yuusha Party o Tsuihou Sareta Beast Tamer, Saikyoushu no Nekomimi Shoujo to Deau [Ma10p_1080p]",anchor="center", )
        label.place(x=80, y=0, width=671, height=30)
        return label

    def __tk_label_li4e108n(self,parent):
        label = Label(parent,text="对应番剧",anchor="center", )
        label.place(x=0, y=30, width=80, height=30)
        return label

    def __tk_label_li4e128f(self,parent):
        label = Label(parent,text="中文译名",anchor="center", )
        label.place(x=0, y=60, width=80, height=30)
        return label

    def __tk_label_li4e1frr(self,parent):
        label = Label(parent,text="勇者パーティーを追放されたビーストテイマー、最強種の猫耳少女と出会う",anchor="center", )
        label.place(x=80, y=30, width=422, height=30)
        return label

    def __tk_label_li4e1lrq(self,parent):
        label = Label(parent,text="被勇者队伍开除的驯兽师，邂逅最强种猫耳少女",anchor="center", )
        label.place(x=80, y=60, width=272, height=30)
        return label

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def acdseey(self,evt):
        print("<Button-1>事件未处理",evt)
        
    def __event_bind(self):
        self.widget_dic["tk_button_li4cctpt"].bind('<Button-1>',self.acdseey)
        
if __name__ == "__main__":
    win = Win()
    win.mainloop()
