a, b , c= 0,1,0
x = int(input("please input the number column : \n"))
y = int(input("please input the number row : \n"))

for i in range(y):
    for j in range(x):
        print(a,' ', end='')
        c=a+b
        a=b
        b=c
    print("\n")  