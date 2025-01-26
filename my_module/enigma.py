import ipdb
import string
class Enigma:
    def __init__(self, password, key, date):
        self.password = password
        self.key = key
        self.date = date

    def encrypt(self):
       pass
       
    def decrypt(self):
        reverse_shift()

    def shift_key(self):
        split_key = list(self.key)
        key_offset = {
            "a": ''.join(split_key[0:2]),
            "b": ''.join(split_key[1:3]),
            "c": ''.join(split_key[2:4]),
            "d": ''.join(split_key[3:5])
        }
        return key_offset

    def shift_date(self):
        square = int(self.date) ** 2
        split_date = list(str(square))
        date_offset = {
            "a": ''.join(split_date[-1]),
            "b": ''.join(split_date[-2]),
            "c": ''.join(split_date[-3]), 
            "d": ''.join(split_date[-4])
        }
        return date_offset

    def final_key(self):
        final = {}
        for key in self.shift_date():
            final[key] = int(self.shift_date()[key]) + int(self.shift_key()[key])
        return final

    def rotate(self, l, n):
        if len(l) == 0:
            return l
        n = n % len(l)
        return l[n:] + l[:n]

    def offest(self):
        hash_letter_key = {}
        letter_key = self.letters()
        for index, value in enumerate(letter_key):
             hash_letter_key[value] = value

        a_key = hash_letter_key.copy()
        b_key = hash_letter_key.copy()
        c_key = hash_letter_key.copy()
        d_key = hash_letter_key.copy()

        a_offset = self.rotate(letter_key, self.final_key()["a"])
        b_offset = self.rotate(letter_key, self.final_key()["b"])
        c_offset = self.rotate(letter_key, self.final_key()["c"])
        d_offset = self.rotate(letter_key, self.final_key()["d"])
 
        for index, key in enumerate(a_key.keys()):
            a_key[key] = a_offset[index]
        ipdb.set_trace()

    def reverse_shift(self):
        pass

    def letters(self):
        lowercase = list(string.ascii_lowercase)
        return lowercase
