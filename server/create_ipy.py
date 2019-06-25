
# coding: utf-8

# In[4]:


# import


# In[5]:


# 完成
def get_import():
    str_import = """from random import randint, seed
import time"""
    return str_import


# In[6]:


# SkipNode


# In[7]:


def str_class_skipNode_parpmeter(key):
    str_class_skipNode_parpmeter = ",{} = None ".format(key)
    return str_class_skipNode_parpmeter


# In[8]:


def str_class_skipNode_Self_parpmeter(key):
    str_class_skipNode_Self_parpmeter = "\n\t\tself.{} = {}".format(key,key)
    return str_class_skipNode_Self_parpmeter


# In[9]:


# 完成
def get_str_class_skipNode(data):
    str_class_skipNode = """class SkipNode:
\tdef __init__(self, height = 0, elem = None ,key = None """
    for line in data:
        tmp = """"""
        parpmeter = str_class_skipNode_parpmeter(line)
        tmp = tmp+parpmeter
        str_class_skipNode = str_class_skipNode+tmp
    str_class_skipNode = str_class_skipNode+"""):
\t\tself.next = [None]*height
\t\tself.elem = elem
\t\tself.key = key"""
    for line in data:
        tmp =""""""
        Self_parpmeter = str_class_skipNode_Self_parpmeter(line)
        tmp = tmp + Self_parpmeter
        str_class_skipNode += tmp
    return str_class_skipNode


# In[10]:


# str_class_skipNode = get_str_class_skipNode(data)


# In[11]:


# class_SkipList


# In[12]:


def str_class_SkipList_parpmeter(key):
    str_class_SkipList_parpmeter = ",{} = None ".format(key)
    return str_class_SkipList_parpmeter


# In[13]:


def str_class_SkipList_Self_parpmeter(key):
    str_class_SkipList_Self_parpmeter = ",{} ".format(key)
    return str_class_SkipList_Self_parpmeter


# In[14]:


def get_class_SkipList(data):
    str_class_SkipList = """class SkipList:
\tdef __init__(self):
\t\tself.head = SkipNode()
\t\tself.len = 0
\t\tself.maxHeight = 0

\tdef __len__(self):
\t\treturn self.len

\tdef randomHeight(self):
\t\theight = 1
\t\twhile randint(1, 2)!= 1:
\t\t\theight += 1
\t\treturn height

\tdef remove(self, elem):
\t\tupdate = self.updateList(elem)
\t\tx = self.find(elem, update)
\t\tif x != None:
\t\t\tfor i in reversed(range(len(x.next))):
\t\t\t\tupdate[i].next[i] = x.next[i]
\t\t\t\tif self.head.next[i] == None:
\t\t\t\t\tself.maxHeight -= 1
\t\t\tself.len -= 1

\tdef printList(self):
\t\tfor i in range(len(self.head.next)-1, -1, -1):
\t\t\tx = self.head
\t\t\twhile x.next[i] != None:
\t\t\t\tprint (x.next[i].elem + '-',end="")
\t\t\t\tx = x.next[i]
\t\t\tprint ('')

\tdef find(self, elem, update = None):
\t\tif update == None:
\t\t\tupdate = self.updateList(elem)
\t\tif len(update) > 0:
\t\t\tcandidate = update[0].next[0]
\t\t\tif candidate != None and candidate.elem == elem:
\t\t\t\treturn candidate
\t\treturn None

\tdef contains(self, elem, update = None):
\t\treturn self.find(elem, update) != None

\tdef updateList(self, elem):
\t\tupdate = [None]*self.maxHeight
\t\tx = self.head
\t\tfor i in reversed(range(self.maxHeight)):
\t\t\twhile x.next[i] != None and x.next[i].elem < elem:
\t\t\t\tx = x.next[i]
\t\t\tupdate[i] = x
\t\treturn update

\tdef insert(self, elem, key"""
    for line in data:
        tmp = """"""
        parpmeter = str_class_SkipList_parpmeter(line)
        tmp = tmp+parpmeter
        str_class_SkipList = str_class_SkipList+tmp 
    str_class_SkipList += """):
\t\tnode = SkipNode(self.randomHeight(), elem, key """
    for line in data:
        tmp =""""""
        Self_parpmeter = str_class_SkipList_Self_parpmeter(line)
        tmp = tmp + Self_parpmeter
        str_class_SkipList += tmp
    str_class_SkipList += """)
\t\tself.maxHeight = max(self.maxHeight, len(node.next))
\t\twhile len(self.head.next) < len(node.next):
\t\t\tself.head.next.append(None)
\t\tupdate = self.updateList(elem)            
\t\tif self.find(elem, update) == None:
\t\t\tfor i in range(len(node.next)):
\t\t\t\tnode.next[i] = update[i].next[i]
\t\t\t\tupdate[i].next[i] = node
\t\t\tself.len += 1"""
    return str_class_SkipList


# In[3]:


def get_ALL():
    str_get_ALL = """"""
    tmp = "\tdef get_ALL(self):\n\t\tdata = []\n\t\tdata2 = []\n\t\tx = self.head\n\t\twhile x.next[0] != None:\n\t\t\tdata.append(x.next[0].elem)\n\t\t\tdata2.append(x.next[0].key)\n\t\t\tx = x.next[0]\n\t\treturn data,data2"
    str_get_ALL += tmp
    return str_get_ALL


# In[5]:


def create_table(data):
    str_import = get_import()
    str_class_skipNode = get_str_class_skipNode(data)
    str_class_SkipList = get_class_SkipList(data)
    str_get_ALL = get_ALL()
    with open("create_python.py",'w',encoding='utf-8') as f:
            f.write(str_import)
            f.write("\n")
            f.write(str_class_skipNode)
            f.write("\n")
            f.write(str_class_SkipList)
            f.write("\n")
            f.write("\n")
            f.write(str_get_ALL)
            f.write("\n")


# In[ ]:


#神奇FIND
#好像不用，因為不能這樣用。


# In[124]:


def get_find_function(key_Word):
    find_function = """\tdef find_"""
    tmp = """"""
    find_parpmeter = "{}(self, elem, update = None):".format(key_Word)
    tmp +=find_parpmeter
    find_function += tmp
    tmp = """"""
    tmp = """\n\t\tif update == None:
\t\t\tupdate = self.updateList_"""
    updateList_parpmeter = "{}(elem)".format(key_Word)
    tmp += updateList_parpmeter
    find_function += tmp
    tmp = """"""
    tmp = """
\t\tif len(update) > 0:
\t\t\tcandidate_"""
    candidate_parpmeter = "{} = update[0].next[0]\n\t\t\tif candidate_{} != None and candidate_{}.{} == elem:\n\t\t\t\treturn candidate_{}\n\t\treturn None".format(key_Word,key_Word,key_Word,key_Word,key_Word)
    tmp += candidate_parpmeter
    find_function += tmp
    return find_function


# In[125]:


def get_contains_funtion(key_Word):
    contains_function = """"""
    tmp = "\tdef contains_{}(self, elem, update = None):\n\t\treturn self.find_{}(elem, update) != None".format(key_Word,key_Word) 
    contains_function += tmp
    return contains_function


# In[126]:


def get_updateList_funtion(key_Word):
    updateList_function = """"""
    tmp = "\tdef updateList_{}(self, elem):\n\t\tupdate = [None]*self.maxHeight\n\t\tx = self.head\n\t\tfor i in reversed(range(self.maxHeight)):\n\t\t\twhile x.next[i] != None and x.next[i].{} < elem:\n\t\t\t\tx = x.next[i]\n\t\t\tupdate[i] = x\n\t\treturn update".format(key_Word,key_Word) 
    
    updateList_function += tmp
    return updateList_function

