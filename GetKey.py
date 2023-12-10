from Diffie_Hellman import GeneratePublicKey , GenerateSharedKey



if __name__ == '__main__' :

    prime = int(input("Enter a large prime\t\t: "))
    Generator = int(input("Enter a generator (Pseuso Root)\t: "))
    privateKey = int(input("Enter the private key\t\t: "))

    publicKey = GeneratePublicKey(prime = prime , pseudoRoot = Generator , privateKey = privateKey)

    print("The public key\t\t: " , publicKey)