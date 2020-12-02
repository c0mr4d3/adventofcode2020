
arr = [int(x[:-1]) for x in open("/home/comrade/Funstuff/adventofcode2020/1/input.txt").readlines()]

def twosum(sumval):
    hm = set()
    for x in range(len(arr)):
        needed = sumval-arr[x]
        if needed in hm:
            return needed,arr[x]
        hm.add(arr[x])
    return 0,0

for x in arr:
    v1,v2 = twosum(2020-x)
    if v1!=0:
        print(x,v1,v2)
