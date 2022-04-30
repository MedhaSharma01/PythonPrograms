# WAP to Find out the sum of all the squares of all the numbers upto n.
a = int(input("enter the number  "))
n = 0
sum = 0
while(n <= a):
    sum += (n*n)
    n += 1
print(sum)
