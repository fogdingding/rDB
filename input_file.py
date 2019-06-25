import time
import test
def get_dd():
	dd = {"@key_1:" : 0,"@key_2:" : 0,"@key_3:" : 0,"@end : 0" }
	dreturn dd
def get_ddc():
	dd = {"@key_1:" : "","@key_2:" : "","@key_3:" : "","@end : """ }
	dreturn dd
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
				if(line.find("@key_1:")!=-1):
				ddc["key_1:"] = line
				dd["@key_1"] = 1
				continue
				if(line.find("@key_2:")!=-1):
				ddc["key_2:"] = line
				dd["@key_2"] = 1
				continue
				if(line.find("@key_3:")!=-1):
				ddc["key_3:"] = line
				dd["@key_3"] = 1
				flag = 1
				continue
	ticks = time.time()
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	print ("完成讀取，總共有幾組DATA:{}".format(len(data)))
	print("請下寫入檔案指令")
	print("write_DB_file()")
	return data
def url_index_DB(data):
	file_name = "測試用"
	sSkipList = test.SkipList()
	print("開使建立INDEX的時間")
	ticks = time.time()
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	for i in range(len(data)):
		sSkipList.insert(data[i]["@key_1:"],data[i]["@key_2:"],data[i]["@key_3:"],)
	ticks = time.time()
	print("完成建立INDEX的時間")
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	return sSkipList
def write_DB_file(data):
	print("寫入時間是很久的唷，請去寫其他功課吧！")
	print("開始寫入檔案的時間")
	name_number = 0
	file_name = "DB_{}.txt".format(name_number)
	sSkipList = test.SkipList()
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
