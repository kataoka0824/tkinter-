import tkinter as tk
from tkinter import messagebox
from tkinter import font
import random
jud=0
def exit_root1():
	root1.quit()
	root1.destroy()
def exit_root():
	root.quit()
	root.destroy()
def decide_1():
	global o_n,x_n,jud
	if str.isdecimal(e_o.get()) and str.isdecimal(e_x.get()):
		o_n=int(e_o.get())
		x_n=int(e_x.get())
		if o_n==0 or x_n==0:
			messagebox.showerror("エラー","あたりかはずれが0です")
		elif o_n+x_n<=20:
			jud=1
			exit_root1()
		else:
			messagebox.showerror("エラー","あたり、はずれが20より大きいです")
	else:
		messagebox.showerror("エラー","数字以外が入力されました")
def jud_ox(i_jud):
	global rand
	def x1():
		if i_jud in rand:
			messagebox.showinfo("あたり！","あたり！")
		else:
			messagebox.showinfo("はずれ","はずれ")
	return x1
root1=tk.Tk()
root1.title("あたり、はずれ")
root1.geometry("400x200")
label_o=tk.Label(root1,text="あたりの数")
label_o.pack(side="top")
e_o=tk.Entry(root1,bd=1)
e_o.pack(side="top")
label_x=tk.Label(root1,text="はずれの数")
label_x.pack(side="top")
e_x=tk.Entry(root1,bd=1)
e_x.pack(side="top")
exit1_b=tk.Button(root1,text="終了",command=exit_root1)
exit1_b.pack(side="bottom")
decide_b=tk.Button(root1,text="決定",command=decide_1)
decide_b.pack(side="bottom")
root1.mainloop()
if jud==1:
	list=[]
	i1=o_n+x_n
	i2=i1//5
	j2=i1%5
	for i in range(o_n+x_n):
		list.append(i+1)
	rand=random.sample(list,o_n)
	kuji_b=[]
	root=tk.Tk()
	root.title("くじ")
	root.geometry("500x500")
	font1=font.Font(size=30)
	label1=tk.Label(root,text="くじ",font=font1)
	label1.pack(side="top")
	for i in range(i1):
		i_jud=i+1
		kuji_b.append(tk.Button(root,text=str(i+1),width=4,height=2,command=jud_ox(i_jud)))
	for i in range(i2+1):
		if i<i2:
			for j in range(5):
				kuji_b[5*i+j].place(x=j*70+90,y=i*70+100)
		else:
			for j in range(j2):
				kuji_b[5*i+j].place(x=j*70+90,y=i*70+100)
	exit_b=tk.Button(root,text="終了",command=exit_root)
	exit_b.pack(side="bottom")
	root.mainloop()