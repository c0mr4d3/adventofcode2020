arr = [x[:-1] for x in open("/home/comrade/Funstuff/adventofcode2020/2/input.txt").readlines()]


count = 0
for s in arr:

    maxm = int(s[s.index("-")+1:s.index(" ")])
    minm = int(s[:s.index("-")])
    chrr = s[s.index(" ")+1]
    pas = s[s.index(": ")+2:] 
    if (pas[minm-1]==chrr) != (pas[maxm-1]==chrr): 
        count+=1


print(count)
