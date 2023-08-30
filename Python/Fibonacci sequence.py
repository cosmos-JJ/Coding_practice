#피보나치 수열 : 1 1 2 3 5 8 13 ....
#a1 = 1 ,a2 = 1 ,an= (n-1) + (n-2) 


#재귀함수를 이용하여 피보나치 수열 나타내기


def fibonacci(n):
    if n==1 or n==2 : 
        return 1           
    else:
        return fibonacci(n-1) + fibonacci(n-2)    

value = int(input())

count = value
for i in range (0,value):
    print(fibonacci(count))
    count -= 1
