def is_palindrom(palindrom):
    """
    :param palindrom: give a word to check
    :return: return true or false
    """
    if (palindrom == palindrom[::-1]):
        print("Słowo jest palindromem")
    else:
        print("Słowo nie jest palindromem")

if __name__ == "__main__":
    palidrom = input("Podaj słowo do sprawdzenia: ")
    is_palindrom(palidrom)
