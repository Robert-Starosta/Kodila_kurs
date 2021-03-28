def is_palindrom(palindrom):
    """
    :param palindrom: Podaj słowo do sprawdzenia
    :return: zwraca prawda lub fałsz
    """
    if (palindrom == palindrom[::-1]):
        print("Słowo jest palindromem")
    else:
        print("Słowo nie jest palindromem")

if __name__ == "__main__":
    palidrom = input("Podaj słowo do sprawdzenia: ")
    is_palindrom(palidrom)
