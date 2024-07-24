import cv2
import string
import os
d={}
c={}
for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)

x=cv2.imread(r"C:\Users\91628\OneDrive\Desktop\stenography\image1.jpg")

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("Enter key to edit(Security key): ")
text=input("Enter text to hide: ")

kl=0
tln=len(text)
z=n=m=0
l=tln

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]
    n+=1
    m+=1
    z=(z+1)%3
    kl=(kl+1)%len(key)
    
cv2.imwrite("encrypted.jpg", x)
os.startfile("encrypted.jpg")
print("Data hiding in image completed successfully")

kl=0
tln=len(text)
z=n=m=0

ch=int(input("\nEnter 1 to extract data from image : "))
if ch==1:
    key1=input("\n\nRe enter key to extract text: ")
    decrypt=""
    
    if key == key1:
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[kl]]]
            n+=1
            m+=1
            z=(z+1)%3
            kl=(kl+1)%len(key)
        print("Encrypted text was: ",decrypt)
    else:
        print("Key doesn't matched")
else:
    print("Thankyou. EXITING")