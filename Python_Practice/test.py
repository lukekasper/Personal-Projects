# Given an array containing None values fill in the None values with most recent
# non None value in the array

array1 = [1, None, 2, 3, None, None, 5, None]


def solution(nums):
    for ind, num in enumerate(nums):
        if num is None:
            nums[ind] = nums[ind-1]

    return nums


# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'


def solution2(sent1, sent2):

    common = []
    not_common = []

    sent1 = sent1.split()
    sent2 = sent2.split()

    for word1 in sent1:
        for word2 in sent2:
            if word1 == word2:
                common.append(word1)

    for word in sent1:
        if word not in common:
            not_common.append(word)

    for word in sent2:
        if word not in common:
            not_common.append(word)

    return common, not_common


# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

n = 35


def solution3(num):

    primes = set()
    for i in range(2, num):
        prime_flag = 0
        for j in range(2, i):
            if i % j == 0:
                prime_flag = 1

        if prime_flag == 0:
            primes.add(i)

    return primes


print(solution3(n))
