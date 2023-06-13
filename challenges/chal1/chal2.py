from Crypto.Util.number import getPrime, bytes_to_long
from gmpy2 import is_prime, invert
from typing import Tuple
from secert import flag

def gen_rsa_param() -> Tuple[int, int, int, int, int]:
    """Generate usable RSA parameters.
    
    params:
        None
    
    return:
        a tuple, including `p, q, n, e, d`
    """
    p = getPrime(256)
    q = p + 2
    while True:
        q += 2
        if is_prime(q):
            break
        
    assert p < q
    
    n = p * q
    phi_n = (p-1) * (q-1)
    e = 0x10001
    d = invert(e, phi_n)
    
    return p, q, n, e, d

def rsa_encrypt(m: str, *args) -> str:
    """Generate usable RSA parameters.
    
    params:
        m: message to be encrypted
        args: RSA parameters
    
    return:
        a string, which is the encrypted message
    """
    assert len(args) == 5
    p, q, n, e, d = args
    m = bytes_to_long(m)
    c = pow(m, e, n)
    return c

params = gen_rsa_param()
print(rsa_encrypt(flag, *params))
print(params[2])
# 5796768148637887491255587039409951397511832995737366433505141785703232675749200657380232851343254281355390391562734825283953711907092653161783752372166386
# 7948512242985881433771203281939490726039994357587772712416312873824297606161653053722572268861029945737411249803561023517431875922105282741637330609169129