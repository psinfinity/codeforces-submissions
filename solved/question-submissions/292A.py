queue = 0
time = 0
prev_time = 0
max_q = 0
for task in range(int(input())):
    t,c = map(int,input().split())
    time_elapsed = t-prev_time
    queue = max(c, queue-time_elapsed+c)
    max_q = max(queue,max_q)
    time+=time_elapsed
    prev_time = t
print(time+queue, max_q)