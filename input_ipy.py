
# coding: utf-8

# In[76]:


# 完成
def get_import():
    str_import = """import time
import create_python"""
    return str_import


# In[77]:


def get_dd(data):
    
    str_tmp1 = """def get_dd():
\tdd = {"""
    for line in data:
        str_tmp1 += ("""\"@{}:\" : 0,""".format(line))
    str_tmp1+= """\"@end\" : 1"""
    str_tmp2 = """ }
\treturn dd"""
    str_tmp1+=str_tmp2
    return str_tmp1


# In[78]:


def get_ddc(data):
    str_tmp1 = """def get_ddc():
\tdd = {"""
    for line in data:
        str_tmp1 += ("""\"@{}:\" : \"\",""".format(line))
    str_tmp1+= """\"@end\" : \"\""""
    str_tmp2 = """ }
\treturn dd"""
    str_tmp1+=str_tmp2
    return str_tmp1


# In[79]:


def get_bool():
    str_tmp = """def get_bool(dd):
\tfor i in dd:
\t\tif (dd[i] == 0):
\t\t\treturn False
\treturn True"""
    return str_tmp


# In[80]:


def write_file():
    str_tmp = """def write_file(file_name,data):
\twith open(file_name,'a',encoding='utf-8') as f:
\t\tfor line in data:
\t\t\tf.write(data[line])
\t\tf.write("@\\n")"""
    return str_tmp


# In[81]:


def input_main(data):
    str_tmp1 = """def input_main(file_path):
\tdata = []
\tline_text = ""
\tticks = time.time()
\tprint("讀取檔案的時間")
\tprint (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
\twith open(file_path,encoding='utf-8') as fin:
\t\tflag = 0
\t\tcount = 0
\t\tddc = get_ddc()
\t\tdd = get_dd()
\t\tfor line in fin:
\t\t\tcount+=1
\t\t\tif (get_bool(dd)):
\t\t\t\tdata.append(ddc)
\t\t\t\tddc = get_ddc()
\t\t\t\tdd = get_dd()
\t\t\t\tcontinue
\t\t\telse:"""
    count = len(data)
    cnt = 1
    for line in data:
        if count!=cnt:
            str_tmp1+="""
\t\t\t\tif(line.find("@{}:")!=-1):
\t\t\t\t\tddc["@{}:"] = line
\t\t\t\t\tdd["@{}:"] = 1
\t\t\t\t\tcontinue""".format(line,line,line)
            cnt+=1
        else:
            str_tmp1+="""
\t\t\t\tif(line.find("@{}:")!=-1):
\t\t\t\t\tddc["@{}:"] = line
\t\t\t\t\tdd["@{}:"] = 1
\t\t\t\t\tflag = 1
\t\t\t\t\tcontinue""".format(line,line,line)
    str_tmp1+="""
\tticks = time.time()
\tprint (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
\tprint ("完成讀取，總共有幾組DATA:{}".format(len(data)))
\tprint("請下寫入檔案指令")
\tprint("write_DB_file()")
\treturn data"""
    return str_tmp1
        


# In[82]:


def url_index_DB(data):
    flag = 0
    str_tmp1 = """def url_index_DB(data):
\tdata_len = len(data)
\tcount = 0
\tfile_name = "測試用"
\tsSkipList = create_python.SkipList()
\tprint("開使建立INDEX的時間")
\tticks = time.time()
\tprint (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
\tfor i in range(len(data)):
\t\tif(i%5000==0):
\t\t\tcount+=1
\t\tsSkipList.insert("""
    
    for line in data:
        str_tmp1+="""data[i]["@{}:"],""".format(line)
        if(flag == 0):
            str_tmp1+="""\"DB_{}.txt\".format(count),"""
            str_tmp1+="""data[i]["@{}:"],""".format(line)
            flag=1
        
    str_tmp1+=""")
\tticks = time.time()
\tprint("完成建立INDEX的時間")
\tprint (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
\treturn sSkipList"""
    return str_tmp1


# In[83]:


def write_DB_file():
    str_tmp1 = """def write_DB_file(data):
\tprint("寫入時間是很久的唷，請去寫其他功課吧！")
\tprint("開始寫入檔案的時間")
\tname_number = 0
\tfile_name = "DB_{}.txt".format(name_number)
\tsSkipList = create_python.SkipList()
\tticks = time.time()
\tprint (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
\tfor i in range(len(data)):
\t\tif i%5000 == 0:
\t\t\tname_number +=1
\t\t\tfile_name = "DB_{}.txt".format(name_number)
\t\t\tprint(file_name)
\t\t\tticks = time.time()
\t\t\tprint (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
\t\twrite_file(file_name,data[i])
\t\tsSkipList.insert(data[i]["@url:"],file_name)
\tticks = time.time()
\tprint("完成寫入檔案時間")
\tprint (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
\treturn sSkipList"""
    return str_tmp1


# In[84]:


def create_input(data):
    str_tmp1 = get_import()
    str_tmp2 = get_dd(data)
    str_tmp3 = get_ddc(data)
    str_tmp4 = get_bool()
    str_tmp5 = write_file()
    str_tmp6 = input_main(data)
    str_tmp7 = url_index_DB(data)
    str_tmp8 = write_DB_file()
    with open("input_python.py",'w',encoding='utf-8') as f:
            f.write(str_tmp1)
            f.write("\n")
            f.write(str_tmp2)
            f.write("\n")
            f.write(str_tmp3)
            f.write("\n")
            f.write(str_tmp4)
            f.write("\n")
            f.write(str_tmp5)
            f.write("\n")
            f.write(str_tmp6)
            f.write("\n")
            f.write(str_tmp7)
            f.write("\n")
            f.write(str_tmp8)
            f.write("\n")


# In[86]:


# create_input(data)

