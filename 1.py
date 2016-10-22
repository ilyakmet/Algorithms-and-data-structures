#=================================================1
def divcount(n):
	count = 0
	i = 1
	while i ** 2 <= n:
		if (n % i == 0):
			if (i ** 2 != n):
				count += 2
			else:
				count += 1
		i += 1
	return count

def test_divcount(n, answer):
	assert divcount(n) == answer

test_divcount(1, 1)
test_divcount(5, 2)
test_divcount(121, 3)
test_divcount(10 ** 5, 36)
test_divcount(2 * 3 * 5, 8)
test_divcount(2 ** 7 * 5 ** 3 * 11, 64)
test_divcount(13 ** 3 * 41 ** 5, 24)
test_divcount(10 ** 9 + 7, 2)
test_divcount(10 ** 12 + 39, 2)


#=================================================2
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


#=================================================3
def factors(n):
    result = []
    i = 2
    k = n
    if n == 1:
    	result.append(n)
    else:
    	while i*i <= n:
    	    while k % i == 0:
    		    k /= i
    		    result.append(i)
    	    i += 1
    if k != 1:
    	result.append(k)
    return result
        
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
def mul(lst):
    result = 1
    for x in lst:
        result *= x
    return result
    
def test_factors(n):
    n_factors = factors(n)
    assert mul(n_factors) == n
    for x in n_factors:
        assert is_prime(x)
        
test_factors(1)
test_factors(2)
test_factors(5)
test_factors(10)
test_factors(81)
test_factors(10 ** 6)
test_factors(7 ** 3 * 43 ** 4 * 67 ** 2)
test_factors(10 ** 12 + 39)
test_factors(2 ** 50)
test_factors(2 ** 10 * 3 ** 20)


#=================================================4
import math

def gcd(a, b):
    print('enter recursive call, a =', a, 'b =', b)
    while a != 0 and b != 0:
    	if a > b:
    		a %= b
    	elif b > a:
    		b %= a
    if a == 0:
    	return b
    elif b == 0:
    	return a

def test_gcd(a, b):
    assert gcd(a, b) == math.gcd(a, b)
   
test_gcd(2, 3)
test_gcd(81, 27)
test_gcd(10 ** 7, 10 ** 11)
test_gcd(123456, 12345678)
test_gcd(10 ** 12 + 39, 999983)
test_gcd(12586269025, 7778742049)


#=================================================5
import math

def powmod(x, y, z):
  if y == 1:
    return x % z
  test = powmod(x, y // 2, z)
  if y % 2 == 1:
    return x * (test**2) % z
  else:
    return  (test**2) % z
    
def test_powmod(x, y, z):
    assert powmod(x, y, z) == pow(x, y, z)
    
test_powmod(2, 100, 17)
test_powmod(10, 36, 239)
MOD = 10 ** 9 + 7
test_powmod(123, 12345, MOD)
test_powmod(5, 10 ** 100, MOD)
test_powmod(997, 10 ** 200, MOD)
test_powmod(239, 10 ** 300, MOD)

