#===============================================1
def check_brackets(s):
    stack = []
    pairs = {')' : '(', ']' : '['}
    for i in s:
        if i in pairs.values():
            stack.append(i)
        else:
            if i in pairs.keys():
                if stack == []:
                    return False
                else:
                    if pairs[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
    return not stack
 
def test_check_brackets(s, answer):
    assert check_brackets(s) == answer

test_check_brackets('()()', True)
test_check_brackets('[[]]', True)
test_check_brackets('([])[()]', True)
test_check_brackets('(]', False)
test_check_brackets('[)', False)
test_check_brackets('([)]', False)
test_check_brackets(')', False)
test_check_brackets('()]', False)
test_check_brackets('(([]())', False)


#===============================================2
def upper_bound(lst, x):
    n, l = len(lst) // 2, 2
    if lst[0] > x:
        return 0
    else:
        if lst[-1] <= x:
            return len(lst)
    while (lst[n + 1] <= x or lst[n] > x) and ((len(lst) // l) > 1):
        if x >= lst[n + 1]:
            l *= 2
            n += len(lst) // l
        elif x < lst[n]:
            l *= 2
            n -= len(lst) // l
    while (lst[n + 1] <= x or lst[n] > x):
        if x >= lst[n + 1]:
            n += 1
        elif x < lst[n]:
            n -= 1
    return n + 1

def test_upper_bound(lst, x):
  i = upper_bound(lst, x)
  assert (i == len(lst) or lst[i] > x) and (i == 0 or lst[i - 1] <= x)

def small_tests():
  test_upper_bound([1, 2, 3, 4, 5, 6], 4)
  test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 3)
  test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 2)
  test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], -2)
  test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 6)
  test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 8)
  test_upper_bound([3, 7, 12, 22, 47], 17)
  test_upper_bound([-200, -34, -5, 0, 45], -12)
  
def big_tests():
  lst = [i for i in range(0, 10 ** 6, 5)]
  test_upper_bound(lst, 3)
  test_upper_bound(lst, 45)
  test_upper_bound(lst, 10 ** 7)
  test_upper_bound(lst, -12)
  test_upper_bound(lst, 3454)
  test_upper_bound(lst, 23)
  test_upper_bound(lst, 324)
  test_upper_bound(lst, 10 ** 6 - 1)
  test_upper_bound(lst, 10 ** 6 - 5)
  test_upper_bound(lst, 0)

small_tests()
big_tests()


#===============================================3
import numpy as np

def solve_equation():
    eps = 0.03
    n1, n2 = 0, 1.6
    n = (n1 + n2) / 2
    x = n - np.cos(n)
    while abs(x) > eps:
        if x > 0:
            n2 = n
            n = (n1 + n2) / 2
            x = n - np.cos(n)
        else:
            if x < 0:
                n1 = n
                n = (n1 + n2) / 2
                x = n - np.cos(n)
    return n

x = solve_equation()
print(x, np.cos(x), abs(x - np.cos(x)))




#===============================================4
import random

def merge(left, right):
    new_lst, l, r = [0] * (len(left) + len(right)), 0, 0
    if (len(left)) == 0 and (len(right) == 0):
        return None
    else:
        if len(left) == 0:
            return right 
        else:
            if len(right) == 0:
                return left
    for i in range(len(right) + len(left)):
        if left[l] <= right[r]:
            new_lst[i] = left[l]
            l += 1
            if l == len(left):
                for k in range(i + 1, len(right) + len(left)):
                    new_lst[k] = right[r]
                    r += 1
                break
        else: 
            new_lst[i] = right[r]
            r += 1
            if r == len(right):
                for k in range(i + 1, len(left) + len(right)):
                    new_lst[k] = left[l]
                    l += 1
                break
    return new_lst

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        cur_deg = 2
        deg = 1
        while 2**deg < len(lst): 
            deg += 1
        for k in range(0, deg):
            for i in range(0, len(lst), cur_deg):
                lst[i:i + cur_deg] = merge(lst[i:(i + (cur_deg // 2))],
                        lst[(i + (cur_deg // 2)):(i + cur_deg)])
            cur_deg *= 2
    return lst

def test_merge_sort(lst):
  assert merge_sort(lst) == sorted(lst)

def small_tests():
  test_merge_sort([1, 2, 3, 4, 5, 6])
  test_merge_sort([6, 5, 4, 3, 2, 1])
  test_merge_sort([46, 76, 23, 6, 2345, 4, 87, 4, 4, 4, 456])
  test_merge_sort([5])
  test_merge_sort([23, 56, 12, 6, 2, 6, 1, 56, 123])

def big_tests():
  lst = list(range(10 ** 4))
  for i in range(10):
    random.shuffle(lst)
    test_merge_sort(lst)

small_tests()
big_tests()
