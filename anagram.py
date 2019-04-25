from typing import List, Any, Iterator

input_str_1 = "practice makes perfect"
input_str_2 = "Perfect makes practice"
input_str_3 = "galleryq"
input_str_4 = "galleric"
input_str_5 = "kajak" #"Was it a cat I saw"
input_str_6 = "galleric"

# def clear_text(str_1: object) -> object:
def clear_text(str_1):
    str_1 = str_1.replace(" ", "")
    str_1 = str_1.lower()
    return str_1


def is_anagram(str_1, str_2):
    str_1 = clear_text(str_1)
    str_2 = clear_text(str_2)

    if len(str_1) != len(str_2):
        return False

    alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)
    for litera in str_1:
        dict_1[litera] += 1
    for litera in str_2:
        dict_2[litera] += 1
    if dict_1 == dict_2:
        return True
    else:
        return False


def is_palindrome(str_1):
    clear_text(str_1)
    list_1 = list(reversed(str_1))
    print(list_1)
    if list_1 == list(str_1):
        print(list_1)
        return True

def is_palindrome_2(str_1):
    clear_text(str_1)
    str_2 = str_1[::-1]  #odwraca stringa (:: wypisuje wszystko)
    if str_1 == str_2:
        print("palindrom")
        return True
    else: return False

print("practice: ",is_anagram(input_str_1, input_str_2))
print(is_anagram(input_str_3, input_str_4))
print("czy palindrom:",is_palindrome(input_str_5))
print("czy palindrom2:",is_palindrome_2(input_str_5))

napis = "jakiś napis"
print(napis.find("pi",0,10))
# lista = list(napis1)
