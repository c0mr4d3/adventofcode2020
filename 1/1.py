
arr = [int(x[:-1]) for x in open("/home/comrade/Funstuff/adventofcode2020/1/input.txt").readlines()]
hm = set()

for x in range(len(arr)):
    needed = 2020-arr[x]
    if needed in hm:
        print(needed*arr[x])
    hm.add(arr[x])


