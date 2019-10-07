import sys
import csv
list_f="name_num_data.csv"
with open(list_f,mode="r") as f:
	global name1,num1,data
	reader=csv.reader(f)
	l=[row for row in reader]
	name1=l[0]
	num1=l[2]
	data=int(l[4][0])
def write_data(ent_name,ent_num):
	global name1,num1,data
	name1,num1,data=reader_data(name1,num1,data)
	name1.append(ent_name)
	num1.append(ent_num)
	data+=1
	with open(list_f,mode="w") as f:
		writer=csv.writer(f)
		writer.writerow(name1)
		writer.writerow(num1)
		writer.writerow(str(data))
def writer_data(name1,num1,data):
	with open(list_f,mode="w") as f:
		writer=csv.writer(f)
		writer.writerow(name1)
		writer.writerow(num1)
		writer.writerow(str(data))
	return name1,num1,data
def reader_data(name1,num1,data):
	with open(list_f,mode="r") as f:
		reader=csv.reader(f)
		l=[row for row in reader]
		name1=l[0]
		num1=l[2]
		data=int(l[4][0])
	return name1,num1,data
def read_data():
	return name1,num1,data
