# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import json
from flask_cors import CORS, cross_origin
import create_ipy
import input_ipy
from random import *

def get_youtubeId(youtube_url):
    tmp = youtube_url.split("https://www.youtube.com/watch?v=")
    tmp = tmp[1].replace('\n','')
    return tmp

def get_youtube_jpg(youtube_id):
    return "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(youtube_id)

def get_list_url_data(string_data):
    tmp = string_data.split("---")
    key = tmp[0]
    youtube = tmp[1].replace("@url:","").replace("\n","")
    youtube_id = get_youtubeId(youtube)
    youtube_jpg = get_youtube_jpg(youtube_id)
    tmp_data = []
    tmp_data.append(key)
    tmp_data.append(youtube)
    tmp_data.append(youtube_id)
    tmp_data.append(youtube_jpg)
    return tmp_data

def get_find_full(data,key_word):
    ans = []
    for index,line in enumerate(data[0]):
        if line.find(key_word)!=-1:
            tmp = ""
            tmp = "{}---{}".format(data[1][index],line)
            ans.append(tmp)
    return ans

def write_file(file_name,table_name,data):
    with open(table_name,'w',encoding='utf-8') as f:
        f.write(file_name)
        f.write("\n")
        f.write(table_name)
        f.write("\n")
        for line in data:
            f.write(line)
            f.write("\n")
        f.write("\n")

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#server test
@app.route("/")
@cross_origin()
def hello():
    return "server live!"

title_data = []
data = None
sSkipList = None
#創立
# @app.route("/dataInfo/get_All_place", methods=['POST'])
@app.route("/create/<file_name>/<table_name>/<tile1>/<tile2>/<tile3>/<tile4>/<tile5>/<tile6>/<tile7>/<tile8>", methods=['GET'])
@cross_origin()
def get_All_place(file_name,table_name,tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8):
    global title_data
    title_data = []
    if tile1 != "NULL":
        title_data.append(tile1)
    if tile2 != "NULL":
        title_data.append(tile2)
    if tile3 != "NULL":
        title_data.append(tile3)
    if tile4 != "NULL":
        title_data.append(tile4)
    if tile5 != "NULL":
        title_data.append(tile5)
    if tile6 != "NULL":
        title_data.append(tile6)
    if tile7 != "NULL":
        title_data.append(tile7)
    if tile8 != "NULL":
        title_data.append(tile8)
    write_file(file_name,table_name,title_data)

    create_ipy.create_table(title_data)
    input_ipy.create_input(title_data)
    import create_python
    import input_python
    global data
    global sSkipList
    print(file_name)
    data = input_python.input_main(file_name)
    print(len(data))
    sSkipList = input_python.url_index_DB(data)
    ans_data = "OK,GOOD"
    return json.dumps(ans_data, ensure_ascii=False).encode('utf8')
    # return json.dumps(ans, ensure_ascii=False).encode('utf8')

#查詢
@app.route("/search/<file_name>/<table_name>/<table_title>/<keyword>/<page_number>", methods=['GET'])
@cross_origin()
def get_search(file_name,table_name,table_title,keyword,page_number=None):
    import create_python
    import input_python
    # print(file_name)
    # data = input_python.input_main(file_name)
    # print(len(data))
    # sSkipList = input_python.url_index_DB(data)
    global data
    global sSkipList

    if(table_title!="url"):
        return "只能搜尋RUL"
    if(page_number=='0'):
        ans_data = None
        All_sSkipList = sSkipList.get_ALL()
        tmp_data = get_find_full(All_sSkipList,keyword)
        ans_data = len(tmp_data)
        return json.dumps(ans_data, ensure_ascii=False).encode('utf8')
    else:
        ans_data = None
        ans_data = []
        All_sSkipList = sSkipList.get_ALL()
        tmp_data = get_find_full(All_sSkipList,keyword)
        page_number = int(page_number)
        # ans_data.append(len(tmp_data))
        if(len(tmp_data)<10):
            for i in range(0,len(tmp_data)):
                tmp = get_list_url_data(tmp_data[i])
                ans_data.append(tmp)
                return json.dumps(ans_data, ensure_ascii=False).encode('utf8')
        for i in range(9*(page_number-1) ,(9*page_number)-1 ):
            tmp = get_list_url_data(tmp_data[i])
            ans_data.append(tmp)
        return json.dumps(ans_data, ensure_ascii=False).encode('utf8')
#新增
# @app.route("/input/<file_name>/<table_name>", methods=['GET'])
@app.route("/input", methods=['GET'])
@cross_origin()
def get_input_title():
    global title_data
    if(len(title_data)<8):
        for line in range(0,8-len(title_data)):
            title_data.append("NULL")
    return json.dumps(title_data, ensure_ascii=False).encode('utf8')


@app.route("/input/<file_name>/<table_name>/<tile1>/<tile2>/<tile3>/<tile4>/<tile5>/<tile6>/<tile7>/<tile8>", methods=['GET'])
@cross_origin()
def get_input(file_name,table_name,tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8):
    global title_data
    global data
    global sSkipList
    count = randint(1, 100)
    tile1 = "@url:https://www.youtube.com/watch?v={}\n".format(tile1)
    if(tile3=="NULL"):
        sSkipList.insert(tile1,"DB_{}.txt".format(count),tile1,tile2)
        return json.dumps("OK,{}".format(tile1), ensure_ascii=False).encode('utf8')
    if(tile4=="NULL"):
        sSkipList.insert(tile1,"DB_{}.txt".format(count),tile1,tile2,tile3)
        return json.dumps("OK,{}".format(tile1), ensure_ascii=False).encode('utf8')
    if(tile5=="NULL"):
        sSkipList.insert(tile1,"DB_{}.txt".format(count),tile1,tile2,tile3,tile4)
        return json.dumps("OK,{}".format(tile1), ensure_ascii=False).encode('utf8')
    if(tile6=="NULL"):
        sSkipList.insert(tile1,"DB_{}.txt".format(count),tile1,tile2,tile3,tile4,tile5)
        return json.dumps("OK,{}".format(tile1), ensure_ascii=False).encode('utf8')
    if(tile7=="NULL"):
        sSkipList.insert(tile1,"DB_{}.txt".format(count),tile1,tile2,tile3,tile4,tile5,tile6)
        return json.dumps("OK,{}".format(tile1), ensure_ascii=False).encode('utf8')
    if(tile8=="NULL"):
        sSkipList.insert(tile1,"DB_{}.txt".format(count),tile1,tile2,tile3,tile4,tile5,tile6,tile7)
        return json.dumps("OK,{}".format(tile1), ensure_ascii=False).encode('utf8')
    if(tile8!="NULL"):
        sSkipList.insert(tile1,"DB_{}.txt".format(count),tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8)
        return json.dumps("OK,{}".format(tile1), ensure_ascii=False).encode('utf8')
    return json.dumps("ERROR,{}".format(tile1), ensure_ascii=False).encode('utf8')

#刪除
@app.route("/delete/<file_name>/<table_name>/<tile1>", methods=['GET'])
@cross_origin()
def get_delete(file_name,table_name,tile1):
    global title_data
    global data
    global sSkipList
    tile1 = "@url:https://www.youtube.com/watch?v={}\n".format(tile1)
    sSkipList.remove(tile1)
    return "OK,remove:{}".format(tile1)
#main
if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=8080)
    CORS(app)