""" import random
human = []

random_number = random.randint(3, 12)

def generate_pw(number = random_number):  
    low_let = 'abcdefghijklmnopqrstuvwxyz'
    up_let = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    digits = '0123456789'
    all_chars = low_let +up_let + digits
    pw = ''
    for _ in range(random_number):
        pw += random.choice(all_chars)

    return pw

print(random_number)
s = human.append(generate_pw)
print(s)
 """