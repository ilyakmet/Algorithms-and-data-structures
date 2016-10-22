import random

#====================================================================1
def counting_sort(lst):
  count = [0] * (max(lst) + 1)
  for x in lst:
    count[x] += 1
  result = []
  for i in range(len(count)):
    for j in range(count[i]):
      result.append(i)
  return result

def test_counting_sort(lst):
  assert counting_sort(lst) == sorted(lst)

def small_tests():
  test_counting_sort([1, 2, 3, 4, 5, 6])
  test_counting_sort([6, 5, 4, 3, 2, 1])
  test_counting_sort([46, 76, 23, 6, 2345, 4, 87, 4, 4, 4, 456])
  test_counting_sort([5])
  test_counting_sort([23, 56, 12, 6, 2, 6, 1, 56, 123])

def big_tests():
  lst = list(range(10 ** 4))
  for i in range(10):
    random.shuffle(lst)
    test_counting_sort(lst)

small_tests()
big_tests()

#====================================================================2
def nth_element(lst, n):
  if len(lst) == 1:
    return lst[0]
  pivot = random.choice(lst)
  less = [x for x in lst if x < pivot]
  equal = [x for x in lst if x == pivot]
  greater = [x for x in lst if x > pivot]
  if len(less) > n:
    return nth_element(less, n)
  elif len(less) + len(equal) > n:
    return pivot
  else:
    return nth_element(greater, n - len(less) - len(equal))

def test_nth_element(lst, n, answer):
  assert nth_element(lst, n) == answer

def small_tests():
  test_nth_element([8, 5, 3, 1], 1, 3)
  test_nth_element([2, 8, 4, 6], 2, 6)
  test_nth_element([23, 675, 13, 57, 6], 0, 6)

def random_test():
  lst = list(range(100))
  random.shuffle(lst)
  n = random.choice(lst)
  test_nth_element(lst, n, n)

def test_equal():
  lst = [1] * 100
  for i in range(100):
    test_nth_element(lst, i, 1)

def medium_tests():
  test_equal()
  for i in range(20):
    random_test()

small_tests()
medium_tests()

#====================================================================3
INFINITY = 10 ** 10

def min_cost_grig(costs, jumps):
	min_cost = [INFINITY] * len(costs)
	min_cost[0] = costs[0]
	for i in range(1, len(costs)):
		r = [INFINITY]
		for j in jumps:
			if j <= i:
				r.append(min_cost[i - j])
		min_cost[i] = costs[i] + min(r)
	return min_cost

def test_min_cost_grig(costs, jumps, answer):
    out = min_cost_grig(costs, jumps)
    for i in range(len(answer)):
        assert out[i] == answer[i] or (out[i] >= INFINITY and answer[i] >= INFINITY)

test_min_cost_grig([6, 9, 5, 4, 7, 7, 4, 10], [5, 5, 2], [6, 10000000009, 11, 10000000004, 18, 13, 22, 21])
test_min_cost_grig([3, 1, 7, 2, 3], [1, 5], [3, 4, 11, 13, 16])
test_min_cost_grig([7, 10, 8, 0, 7, 8, 9, 4, 5], [5, 3, 1], [7, 17, 25, 7, 14, 15, 16, 18, 12])
test_min_cost_grig([10, 1, 0, 7, 9, 0, 4, 7, 2, 9], [4, 5, 1, 2], [10, 11, 10, 17, 19, 10, 14, 17, 16, 19])
test_min_cost_grig([8, 7, 4, 7, 10, 5], [5, 4], [8, 10000000007, 10000000004, 10000000007, 18, 13])
test_min_cost_grig([2, 6, 8, 5, 5, 3, 7], [5, 4], [2, 10000000006, 10000000008, 10000000005, 7, 5, 10000000007])
test_min_cost_grig([1, 4, 7, 1, 6, 4], [1, 6, 1, 5, 4], [1, 5, 12, 13, 7, 5])
test_min_cost_grig([4, 0, 0, 1, 6, 8, 6, 4, 7, 1, 5], [2, 4, 1], [4, 4, 4, 5, 10, 12, 10, 9, 16, 10, 15])
test_min_cost_grig([6, 0, 7, 8, 9, 8, 6, 5, 2, 4], [2, 6, 6, 6, 5], [6, 10000000000, 13, 10000000008, 22, 14, 12, 18, 14, 22])
test_min_cost_grig([6, 10, 8, 6, 0, 1, 0, 8, 6, 8, 8, 9], [4, 4, 5, 1, 2], [6, 16, 14, 20, 6, 7, 6, 14, 12, 14, 14, 15])
test_min_cost_grig([4, 9, 3, 0, 4, 10, 8], [4, 4, 2], [4, 10000000009, 7, 10000000000, 8, 10000000010, 15])
test_min_cost_grig([3, 5, 3, 7, 1], [5, 1], [3, 8, 11, 18, 19])
test_min_cost_grig([2, 2, 6, 0, 5, 1, 5, 7, 7, 10], [4, 4, 4, 3], [2, 10000000002, 10000000006, 2, 7, 10000000001, 7, 9, 14, 17])
test_min_cost_grig([0, 5, 4, 5, 9, 7, 2], [2, 5, 1], [0, 5, 4, 9, 13, 7, 7])
test_min_cost_grig([7, 0, 4, 7, 10, 0], [5, 5, 6, 3], [7, 10000000000, 10000000004, 14, 10000000010, 7])

