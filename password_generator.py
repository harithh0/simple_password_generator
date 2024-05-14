# password generator
import random
import pyperclip

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "~", "<", ">", "/"]

# combined = digits + lower_case + upper_case + symbols

combined = []

choices = ["y", "n"]

random_digit = random.choice(digits)
random_lower = random.choice(lower_case)
random_upper = random.choice(upper_case)
random_symbol = random.choice(symbols)

# future idea is to put the password through howsecureismypassword.com and then return how long it would take for it to be cracked


def pass_choice():
    global choices
    global combined
    pass_digt = input(
        "Do You Want Your Password To Have Digits? (y/n):").lower().strip()
    while pass_digt not in choices:
        pass_digt = input(
            "Do You Want Your Password To Have Digits? (y/n):").lower().strip()
    else:
        if pass_digt == "y":
            combined += digits
        else:
            None

    pass_lc = input(
        "Do You Want Your Password To Have Lower Case Letters? (y/n):").lower().strip()
    while pass_lc not in choices:
        pass_lc = input(
            "Do You Want Your Password To Lower Case Letters? (y/n):").lower().strip()
    else:
        if pass_lc == "y":
            combined += lower_case
        else:
            None

    pass_uc = input(
        "Do You Want Your Password To Have Upper Case Letters? (y/n):").lower().strip()
    while pass_uc not in choices:
        pass_uc = input(
            "Do You Want Your Password To Have Upper Case Letters? (y/n):").lower().strip()
    else:
        if pass_uc == "y":
            combined += upper_case
        else:
            None

    pass_sym = input(
        "Do You Want Your Password To Have Symbols? (y/n):").lower().strip()
    while pass_sym not in choices:
        pass_sym = input(
            "Do You Want Your Password To Have Symbols? (y/n):").lower().strip()
    else:
        if pass_sym == "y":
            combined += symbols
        else:
            None


def password_creator():
    global choices
    global combined

    want_all = input("Do You Want All The Characters? (y/n): ").lower().strip()
    while want_all not in choices:
        want_all = input(
            "Do You Want All The Characters? (y/n): ").lower().strip()
    else:
        if want_all == "y" and combined == []:
            combined = digits + lower_case + upper_case + symbols
        else:
            pass_choice()

    if combined == []:
        combined = digits + lower_case + upper_case + symbols

    while True:
        try:
            password_len = int(input("Length Of Password: "))
            break
        except ValueError:
            print("\nPlease Enter A Valid Number.")

    password = ""

    for i in range(password_len):
        password += random.choice(combined)
    print("\n" + password)
    
    
#    retry = input("\nWould You Like To Make A New Password?").lower().strip()
    
#    while retry not in choices:
#        retry = input("\nWould You Like To Make A New Password?").lower().strip()
#    else:
#        if retry == "y":
#            for i in range(password_len):
#                password += random.choice(combined)
#            print("\n" + password)
#            exit()
#       else:
#            exit()
    
    copy_paste = input(
        "\nWould You Like To Copy Password? (y/n): ").lower().strip()
    while copy_paste not in choices:
        copy_paste = input(
            "\nWould You Like To Copy Password? (y/n): ").lower().strip()
    else:
        if copy_paste == "y":
            pyperclip.copy(password)
            exit()
        else:
            exit()


password_creator()
