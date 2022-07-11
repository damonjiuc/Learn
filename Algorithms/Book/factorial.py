def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

def fact_for(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

def fact_while(x):
    i = 1
    fact = 1
    while i != x + 1:
        fact *= i
        i += 1
    return fact

n = 2
print(fact(n))
print(fact_for(n))
print(fact_while(n))