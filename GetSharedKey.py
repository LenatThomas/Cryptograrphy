from Diffie_Hellman import GenerateSharedKey

if __name__ == "__main__" :

    privateKey = int(input("Enter private key\t: "))
    publicKeyAsStrings  = input("Enter the public key\t: ").split()
    publicKey = [int(x) for x in publicKeyAsStrings]
    publicKey = tuple(publicKey)

    sharedKey = GenerateSharedKey(Key = publicKey , privateKey = privateKey)
    print("The shared key is\t: " , sharedKey)