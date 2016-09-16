def powmod(x, y, z):
    return x
    
def test_powmod(x, y, z):
    assert powmod(x, y, z) == pow(x, y, z)
    
test_powmod(2, 100, 17)
test_powmod(10, 36, 239)
MOD = 10 ** 9 + 7
test_powmod(123, 12345, MOD)
test_powmod(5, 10 ** 100, MOD)
test_powmod(997, 10 ** 200, MOD)
# test_powmod(239, 10 ** 300, MOD)
