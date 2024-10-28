n,m = list(map(int,input().split()))
rows = list(map(int,input().split()))
columns = list(map(int,input().split()))

print(sum([abs(rows[i]-rows[i+1]) for i in range(len(rows)-1)])+sum([abs(columns[i]-columns[i+1]) for i in range(len(columns)-1)]))