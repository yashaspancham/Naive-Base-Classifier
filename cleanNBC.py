#Step-1:Calculation occurence
f=open("/home/yashas/Desktop/delete me later/clg.csv",'r')
full=f.readlines()
f.close()
f=open("/home/yashas/Desktop/delete me later/clg.csv",'r')
title=list((f.readline()).split(','))
title.pop(-1)
INPUT=list(input(f"Enter the conditions in the order {title}: ").split(","))
count_list=[] #occurrence of quality attributes
list_yes=[] #occurrence of quality attributes and yes
list_no=[] #occurrence of quality attributes and no
prob_list_yes=[] #probability of occurrence of quality attributes and yes
prob_list_no=[] #probability of occurrence of quality attributes and no
for i in title:
    count_list.append(0)
    list_yes.append(0)
    list_no.append(0)
    prob_list_yes.append(0)
    prob_list_no.append(0)
for i in range(0,len(full)):
    temp_list=list(full[i].split(","))
    for  j in range(0,len(INPUT)):
        if INPUT[j] in temp_list:
            count_list[j]+=1
        if INPUT[j] in temp_list and 'Yes\n' in temp_list:
            list_yes[j]+=1
        if INPUT[j] in temp_list and 'No\n' in temp_list:
            list_no[j]+=1
f.close()
#End of Step-1

#step-2 calculation of chance
for j in range(0,len(prob_list_no)):
    prob_list_no[j]=list_no[j]/count_list[j]
for k in range(0,len(prob_list_yes)):
    prob_list_yes[k]=list_yes[k]/count_list[k]
#end of step-2

#step-3 Calculation of final result
p_final_yes=1
p_final_no=1
for i in range(0,len(prob_list_yes)):
    p_final_yes=p_final_yes*prob_list_yes[i]
for e in range(0,len(prob_list_no)):
    p_final_no=p_final_no*prob_list_no[e]
if p_final_yes>p_final_no:
    print("Yes")
else:
    print("No")
#End of step-3
#try i/p- 1)Autonomous,B,5,3 2)Deemed,S,4,2
