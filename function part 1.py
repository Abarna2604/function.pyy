print("1.ADD NUM:")
def add(a,b):
    print("SUM IS",a+b)
add(5,10)
print("2.SUB NUM:")
def sub(a,b):
    print("DIFF IS",a-b)
add(10,5)

print("3.MUL NUM:")
def multi(a,b):
    print("PRODUCT IS",a*b)
multi(2,3)

print("4.DIVISION :")
def div (a,b):
    print("DIV IS",a/b)
div(4,2)

print("5.SQUARE OF NUMBER:")
def squart(a):
    print(a*2)
squart(2)

print("6.ODD OR EVEN:")
def number(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
number(2)
print("7.LARGEST OF TWO:")
def large(a,b):
    if(a>b):
        print("a is lsrgest")
    else:
        print("b is largest")
large(2,4)

print("8.SUM OF LIST ELEMENT:")
def total(list):
     sum=0
     for i in list:
         sum=sum+i
         print(sum)
total([1,2,3,4])
print("9.MAXIMUM NUMBER;")
def maximum(a):
    max_val=a[0]
    for i in range(len(a)):
        if a[i]>max_val:
            max_val=a[i]
    print(max_val)
maximum([1,2,3,4])
print("10.PRIME OR NOT:")
def prime_num(a):
    for i in range(2,a):
        if(a%i==0):
         print("NOT PRIME")
         break
        else:
            print("PRIME")
prime_num(7)            
print("11.COUNT VOWELS:")
def vowels_name(a):
    len=0
    for ch in a:
        if(ch=="a"or ch=="e"or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
          len=len+1
    print(len)
vowels_name("ABARNA")
print("12.COUNT LETTERS:")
def letters(a):
    count=0
    for i in a:
        count=count+1
    print(count)
letters([1,2,3,4])    
print("13.FACTORIAL:")
def fact_num(n):
     fact=1
     for i in range(1,n):
         fact=fact*i
     print(fact)
fact_num(4)         
print("14.MULTIPLICATION TABLE:")
def multi_table():
    for i in range(1,11):
        n=i*5
        print(n)
multi_table()
print("15.REVERSE STRING:")
def rev_sstr(a):
    print(a[::-1])
rev_sstr("BESANT")    

         
       

    
    




        










