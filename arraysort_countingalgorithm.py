input_num = [1,4,1,2,7,5,2,8,9,1,10,20,22,24,999,756,435,2322]
maximum_num=max(input_num)
minimim_num=min(input_num)
size = maximum_num-minimim_num+1
test_array=[0]*(size)
count = [0]*(size)

for i in range(0,len(count)):
    total_counts=input_num.count(i+1)
    count[i]=total_counts
for g in range(1,len(count)):
    count[g]+=count[g-1]
for f in range(len(input_num)):
    index_insertion=(count[input_num[f]-minimim_num])
    count[input_num[f]-minimim_num]-=1
    test_array[index_insertion]=input_num[f]
for i in range(0,len(input_num)):
    input_num[i]=test_array[i+1]
print(input_num)
