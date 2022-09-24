s="pwwkew"
counter =0
breaker =0
#print(s)
letters=[]
countlist =[]

for x in s:
    #print(x)
    letters.append(x)
    counter+=1
    breaker = 0
    for j  in range(breaker,len(letters)-1):
        
        
        if(letters[j] ==x):
            breaker =j
            counter = counter -(j+1)
            for i in range(j+1):
                letters.pop(0)
            
            break
            
    countlist.append(counter)
max =0
for a in range (len(s)):
    if(countlist[a] > max):
        max = countlist[a]
        
print(countlist)
print(max)