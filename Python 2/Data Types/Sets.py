N = int(raw_input())
a = set(map(int,(raw_input().strip().split(' '))))
M = int(raw_input())
b = set(map(int,(raw_input().strip().split(' '))))

mySet = set() # holds the answer

mySet.update(a.difference(b))
mySet.update(b.difference(a))
#mySet.sort()
myList = list(mySet)
myList.sort()
for i in range(len(myList)):
    print myList[i]
