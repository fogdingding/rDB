import time
import create_python
def get_dd():
	dd = {"@url:" : 0,"@title:" : 0,"@viewCount:" : 0,"@end" : 1 }
	return dd
def get_ddc():
	dd = {"@url:" : "","@title:" : "","@viewCount:" : "","@end" : "" }
	return dd
def get_bool(dd):
	for i in dd:
		if (dd[i] == 0):
			return False
	return True
def write_file(file_name,data):
	with open(file_name,'a',encoding='utf-8') as f:
		for line in data:
			f.write(data[line])
		f.write("@\n")
def input_main(file_path):
	data = []
	line_text = ""
	ticks = time.time()
	print("讀取檔案的時間")
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	with open(file_path,encoding='utf-8') as fin:
		flag = 0
		count = 0
		ddc = get_ddc()
		dd = get_dd()
		for line in fin:
			count+=1
			if (get_bool(dd)):
				data.append(ddc)
				ddc = get_ddc()
				dd = get_dd()
				continue
			else:
				if(line.find("@url:")!=-1):
					ddc["@url:"] = line
					dd["@url:"] = 1
					continue
				if(line.find("@title:")!=-1):
					ddc["@title:"] = line
					dd["@title:"] = 1
					continue
				if(line.find("@viewCount:")!=-1):
					ddc["@viewCount:"] = line
					dd["@viewCount:"] = 1
					flag = 1
					continue
	ticks = time.time()
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	print ("完成讀取，總共有幾組DATA:{}".format(len(data)))
	print("請下寫入檔案指令")
	print("write_DB_file()")
	return data
def url_index_DB(data):
	data_len = len(data)
	count = 0
	file_name = "測試用"
	sSkipList = create_python.SkipList()
	print("開使建立INDEX的時間")
	ticks = time.time()
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	for i in range(len(data)):
		if(i%5000==0):
			count+=1
		sSkipList.insert(data[i]["@url:"],"DB_{}.txt".format(count),data[i]["@url:"],data[i]["@title:"],data[i]["@viewCount:"],)
	ticks = time.time()
	print("完成建立INDEX的時間")
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	return sSkipList
def write_DB_file(data):
	print("寫入時間是很久的唷，請去寫其他功課吧！")
	print("開始寫入檔案的時間")
	name_number = 0
	file_name = "DB_{}.txt".format(name_number)
	sSkipList = create_python.SkipList()
	ticks = time.time()
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	for i in range(len(data)):
		if i%5000 == 0:
			name_number +=1
			file_name = "DB_{}.txt".format(name_number)
			print(file_name)
			ticks = time.time()
			print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
		write_file(file_name,data[i])
		sSkipList.insert(data[i]["@url:"],file_name)
	ticks = time.time()
	print("完成寫入檔案時間")
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	return sSkipList
