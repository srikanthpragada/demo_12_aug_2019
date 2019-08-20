def factors(n):
    factors_list = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors_list.append(i)

    return factors_list


print(factors(120))
