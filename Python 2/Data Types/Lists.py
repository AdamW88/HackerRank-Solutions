L = []  # empty list

T = int(raw_input().strip())  # number of cases

for t in xrange(T):
    args = raw_input().strip().split(" ")  # formats the command from HR
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "index":
        L.index(int(args[1]))
    elif args[0] == "count":
        L.count(int(args[1]))
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print L
