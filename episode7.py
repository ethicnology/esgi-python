#episode 7
import math
import re
import tkinter as tk


class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.source = tk.Label(self)
    self.source["text"] = "Source :"
    self.source.pack(side="top")

    self.input = tk.Entry(self)
    self.input.pack(side="top")

    self.hi_there = tk.Button(self)
    self.hi_there["text"] = "Clean"
    self.hi_there["command"] = self.say_hi
    self.hi_there.pack(side="top")

    self.dest = tk.Label(self)
    self.dest["text"] = "Destination :"
    self.dest.pack(side="top")

    self.inputleft = tk.Entry(self)

    self.inputleft.pack(side="left")

    self.inputright = tk.Entry(self)
    self.inputright.pack(side="right")

  def say_hi(self):
    str = self.input.get()
    temp = re.findall(r'\d+', str)
    res = list(map(int, temp))
    self.inputleft.insert(0, res[0])
    self.inputleft.insert("end" , "cm")
    self.inputright.insert(0, res[1])
    self.inputright.insert("end", "cm")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
