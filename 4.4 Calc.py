import logging
logging.basicConfig(level=logging.DEBUG)

def sum (a, b):
    logging.debug("Ten program dodał do siebie liczbę %i oraz %i" % (a, b))
    print ("Wynik działania to: %i" % (a+b))
def difference(a, b):
    logging.debug("Ten program odjoł do siebie liczbę %i oraz %i" % (a, b))
    print ("Wynik działania to: %i" % (a-b))
def multiplication(a, b):
    print ("Wynik działania to: %i" % (a*b))
    logging.debug("Ten program pomnożył dwie liczby %i oraz %i" % (a, b))
def division(a, b):
    logging.debug("Ten program podzielił przez siebie liczby %i oraz %i" % (a, b))
    if b == 0:
        print("Nie można wykonanć działania dzielenie przez 0 niemożliwe")
    else:
        print ("Wynik działania to: %i" % (a/3b))



if __name__ == "__main__":
    calc_function = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    calc_function = int(calc_function)
    a = int(input("Podaj pierwsza liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    if calc_function == 1:
        sum(a, b)
    elif calc_function == 2:
        difference(a, b)
    elif calc_function == 3:
        multiplication(a, b)
    elif calc_function == 4:
        division(a, b)



