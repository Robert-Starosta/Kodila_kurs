def sum (a, b):
    print (a + b)
def difference(a, b):
    print (a - b)
def multiplication(a, b):
    print (a * b)
def division(a, b):
    print (a / b)



if __name__ == "__main__":
    calc_function = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    calc_function = int(calc_function)
    a = input("Podaj pierwsza liczbę: ")
    b = input("Podaj drugą liczbę: ")
    a = int(a)
    b = int(b)
    if calc_function == 1:
        sum(a, b)
    elif calc_function == 2:
        difference(a, b)
    elif calc_function == 3:
        multiplication(a, b)
    elif calc_function == 4:
        if b == 0:
            print("Nie można wykonanć działania dzielenie przez 0 niemożliwe")
        else:
            division(a, b)



