from tkinter import *
#pip install pillow
from PIL import Image, ImageTk

import PIL
import tkinter as tk
import os
import jikan_hook


class UI:
	
	def __init__(self,master):
		frame = Frame(master, bg="#aedb9f")
		frame.pack()

		self.label1 = Label(frame, text = "---------This App can recommend other Animes that you may like---------", fg = "red", font='Helvetica 13 bold', bg="#aedb9f")
		self.label1.pack()

		self.label2 = Label(frame, text = "Enter The ID of An Anime You Watch ", font='Helvetica 10 bold', bg="#aedb9f")
		self.label2.pack()

		self.input = Entry(frame, font='Helvetica 8 bold')
		self.input.pack()

		self.space = Label(frame, bg="#aedb9f")
		self.space.pack()

		self.sumbit = Button(frame, text = "Submit", command = self.search)
		self.sumbit.pack()
		
		self.space = Label(frame, bg="#aedb9f")
		self.space.pack()

		self.result = Text(frame, wrap = WORD, font='Helvetica 10 bold')
		self.result.pack(fill = Y)

		imgfile = Image.open("92325.jpg")
		img = PhotoImage(imgfile)
		self.label_img = Label(master, image = img)
		self.label_img.image = img
		self.label_img.pack()

	def search(self):
		char_id = self.input.get()
		img = jikan_hook.pull_img(char_id)
		
		self.result.delete(0.0, END)
		self.result.insert(0.0,img)
		print(img)
		#clears old data and outputs new recc data


root = Tk()
root.title("AnimeRecommendation")
root.configure(background="#aedb9f")
root.geometry("600x400")
App = UI(root)
root.mainloop()