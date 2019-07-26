#1) if-elif-else

x=1000;y=400;z=70;
if x>y & x>z:
  print "x is max";
elif y>z:
   print "y is max";
else:
 print "z is max";

#2) while

i=1;
while i<=10:
 print i;
 i=i+1;
 
#2.1) from 1 to 100

i=1;
while i<=100:
  print i;
  i=i+1;
 
#3)For loop

for i in range (1,10,1):
 print i;
#3.1) odd no

for i in range(1,10,2):
 print i;

#3.2) even no

for i in range(1,10):
      if i%2==0:
        print i,  ;

#3.3) Numbers in reverse order 
for i in range(-10,1,1):
  print -i;

#3.4) Print same no

n=5;
for i in range(1,10):
        print n;
#3.5) Multiplication table

n=input("enter num for mul = ");
for i in range (1,10):
 print ("{0}x{1}={2}".format(n,i,n*i));

#3.6) range of no's printed repeatedly

for j in range(1,6):
 for i in range(1,6):
            print i,;
 print;

#3.7) To print in format

for j in range(1,6):
 for i in range(1,j):
         print i,;
 print; 
print "----------Or-----------";

for j in range(1,6):
 for i in range(1,j+1):
             print i,;
 print;
print "------------------------------";

#3.7) To print in reverse format

for j in range(-6,1):
  for i in range(1,-j):
               print i,;
  print;

#3.8) Runtime array

x=[];
for i in range(0,5):
    n=input("enter a value");
    x.append(n);
for ele in x:
        print ele,;
