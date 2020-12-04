arr = [x[:-1] for x in open("/home/comrade/Funstuff/adventofcode2020/3/input.txt").readlines()]
pos = 0
maxlen = len(arr[0])
count = 0
for s in arr:
    if pos>=maxlen:
        pos = pos%maxlen
    if s[pos]=="#":
        count+=1
    pos+=3
    

print(count)


ml = 7 
0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6  
0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6 

c=3
