B = []
m = 1

for r in range(2):
    B.append([])
    for c in range(2):
        B[r].append([])
        for n in range(2):
            B[r][c].append(m)
            m += 1 
print(B)