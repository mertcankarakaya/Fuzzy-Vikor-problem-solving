# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:08:41 2020

@author: Hp
"""

print('Solving problem of "choosing the worker" that have been found from literature')

#Linguistic variables for the importance weight of each criterion
vl=[0,0,0.1] #very low (vl)
l=[0,0.1,0.3] #low (l)
ml=[0.1,0.3,0.5] #medium low (ml)
m=[0.3,0.5,0.7] #medium (m)
mh=[0.5,0.7,0.9] #medium high (mh)
h=[0.7,0.9,1] #high (h)
vh=[0.9,1,1] #very high (vh)

#Linguistic variables for the ratings
vp=[0,0,1] #very poor (vp)
p=[0,1,3] # poor (p)
mp=[1,3,5] #medium poor (mp)
f=[3,5,7] #fair (f)
mg=[5,7,9] #medium good (mg)
g=[7,9,10] #good (g)
vg=[9,10,10] #very good (vg)


#have been written values that found from literature
deciders=3
criteria=5
alternative=5

#Created a matrix of important criteria for characters of Criteria.
matrixOfImportantCriteria=[[0 for col in range(criteria)]for row in range(deciders) ]

matrixOfImportantCriteria[0][0]="h"
matrixOfImportantCriteria[0][1]="h"
matrixOfImportantCriteria[0][2]="mh"
matrixOfImportantCriteria[0][3]="mh"
matrixOfImportantCriteria[0][4]="h"
matrixOfImportantCriteria[1][0]="h"
matrixOfImportantCriteria[1][1]="mh"
matrixOfImportantCriteria[1][2]="vh"
matrixOfImportantCriteria[1][3]="m"
matrixOfImportantCriteria[1][4]="h"
matrixOfImportantCriteria[2][0]="vh"
matrixOfImportantCriteria[2][1]="m"
matrixOfImportantCriteria[2][2]="mh"
matrixOfImportantCriteria[2][3]="ml"
matrixOfImportantCriteria[2][4]="mh"



#Created a criteria matrix by matrix of important criteria.
matrixOfCriteria=[[[0 for col in range(3)]for row in range(criteria)] for x in range(deciders)]

for i in range(deciders):
    for j in range(criteria):
        for t in range(3):
            if matrixOfImportantCriteria[i][j]=='vl':
                matrixOfCriteria[i][j][t]=vl[t]
            elif matrixOfImportantCriteria[i][j]=='l':
                matrixOfCriteria[i][j][t]=l[t]
            elif matrixOfImportantCriteria[i][j]=='ml':
                matrixOfCriteria[i][j][t]=ml[t]
            elif matrixOfImportantCriteria[i][j]=='m':
                matrixOfCriteria[i][j][t]=m[t]
            elif matrixOfImportantCriteria[i][j]=='mh':
                matrixOfCriteria[i][j][t]=mh[t]
            elif matrixOfImportantCriteria[i][j]=='h':
                matrixOfCriteria[i][j][t]=h[t]
            elif matrixOfImportantCriteria[i][j]=='vh':
                matrixOfCriteria[i][j][t]=vh[t]
#Created a fuzzy criteria matrix by criteria matrix.         
total=0
matrixOfFuzzyCriteria = [[0 for col in range(3)]for row in range(criteria) ]
for i in range(criteria):
    for j in range(3):
        for k in range(deciders):
            total=total+matrixOfCriteria[k][i][j]
        mean_value=total/deciders
        mean_value=round(mean_value,2)
        matrixOfFuzzyCriteria[i][j]=mean_value
        total=0
        mean_value=0 
        

#Created a matrix of important alternative for characters of Criteria.
matrixOfImportantAlternative=[[[0 for col in range(deciders)]for row in range(criteria) ]for x in range(alternative)]

matrixOfImportantAlternative[0][0][0]="g"
matrixOfImportantAlternative[0][0][1]="mg"
matrixOfImportantAlternative[0][0][2]="mg"
matrixOfImportantAlternative[0][1][0]="mg"
matrixOfImportantAlternative[0][1][1]="vg"
matrixOfImportantAlternative[0][1][2]="mg"
matrixOfImportantAlternative[0][2][0]="f"
matrixOfImportantAlternative[0][2][1]="mg"
matrixOfImportantAlternative[0][2][2]="mp"
matrixOfImportantAlternative[0][3][0]="vg"
matrixOfImportantAlternative[0][3][1]="vg"
matrixOfImportantAlternative[0][3][2]="vg"
matrixOfImportantAlternative[0][4][0]="f"
matrixOfImportantAlternative[0][4][1]="f"
matrixOfImportantAlternative[0][4][2]="mg"
matrixOfImportantAlternative[1][0][0]="g"
matrixOfImportantAlternative[1][0][1]="mg"
matrixOfImportantAlternative[1][0][2]="f"
matrixOfImportantAlternative[1][1][0]="mg"
matrixOfImportantAlternative[1][1][1]="mg"
matrixOfImportantAlternative[1][1][2]="mp"
matrixOfImportantAlternative[1][2][0]="p"
matrixOfImportantAlternative[1][2][1]="vg"
matrixOfImportantAlternative[1][2][2]="p"
matrixOfImportantAlternative[1][3][0]="g"
matrixOfImportantAlternative[1][3][1]="mg"
matrixOfImportantAlternative[1][3][2]="g"
matrixOfImportantAlternative[1][4][0]="f"
matrixOfImportantAlternative[1][4][1]="mp"
matrixOfImportantAlternative[1][4][2]="mp"
matrixOfImportantAlternative[2][0][0]="vg"
matrixOfImportantAlternative[2][0][1]="vg"
matrixOfImportantAlternative[2][0][2]="g"
matrixOfImportantAlternative[2][1][0]="g"
matrixOfImportantAlternative[2][1][1]="vg"
matrixOfImportantAlternative[2][1][2]="vg"
matrixOfImportantAlternative[2][2][0]="f"
matrixOfImportantAlternative[2][2][1]="f"
matrixOfImportantAlternative[2][2][2]="mp"
matrixOfImportantAlternative[2][3][0]="g"
matrixOfImportantAlternative[2][3][1]="mg"
matrixOfImportantAlternative[2][3][2]="f"
matrixOfImportantAlternative[2][4][0]="g"
matrixOfImportantAlternative[2][4][1]="vg"
matrixOfImportantAlternative[2][4][2]="vg"
matrixOfImportantAlternative[3][0][0]="mp"
matrixOfImportantAlternative[3][0][1]="mp"
matrixOfImportantAlternative[3][0][2]="f"
matrixOfImportantAlternative[3][1][0]="mp"
matrixOfImportantAlternative[3][1][1]="f"
matrixOfImportantAlternative[3][1][2]="mp"
matrixOfImportantAlternative[3][2][0]="vg"
matrixOfImportantAlternative[3][2][1]="g"
matrixOfImportantAlternative[3][2][2]="g"
matrixOfImportantAlternative[3][3][0]="mp"
matrixOfImportantAlternative[3][3][1]="f"
matrixOfImportantAlternative[3][3][2]="f"
matrixOfImportantAlternative[3][4][0]="f"
matrixOfImportantAlternative[3][4][1]="f"
matrixOfImportantAlternative[3][4][2]="f"
matrixOfImportantAlternative[4][0][0]="mp"
matrixOfImportantAlternative[4][0][1]="mp"
matrixOfImportantAlternative[4][0][2]="f"
matrixOfImportantAlternative[4][1][0]="vg"
matrixOfImportantAlternative[4][1][1]="vg"
matrixOfImportantAlternative[4][1][2]="g"
matrixOfImportantAlternative[4][2][0]="mg"
matrixOfImportantAlternative[4][2][1]="f"
matrixOfImportantAlternative[4][2][2]="f"
matrixOfImportantAlternative[4][3][0]="vg"
matrixOfImportantAlternative[4][3][1]="vg"
matrixOfImportantAlternative[4][3][2]="g"
matrixOfImportantAlternative[4][4][0]="mp"
matrixOfImportantAlternative[4][4][1]="f"
matrixOfImportantAlternative[4][4][2]="f"

#Created a alternative matrix by matrix of important alternative.
matrixOfAlternative=[[[[0 for col in range(3)]for row in range(deciders)]for x in range(criteria) ]for y in range(alternative)]

for i in range(alternative):
    for j in range(criteria):
        for t in range(deciders):
            for k in range(3):
                if matrixOfImportantAlternative[i][j][t]=='vp':
                    matrixOfAlternative[i][j][t][k]=vp[k]
                elif matrixOfImportantAlternative[i][j][t]=='p':
                    matrixOfAlternative[i][j][t][k]=p[k]
                elif matrixOfImportantAlternative[i][j][t]=='mp':
                    matrixOfAlternative[i][j][t][k]=mp[k]
                elif matrixOfImportantAlternative[i][j][t]=='f':
                    matrixOfAlternative[i][j][t][k]=f[k]
                elif matrixOfImportantAlternative[i][j][t]=='mg':
                    matrixOfAlternative[i][j][t][k]=mg[k]
                elif matrixOfImportantAlternative[i][j][t]=='g':
                    matrixOfAlternative[i][j][t][k]=g[k]
                elif matrixOfImportantAlternative[i][j][t]=='vg':
                    matrixOfAlternative[i][j][t][k]=vg[k]
                    
#Created a fuzzy alternative matrix by alternative matrix.  
matrixOfFuzzyAlternative = [[[0 for col in range(3)]for row in range(alternative) ]for row in range(criteria)]
total=0
for i in range(alternative):
    for j in range(criteria):
        for k in range(3):
            for t in range(deciders):
                total=total+matrixOfAlternative[i][j][t][k]
            mean_value=total/deciders
            mean_value=round(mean_value,2)
            matrixOfFuzzyAlternative[j][i][k]=mean_value
            total=0
            mean_value=0

#Have been found the highest values of fj for all of criteria.
fj_high=[[0] * 3 for i in range(criteria)]
theBiggest=[]

for i in range(criteria):
    for j in range(3):
        for k in range(alternative):
            total_value=matrixOfFuzzyAlternative[i][k][j]
            theBiggest.append(total_value)
        fj_high[i][j]=max(theBiggest)
        if len(theBiggest)==criteria:
            theBiggest.clear()

#Have been found the lowest values of fj for all of criteria.
fj_low=[[0] * 3 for i in range(criteria)]
theSmallest=[]

for i in range(criteria):
    for j in range(3):
        for k in range(alternative):
            total_value=matrixOfFuzzyAlternative[i][k][j]
            theSmallest.append(total_value)
        fj_low[i][j]=min(theSmallest)
        if len(theSmallest)==criteria:
            theSmallest.clear()


#Have been found Si values.
si_matrix=[[0] * 3 for i in range(alternative)]
total_value=0
w=0
x=0
for i in range(alternative):
    for j in range(3):
        for k in range(criteria):
            for t in range(deciders):
                w=matrixOfFuzzyCriteria[k][j]
            x=matrixOfFuzzyAlternative[k][i][j]
            high=fj_high[k][j]
            low=fj_low[k][j]
            if (high-low) == 0:
                total_value=total_value+((w*(high-x))*0)
            else:
                total_value=total_value+((w*(high-x))/(high-low))
        total_value=round(total_value,2)
        si_matrix[i][j]=total_value
        total_value=0


#Have been found mean of Si values.
si_mean_value=[]
total_value=0
for i in range(alternative):
    for j in range(3):
        total_value=total_value+si_matrix[i][j]
    total_value=total_value/3
    total_value=round(total_value,2)
    si_mean_value.append(total_value)
    total_value=0

#Have been found Ri values.
ri_matrix=[[0] * 3 for i in range(alternative)]
total_value=0
w=0
x=0
for i in range(alternative):
    for j in range(3):
        for k in range(criteria):
            for t in range(deciders):
                w=matrixOfFuzzyCriteria[k][j]
            x=matrixOfFuzzyAlternative[k][i][j]
            high=fj_high[k][j]
            low=fj_low[k][j]
            if (high-low) == 0:
                total_value=(w*(high-x))*0
            else:
                total_value=(w*(high-x))/(high-low)
            total_value=round(total_value,2)
            theBiggest.append(total_value)
        ri_matrix[i][j]=max(theBiggest)
        theBiggest.clear()

#Have been found mean of Ri values.
ri_mean_value=[]
total_value=0
for i in range(alternative):
    for j in range(3):
        total_value=total_value+ri_matrix[i][j]
    total_value=total_value/3
    total_value=round(total_value,2)
    ri_mean_value.append(total_value)
    total_value=0
    
#Have been found minimum of Si values. (for l,m,u values)
si_min=[]
for i in range(3):
    for j in range(alternative):
        theSmallest.append(si_matrix[j][i])
    total_value=min(theSmallest)
    si_min.append(total_value)
    theSmallest.clear()
    
#Have been found maximum of Si values. (for l,m,u values)
si_max=[]
for i in range(3):
    for j in range(alternative):
        theBiggest.append(si_matrix[j][i])
    total_value=max(theBiggest)
    si_max.append(total_value)
    theBiggest.clear()



#Have been found minimum of Ri values. (for l,m,u values)
ri_min=[]
for i in range(3):
    for j in range(alternative):
        theSmallest.append(ri_matrix[j][i])
    total_value=min(theSmallest)
    ri_min.append(total_value)
    theSmallest.clear()
    
#Have been found maximum of Si values. (for l,m,u values)
ri_max=[]
for i in range(3):
    for j in range(alternative):
        theBiggest.append(ri_matrix[j][i])
    total_value=max(theBiggest)
    ri_max.append(total_value)
    theBiggest.clear()

#Have been found Qi values.
theBiggestS=0
theSmallestS=0
theBiggestR=0
theSmallestR=0
si=0
ri=0
v=0.5
total_value=0
qi_matrix=[[0] * 3 for i in range(alternative)]
for i in range(alternative):
    for j in range(3):
        si=si_matrix[i][j]
        theBiggestS=si_max[j]
        theSmallestS=si_min[j]
        ri=ri_matrix[i][j]
        theBiggestR=ri_max[j]
        theSmallestR=ri_min[j]
        if (theBiggestS-theSmallestS)==0 or (theBiggestR-theSmallestR)==0:
            s_total_value=v*(si-theSmallestS)*0
            r_total_value=(1-v)*(ri-theSmallestR)*0
        else:
            s_total_value=v*(si-theSmallestS)/(theBiggestS-theSmallestS)
            r_total_value=(1-v)*(ri-theSmallestR)/(theBiggestR-theSmallestR)
        total_value=s_total_value+r_total_value
        total_value=round(total_value,3)
        qi_matrix[i][j]=total_value
        

#Have been found mean of Qi values.
qi_mean_value=[]
total_value=0
for i in range(alternative):
    for j in range(3):
        total_value=total_value+qi_matrix[i][j]
    total_value=total_value/3
    total_value=round(total_value,3)
    qi_mean_value.append(total_value)
    total_value=0

#Qi alternative values of sorting
qi_mean_value_sorted=[]
qi_mean_value_sorted=sorted(qi_mean_value,reverse=False)
qi_mean_value_sorted_index=[]

for i in range(alternative):
    for j in range(alternative):
        if qi_mean_value_sorted[i]==qi_mean_value[j]:
            qi_mean_value_sorted_index.append(j)

last_qi_mean_value_sort_index=[]
for i in qi_mean_value_sorted_index:
  if i not in last_qi_mean_value_sort_index:
    last_qi_mean_value_sort_index.append(i)
            
#Si alternative values of sorting
si_mean_value_sorted=[]
si_mean_value_sorted=sorted(si_mean_value,reverse=False)
si_mean_value_sorted_index=[]

for i in range(alternative):
    for j in range(alternative):
        if si_mean_value_sorted[i]==si_mean_value[j]:
            si_mean_value_sorted_index.append(j)

last_si_mean_value_sort_index=[]
for i in si_mean_value_sorted_index:
  if i not in last_si_mean_value_sort_index:
    last_si_mean_value_sort_index.append(i)

#Ri alternative values of sorting
ri_mean_value_sorted=[]
ri_mean_value_sorted=sorted(ri_mean_value,reverse=False)
ri_mean_value_sorted_index=[]

for i in range(alternative):
    for j in range(alternative):
        if ri_mean_value_sorted[i]==ri_mean_value[j]:
            ri_mean_value_sorted_index.append(j)

last_ri_mean_value_sort_index=[]
for i in ri_mean_value_sorted_index:
  if i not in last_ri_mean_value_sort_index:
    last_ri_mean_value_sort_index.append(i)

print("----------------------------------------------------")
#Have been written at screen Qi values of sorting
print("Qi values of sorting: ",end="")
result_qi=""
for i in range(alternative):
        if qi_mean_value_sorted[i-1]==qi_mean_value_sorted[i]:
            result_qi=result_qi+" = A"+str(last_qi_mean_value_sort_index[i]+1)
        else:
            result_qi=result_qi+" > A"+str(last_qi_mean_value_sort_index[i]+1)
print(result_qi[3:])


#Have been written at screen Si values of sorting                
print("Si values of sorting: ",end="")
result_si=""
for i in range(alternative):
        if si_mean_value_sorted[i-1]==si_mean_value_sorted[i]:
            result_si=result_si+" = A"+str(last_si_mean_value_sort_index[i]+1)
        else:
            result_si=result_si+" > A"+str(last_si_mean_value_sort_index[i]+1)
print(result_si[3:])  


#Have been written at screen Ri values of sorting
print("Ri values of sorting ",end="")
result_ri=""
for i in range(alternative):
        if ri_mean_value_sorted[i-1]==ri_mean_value_sorted[i]:
            result_ri=result_ri+" = A"+str(last_ri_mean_value_sort_index[i]+1)
        else:
            result_ri=result_ri+" > A"+str(last_ri_mean_value_sort_index[i]+1)
print(result_ri[3:])


#Have been used for result.
result_liste=[]
result_liste.append(last_qi_mean_value_sort_index[0]+1)
result_liste.append(last_si_mean_value_sort_index[0]+1)
result_liste.append(last_ri_mean_value_sort_index[0]+1)

#Have been used that understanding situation of equaly, bigly and smaly.
first_total_value=result_liste[0]
second_total_value=result_liste[1]
counter=0
counter2=0
result1=0
for i in range(len(result_liste)):
    if result_liste[i]==first_total_value:
        counter=counter+1
    if result_liste[i]==second_total_value:
        counter2=counter2+1
    if counter==2 or counter2==2:
        result1=result_liste[i]

print("----------------------------------------------------")
print("From inside of Alternatives;")
if counter==1 and counter2==1:
    print("You can choose all of them for there was 3 different values... : A"+str(result_liste[0])+", A"+str(result_liste[1])+", A"+str(result_liste[2]))
elif counter==2 or counter2==2:
    print("If you choose single value, You should choose to this value: A"+ str(result1))
    result_liste.remove(result1)
    print("If you choose two values, You should choose to this values: A"+ str(result1)+", A"+ str(result_liste[0]))
else:
    print("You must choose single value : A"+str(result_liste[i]))
  

