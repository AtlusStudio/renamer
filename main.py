from tkinterdnd2 import DND_FILES

from module import gui
from module import appfunct



if __name__ == "__main__":

    gui.win.table_files.drop_target_register(DND_FILES)
    gui.win.table_files.dnd_bind('<<Drop>>',appfunct.drop_print)

    gui.win.mainloop()