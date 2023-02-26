# count number of square numbers < N
import math


def count_squares(n):
    count = 0
    for i in range(1, math.floor(n ** 0.5) + 1):
        if i ** 2 < n:
            count += 1

    return count


# tell if 4 points form a square
def square(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    d2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    d3 = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    d4 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
    d5 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    d6 = math.sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)
    a = set([d1, d2, d3, d4, d5, d6])
    if len(a) == 2:
        return "Yes"
    else:
        return "No"


# by recieving extremes of 2 rectangle (upper left and lower right), determine if they overlap
def overlap(l1, r1, l2, r2):
    if (r1[1] > l2[1]) or (r2[1] > l1[1]) or (l2[0] > r1[0]) or (l1[0] > r2[0]):
        return 0
    return 1


# find the number of trainling zeros in n!
def trailing_z(n):
    n_fact = 1
    for i in range(n, 1, -1):
        n_fact *= i

    n_str = str(n_fact)[::-1]

    count = 0
    for j in n_str:
        if j == '0':
            count += 1
        else:
            break

    return count

    ''' ALT SOLUTION
     count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (N / i>= 1):
        count += int(N / i)
        i *= 5

    return int(count)
    '''


# determine min angle between clock hands given integer inputs of h and m
def clock_angle(h, m):
    h = h % 12
    m = m % 60

    # each term is fraction of 360 deg clock face, last term accounts for change in hour hand due to minutes
    ans = abs((h * 30) - (m * 6) + m * 0.5)

    if ans <= 180:
        return int(ans // 1)
    else:
        return int((360 - ans) // 1)  # '//' is floor division


'''
Consider a long alley with a N number of doors on one side. All the doors are closed initially. You move to and fro in 
the alley changing the states of the doors as follows: you open a door that is already closed and you close a door that 
is already opened. You start at one end go on altering the state of the doors till you reach the other end and then you 
come back and start altering the states of the doors again.
In the first go, you alter the states of doors numbered 1, 2, 3, , n.
In the second go, you alter the states of doors numbered 2, 4, 6
In the third go, you alter the states of doors numbered 3, 6, 9
You continue this till the Nth go in which you alter the state of the door numbered N.
You have to find the number of open doors at the end of the procedure.
'''


def open_doors(n):
    doors = [0]*n
    for i in range(1, n+1):
        j = i-1
        while j < n:
            if doors[j] == 0:
                doors[j] = 1
            else:
                doors[j] = 0
            j += i

    return sum(doors)

    '''
    ALTERNATE SOLUTION:
    ans=int(math.sqrt(N))
    return ans
    '''


# determine if n is a triangular number
def triangular(n):
    i, j = 1, 1
    while i <= n:
        if i == n:
            return 1
        else:
            j += 1
            i += j
    return 0


# find the nth even fibonacci number
def nth_even_fibonacci(n):
    count, i = 0, 2
    fib = [0, 1]
    while count < n:
        fib_new = fib[i-2] + fib[i-1]
        fib.append(fib_new)
        if fib_new % 2 == 0:
            count += 1
        i += 1
    return fib_new % 1000000007


# number of squares in an m x n matrix
def num_squares(m, n):
    s = 0
    while m and n:
        s += (m * n)
        m = m - 1
        n = n - 1
    return s


# calculate the day of the week for any day in the past or future
# can also import calendar and use day_num = calendar.weekday(y, m, d)
def day_of_week(d, m, y):

    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3  # either subtracts 0 or 1 depending on if m < 3 is true or false
    res = ((y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7)
    return day[res]
