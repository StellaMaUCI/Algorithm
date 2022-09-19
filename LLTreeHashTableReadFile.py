
import string,re,time,xlwt
from xlwt import *

#Linkedlist Set
class LinkedListNode:
   # def __init__(self, value)->object:
    def __init__(self, value=None, next=None):
        self.value = value
        #self.next = None
        self.next = next
'''
#insert at the front
class LinkedList:
    def __init__(self)-> object:
        self.head = None
        self.tail = None
        self.count=0

    def add(self, value):
        value=str(value)
        if not self.head:
            self.head=LinkedListNode(value)
            self.tail = self.head
            self.count += 1
            return True
        elif not self.contains(value):
            new=LinkedListNode(value)
            new.next=self.head
            self.head=new
            self.count += 1
            return True
        return False
'''



#insert at the end
class LinkedList:
    def __init__(self)-> object:
        #self.head = None
        #self.tail = None
        self.count = 0
        self.head = LinkedListNode(0)
        self.tail = LinkedListNode(0)
        self.head.next=self.tail

    def add(self, value):
        value = str(value)
        if self.contains(value):
            return False
        node = self.head
        while node.next != self.tail:
            node = node.next
        node.next = LinkedListNode(value, self.tail)
        self.count += 1
        return True


    # <Exercise1.LinkedList object at 0x000001F99945DF70>若没有__str__
    # https://www.geeksforgeeks.org/pretty-print-linked-list-in-python/
    def __str__(self):
        res = "head->"
        ptr = self.head
        while ptr: #ptr不指向空时
            res += str(ptr.value) + "->"
            ptr = ptr.next
        # removing trailing commas
        res = res.strip(", ")
        return "[" + res +  "tail]"


    def size(self):
        return self.count

    def contains(self, value):
        value = str(value)
        ptr = self.head
        #        cc=0
        while ptr.next != self.tail:
            ptr = ptr.next
            if ptr.value == value:
                return True
        #            cc+=1
        #            print("count, cc",self.count,cc)
        return False


    # def contains(self, value):
    #     value = str(value)
    #     ptr = self.head.next
    #     while (ptr):
    #         if ptr.value == value:
    #            return True
    #         ptr = ptr.next
    #     return False


#Binary Tree Set
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def add(self, value):
        value=str(value)
        if not self.root:
            self.root= TreeNode(value) #insert first treenode as root
            self.count += 1
            return True
        ptr= self.root
        while ptr:
            if value < ptr.value:
                if not ptr.left :
                    ptr.left = TreeNode(value)
                    self.count += 1
                    return True
                ptr = ptr.left
            elif value>ptr.value :
                if not ptr.right:
                    ptr.right = TreeNode(value)
                    self.count += 1
                    return True
                ptr = ptr.right
            else:
                return False

#Search member function
    def contains(self, value):
        value = str(value)
        ptr = self.root
        while ptr:
            if value < ptr. value:
                ptr = ptr.left
            elif value > ptr.value:
                ptr = ptr.right
            elif value == ptr.value:
                return True
            else:
                return False

'''
    # https: // gist.github.com / swarooprath / 44c9c59d36cb940579707f803919ef23
    def __str__(self, depth=0):
        res = ""
        if self.right != None:
            res = str(self.value) + ("____" * depth) + "\n"
        if self.left != None:
            res = str(self.value) + ("____" * depth) + "\n"
        return res
'''



#https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/
class HashTable:
    def __init__(self):
        self.buckets_size = 10000
        self.buckets = [[] for _ in range(self.buckets_size)]
        self.count = 0

    #textbook Algorithms Ch3.4
    def hashcode(self,value):
        h=0
        for i in value:
            # for any s: s % (2^t) = s & (1<<t) - 1.
            # 0xFFFFFFFF=hexadecimal MASK=2^32-1(DictMinSize)-1
            #h = (((5381 << 5) + 5381) + ord(x)) & 0xFFFFFFFF # hash * 33 + c
            h=h*31+ord(i)
        return h % len(self.buckets)

    def contains(self, key):
        key = str(key)
        ptr=0
        hValue = self.hashcode(key)
        if not self.buckets[hValue]: #若bucket为空
            return False # 课程要求contain没有算false
        ptr = self.buckets[hValue]
        # while ptr:
        #     if ptr.key == key: #compare same
        #         return True # 课程要求contain有算true
        #     ptr = ptr.next #以上都不是的话，keep going
        for v in ptr:
            if v == key:
                return True

        return False #若结尾还没找到算false

    def add(self, key):
        key=str(key)
        hValue = self.hashcode(key)
        if not self.contains(key):
          # self.buckets[hValue] = LinkedListNode(key)  #则在hValue的bucket处添加key
          self.buckets[hValue].append(key)  #则在hValue的bucket处添加key
          self.count += 1
          return True # 课程要求add了算true
        else:
          return False

    def size(self):
        return self.count





def read_file():
    path1 = "./pride-and-prejudice.txt"
    path2 = "./words-shuffled.txt"

    f1 = open(path1, "r",encoding='utf_8')
    str1 = f1.readlines()
    f1.close()

    f2 = open(path2, "r",encoding='utf_8')
    str2 = f2.readlines()
    f2.close()
    return str1,str2


def token_dic(infile,myset):
    pattern = re.compile('[a-zA-Z0-9]+')
    # https: // www.geeksforgeeks.org / python - regex - re - search - vs - re - findall /
    for line in infile:
        line = line.strip()
        words = pattern.findall(line)
        for word in words:
            if word != '':
               myset.add(word)
    return True

def token_search(infile,myset):
    missing=0
    nwords=0
    pattern = re.compile('[a-zA-Z0-9]+')
    # https: // www.geeksforgeeks.org / python - regex - re - search - vs - re - findall /
    for line in infile:
        line = line.strip()
        words = pattern.findall(line)
        for word in words:
            if word != '':
               if not myset.contains(word): #不在file里的词算missing
                  missing+=1
    return missing

def time_measure_insert(infile,myset):
    insert_word_times = [0]
    start = time.time_ns()
    token_dic(infile,myset)
    for w in infile:
        myset.add(w)
        cur = time.time_ns()
        cost = cur - start
        insert_word_times.append(cost)
    return insert_word_times


def time_measure_search(infile,myset):
    search_word_times = [0]
    start = time.time_ns()
    token_dic(infile,myset)
    for w in infile:
        myset.contains(w)
        cur = time.time_ns()
        cost = cur - start
        search_word_times.append(cost)
    return search_word_times



def main():

# #read_file() test
#     r1, r2 = read_file()
#     print(r1)
#     print(r2)



# #token_dic() only test:
# r1, r2 = read_file()
# s1, s2, s3 = LinkedList(), BinaryTree(), HashTable()
# token_dic(r1,s1)
# token_dic(r1,s2)
# token_dic(r1,s3)
# print(s1.size(),s2.size(),s3.size())


# #token_search from dic test
#     r1, r2 = read_file()
#     s1, s2, s3 = LinkedList(), BinaryTree(), HashTable()
#     token_dic(r1,s3)
#     token_dic(r1,s2)
#     token_dic(r1,s1)
#     token1 = token_search(r2,s3)
#     token2 = token_search(r2, s3)
#     token3 = token_search(r2, s3)
#     print('missing1,2,3=',token1,token2,token3)


#time_measure Test：
    r1, r2 = read_file()
    s3 = HashTable()

    print('time_insert_Hash',s3.size)
    time_insert_hash = time_measure_insert(r1, s3)
    print(time_insert_hash)

    print('time_search_Hash')
    time_search_Hash = time_measure_search(r1, s3)
    print(time_search_Hash)



#output to excel
    # insertTimeFile1 = open("ListInsertTime.csv", "w")
    # searchTimeFile1 = open("ListSearchTime.csv", "w")
    # insertTimeData1 = [None] * 11
    # searchTimeData1 = [None] * 11
    #
    #
    # insertTimeFile2 = open("TreeInsertTime.csv", "w")
    # searchTimeFile2 = open("TreeSearchTime.csv", "w")
    # insertTimeData2 = [None] * 11
    # searchTimeData2 = [None] * 11
    #
    # insertTimeFile3 = open("HashInsertTime.csv", "w")
    # searchTimeFile3 = open("HashSearchTime.csv", "w")
    # insertTimeData3 = [None]*11
    # searchTimeData3 = [None]*11
    #
     # for i in range(10):
     #     r1, r2 = read_file()
     #     s1, s2, s3 = LinkedList(), BinaryTree(), HashTable()
     #     print("Experiment ", i)
    #     insertTimeData1[i] = time_measure_insert(r1, s1)
    #     searchTimeData1[i] = time_measure_search(r1, s1)
    #     insertTimeData2[i] = time_measure_insert(r1, s2)
    #     searchTimeData2[i] = time_measure_search(r1, s2)
    #     insertTimeData3[i] = time_measure_insert(r1, s3)
    #     searchTimeData3[i] = time_measure_search(r1, s3)
    #
    # for i, p in enumerate(insertTimeData1):
    #     if p:
    #         for j, q in enumerate(p):
    #             if q:
    #                insertTimeFile1.write(str(p) + ", ")
    #     insertTimeFile1.write("\n")
    #
    #
    # for i, p in enumerate(searchTimeData1):
    #     if p:
    #         for j, q in enumerate(p):
    #             if q:
    #                 searchTimeFile1.write(str(p) + ", ")
    #     searchTimeFile1.write("\n")
    #
    #
    # for i, p in enumerate(insertTimeData2):
    #     if p:
    #         for j, q in enumerate(p):
    #             if q:
    #                 insertTimeFile2.write(str(p) + ", ")
    #     insertTimeFile1.write("\n")
    #
    # for i, p in enumerate(searchTimeData2):
    #     if p:
    #          for j, q in enumerate(p):
    #              if q:
    #                  insertTimeFile2.write(str(p) + ", ")
    #     insertTimeFile2.write("\n")
    #

    # for i, p in enumerate(insertTimeData3):
    #     if p:
    #         for j, q in enumerate(p):
    #             if q:
    #                 searchTimeFile3.write(str(p) + ", ")
    #     searchTimeFile3.write("\n")


if __name__ == "__main__":
     main()

