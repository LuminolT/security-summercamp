from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag

p = getPrime(128)
q = getPrime(128)

n = p * q
phi_n = (p - 1) * (q - 1)

e = 65537

m = bytes_to_long(flag)
c = pow(m, e, n)

print(e)
print(n)
print(c)

# 65537
# 60312637199635801058227385421553206347253918440828187249920737695124886809487
# 14673748133379805475254231366717984351237192567008318062632171353909225806981