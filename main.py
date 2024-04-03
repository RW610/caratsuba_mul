def karatsuba(num1: int, num2: int) -> int:
    if num1 < 10 or num2 < 10:
        return num1 * num2
    
    n = max(len(str(num1)), len(str(num2)))
    half = n // 2
    
    a, b = divmod(num1, 10 ** half)
    c, d = divmod(num2, 10 ** half)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    
    return (ac * (10 ** (2 * half))) + (ad_bc * (10 ** half)) + bd


mul = karatsuba(10, 100) 
print(mul)