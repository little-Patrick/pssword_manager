import ipdb
import string
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
        n = n % len(lst)
        return l[n:] + l[:n]

    def offest(self):
       hash_letter_key = {}
       letter_key = self.letters()
       for index, value in enumerate(letter_key):
            hash_letter_key[value] = value
       ipdb.set_trace()

    def reverse_shift(self):
        pass

    def letters(self):
        lowercase = list(string.ascii_lowercase)
        return lowercase
