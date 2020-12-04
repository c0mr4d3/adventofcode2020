arr = [x[:-1] for x in open("/home/comrade/Funstuff/adventofcode2020/3/input.txt").readlines()]

def countTrees(rightc,downc):
    pos = 0
    maxlen = len(arr[0])
    count = 0
    rownum=0 
    while len(arr)>rownum:
        if pos>=maxlen:
            pos = pos%maxlen
        if arr[rownum][pos]=="#":
            count+=1
        pos+=rightc
        rownum+=downc
    return count
        

print(countTrees(1,1)*countTrees(3,1)*countTrees(5,1)*countTrees(7,1)*countTrees(1,2))
