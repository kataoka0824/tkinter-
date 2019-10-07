import tkinter as tk
import csv
import pandas as pd
from tkinter import messagebox
from tkinter import font
f_name="key_code.csv"
def exit_root():
	root.quit()
	root.destroy()
def exit_root1():
	root1.quit()
	root1.destroy()
def show_text():
	global root1,text_1,l1
	l1=[]
	with open(f_name,mode="r") as f:
		global key_1st,key_2nd,text_2
		reader=csv.reader(f)
		l=[row for row in reader]
		key_1st=l[0]
		key_2nd=l[2]
		text_2="".join(l[4])
		l2=list(text_2)
		len_2=len(text_2)
		for i in range(len_2):
			for j in range(len(key_2nd)):
				if l2[i]==key_2nd[j]:
					l1.append(key_1st[j])
			if l2[i]=='"':
				l1.append('"')
			if l2[i]==',':
				l1.append(',')
			if l2[i]=='\n':
				l1.append('\n')
		text_1="".join(l1)
	root1=tk.Toplevel()
	root1.title("受信テキスト")
	root1.geometry("400x400")
	label1=tk.Label(root1,text="受信テキスト",font=font1)
	label1.pack(side="top")
	var=tk.StringVar()
	var.set(text_1)
	label2=tk.Label(root1,textvariable=var,font=font2)
	label2.pack(side="top")
	button2=tk.Button(root1,text="終了",command=exit_root1)
	button2.pack(side="bottom")
	root1.mainloop()
with open(f_name,mode="r") as f:
	global key_1st,key_2nd,text_2,l1
	l1=[]
	reader=csv.reader(f)
	l=[row for row in reader]
	key_1st=l[0]
	key_2nd=l[2]
	text_2="".join(l[4])
	l2=list(text_2)
	len_2=len(text_2)
	for i in range(len_2):
		for j in range(len(key_2nd)):
			if l2[i]==key_2nd[j]:
				l1.append(key_1st[j])
		if l2[i]=='"':
			l1.append('"')
		if l2[i]==',':
			l1.append(',')
		if l2[i]=='\n':
			l1.append('\n')
	text_1="".join(l1)
root=tk.Tk()
root.title("暗号テキスト⇒受信テキスト")
root.geometry("100x100")
label1_1=tk.Label(root,text="テキストの受信")
label1_1.pack(side="top")
font1=font.Font(size=30)
font2=font.Font(size=25)
button1_1=tk.Button(root,text="終了",command=exit_root)
button1_1.pack(side="bottom")
button1=tk.Button(root,text="受信",command=show_text)
button1.pack(side="bottom")
root.mainloop()