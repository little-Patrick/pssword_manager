import ipdb
class Enigma:
    def __init__(self, password, key1, key2):
        self.password = password
        self.key1 = key1
        self.key2 = key2

    def encrypt(self):
        return self.shift()
       
    def decrypt(self):
        reverseShift()

    def shift(self):
        splitKey = list(self.key1)
        aKey = ''.join(splitKey[0:2])
        bKey = ''.join(splitKey[1:3])
        cKey = ''.join(splitKey[2:4])
        dKey = ''.join(splitKey[3:5])
        
        ipdb.set_trace()

        return a

    def reverseShift(self):
        pass

