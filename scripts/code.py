
# extract dataframe from excel-> convert into a array-> convert all 0's into zero.

import pandas as pd
import math 
import numpy as np
from scipy.stats import sem

df = pd.read_csv (r'C:/Users/prakr/OneDrive/Desktop/Term paper/burs_nachbac_baseline.csv')   
df = df.iloc[range(0,len(df),1),64:96]
df = df[0:1440]

ls = []                         
                      

for col in df.columns:
    col_ls = df[col].tolist()
    ls.append((col_ls))    
    
d_lst=[]
for sublist in ls:
    for item in sublist:
        d_lst.append(item)
d_lst = [int((x)) for x in d_lst] 

main=[d_lst[1440*x:1440*x+1440] for x in range(0,math.ceil(len(d_lst)/1440))]
hour=[d_lst[60*x:60*x+60] for x in range(0,math.ceil(len(d_lst)/60))]


for a in main:
    k = 5
    for i in range(len(a)-5):
        if a[i:i+k] == [0 for i in range(k)]:
            a[i:i+k] = ['zero' for i in range(k)]
    for i in range(len(a)-1):
        if a[i] == 'zero' and a[i+1] == 0:
            a[i+1] = 'zero'

list2= []
for i in main:
    for j in i:
        list2.append(j)


per_day=[hour[24*x:24*x+24] for x in range(0,math.ceil(len(hour)/24))]

#---------------------------------------------COUNTMIN----------------------------------------------------------------------------
countm=[]
countmin=[]
countminn=[]
numerator=[]
denominator=[]
for i in per_day:
    for j in i:
        min=[]
        for e in j:
            if e != 0:   
                min.append(e)  
        countm.append(min)
    countm.append
print(countm)
per_fly=[countm[24*x:24*x+24] for x in range(0,math.ceil(len(countm)/24))]
print(per_fly)

for i in per_fly:
    for j in i:
        n=(sum(j))
        numerator.append(n)
per_f=[num[24*x:24*x+24] for x in range(0,math.ceil(len(num)/24))]

for i in per_day2:
    for j in i:
        min=[]
        for e in j:
            if e != 'zero':   
                min.append(e)  
        countminn.append(min)
per_fly1=[countminn[24*x:24*x+24] for x in range(0,math.ceil(len(countminn)/24))]

for i in per_fly1:
    for j in i:
        d=(len(j))
        den.append(d)
per_f1=[den[24*x:24*x+24] for x in range(0,math.ceil(len(den)/24))]

for m,n in zip(num,den):
    z= m/n if n!= 0 else 0
    countmin.append(z)
per_f2=[countmin[24*x:24*x+24] for x in range(0,math.ceil(len(countmin)/24))]

cm=np.array(per_f2)
cm_avg=np.mean(cm)
error=np.std(cm)/np.sqrt(len(cm))

frame1=pd.DataFrame(per_f2, columns = ['hr-1', 'hr-2','hr-3','hr-4','hr-5','hr-6','hr-7','hr-8','hr-9','hr-10','hr-11','hr-12','hr-13', 'hr-14','hr-15','hr-16','hr-17','hr-18','hr-19','hr-20','hr-21','hr-22','hr-23','hr-24'])
w=frame1.sem()
w1=w.transpose()
print(w1)
idx = 0
data = ['Ch-1', 'Ch-2', 'Ch-3', 'Ch-4','Ch-5','Ch-6','Ch-7','Ch-8','Ch-9','Ch-10','Ch-11','Ch-12','Ch-13','Ch-14','Ch-15','Ch-16','Ch-17','Ch-18','Ch-19','Ch-20','Ch-21','Ch-22','Ch-23','Ch-24','Ch-25','Ch-26','Ch-27','Ch-28','Ch-29','Ch-30','Ch-31','Ch-32']
frame1.insert(loc=idx, column='fly', value=data) 

#------------------------------------------------------SLEEP/HOUR-----------------------------------------------------------------

d=[list2[60*x:60*x+60] for x in range(0,math.ceil(len(list2)/60))]
p=[d[24*x:24*x+24] for x in range(0,math.ceil(len(d)/24))]
mph=[]
for i in p:
    for j in i:
        #print(j)                            
        cnt= j.count('zero')
        mph.append(cnt)


new2_lst=[mph[24*x:24*x+24] for x in range(0,math.ceil(len(mph)/24))]


frame=pd.DataFrame(new2_lst, columns = ['hr-1', 'hr-2','hr-3','hr-4','hr-5','hr-6','hr-7','hr-8','hr-9','hr-10','hr-11','hr-12','hr-13', 'hr-14','hr-15','hr-16','hr-17','hr-18','hr-19','hr-20','hr-21','hr-22','hr-23','hr-24'])
chng9=frame.transpose()   
x=chng9.to_numpy()
er=[]
for i in x:
    er.append(sem(i))

idx = 0
data = ['Ch-1', 'Ch-2', 'Ch-3', 'Ch-4','Ch-5','Ch-6','Ch-7','Ch-8','Ch-9','Ch-10','Ch-11','Ch-12','Ch-13','Ch-14','Ch-15','Ch-16','Ch-17','Ch-18','Ch-19','Ch-20','Ch-21','Ch-22','Ch-23','Ch-24','Ch-25','Ch-26','Ch-27','Ch-28','Ch-29','Ch-30','Ch-31','Ch-32']
frame.insert(loc=idx, column='fly', value=data)  

#---------------------------------------------------------DAY&NIGHT BOUTS---------------------------------------------------------------

new3_lst=[list2[720*x:720*x+720] for x in range(0,math.ceil(len(list2)/720))]

    
day=new3_lst[::2]

day_lst=[]
day1_lst=[]
for i in day:
    day_lst=[]                          
    count=0
    for e in i:
        if e== 'zero':
            count=count+1    
        else:
            if(count>=5):
                day_lst.append(count)
            count=0
    if(count>=5):
        day_lst.append(count)
            
    day1_lst.append(day_lst)
 

night=new3_lst[1:][::2]

night_lst=[]
night1_lst=[]
for i in night:
    night_lst=[]                          
    count=0
    for e in i:
        if e== 'zero':
            count=count+1    
        else:
            if(count>=5):
                night_lst.append(count)
            count=0
    if(count>=5):
        night_lst.append(count)
            
    night1_lst.append(night_lst)



zeroCount = 0
countLst = []
for i in night:
    print(i)
    for j in i:
        if j == "zero":
            countLst.append(zeroCount+1 if (zeroCount) != 0 else 0)
            break
        zeroCount+=1
    zeroCount=0


#-----------------------------------------------------Deep SLEEP-----------------------------------------------------------------------

list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
list_6=[]
list_7=[]
list_8=[]
list_9=[]  

for lst in day1_lst:
    
        len_d_lst= (len(lst))    
        sum_d_lst= (sum(lst))
        avg_d_lst=(sum(lst) / len(lst)) if (len(lst)) != 0 else 0
        
        list_1.append(lst)
        list_2.append(len_d_lst)                     #Total number of day bouts - day
        list_3.append(sum_d_lst)                     #Total minutes of deep sleep - day 
        list_4.append(avg_d_lst)                     #Average deep sleep per fly - day
        
for lstt in night1_lst:
    
        len_n_lst= (len(lstt))
        sum_n_lst= (sum(lstt))
        avg_n_lst=(sum(lstt) / len(lstt)) if (len(lstt)) != 0 else 0
        
        list_5.append(lstt)
        list_6.append(len_n_lst)                     #Total number of day bouts - night
        list_7.append(sum_n_lst)                     #Total minutes of deep sleep - night
        list_8.append(avg_n_lst)                     #Average deep sleep per fly - night

for i,j in zip(list_3,list_7):
    list_9.append(i+j)

list_11= (sum(list_9) / len(list_9)) if (len(list_9)) != 0 else 0


    
#---------------------------------------------------------CONVERSION----------------------------------------------------------------------

jnt_list=[list_1,list_2,list_3,list_4]                
jnt_list1=[list_5,list_6,list_7,list_8]
jnt_list2=[list_9,countLst]

d_frame=pd.DataFrame(jnt_list)            
d_frame1=pd.DataFrame(jnt_list1)
d_frame2=pd.DataFrame(jnt_list2) 
chng=d_frame.transpose()              
chng1=d_frame1.transpose() 
chng2=d_frame2.transpose() 
chng.columns =["length of day bouts","Total no. of day bouts","Total minutes of deep sleep in daylight","Average day bout length"]  
chng1.columns =["length of night bouts","Total no. of night bouts","Total minutes of deep sleep in night","Average night bout length"]
chng2.columns =["Total deep sleep in a day","Latency"]
idx = 0
data = ['Ch-1', 'Ch-2', 'Ch-3', 'Ch-4','Ch-5','Ch-6','Ch-7','Ch-8','Ch-9','Ch-10','Ch-11','Ch-12','Ch-13','Ch-14','Ch-15','Ch-16','Ch-17','Ch-18','Ch-19','Ch-20','Ch-21','Ch-22','Ch-23','Ch-24','Ch-25','Ch-26','Ch-27','Ch-28','Ch-29','Ch-30','Ch-31','Ch-32',]
chng.insert(loc=idx, column='fly', value=data)
chng1.insert(loc=idx, column='fly', value=data)
chng2.insert(loc=idx, column='fly', value=data)
#sum_column = chng["Total minutes of deep sleep in daylight"] + chng1["Total minutes of deep sleep in night"]
#chng2["Total deep sleep in a day"] = sum_column
#print(chng)
#print(chng1)
print(chng2)


writer2 = pd.ExcelWriter('Gen-3.xlsx')
 
chng.to_excel(writer2, sheet_name = 'Day sleep', index = False)
chng1.to_excel(writer2, sheet_name = 'Night sleep', index = False)
chng2.to_excel(writer2, sheet_name = 'TsLt', index = False)
frame.to_excel(writer2, sheet_name = 'Sleep per hour', index = False)
frame1.to_excel(writer2, sheet_name = 'Countmin', index = False)
 
writer2.save()    

