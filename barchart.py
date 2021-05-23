import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time



def animated_barplot():
    input_num = [1,4,1,2,7,5,2,8,9,1,10,20,22,33,42,32,7,3,5,8,1,2,7,32,22,13]
    maximum_num=max(input_num)
    minimim_num=min(input_num)
    size = maximum_num-minimim_num+1
    test_array=[0]*(size)
    count = [0]*(size)

    
    x='Calculating total occurances of each number- Currently searching for number:'
    y_pos_count=[]
    y_pos_input_num=[]

    for k in range(len(count)):
        y_pos_count.append(k)

    for h in range(len(input_num)):
        y_pos_input_num.append(h)
    
    fig.clear()

    for i in range(0,len(count)):
        total_counts=input_num.count(i+1)
        count[i]=total_counts
        plt.bar(y_pos_count,count,alpha=0.5)
        time.sleep(.1)
        plt.ylabel('Number of Occurances')
        plt.xlabel((x)+(str(i+1)))
        fig.canvas.draw()
        win.after(20000, animated_barplot)
        fig.clear()
    time.sleep(2.5)
    fig.clear()

    x2='Adding occurances of number+numbers before; arranging number:'

    for g in range(1,len(count)):
        count[g]+=count[g-1]
        plt.bar(y_pos_count,count,alpha=0.5)
        time.sleep(.1)
        plt.ylabel('Total Occurances+Number Before')
        plt.xlabel((x2)+str(g))
        fig.canvas.draw()
        win.after(20000, animated_barplot)
        fig.clear()
    time.sleep(2)
    fig.clear()
    x3='organizing numbers from least to greatest:'
    for f in range(len(input_num)):
        index_insertion=(count[input_num[f]-minimim_num])
        count[input_num[f]-minimim_num]-=1
        test_array[index_insertion]=input_num[f]
        plt.bar(y_pos_count,test_array,alpha=0.5)
        time.sleep(.1)
        plt.xlabel((x3)+str(f))
        plt.title('Arranging numbers in output_array')
        fig.canvas.draw()
        win.after(20000, animated_barplot)
        fig.clear()
    time.sleep(2)
    fig.clear()
    for i in range(0,len(input_num)):
        input_num[i]=test_array[i+1]
        plt.bar(y_pos_input_num,input_num,alpha=0.5)
        time.sleep(.1)
        plt.title('Inputting final array of numbers into the main input array')
        plt.xlabel((x2)+str(g))
        fig.canvas.draw()
        win.after(20000, animated_barplot)
        fig.clear()
    plt.bar(y_pos_input_num,input_num,alpha=.5)
    plt.title('ORGANIZED FROM LEAST TO GREATEST(Sorting Algorithm)')
    final='Sorted numbers:'
    plt.xlabel((final)+str(input_num))
    fig.canvas.draw()
    win.after(20000, animated_barplot)
    time.sleep(5)
    fig.clear()
    plt.close()
    print(input_num)








fig = plt.figure()
win = fig.canvas.manager.window
win.after(100, animated_barplot)
plt.show()