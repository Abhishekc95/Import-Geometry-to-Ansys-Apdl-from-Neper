
"""
At the time of uploading this file, python3.8 is the version used.

when running this code, .geo file from neper should be in the same directory of this file.


P.S: output can take time depending on the number of tessellations and hardware utilised.
ex: generation of output text file takes less than 50 secs for 1,20,000 3D tessellations.

"""



import re

f1 = open ("example.geo",'r')             # insert your .geo file name here
f2 = open ("output.txt",'w')             # output filename -- prints all the apdl commands in the text file  after runnning this script

st = f1.read()

pattern1 =re.compile(r'Point\s\((\d*)\)\s\=\s\{(-?\d*\.\d*\,-?\d*\.\d*\,-?\d*\.\d*)')

matches1 = pattern1.finditer(st)

count = 0

for match1 in matches1:
    print("K,",match1.group(1),",",match1.group(2), file =f2)
    count = count + 1

print ("C*** keypoint count = ",count, file = f2) 
print ("C*** keypoint count = ",count)

count = 0
pattern2 = re.compile(r'Line\s\(\d*\)\s\=\s\{(\d*\,\d*)\}')

matches2 = pattern2.finditer(st)

for match2 in matches2:
    count = count + 1
    print("L,",match2.group(1)," ! ", count, file =f2)
    
    
print("C*** line count = ",count, file = f2)

print("C*** line count = ",count)


count = 0    
pattern3 = re.compile(r'Line\sLoop.*\b')

matches3 = pattern3.finditer(st)

for match3 in matches3:
    list3 =  re.findall(r'-?(\d+)',match3.group(0))
    list3.pop(0)
    count = count + 1
    if len(list3) > 10:
        print("allsel",file=f2)
        print ("lsel,r,line,,",list3[0],file=f2)
        for i in range(1,len(list3)):
            print("lsel,a,line,,",list3[i],file=f2)
        print("AL,all  ! ",count, file=f2)
        print("allsel",file=f2)
    else:
        print ("AL,",','.join(list3), " ! ",count,file =f2)
    
    

print("C*** area count = ",count, file = f2)

print("C*** area count = ",count)
 
count = 0
pattern4 = re.compile(r'Surface\sLoop.*\b')

matches4 = pattern4.finditer(st)

for match4 in matches4:
    list4 = re.findall(r'-?(\d+)',match4.group(0))
    list4.pop(0)
    if len(list4) > 10:
        print("allsel",file=f2)
        print ("asel,r,area,,",list4[0],file=f2)
        for i in range(1,len(list4)):
            print("asel,a,area,,",list4[i],file=f2)
        print("VA,all",file=f2)
        print("allsel",file=f2)
    else:
        print ("VA,",','.join(list4),file =f2)
    count = count + 1

print("C*** volume count = ",count, file =f2)     
print("C*** volume count = ",count)  