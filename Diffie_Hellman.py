def ModuloExponent(base : int , exponent : int , modulus : int ) :
    result = 1
    while exponent > 0 :
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def GeneratePublicKey(prime : int , pseudoRoot : int , privateKey : int) :
    publicKey = ModuloExponent(base = pseudoRoot , exponent = privateKey , modulus = prime)
    return (prime , pseudoRoot , publicKey)

def GenerateSharedKey(Key : tuple , privateKey : int) :
    prime = Key[0]
    publicKey = Key[2]
    secretKey = ModuloExponent(publicKey , privateKey , prime)
    return secretKey