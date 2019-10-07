import tkinter as tk
import sys,os
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import name_num_data as nnd
jud=0
jud1=0
name,num,data=nnd.read_data()
data_f="name_num_data.py"
def chack_pass_b():
	global jud
	pass_text=entry1.get()
	if pass_text=="robot":
		root.destroy()
		root.quit()
		jud=1
	else:
		messagebox.showerror("パスワード","パスワードが違います")
root=tk.Tk()
root.title("名前,学籍番号")
root.geometry("300x100")
label1=tk.Label(root,text="password:")
label1.pack(side="left")
entry1=tk.Entry(root,bd=1)
entry1.pack(side="left")
pass_b=tk.Button(root,text="決定",command=chack_pass_b)
pass_b.pack(side="left")
menubar=tk.Menu(root)
menuact=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="menu",menu=menuact)
root.config(menu=menubar)
root.mainloop()
if jud==1:
	def search():
		global num,var,data
		name,num,data=nnd.read_data()
		name,num,data=nnd.reader_data(name,num,data)
		for i in range(data):
			if combo.get()==name[i]:
				var.set(num[i])
	def decide_b():
		global name,num,jud1,ent_name1,ent_num1,data
		name,num,data=nnd.read_data()
		name,num,data=nnd.reader_data(name,num,data)
		if ent_name1.get()=="" or ent_num1.get()=="":
			messagebox.showerror("エラー","名前か学籍番号の入力がありません")
		else:
			nnd.write_data(ent_name1.get(),ent_num1.get())
			ent_name1.delete(0,tk.END)
			ent_num1.delete(0,tk.END)
	def edit_data():
		global name,num,ent_name1,ent_num1,data
		root2=tk.Toplevel()
		root2.title("編集")
		root2.geometry("500x300")
		name,num,data=nnd.reader_data(name,num,data)
		lab_name1=tk.Label(root2,text="名前")
		lab_num1=tk.Label(root2,text="学籍番号")
		lab_name1.place(x=20,y=50)
		lab_num1.place(x=20,y=80)
		ent_name1=tk.Entry(root2,bd=1)
		ent_name1.place(x=50,y=50)
		ent_num1=tk.Entry(root2,bd=1)
		ent_num1.place(x=80,y=80)
		dec_b=tk.Button(root2,text="決定",command=decide_b)
		dec_b.place(x=60,y=150)
		root2.mainloop()
	def update_name():
		global name,num,data,combo
		name,num,data=nnd.read_data()
		name,num,data=nnd.reader_data(name,num,data)
		combo=ttk.Combobox(root1,state="readonly")
		combo["values"]=name
		combo.current(0)
		combo.place(x=50,y=50)
	def delete_b():
		global name,num,data,combo,root3
		for i in range(data):
			if combo.get()==name[i]:
				name.remove(name[i])
				num.remove(num[i])
				data=data-1
				name,num,data=nnd.writer_data(name,num,data)
				break; 
		root3.quit()
		root3.destroy()
	def delete_data():
		global name,num,data,combo,root3
		name,num,data=nnd.reader_data(name,num,data)
		root3=tk.Toplevel()
		root3.title("削除モード")
		root3.geometry("500x300")
		del_b=tk.Button(root3,text="削除",command=delete_b)
		del_b.place(x=200,y=48)
		combo=ttk.Combobox(root3,state="readonly")
		combo["values"]=name
		combo.current(0)
		combo.place(x=50,y=50)
		root3.mainloop()
	def exit_root1():
		root1.quit()
		root1.destroy()
	global combo,ent_name1,ent_num1
	root1=tk.Tk()
	root1.title("名前,学籍番号")
	root1.geometry("500x300")
	var=tk.StringVar()
	var.set("")
	name,num,data=nnd.reader_data(name,num,data)
	num_lab=tk.Label(root1,textvariable=var)
	num_lab.place(x=80,y=80)
	name_l=tk.Label(root1,text="名前")
	name_l.place(x=20,y=50)
	num_l=tk.Label(root1,text="学籍番号")
	num_l.place(x=20,y=80)
	ser_b=tk.Button(root1,text="検索",command=search)
	ser_b.place(x=200,y=48)
	up_name_b=tk.Button(root1,text="更新",command=update_name)
	up_name_b.place(x=250,y=48)
	combo=ttk.Combobox(root1,state="readonly")
	combo["values"]=name
	combo.current(0)
	combo.place(x=50,y=50)
	menubar=tk.Menu(root1)
	menuact=tk.Menu(menubar,tearoff=0)
	menuact.add_command(label="編集",command=edit_data)
	menuact.add_command(label="削除",command=delete_data)
	menuact.add_command(label="終了",command=exit_root1)
	menubar.add_cascade(label="メニュー",menu=menuact)
	root1.config(menu=menubar)
	root1.mainloop()