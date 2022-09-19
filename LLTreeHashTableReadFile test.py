from LLTreeHashTableReadFile import LinkedListNode,LinkedList,TreeNode,BinaryTree,HashTable
import string,re,time,xlwt,sys
#sys for recursive function

# test linked list set
def LinkedListTest():
    print('LinkedList Test:')
    print('test = [I, love, dog, house, 4, 79, 84, 245, 66666,4]')
    test = ['I', 'love', 'dog', 'house', 4, 79, 84, 245, 66666,4]
    s1 = LinkedList()
    for t in test:
        s1.add(t)
    print(s1) #<Exercise1.LinkedList object at 0x000001F99945DF70>若没有__str__
    print('List Size: ' + str(s1.size()))
    print('dog: '+str(s1.contains(('dog'))))  # exist
    print('79: '+str(s1.contains(('79')))) # exist
    print('1: '+str(s1.contains(('1'))))  # not exist


def BinaryTreeTest():
    print('')
    print('BinaryTree Test:')
    test = ['one', 'two', 'three', 'four', 5, 6, 7, 8, 9]
    s2 = BinaryTree()
    for t in test:
        s2.add(t)
    print(s2)
    print('Tree Size: ' + str(s2.size()))
    print('four: ' + str(s2.contains(('four'))))  # exist
    print('6: ' + str(s2.contains(('6'))))  # exist
    print('1: ' + str(s2.contains(('1'))))  # not exist


def HashTableTest():
    print('')
    print('HashTable Test:')
    test = ['one', 'two', 'three', 'four', 5, 6, 7, 8, 9]
    s3 = HashTable()
    for t in test:
        s3.add(t)
    print(s3)
    print('HashTable Size: ' + str(s3.size()))
    print('four: ' + str(s3.contains(('four'))))  # exist
    print('6: ' + str(s3.contains(('6'))))  # exist
    print('1: ' + str(s3.contains(('1'))))  # not exist

def ReadTest(): #can't call here
    r1, r2 = read_file()
    print(r1)
    print(r2)


def timeAddTest():
    s1,s2,s3=LinkedList(),BinaryTree(),HashTable()
    timeAddHash = time_measure_add(words1,s1)
    print(timeAddHash)

def main():
    LinkedListTest()
   # BinaryTreeTest()
 #   HashTableTest()
 #   timeAddTest()



if __name__ == "__main__":
    main()
