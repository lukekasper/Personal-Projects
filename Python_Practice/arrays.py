from collections import Counter


# if the element is found in the list
# function  must return true or else
# return false
def search_ele(a, x):
    return x in a


# function must return true if
# insertion is successful or else
# return false
def insert_ele(a, y, yi):
    if abs(yi) < len(a):
        a.insert(yi, y)
        return True
    else:
        return False


# function must return true if
# deletion is successful or else
# return false
def delete_ele(a, z):
    if z in a:
        a.remove(z)
        return True
    else:
        return True


# print min/max value of array
def max_min(a):
    min_val, max_val = a[0], a[0]
    for i in a:
        if i <= min_val:
            min_val = i
        if i >= max_val:
            max_val = i

    return min_val, max_val


# print second largest value of array
def second_max(a):
    max_val = a[0]
    for i in a:
        if i >= max_val:
            max_val = i

    a.remove(max_val)
    sec_max = a[0]

    for i in a:
        if i >= sec_max:
            sec_max = i
    return sec_max

    '''ALT SOLUTION:
    arr1=list(set(arr))
    arr1.sort()
    if len(arr1)==1:
      return -1
     
    else:    
    return arr1[-2]
    '''


# rotate array by D elements
def rotate_array(a, d):
    array_new = a[d:]
    array_new.extend(a[0:d])
    return array_new


def remove_duplicates(a):
    i = 0
    while i < len(a):
        if a[i] in a[i+1:]:
            a.pop(i)
            i -= 1
        i += 1
    return a, len(a)


# function to count the number of possible triangles.
def find_num_triangles(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n-2):
        k = i+2
        for j in range(i+1, n):
            while k < n and arr[i]+arr[j] > arr[k]:
                k += 1
            if k > j:
                count += k-j-1
    return count


# find leader in array, a leader means it's greater than or equal to all elements to its right
def leaders(a):
    lead_list = []
    for i in range(len(a)-1):
        sorted_list = a[i+1:]
        sorted_list.sort(reverse=True)
        if a[i] >= sorted_list[0]:
            lead_list.append(a[i])

    lead_list.append(a[-1])
    return lead_list


# find the minimum distance between two numbers in an array
def min_dist(a, x, y):
    dist = -1
    for i in range(len(a)):
        if a[i] == x:
            j = 0
            while j < len(a):
                if a[j] == y:
                    if dist == -1 or dist > abs(i - j):
                        dist = abs(i - j)
                j += 1

    return dist

    '''ALT Solution (less loops)
    idx1=-1; idx2=-1; min_dist = 999999;
    for i in range(n) :
       # if current element is x then change idx1
       if arr[i]==x :
          idx1=i
           
       # if current element is y then change idx2
       elif arr[i]==y :
          idx2=i
        
       # if x and y both found in array
       # then only find the difference and store it in min_dist
       if idx1!=-1 and idx2!=-1 :
           min_dist=min(min_dist,abs(idx1-idx2));
     
    # if left or right did not found in array
    # then return -1
    if idx1==-1 or idx2==-1 :
        return -1
    # return the minimum distance
    else :
        return min_dist
    '''


# find any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k
def sub_seq(a):
    seq_subset = []
    i = 0
    while i < len(a)-2:
        j = i + 1
        while j < len(a) - 1:
            k = j + 1
            while k < len(a):
                if a[i] < a[j] < a[k]:
                    seq_subset.append((a[i], a[j], a[k]))
                k += 1
            j += 1
        i += 1
    return seq_subset


# max (max sum) sub-array of non-negative numbers
def max_sub(a):
    max_arr = []
    i = 0
    while i < len(a) - 1:
        if a[i] < 0:
            continue
        j = i + 1
        current_arr = [a[i]]

        while a[j] > 0:
            current_arr.append(a[j])
            if j == len(a) - 1:
                break
            j += 1

        if sum(max_arr) < sum(current_arr) or len(max_arr) == 0:
            max_arr = current_arr

        i = j + 1

    return max_arr


# tell if number of occurrences of an element of the array is a majority of the array
def majority_element(a):
    k = Counter(a)
    for i in k.keys():
        if k[i] > len(a) // 2:
            return i
    else:
        return -1


# find max distance in array of A[i] <= A[j] and i <= j
def max_separation(a):
    max_dist = -1
    for i in range(len(a)):
        j = len(a)-1
        while i < j:
            if a[i] <= a[j]:
                max_dist = max(max_dist, j-i)
                break
            j -= 1
    return max_dist


# find max sum between two arrays, switching paths only when numbers are duplicated between arrays
def max_sum_path(a, b):
    suma = sumb = i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            suma += a[i]
            i += 1
        elif a[i] > b[j]:
            sumb += b[j]
            j += 1
        else:
            suma += a[i]
            sumb += b[j]
            suma = sumb = max(suma, sumb)
            i += 1
            j += 1

    while i < len(a):
        suma += a[i]
        i += 1

    while j < len(b):
        sumb += b[j]
        j += 1

    return max(suma, sumb)


# construct a product array, where each element is a product of all other elements in the array except the current one
def product_arr(a):
    prod_arr = []
    for i in range(len(a)):
        j = 0
        prod = 1
        while j < len(a):
            if j != i:
                prod *= a[j]
            j += 1
        prod_arr.append(prod)

    return prod_arr


# return duplicates in an array
def duplicates(a):
    c = 0
    d = {}
    e = []
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i, j in d.items():
        if j > 1:
            c += 1
            e.append(i)
    s = sorted(e)
    if c > 0:
        return s
    else:
        return [-1]


# print which days to buy and sell stock based on array a of stock prices to maximize profit
def buy_stock(a):
    data = []
    buy_ind = sell_ind = i = 0
    while i < len(a)-1:

        if a[i+1] >= a[i]:
            sell_ind += 1
            i += 1
            continue

        if buy_ind != sell_ind:
            data.append((buy_ind, sell_ind))

        buy_ind = sell_ind

        if a[i+1] < a[i]:
            buy_ind += 1
            i += 1
            sell_ind = buy_ind
            continue

    if buy_ind < sell_ind:
        data.append((buy_ind, sell_ind))

    return data


# given array representing height of blocks, how much rain water is trapped between blocks
def rain_trapped(a):
    ans = left = 0
    n = len(a)
    right = n - 1
    left_max = a[0]
    right_max = a[n - 1]
    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, a[left])
            ans += left_max - a[left]
        else:
            right -= 1
            right_max = max(right_max, a[right])
            ans += right_max - a[right]
    return ans


# given an array representing number of chocolate pieces per package
# divide as evenly as possible between m number of students
def chocolates(a, m):
    a.sort()
    i = 0
    min_dif = float('inf')
    j = m - 1
    while j < len(a):
        min_dif = min(min_dif, a[j] - a[i])
        j += 1
        i += 1

    return min_dif


# find length of longest sub-sequence of consecutive ints (can be in any order)
def sub_set(a):
    a.sort()
    length = count = 1
    p = a[0]+1

    for i in range(1, len(a)-1):
        if p in a:
            p += 1
            count += 1
        else:
            p = a[i+1]
            length = max(length, count)
            count = 0

    if a[-1] == a[-2] + 1:
        count += 1

    length = max(length, count)

    return length

