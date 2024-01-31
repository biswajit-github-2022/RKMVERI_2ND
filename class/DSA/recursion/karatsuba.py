def karatsuba(x, y):
    # Base case: If the numbers are single-digit, use the standard multiplication
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    # Split the numbers into halves
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    a = x // 10**n2
    b = x % 10**n2
    c = y // 10**n2
    d = y % 10**n2

    # Recursively compute three products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the products to get the final result
    result = ac * 10**(2*n2) + ad_bc * 10**n2 + bd

    return result

# Example usage:
num1 = 1234
num2 = 5678

result = karatsuba(num1, num2)
print(f"The result of {num1} * {num2} using Karatsuba multiplication is: {result}")
