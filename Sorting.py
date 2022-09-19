import string,re,time,xlwt, math,sys

sys.setrecursionlimit(100000000)

# Selection sort:
class SelectionSort:
    def sort(self,arr):
        print("in SelSort.sort ")
        for i in range(len(arr) - 1):
            #if(i%1000==0):print("i",i)
            minIndex = i # 记录min的索引
            for j in range(i + 1, len(arr)):
                #if(i%100==0 and j%10000==0):print("i,j,len(arr)",i,j,len(arr))
                if arr[j] < arr[minIndex]:
                    minIndex = j
            # i 不是最小数时，将 i 和最小数进行交换
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr


class InsertionSort:
    def sort(self,arr):
        for i in range(1,len(arr)):
            curValue=arr[i]  # 以i为index，选出curValue
            preIndex=i-1 #i-1作为起始点,curValue开始往前比
            while preIndex>=0 and curValue<arr[preIndex]: #只要cur比前一个小，就往前换
                arr[preIndex+1]=arr[preIndex] #记录跟cur交换的元素的值，让它的index往后一个
                preIndex-=1
            arr[preIndex+1]=curValue #到头或者不比前一个小了，就停下
        return arr


#https://www.programiz.com/dsa/heap-sort
class HeapSort():
    def sort(self, arr):
        #把数列里某个index的值给拱上去
        def heapify(arr:list,n:int,index:int)->list:
            largest = index  # 假设largest指的值就是index的值
            left = 2*index+1
            right = 2*index+2
            #找真的最大值
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            # 若真的最大值!=index的值了，就说明上一步找到更大值了，swap，index指的就是真的最大值
            if largest != index:
                arr[index], arr[largest] = arr[largest], arr[index]
                heapify(arr,n, largest) #recursive,把largest拱上去

        #build max heap
        n=len(arr)
        for index in range(n//2, -1, -1): #从一半？到0的每一个index，step=1
            heapify(arr,len(arr), index) #是最大堆了
        #extract elements
        for index in range(len(arr)-1,0,-1): #n-1代表最后一个堆的index
            arr[index], arr[0] = arr[0], arr[index]
            heapify(arr,index, 0)
        return arr



class MergeSort:
    def sort(self, arr):
        if len(arr) > 1:
            #分两半
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            #越分越细，递归，作弊
            self.sort(left)
            self.sort(right)

            i = j = k = 0 #i=左指针，j=右指针，k=总指针
            #左右两边队首，谁小谁就先进总arr
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
           #两边有剩下的怎么办？排队进
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr



class QuickSort:
    def partition(self,arr,begin,end): #begin指向第一个元素，end指向最末元素
        pivot = arr[end]   #选最末一个作pivot
        i = begin - 1 #初始化i
        for j in range(begin, end): #j(探测小的）从begin撸到pivot的前一个，跟pivot比
          if arr[j] <= pivot:
            i = i + 1  # if j<pivot,让i（挖坑）往后指一个，j跟i换
            (arr[i], arr[j]) = (arr[j], arr[i])
           # 撸完一遍，i和i前面的都比pivot小，分区啦！pivot到i+1的位置
        (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
        return i + 1 #分区位置，前面是有序的，后面是无序的



    def sort(self,arr, begin, end):
        '''
        def partition(arr,begin,end): #begin指向第一个元素，end指向最末元素
            pivot = arr[end]   #选最末一个作pivot
            i = begin - 1 #初始化i
            if (i % 1 == 0): print("i", i)
            for j in range(begin, end): #j(探测小的）从begin撸到pivot的前一个，跟pivot比
 #             if (i % 100 == 0 and j % 10000 == 0):
              print("i,j,len(arr)", i, j, len(arr))
              if arr[j] <= pivot:
                i = i + 1  # if j<pivot,让i（挖坑）往后指一个，j跟i换
                (arr[i], arr[j]) = (arr[j], arr[i])
               # 撸完一遍，i和i前面的都比pivot小，分区啦！pivot到i+1的位置
            (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
            return i + 1 #分区位置，前面是有序的，后面是无序的
        '''
        if begin < end:
            p = self.partition(arr, begin, end) #接住分区位置p=i+1
            self.sort(arr, begin, p - 1)
            self.sort(arr, p + 1, end)
        return arr


def test():
    data = [6, 9, 3, 8, 5, 10, 1, 0, 7, 2, 4]
    textdata = []

    # s1=SelectionSort()
    # print(s1.sort(arr))
    # s2=InsertionSort
    # print(s2.sort(data))
    # print(HeapSort.heapify(data,2))
    # s3=HeapSort()
    # print(s3.sort(data))
    # s4=MergeSort()
    # print(s4.sort(data))
    s5 = QuickSort()
    print(s5.sort(data,0,len(data)-1)) #提示有4个变量的话就说明前面sort定义时忘记加self了

def read_token(arr):
    print("in read_token_int")
    path = "./pride-and-prejudice.txt"
    f1 = open(path, "r",encoding='utf_8')
    str1 = f1.readlines()
    f1.close()
    pattern = re.compile('[a-zA-Z0-9]+')
    for line in str1:
        line = line.strip()
        words = pattern.findall(line)
        for word in words:
            if word != '':
                arr.append(word)
    print("finish read_token")
    return arr


def main():
    # test()

    #read_token() test
    data1=[]
    read_token(data1)
    #print(data1)

# #Selection sort time:
#     for i in range(10):
#         s1=SelectionSort()
#         d = [x for x in data1] #for each x in data1, put in the list
#         start = time.monotonic_ns()
#         s1.sort(d)
#         cur = time.monotonic_ns()
#         print(cur - start)


#Selection sort time:
    for i in range(10):
        s2=InsertionSort()
        d = [x for x in data1]
        start = time.monotonic_ns()
        s2.sort(d)
        cur = time.monotonic_ns()
        print(cur - start)


    # #QuickSort time:
    # for i in range(10):
    #     s5=QuickSort()
    #     d = [x for x in data1]
    #     start = time.monotonic_ns()
    #     s5.sort(d,0,len(data1)-1)
    #     cur = time.monotonic_ns()
    #     print("QuickSort time:",cur - start)

# #MergeSort time:
#     for i in range(10):
#         s4=MergeSort()
#         # Python list comprehension
#         d = [x for x in data1]
#         start = time.monotonic_ns()
#         s4.sort(d)
#         cur = time.monotonic_ns()
#         print(i,cur - start)


# # HeapSort time:
#     for i in range(10):
#         s3=HeapSort()
#         d = [x for x in data1]
#         start = time.monotonic_ns()
#         s3.sort(d)
#         cur = time.monotonic_ns()
#         print(i,cur - start)


if __name__ == "__main__":
     main()