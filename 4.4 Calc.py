import logging

interface = {
    1: "Dodawanie",
    2: "Odejmowanie",
    3: "Mnożenie",
    4: "Dzielenie"
}


def sum(a, b):
  return a + b


def difference(a, b):
  return a- b


def multiplication(a, b):
  return a * b


def division(a, b):
  if b == 0:
    return ("b must by diffrent then 0")
  else:
    return a / b


def cli_interface():
    for i in interface.items():
        print(i)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print("Rodzaje działań:")
    cli_interface()
    calc_function = input("Podaj działanie: ")
    calc_function = int(calc_function)
    a = int(input("Podaj pierwsza liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    result = None
    if calc_function == 1:
        result = sum (a, b)
        print("Wynik działania to: %i" % result)
        logging.debug("Ten program dodał do siebie liczbę %i oraz %i" % (a, b))
    elif calc_function == 2:
        result = difference(a, b)
        print("Wynik działania to: %i" % result)
        logging.debug("Ten program odjoł do siebie liczbę %i oraz %i" % (a, b))
    elif calc_function == 3:
        result = multiplication(a, b)
        print("Wynik działania to: %i" % result)
        logging.debug("Ten program pomnożył dwie liczby %i oraz %i" % (a, b))
    elif calc_function == 4:
        result = division(a, b)
        print("Wynik działania to: %s" % result)
        logging.debug("Ten program podzielił przez siebie liczby %i oraz %i" % (a, b))
    else:
        print("Wystąpił bład podana wartość poza zakresem 1-4")
