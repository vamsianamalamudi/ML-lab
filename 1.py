#program1 findS
import csv 
with open('prg1.csv','r') as f :
    reader = csv.reader(f)
    your_list = list(reader)
h = [['0','0','0','0','0','0']]
for i in your_list :    
    print(i)    
    if i[-1] == "yes":
        j = 0
        for x in i:
            if x != "yes":
                if x != h[0][j] and h[0][j] == '0':
                    h[0][j] = x
                elif x != h[0][j] and h[0][j] != '0':
                    h[0][j] = '?'
                else:
                    pass                
                j = j + 1
print("most specfic hypothesis is")    
print (h)
