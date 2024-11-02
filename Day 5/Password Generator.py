import random

from sqlalchemy.sql.visitors import iterate

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
password_letters=(int(input("How many letters would you like in your password?")),0)
password_symbols = (int(input("How many symbols would you like?")),1)
password_numbers = (int(input("How many numbers would you like?")),2)
# defingng a function that can easily do both at same time



def generator(password_criteria, identification_num):
    should_iterate=[]
    print(password_criteria)
    choosen_element=""
    # decide which one u want to iterate
    if identification_num==0:

        should_select_from=letters
    elif identification_num==1:
        should_select_from=symbols
    elif identification_num ==2:
        should_select_from=numbers



#     then iterate that one

    for i in range(password_criteria):
          choosen_element+=random.choice(should_select_from)

    return choosen_element

gen_letters=generator(password_letters[0],password_letters[1])
gen_symbols=generator(password_symbols[0],password_symbols[1])
gen_number= generator(password_numbers[0],password_numbers[1])

final_password = list(gen_letters+gen_number+gen_symbols)
shuffle_final= random.shuffle(final_password)
print(''.join(final_password))