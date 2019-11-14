import os.path
import os
def main():
    mylist = []
    mylist1 = []

    with open("sampletrain.txt", encoding="utf8") as fileobj: #Change file name here
        for line in fileobj:
            for ch in line:
                mylist.extend(ch)
                ch
    print(mylist)
    print("length of list is: ", len(mylist))
    i = 0
    while i < len(mylist):
        t = chr(32)
        if mylist[i] == t:
            mylist1.extend(mylist[i])
        if mylist[i] == "_":
            mylist1.extend(mylist[i])
        if mylist[i] == "\t":
            mylist1.extend(mylist[i])
        if mylist[i] == "\n":
            mylist1.extend(mylist[i])
            
        t = chr(47)
        if mylist[i] == t:
            mylist1.extend(" ")

        p = 48
        g = 57
        while p <= g:
            t = chr(p)
            if mylist[i] == t:
                mylist1.extend(mylist[i])
            if mylist[i] == ".":
                if mylist[i-1] == (t):
                    mylist1.extend(mylist[i])
            p += 1

        p = 65
        g = 90
        while p <= g:
            t = chr(p)
            if mylist[i] == t:
                mylist1.extend(mylist[i])
            p += 1
        p = 97
        g = 122
        while p <= g:
            t = chr(p)
            if mylist[i] == t:
                mylist1.extend(mylist[i])
            p += 1
        i += 1
    
    deleted_words = ("the ", " I", " a  ", " of", " for", " at", " to", " in", "and ")
    if os.path.exists('newtrainfile.txt') == False:
        f = open("newtrainfile.txt","w+")
        f.write(''.join(mylist1))
        print(f.read())
        f.close()
    else:
        f = open("newtrainfile.txt","a+")
        f.write('\n')
        f.write(''.join(mylist1))
        f.close()
    f = open("newtrainfile.txt","r")
    lst = []
    for line in f:
        for word in deleted_words:
            if word in line:
                line = line.replace(word, '')
        lst.append(line)
    f.close()
    s = open('newtrainfile.txt','w')
    for line in lst:
        s.write(line.lower())
    s.close()
        
        
main()