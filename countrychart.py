import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

file=open('countrydata.txt','r')
list_data=[]
for line in file:
    commaspot=line.index(',')
    c=line[:commaspot]
    p=line[commaspot+1:-1]
    list_data.append([c,p])


ups=list_data[:60]   
    
percents=[float(u[1]) for u in ups]
width=.5   
x=range(len(percents))  

colors=['red','red','red','red','red','red','red','red','red','red','red','red',
       'blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue',
       'blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue',
       'blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue',
       'blue','blue','blue','blue','blue','blue','green','green','green','green','green','green']

plt.bar(x,percents,width,color=colors)
plt.xlabel('Sovereign Nation')
plt.title('The 60 Fastest Growing Nations by Population')
plt.ylabel('Annual growth 2010-2015')

red_patch = mpatches.Patch(color='red', label='Asia')
blue_patch = mpatches.Patch(color='blue', label='Africa')
green_patch = mpatches.Patch(color='green', label='Other')
plt.legend(handles=[red_patch,blue_patch,green_patch])

plt.show()


downs=list_data[60:]    
    
percents=[float(d[1]) for d in downs]
width=.5   
x=range(len(percents))  

colors=['cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan',
        'cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan',
        'cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan','cyan',
       'magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta',
     'magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta']

plt.bar(x,percents,width,color=colors)
plt.xlabel('Sovereign Nation')
plt.title('The 60 Slowest Growing (or Shrinking) Nations by Population')
plt.ylabel('Annual growth 2010-2015')

red_patch = mpatches.Patch(color='cyan', label='Europe')
green_patch = mpatches.Patch(color='magenta', label='Other')
plt.legend(handles=[red_patch,green_patch],loc=3)

plt.show()







