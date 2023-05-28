# tk实现小程序
# 点击按钮添加移除

import tkinter as tk
from tkinter import ttk

def add_item():
    item_text = entry.get()
    if item_text:
        tree.insert("", tk.END, values=(item_text, "Value 1", "Value 2"))

def remove_item():
    selected_items = []
    for child in tree.get_children():
        checkbox_state = tree.set(child, "#0")
        if checkbox_state == "1":
            selected_items.append(child)
    
    for item in selected_items:
        tree.delete(item)

root = tk.Tk()
root.title("TreeView Demo")

# 创建TreeView
tree = ttk.Treeview(root)
tree.pack()

# 添加列
tree["columns"] = ("1", "2")
tree.column("#0", width=50, minwidth=50, stretch=tk.NO)
tree.column("1", width=150, minwidth=150, stretch=tk.NO)
tree.column("2", width=150, minwidth=150, stretch=tk.NO)

# 添加列标题
tree.heading("#0", text="Select")
tree.heading("1", text="Column 1")
tree.heading("2", text="Column 2")

# 添加示例数据
tree.insert("", tk.END, values=("Item 1", "Value 1", "Value 2"))
tree.insert("", tk.END, values=("Item 2", "Value 3", "Value 4"))

# 添加项目的输入框和按钮
entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.pack()

root.mainloop()
