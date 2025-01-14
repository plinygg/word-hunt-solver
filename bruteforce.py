w = open("words.txt", "r")

arr = []
for num in range(279496):
    arr.append(w.readline()[:-2])

test = 0
for n in arr:
    test = max(test, len(n))
    
# print(test) length of the longest char is 14
grid = [['O', 'I', 'E', 'A'], 
        ['P', 'N', 'A', 'S'], 
        ['E', 'Y', 'I', 'O'], 
        ['N', 'Y', 'H', 'E']]
row = col = 4

result = []
# len operates more like a "ticker" than a length
def generate(r, c, len, cur):
    if r == row or c == col or r < 0 or c < 0:
        if len >= 2 and cur not in result:
            result.append(cur.copy())
        return
    if len == 14 and cur not in result:
        result.append(cur.copy())
        return
    
    len += 1
    cur.append(grid[r][c])
    generate(r+1, c, len, cur)
    generate(r, c+1, len, cur)
    # generate(r+1, c+1, len, cur)
    # generate(r-1, c, len, cur)
    # generate(r, c-1, len, cur)
    # generate(r-1, c-1, len, cur)
    # generate(r-1, c+1, len, cur)
    # generate(r+1, c-1, len, cur)
    cur.pop()
    generate(r+1, c, len, cur)
    generate(r, c+1, len, cur)
    # generate(r+1, c+1, len, cur)
    # generate(r-1, c, len, cur)
    # generate(r, c-1, len, cur)
    # generate(r-1, c-1, len, cur)
    # generate(r-1, c+1, len, cur)
    # generate(r+1, c-1, len, cur)

generate(0, 0, 0, [])

for temp in result:
    print(temp)
res = []
for temp in result:
    q = "".join(temp)
    if q in arr and len(q) > 2:
        res.append(q)
        
print(res)