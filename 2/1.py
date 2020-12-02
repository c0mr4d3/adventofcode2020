arr = [x[:-1] for x in open("/home/comrade/Funstuff/adventofcode2020/2/input.txt").readlines()]

count = 0

for s in arr:

    maxm = int(s[s.index("-")+1:s.index(" ")])
    minm = int(s[:s.index("-")])
    chrr = s[s.index(" ")+1]
    pas = s[s.index(": ")+2:] 
    cnt = int(pas.count(chrr))
    if minm<=cnt<=maxm:
        count+=1

print(count)