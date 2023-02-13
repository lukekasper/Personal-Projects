import math

# print the pattern
# Input: 3
# Output:
# 3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $
def print_pat(n):
    str = ''
    i = n
    while i > 0:
        for j in range(n, 0, -1):
            for k in range(i, 0, -1):
                str += '%d ' % j
        str += '$'
        i -= 1
    return str


# print multiplication table for N from 1-10
def get_table(n):
    table = []
    for i in range(1, 11):
        table.append(i*n)

    return table


# print the nth term of the arithmatic sequence
def nth_term(a1, a2, n):
    return (a2 - a1)*n


# print the nth term of the geometric sequence, print it in modulo format
def nth_term(a1, r, n):
    nth = a1*r*n
    return nth % (10 ^ 9 + 7)


# find the number closest to N and divisible by M, if more than one exists, output absolute max
def closest_num(n, m):

    i = 1
    while True:
        a1 = (n - i)
        a2 = (n + i)
        m1 = a1 % m
        m2 = a2 % m

        if m1 == 0 and m2 == 0:
            if abs(a1) > abs(a2):
                ans = a1
            else:
                ans = a2
            break
        elif m1 == 0:
            ans = a1
            break
        elif m2 == 0:
            ans = a2
            break
        i += 1

    return ans


# determine if a 3 digit number is an Armstrong number
def armstrong(n):
    digits = [int(str(n)[0]), int(str(n)[1]), int(str(n)[2])]
    return digits[0] ** 3 + digits[1] ** 3 + digits[2] ** 3 == n


# sum of digits is a palindrome?
def digit_pal(n):

    s = str(n)
    dig_sum = 0
    for i in s:
        dig_sum += int(i)
    dig_sum = str(dig_sum)

    if dig_sum[::-1] == dig_sum[::]:
        return 1
    else:
        return 0


# reverse digits of N
def reverse(n):
    s = str(n)
    return s[::-1]


# binary to decimal
def bin2dec(b):
    s = str(b)[::-1]
    dec = 0
    for i in range(0, len(s)):
        dec += int(s[i])*2**i

    return dec


# Given a positive number X. Find the largest Jumping Number which is smaller than or equal to X
# Jumping number has all adjacent digits differ by only 1
def jumping(n):
    for i in range(n, 0, -1):
        i_str = str(i)
        flag = 1
        for j in range(0, len(i_str)-1):
            if abs(int(i_str[j]) - int(i_str[j+1])) != 1:
                flag = 0
                break

        if flag == 1:
            return i_str

    return None


# Given two positive integers A and B, find GCD and LCM of A and B
def gcd_lcm(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break

    for j in range(max(a, b), a*b+1):
        if j % a == 0 and j % b == 0:
            lcm = j
            break

    return i, j


# find the largest prime factor of n
def large_prime(n):
    for i in range(n, 0, -1):
        is_prime = True

        for j in range(i-1, 1, -1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            if n % i == 0:
                return i


# return if n is a perfect number
def perfect_num(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return n == sum(factors)


# Given N, count all ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a3 + b3 = N
def cube_count(n):
    count = 0
    for i in range(1, math.floor(n**(1/3))+1):
        for j in range(0, math.floor(n**(1/3))+1):
            if i**3 + j**3 == n:
                count += 1

    return count


