def max_divisor(n):
	i = 2
	max_d = n // i
	while (i * i < n) and (n % i != 0):
		i += 1
		max_d = n // i
	if n % i == 0:
		return max_d
	return 1
    
def test_max_divisor(n, answer):
    assert max_divisor(n) == answer


    

test_max_divisor(5, 1)
test_max_divisor(30, 15)
test_max_divisor(81, 27)
n = 3 ** 4 * 7 ** 3
test_max_divisor(n, n // 3)
n = 11 ** 5 * 43 ** 3 * 67
test_max_divisor(n, n // 11)
test_max_divisor(10 ** 12 + 39, 1)
test_max_divisor(1009 ** 3, 1009 ** 2)
test_max_divisor(999983 ** 2, 999983)


