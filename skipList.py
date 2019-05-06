from random import randint, seed

class SkipNode:
    """A node from a skip list"""    
    def __init__(self, height = 0, elem = None , key=None):
        self.key = key
        self.elem = elem
        self.next = [None]*height

class SkipList:

    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    def find(self, elem, update = None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None
    
    def contains(self, elem, update = None):
        return self.find(elem, update) != None
    
    def randomHeight(self):
        height = 1
        while randint(1, 2)!= 1:
            height += 1
        return height

    def updateList(self, elem):
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update
        
    def insert(self, elem, key):

        node = SkipNode(self.randomHeight(), elem, key)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)            
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def remove(self, elem):

        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1            
                
    def printList(self):
        for i in range(len(self.head.next)-1, -1, -1):
            x = self.head
            while x.next[i] != None:
                print (x.next[i].elem + '-',end="")
                x = x.next[i]
            print ('')
    
# 
    def find2(self, elem, update = None):
        if update == None:
            update = self.updateList2(elem)
        if len(update) > 0:
            candidate2 = update[0].next[0]
            if candidate2 != None and candidate2.key == elem:
                return candidate2
        return None
    
    def contains2(self, elem, update = None):
        return self.find(elem, update) != None


    def updateList2(self, elem):
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].key < elem:
                x = x.next[i]
            update[i] = x
        return update
    


url_list = ["https://www.youtube.com/watch?v=1R2vIsIPI38","https://www.youtube.com/watch?v=1R2vIsIPI38","https://www.youtube.com/watch?v=adex5YdEbOs","https://www.youtube.com/watch?v=vlCumuwLkEM","https://www.youtube.com/watch?v=d25EQaECNnU","https://www.youtube.com/watch?v=Qh8DoWbumgs&t=4s","https://www.youtube.com/watch?v=OE9mcx_iJrE"]
sSkipList = SkipList()
for index,url in enumerate (url_list):
    key = "{}".format(index)
    elem = url
    sSkipList.insert(elem,key)
sSkipList.printList()