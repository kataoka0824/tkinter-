import tkinter as tk
import csv
import pandas as pd
from tkinter import messagebox
from tkinter import font
f_name="key_code.csv"
jud=0
with open(f_name,mode="r") as f:
	global key_1st,key_2nd
	reader=csv.reader(f)
	l=[row for row in reader]
	key_1st=l[0]
	key_2nd=l[2]
def send_text():
	global text_1,text_2,jud
	text_1=text1.get("1.0","end -1c")
	if text_1=="":
		messagebox.showerror("入力エラー","入力がありません")
	else:
		l2=[]
		l1=list(text_1)
		len_1=len(text_1)
		for i in range(len_1):
			for j in range(len(key_1st)):
				if l1[i]==key_1st[j]:
					l2.append(key_2nd[j])
			if l1[i]=='"':
				l2.append('\"')
			if l1[i]==',':
				l2.append(',')
			if l1[i]=='\n':
				l2.append('\n')
		text_2="".join(l2)
		with open(f_name,mode="w") as f:
			writer=csv.writer(f)
			writer.writerow(key_1st)
			writer.writerow(key_2nd)
			writer.writerow(text_2)
		show_text2()
def exit_root():
	root.quit()
	root.destroy()
def exit_root1():
	global root1
	root1.quit()
	root1.destroy()
def exit_root2():
	global root2
	root2.quit()
	root2.destroy()
def show_text1():
	global text_1,root2
	root2=tk.Toplevel()
	root2.title("元テキスト")
	root2.geometry("400x400")
	label3_1=tk.Label(root2,text="元テキスト",font=font1)
	label3_1.pack(side="top")
	var1=tk.StringVar()
	var1.set(text_1)
	label3_2=tk.Label(root2,textvariable=var1,font=font2)
	label3_2.pack(side="top")
	button3=tk.Button(root2,text="終了",command=exit_root2)
	button3.pack(side="bottom")
	root2.mainloop()
def show_text2():
	global root1,var2,font1,font2
	root1=tk.Toplevel()
	root1.title("暗号テキスト")
	root1.geometry("400x400")
	font1=font.Font(size=30)
	font2=font.Font(size=25)
	label2_1=tk.Label(root1,text="暗号テキスト",font=font1)
	label2_1.pack(side="top")
	var2=tk.StringVar()
	var2.set(text_2)
	label2_2=tk.Label(root1,textvariable=var2,font=font2)
	label2_2.pack(side="top")
	button2_1=tk.Button(root1,text="終了",command=exit_root1)
	button2_1.pack(side="bottom")
	button2=tk.Button(root1,text="元テキスト",command=show_text1)
	button2.pack(side="bottom")
	root1.mainloop()
root=tk.Tk()
root.title("元テキスト⇒暗号テキスト")
root.geometry("500x300")
label1=tk.Label(root,text="送信コード")
label1.pack(side="left")
text1=tk.Text(root,bd=1,height=5,width=30)
text1.pack(side="left")
button1=tk.Button(root,text="送信",command=send_text)
button1.pack(side="left")
button1_1=tk.Button(root,text="終了",command=exit_root)
button1_1.place(x=230,y=270)
root.mainloop()