#1) Len

str="hello world"
print len(str);

#1.1) Len 
 
print len("Anjana");

#2) Capitalize 1st word

str="hello sir";
print str.capitalize();

#3) All 1st words capital

str="hello sir, who are you?";
print str.title();

#4) Gives position of the character in the string

str="hello world";
print str.index("w");

#5) gives character in that position

str="hello";
print str[3];

#6) ASCII char of that number

print chr(97);

#6.1) ASCII value of that char

print ord('a');

#7) For ASCII no's in a range

for i in range(65,91):
 print i,;
print;

#7.1)For ASCII char in a range

for i in range(65,91):
  print chr(i),;
print;

#7.2)For 1-9 in ASCII

for i in range(48,57):
  print chr(i);

#8) to convert lowercase to uppercase

str="hello world"
print str.upper();

#8.1) upper to lower case

str="HELLO WORLD";
print str.lower();

#8.2)Check the lower case

str="Valli";
print str.islower();

#8.3)Check upper case

str="valli";
print str.isupper();

#9)Check is it digit

str="123";
print str.isdigit();

#9.1) check there is alphabets

str="123";
print str.isalpha();

#9.2) check there is both alphabets & no's

str="abc123";
print str.isalnum();

#10) to replace values/char

str="red apple is red";
print str.replace("red","green");

#11) deletes the selected one

str="read this text";
print str.translate(None,"aeiou");

#12) to check there is apace 

b=" "
print b.isspace();

#13) to check how many times values are repeated

str="red apple is red";
print str.count("red");

#14) length is given including spaces

str="  abc  ";
print len(str);

#15) length is given by excluding spaces

str="  abc  ";
print len(str.strip());

#16)to delete certain char/symbols

str="@@@@@@hello world";
print str.strip('@');

#17)to check whether with which value the str is starting

str="hello";
print str.startswith("h");

#18)to check whether of which value the str is ending

str="home";
print str.endswith("me");

#19)to check 2 str's are equal or not using "=="

print "heelo"=="hello";

#19.1)to check 2 str's using "is"

str="abd";
str1="ABD";
print str is str1;
#to convert both of them into LC
str.lower() is str1.lower();
#"is" is used for original values not for the transferred ones
s1=str.lower();
s2=str1.lower();
print s1 is s2;
print s1==s2;

#20) to print the values in reverse order

str="srisaivalli";
rev=reversed(str);
print list(rev);