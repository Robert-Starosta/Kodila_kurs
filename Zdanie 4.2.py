def check_palindrom(palindrom):
    """
    :param palindrom: Podaj słowo do sprawdzenia
    :return: zwraca prawda lub fałsz
    """
    print (palindrom == palindrom[::-1])
help(check_palindrom)
check_palindrom("kajak")
