N = int(input("Ввекдите число N: "))
i = 2
list1 = []
old  = N
while i <= N:
    if N % i == 0:
        list1.append(i)
        N //= i
        i = 2
    else:
        i += 1
    
print(f"Простые множетели числа {old} представлены в списке: {list1} ")