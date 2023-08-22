import random, string

# PASSWORD CHARACTERS
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
numbers = '123456789'
symbols = '()[]{}.:;-_=+\|?/!@#$%&*'

# USED TYPES
upper, lower, nums, syms = True,True,True,False

# STRING PASSWORD 
all = ''

# INSERT CHARACTERS
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols

# PASSWORD SIZE
length = 20
# QUANTITY OF PASSWORDS
amount = 10

y = 1

# GENERATOR LOOP
for x in range(amount):
    password = "".join(random.sample(all,length))
    print(f"{y}. {password}")
    y += 1

    # SAVE CRATED PASSWORDS IN A TXT FILE
    with open('password_bank.txt', 'a') as archive:
        archive.write(f"{str(password)}\n")

    # SCORE OF PASSWORD
    # upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    # lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    # numbers_case = any([1 if c in str(string.ascii_numberscase) else 0 for c in password])
    # symbols_case = any([1 if c in str(string.ascii_symbolscase) else 0 for c in password])

    # characters = [upper_case, lower_case, numbers_case, symbols_case]

    # score = 0 

    # if length > 8:
    #     score = score + 1
    # if length > 12:
    #     score = score + 1
    # if length > 17:
    #     score = score + 1
    # if length > 20:
    #     score = score + 1

    # print(f"{score}")
    

    






