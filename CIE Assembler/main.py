try:
    from Tkinter import *
except:
    from tkinter import *
from toolbar import *
from editorButtons import *
from editor import *
from ramDisplay import *
from errorLine import *


if __name__ == "__main__":
    root = Tk()
    root.title("CIE Assembler virtual machine")
    root.geometry("1200x800")
    root.resizable(False, False)

    toolBar = ToolBar(root)
    editButtons = EditorButtons(root, 0,0)
    editor = Editor(root,1,0)
    ramDisplay = RamDisplay(root, 1,2)
    errorBar = ErrorBar(root,3,0)
    editor.rep = errorBar.update
    root.bind("<F5>", editor.lexical_analysis)





    root.mainloop()
