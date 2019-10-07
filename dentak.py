import tkinter as tk
from tkinter import font
from tkinter import messagebox
import os,sys
x_c=""
code=""
y_c="0"
def show_num(event):
	global x_c
	x_c1=repr(event.char).strip("'")
	if x_c1=="0" and x_c=="0":
		x_c=""
		var.set("入力:0")
	if x_c=="" and x_c1=="0":
		x_c=""
		var.set("入力:0")
	if x_c1=="0" and x_c==".":
		x_c="0."
		var.set("入力:"+x_c)
	if x_c=="" and x_c1==".":
		x_c="0."
		var.set("入力:"+x_c)
	if x_c=="0" and x_c1!=".":
		x_c=x_c1
		var.set("入力:"+x_c)
	else:
		if "." in x_c:
			if x_c1==".":
				x_c1=""
		x_c=x_c+x_c1
		var.set("入力:"+x_c)
def show_num_b(i):
	def pre():
		global x_c,a_b
		x_c1=str(i)
		if x_c=="0" and x_c1=="0":
			x_c=""
			var.set("入力:0")
		if x_c=="" and x_c1=="0":
			x_c=""
			var.set("入力:0")
		if x_c1=="0" and x_c==".":
			x_c="0."
			var.set("入力:"+x_c)
		if x_c=="" and x_c1==".":
			x_c="0."
			var.set("入力:"+x_c)
		if x_c=="0" and x_c1!=".":
			x_c=x_c1
			var.set("入力:"+x_c)
		else:
			if "." in x_c:
				if x_c1==".":
					x_c1=""
			x_c=x_c+x_c1
			var.set("入力:"+x_c)
	return pre
def show_delete(event):
	global x_c
	if x_c=="":
		var.set("入力:0")
	else:
		x=float(x_c)
		x_c=x_c[:-1]
		var.set("入力:"+x_c)
def show_delete_b():
	global x_c
	if x_c=="":
		var.set("入力:0")
	else:
		x_c=x_c[:-1]
		var.set("入力:"+x_c)
def show_code(event):
	global code,y,x_c,y_c
	code=repr(event.char).strip("'")
	if x_c=="":
		x=0
	else:
		x=float(x_c)
	y=float(y_c)
	if code=="+":
		if (y+x)<-0.00000001 and (y+x)>-99999999 or (y+x)<99999999 and (y+x)>=0.00000001 or (y+x)==0:
			y_c=str(y+x)
			x_c=""
			var.set("入力:"+"0")
		else:
			messagebox.showerror("桁数オーバー","桁数が多すぎます")
	if code=="-":
		if (y-x)<-0.00000001 and (y-x)>-99999999 or (y-x)<99999999 and (y-x)>=0.00000001 or (y-x)==0:
			y_c=str(y-x)
			x_c=""
			var.set("入力:"+"0")
		else:
			messagebox.showerror("桁数オーバー","桁数が多すぎます")
	if code=="*":
		if (y*x)<-0.00000001 and (y*x)>-99999999 or (y*x)<99999999 and (y*x)>=0.00000001 or (y*x)==0:
			y_c=str(y*x)
			x_c=""
			var.set("入力:"+"0")
		else:
			messagebox.showerror("桁数オーバー","桁数が多すぎます")
	if code=="/":
		try:
			if (y/x)<-0.00000001 and (y/x)>-99999999 or (y/x)<99999999 and (y/x)>=0.00000001 or (y/x)==0:
				y_c=str(y/x)
				x_c=""
				var.set("入力:"+"0")
			else:
				messagebox.showerror("桁数オーバー","桁数が多すぎます")
		except ZeroDivisionError:
			messagebox.showerror("割り算エラー","割れない数です！")
	var2.set("合計:"+y_c)
def show_code_b(code):
	def pre_2():
		global y,x_c,y_c
		if x_c=="":
			x=0
		else:
			x=float(x_c)
		y=float(y_c)
		if code=="+":
			if (y+x)<-0.00000001 and (y+x)>-99999999 or (y+x)<99999999 and (y+x)>=0.00000001 or (y+x)==0:
				y_c=str(y+x)
				x_c=""
				var.set("入力:"+"0")
			else:
				messagebox.showerror("桁数オーバー","桁数が多すぎます")
		if code=="-":
			if (y-x)<-0.00000001 and (y-x)>-99999999 or (y-x)<99999999 and (y-x)>=0.00000001 or (y-x)==0:
				y_c=str(y-x)
				x_c=""
				var.set("入力:"+"0")
			else:
				messagebox.showerror("桁数オーバー","桁数が多すぎます")
		if code=="*":
			if (y*x)<-0.00000001 and (y*x)>-99999999 or (y*x)<99999999 and (y*x)>=0.00000001 or (y*x)==0:
				y_c=str(y*x)
				x_c=""
				var.set("入力:"+"0")
			else:
				messagebox.showerror("桁数オーバー","桁数が多すぎます")
		if code=="/":
			try:
				if (y/x)<-0.00000001 and (y/x)>-99999999 or (y/x)<99999999 and (y/x)>=0.00000001 or (y/x)==0:
					y_c=str(y/x)
					x_c=""
					var.set("入力:"+"0")
				else:
					messagebox.showerror("桁数オーバー","桁数が多すぎます")
			except ZeroDivisionError:
				messagebox.showerror("割り算エラー","割れない数です！")
		var2.set("合計:"+y_c)
	return pre_2
def ac():
	global x_c,y_c
	x_c=""
	y_c="0"
	var.set("入力:"+"0")
	var2.set("合計:"+"0")
def exit(event):
	root.quit()
a_b=[0,0,0,0,0,0,0,0,0,0,0,0]
code_b=[0,0,0,0,0]
root=tk.Tk()
root.title("簡易電卓")
root.geometry("350x400")
var=tk.StringVar()
var.set("入力:"+"0")
var2=tk.StringVar()
var2.set("合計:"+"0")
menubar=tk.Menu(root)
commandmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="コマンドリスト",menu=commandmenu)
commandmenu.add_command(label="初期化",command=ac)
font1=font.Font(size=20)
canvas=tk.Canvas(root,bg="black",height=70,width=410)
canvas.pack(side="top")
frame=tk.Frame(root,width=350,height=400)
for i in range(10):
	frame.bind(i,show_num)
	a_b[i]=tk.Button(root,text=i,command=show_num_b(i),width=4,height=1,font=font1)
for i in range(3):
	for j in range(3):
		a_b[i*3+j+1].place(x=j*70,y=210-i*50)
a_b[10]=tk.Button(root,text="C",command=ac,font=font1)
a_b[11]=tk.Button(root,text="del",command=show_delete_b,font=font1)
a_b[0].place(x=0,y=260)
a_b[10].place(x=70,y=260)
a_b[11].place(x=150,y=260)
code_b[0]=tk.Button(root,text="+",command=show_code_b("+"),font=font1)
code_b[1]=tk.Button(root,text="-",command=show_code_b("-"),font=font1)
code_b[2]=tk.Button(root,text="*",command=show_code_b("*"),font=font1)
code_b[3]=tk.Button(root,text="/",command=show_code_b("/"),font=font1)
code_b[4]=tk.Button(root,text=".",command=show_num_b("."),font=font1)
for i in range(4):
	code_b[i].place(x=210,y=110+i*50)
code_b[4].place(x=110,y=260)
frame.bind(".",show_num)
frame.bind("+",show_code)
frame.bind("-",show_code)
frame.bind("*",show_code)
frame.bind("/",show_code)
frame.bind("<BackSpace>",show_delete)
frame.bind("q",exit)
label1=tk.Label(root,textvariable=var,fg="white",bg="black",font=font1)
label1.place(x=2,y=2)
label2=tk.Label(root,textvariable=var2,fg="white",bg="black",font=font1)
label2.place(x=2,y=32)
frame.focus_set()
frame.pack(side="top")
root.config(menu=menubar)
root.mainloop()